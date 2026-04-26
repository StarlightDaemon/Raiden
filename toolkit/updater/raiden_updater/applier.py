"""Apply command — execute a conflict-free update plan.

The applier copies only the files that need updating from the package
payload into the instance managed root, then writes a new installed
baseline record. Safe removal actions are applied only for baseline-tracked
managed files that passed planning without conflict.
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from .hasher import hash_file
from .models import InstalledBaseline, ManagedFileEntry, PlanResult


class ApplyError(Exception):
    """Raised when apply cannot proceed."""


def apply_plan(
    plan: PlanResult,
    instance_root: Path,
    package_root: Path,
) -> None:
    """Execute an update plan.

    Parameters
    ----------
    plan:
        A ``PlanResult`` from ``create_plan()``. Must have
        ``can_apply=True``.
    instance_root:
        Path to the target repo root.
    package_root:
        Path to the package directory (contains ``payload/``).

    Raises
    ------
    ApplyError
        If the plan cannot be applied.
    """
    if not plan.can_apply:
        raise ApplyError(
            f"Plan is not apply-safe: {plan.block_reason}"
        )

    payload_root = package_root / "payload"
    if not payload_root.is_dir():
        raise ApplyError(
            f"Package payload directory not found: {payload_root}"
        )

    # Determine the managed root inside the instance
    if not plan.protected_paths and not plan.file_actions:
        raise ApplyError("Plan has no file actions and no protected paths")

    # We derive managed root from the plan's context — it was built using
    # metadata.managed_roots[0], but we reconstruct it here.
    # MVP: always .raiden/writ
    managed_root = instance_root / ".raiden" / "writ"
    managed_root.mkdir(parents=True, exist_ok=True)

    # ── Apply file actions ────────────────────────────────────────────────
    for action in plan.file_actions:
        if action.action == "update" or action.action == "add":
            src = payload_root / action.path
            dst = managed_root / action.path

            if not src.exists():
                raise ApplyError(
                    f"Source file not found in package payload: {src}"
                )

            # Ensure parent directory exists
            dst.parent.mkdir(parents=True, exist_ok=True)

            # Copy the file
            shutil.copy2(src, dst)

        elif action.action == "unchanged":
            # No action needed
            pass

        elif action.action == "remove":
            dst = managed_root / action.path
            if dst.exists():
                if dst.is_dir():
                    raise ApplyError(
                        f"Managed file removal target is a directory: {dst}"
                    )
                dst.unlink()
                _prune_empty_dirs(dst.parent, managed_root)

    # ── Write new baseline ────────────────────────────────────────────────
    new_baseline_entries: list[ManagedFileEntry] = []
    for action in plan.file_actions:
        if action.action in ("update", "add", "unchanged"):
            installed_path = managed_root / action.path
            if installed_path.exists():
                new_baseline_entries.append(ManagedFileEntry(
                    path=action.path,
                    hash=hash_file(installed_path),
                ))

    new_baseline = InstalledBaseline(
        installed_edict_version=plan.target_version,
        installed_at=datetime.now(timezone.utc).isoformat(),
        managed_files=new_baseline_entries,
    )

    baseline_path = instance_root / ".raiden" / "instance" / "baseline.json"
    baseline_path.parent.mkdir(parents=True, exist_ok=True)

    with open(baseline_path, "w", encoding="utf-8") as f:
        json.dump(_baseline_to_dict(new_baseline), f, indent=2)

    # ── Update instance metadata version ──────────────────────────────────
    metadata_path = instance_root / ".raiden" / "instance" / "metadata.json"
    if metadata_path.exists():
        with open(metadata_path, "r", encoding="utf-8") as f:
            meta_data = json.load(f)
        meta_data["installed_edict_version"] = plan.target_version
        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, indent=2)


def _baseline_to_dict(baseline: InstalledBaseline) -> dict:
    """Serialize a baseline to a JSON-compatible dict."""
    return {
        "installed_edict_version": baseline.installed_edict_version,
        "installed_at": baseline.installed_at,
        "managed_files": [
            {"path": e.path, "hash": e.hash}
            for e in baseline.managed_files
        ],
    }


def _prune_empty_dirs(start: Path, stop: Path) -> None:
    """Remove now-empty parent directories without removing the managed root."""
    current = start
    while current != stop:
        try:
            current.rmdir()
        except OSError:
            break
        current = current.parent
