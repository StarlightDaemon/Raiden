"""Plan command — produce a conflict-aware, delta-only update plan.

The planner never mutates the filesystem. It reads the current instance
state and the target package, then returns a ``PlanResult`` describing
what an apply would do.
"""

from __future__ import annotations

from pathlib import Path

from .anomaly import classify_anomalies
from .compatibility import check_schema_compatibility
from .hasher import hash_file
from .loader import (
    LoadError,
    load_installed_baseline,
    load_instance_metadata,
    load_package_manifest,
)
from .models import (
    Conflict,
    FileAction,
    ManagedFileEntry,
    PlanResult,
)
from .version import compare_versions


def create_plan(
    instance_root: Path,
    package_root: Path,
    allow_downgrade: bool = False,
) -> PlanResult:
    """Produce an update plan without mutating the filesystem.

    Parameters
    ----------
    instance_root:
        Path to the target repo root (parent of ``.raiden/``).
    package_root:
        Path to the package directory (contains ``manifest.json`` and
        ``payload/``).

    Returns
    -------
    PlanResult
        A fully populated plan showing compatibility, version comparison,
        file actions, conflicts, anomalies, and whether apply can proceed.
    """

    # ── 1. Load metadata ──────────────────────────────────────────────────
    try:
        metadata = load_instance_metadata(instance_root)
    except LoadError as exc:
        return _blocked_plan(
            reason=f"Cannot load instance metadata: {exc}",
            conflict_type="missing_metadata",
        )

    try:
        manifest = load_package_manifest(package_root)
    except LoadError as exc:
        return _blocked_plan(
            reason=f"Cannot load package manifest: {exc}",
            conflict_type="invalid_manifest",
        )

    baseline = None
    try:
        baseline = load_installed_baseline(instance_root)
    except LoadError as exc:
        return _blocked_plan(
            reason=f"Cannot load installed baseline: {exc}",
            conflict_type="invalid_baseline",
        )

    # ── 2. Compatibility check ────────────────────────────────────────────
    compatible, compat_detail = check_schema_compatibility(metadata, manifest)
    try:
        version_cmp = compare_versions(
            metadata.installed_edict_version, manifest.edict_version
        )
    except ValueError as exc:
        return _blocked_plan(
            reason=f"Invalid version value: {exc}",
            conflict_type="invalid_version",
        )

    if version_cmp == "downgrade" and not allow_downgrade:
        return PlanResult(
            compatible=compatible,
            compatibility_detail=compat_detail,
            version_comparison=version_cmp,
            current_version=metadata.installed_edict_version,
            target_version=manifest.edict_version,
            conflicts=[Conflict(
                path="",
                conflict_type="downgrade_blocked",
                detail=(
                    "Downgrade blocked: target version is lower than installed "
                    "version. Use --allow-downgrade to override."
                ),
            )],
            protected_paths=metadata.overlay_roots + metadata.live_state_roots,
            can_apply=False,
            block_reason=(
                "Downgrade blocked: target version is lower than installed "
                "version. Use --allow-downgrade to override."
            ),
        )

    if not compatible:
        return PlanResult(
            compatible=False,
            compatibility_detail=compat_detail,
            version_comparison=version_cmp,
            current_version=metadata.installed_edict_version,
            target_version=manifest.edict_version,
            conflicts=[Conflict(
                path="",
                conflict_type="schema_incompatibility",
                detail=compat_detail,
            )],
            protected_paths=metadata.overlay_roots + metadata.live_state_roots,
            can_apply=False,
            block_reason=f"Schema incompatibility: {compat_detail}",
        )

    # ── 3. Build baseline hash index ──────────────────────────────────────
    baseline_hashes: dict[str, str] = {}
    if baseline is not None:
        baseline_hashes = {e.path: e.hash for e in baseline.managed_files}

    # ── 4. Build target hash index ────────────────────────────────────────
    target_hashes: dict[str, str] = {
        e.path: e.hash for e in manifest.managed_files
    }

    # ── 5. Determine the managed root ─────────────────────────────────────
    # MVP: only .raiden/writ is supported as a managed root.
    if not metadata.managed_roots:
        return _blocked_plan(
            reason="Instance has no managed_roots defined",
            conflict_type="missing_metadata",
        )
    managed_root_rel = metadata.managed_roots[0]  # ".raiden/writ"
    managed_root = instance_root / managed_root_rel

    if baseline is None and _managed_root_has_files(managed_root):
        return _blocked_plan(
            reason=(
                "Installed baseline is missing for a non-empty managed root; "
                "the updater cannot distinguish safe updates from local "
                "managed-file modifications"
            ),
            conflict_type="missing_baseline",
        )

    # ── 6. Compute file actions and detect conflicts ──────────────────────
    file_actions: list[FileAction] = []
    conflicts: list[Conflict] = []

    # 6a. Files in the target package
    for target_entry in manifest.managed_files:
        installed_path = managed_root / target_entry.path
        baseline_hash = baseline_hashes.get(target_entry.path)

        if not installed_path.exists():
            # New file — will be added
            file_actions.append(FileAction(
                path=target_entry.path,
                action="add",
                reason="New managed file not present in instance",
            ))
            continue

        # File exists — hash the current content
        current_hash = hash_file(installed_path)

        if current_hash == target_entry.hash:
            # Already matches target — no action needed
            file_actions.append(FileAction(
                path=target_entry.path,
                action="unchanged",
                reason="Current content already matches target package",
            ))
            continue

        # File differs from target — check if it was locally modified
        if baseline_hash is not None and current_hash != baseline_hash:
            # Locally modified managed file → CONFLICT
            conflicts.append(Conflict(
                path=target_entry.path,
                conflict_type="local_modification",
                detail=(
                    f"Managed file {target_entry.path!r} was locally "
                    f"modified (current hash {current_hash[:12]}... "
                    f"differs from baseline {baseline_hash[:12]}...)"
                ),
            ))
            continue

        # File differs from target but matches baseline (or no baseline)
        # → safe to update
        file_actions.append(FileAction(
            path=target_entry.path,
            action="update",
            reason="Content differs from target package",
        ))

    # 6b. Files in baseline but NOT in target package (safe removals only)
    for baseline_path, baseline_hash in baseline_hashes.items():
        if baseline_path not in target_hashes:
            installed_path = managed_root / baseline_path

            if installed_path.exists():
                current_hash = hash_file(installed_path)
                if current_hash != baseline_hash:
                    conflicts.append(Conflict(
                        path=baseline_path,
                        conflict_type="local_modification",
                        detail=(
                            f"Managed file {baseline_path!r} is slated for "
                            f"removal but was locally modified (current hash "
                            f"{current_hash[:12]}... differs from baseline "
                            f"{baseline_hash[:12]}...)"
                        ),
                    ))
                    continue

            file_actions.append(FileAction(
                path=baseline_path,
                action="remove",
                reason=(
                    "File is in installed baseline, absent from new package, "
                    "and safe to remove"
                    if installed_path.exists()
                    else (
                        "File is already absent locally and absent from the "
                        "new package; baseline entry will be dropped"
                    )
                ),
            ))

    # ── 7. Protected paths ────────────────────────────────────────────────
    protected_paths = metadata.overlay_roots + metadata.live_state_roots

    # ── 8. Anomaly classification ─────────────────────────────────────────
    anomalies = classify_anomalies(metadata, manifest, file_actions)

    # Check for blocking anomalies
    blocking_anomalies = [a for a in anomalies if a.severity == "block"]

    # ── 9. Determine can_apply ────────────────────────────────────────────
    has_conflicts = len(conflicts) > 0
    has_blocking_anomalies = len(blocking_anomalies) > 0

    block_reasons: list[str] = []
    if has_conflicts:
        block_reasons.append(
            f"{len(conflicts)} conflict(s): "
            + "; ".join(c.detail for c in conflicts)
        )
    if has_blocking_anomalies:
        block_reasons.append(
            f"{len(blocking_anomalies)} blocking anomaly(ies): "
            + "; ".join(a.detail for a in blocking_anomalies)
        )

    can_apply = not has_conflicts and not has_blocking_anomalies
    block_reason = " | ".join(block_reasons) if block_reasons else None

    # If version is "same" and no changes, it's a no-op
    if version_cmp == "same" and all(
        a.action == "unchanged" for a in file_actions
    ):
        can_apply = False
        block_reason = "Already up to date — no changes needed"

    return PlanResult(
        compatible=True,
        compatibility_detail=compat_detail,
        version_comparison=version_cmp,
        current_version=metadata.installed_edict_version,
        target_version=manifest.edict_version,
        file_actions=file_actions,
        conflicts=conflicts,
        anomalies=anomalies,
        protected_paths=protected_paths,
        can_apply=can_apply,
        block_reason=block_reason,
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _blocked_plan(reason: str, conflict_type: str) -> PlanResult:
    """Return a plan that cannot be applied due to a pre-check failure."""
    return PlanResult(
        compatible=False,
        compatibility_detail=reason,
        version_comparison="unknown",
        current_version="unknown",
        target_version="unknown",
        conflicts=[Conflict(path="", conflict_type=conflict_type, detail=reason)],
        can_apply=False,
        block_reason=reason,
    )


def _managed_root_has_files(managed_root: Path) -> bool:
    """Return True when an existing managed root contains any file."""
    return managed_root.exists() and any(
        path.is_file() for path in managed_root.rglob("*")
    )
