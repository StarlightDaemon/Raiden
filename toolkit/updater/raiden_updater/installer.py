"""Shared installer services for RAIDEN Instance setup and inspection.

This module is the canonical backend surface for first-install flows that
create or inspect a downstream RAIDEN Instance. It is intentionally reusable
from CLI wrappers and future local web API layers.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


INSTANCE_SCHEMA_VERSION = "1"
INSTANCE_FORM_TYPE = "raiden-instance"
INITIAL_INSTALLED_VERSION = "0.0.0"
BRIDGE_HEADER = "# Agent Startup"
BRIDGE_BODY = "Read `.raiden/README.md` before doing repo-local work.\n"
LEGACY_REVIEW_RELATIVE_PATH = ".raiden/state/LEGACY_REVIEW.md"


@dataclass(frozen=True)
class LegacyArtifact:
    """A detected pre-RAIDEN repo-agent artifact."""

    path: str
    status: str
    reason: str


@dataclass(frozen=True)
class PlannedWrite:
    """A file write the installer would make."""

    path: str
    action: str
    reason: str


@dataclass(frozen=True)
class InitPreviewResult:
    """Preview of instance initialization."""

    legacy_artifacts: list[LegacyArtifact] = field(default_factory=list)
    planned_writes: list[PlannedWrite] = field(default_factory=list)
    review_file: str = LEGACY_REVIEW_RELATIVE_PATH


@dataclass(frozen=True)
class InitApplyResult:
    """Result of instance initialization."""

    written_paths: list[str] = field(default_factory=list)
    legacy_artifacts: list[LegacyArtifact] = field(default_factory=list)
    review_file: str = LEGACY_REVIEW_RELATIVE_PATH


@dataclass(frozen=True)
class DoctorResult:
    """Result of checking the required instance shape."""

    ok: bool
    problems: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class RepoScanResult:
    """Summary of repo readiness for install or update mode."""

    legacy_artifacts: list[LegacyArtifact] = field(default_factory=list)
    has_instance_root: bool = False
    has_bridge: bool = False
    review_file: str = LEGACY_REVIEW_RELATIVE_PATH


def _write_text(path: Path, content: str, *, force: bool) -> bool:
    """Write text if missing or forced. Return True when a write happened."""
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def _write_json(path: Path, data: dict, *, force: bool) -> bool:
    """Write JSON if missing or forced. Return True when a write happened."""
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return True


def _metadata(installed_version: str) -> dict:
    return {
        "instance_schema_version": INSTANCE_SCHEMA_VERSION,
        "instance_form_type": INSTANCE_FORM_TYPE,
        "installed_edict_version": installed_version,
        "managed_roots": [".raiden/writ"],
        "overlay_roots": [".raiden/local"],
        "live_state_roots": [".raiden/state"],
    }


def is_raiden_bridge(content: str) -> bool:
    """Return True when AGENTS.md already matches the current RAIDEN bridge."""
    return content.startswith(BRIDGE_HEADER) and BRIDGE_BODY.strip() in content


def scan_legacy_artifacts(target: Path) -> list[LegacyArtifact]:
    """Detect likely legacy repo-agent surfaces that need operator review."""
    candidates = [
        (
            "AGENTS.md",
            "active-legacy",
            "Existing repo-root AGENTS startup instructions predate the RAIDEN bridge",
        ),
        (
            "agent-ledger",
            "active-legacy",
            "Legacy continuity/state area should be reviewed for mapping into .raiden/state/",
        ),
        (
            "agent-prompts",
            "active-legacy",
            "Legacy repo-agent prompts should be reviewed for mapping into .raiden/local/prompts/",
        ),
    ]

    findings: list[LegacyArtifact] = []
    for rel_path, status, reason in candidates:
        path = target / rel_path
        if not path.exists():
            continue

        if rel_path == "AGENTS.md":
            content = path.read_text(encoding="utf-8")
            if is_raiden_bridge(content):
                continue

        findings.append(LegacyArtifact(path=rel_path, status=status, reason=reason))

    return findings


def build_repo_scan(target: Path) -> RepoScanResult:
    """Summarize repo readiness for install or update mode."""
    agents_path = target / "AGENTS.md"
    has_bridge = False
    if agents_path.exists():
        has_bridge = is_raiden_bridge(agents_path.read_text(encoding="utf-8"))

    return RepoScanResult(
        legacy_artifacts=scan_legacy_artifacts(target),
        has_instance_root=(target / ".raiden").exists(),
        has_bridge=has_bridge,
    )


def _build_legacy_review(findings: list[LegacyArtifact]) -> str:
    """Render the legacy review file content."""
    lines = [
        "# Legacy Review",
        "",
        "These repo-local agent surfaces predate the current RAIDEN Instance layout.",
        "Review them before assuming RAIDEN migration is complete.",
        "",
    ]

    if not findings:
        lines.extend([
            "- No legacy repo-agent artifacts were detected during install.",
            "",
        ])
        return "\n".join(lines)

    lines.extend([
        "## Detected Legacy Artifacts",
        "",
    ])
    for artifact in findings:
        lines.append(f"- `{artifact.path}`")
        lines.append(f"  Status: `{artifact.status}`")
        lines.append(f"  Reason: {artifact.reason}")

    lines.extend([
        "",
        "## Review Actions",
        "",
        "- Map legacy prompts into `.raiden/local/prompts/` where appropriate.",
        "- Map legacy continuity/state into `.raiden/state/` where appropriate.",
        "- Retire or archive stale legacy paths only after operator review.",
        "",
    ])
    return "\n".join(lines)


def _build_current_state(findings: list[LegacyArtifact]) -> str:
    lines = [
        "# Current State",
        "",
        "- Initial RAIDEN Instance scaffold created.",
    ]
    if findings:
        lines.append(
            f"- Legacy repo-agent artifacts detected; review `{LEGACY_REVIEW_RELATIVE_PATH}`."
        )
    lines.append("")
    return "\n".join(lines)


def _build_open_loops(findings: list[LegacyArtifact]) -> str:
    lines = ["# Open Loops", ""]
    if findings:
        lines.append(
            f"- Review legacy repo-agent artifacts listed in `{LEGACY_REVIEW_RELATIVE_PATH}`."
        )
        lines.append("")
        return "\n".join(lines)

    lines.append("")
    return "\n".join(lines)


def _archive_existing_agents(target: Path, *, force: bool) -> list[Path]:
    """Preserve a pre-RAIDEN AGENTS.md copy before replacing it with the bridge."""
    agents_path = target / "AGENTS.md"
    if not agents_path.exists():
        return []

    content = agents_path.read_text(encoding="utf-8")
    if is_raiden_bridge(content):
        return []

    archive_path = target / ".raiden" / "local" / "legacy" / "AGENTS.legacy.md"
    writes: list[Path] = []
    archived = _write_text(archive_path, content, force=force)
    if archived:
        writes.append(archive_path)
    return writes


def _instance_file_map(findings: list[LegacyArtifact]) -> dict[Path, str]:
    return {
        Path("AGENTS.md"): f"{BRIDGE_HEADER}\n\n{BRIDGE_BODY}",
        Path(".raiden/README.md"): (
            "# RAIDEN Instance\n\n"
            "This directory is the local RAIDEN Instance control plane.\n\n"
            "Read order:\n"
            "1. `.raiden/state/CURRENT_STATE.md`\n"
            "2. `.raiden/state/OPEN_LOOPS.md`\n"
            "3. `.raiden/state/LEGACY_REVIEW.md` when present\n"
            "4. `.raiden/local/README.md`\n"
            "5. `.raiden/writ/README.md`\n"
        ),
        Path(".raiden/local/README.md"): (
            "# Local Overlay\n\n"
            "Repo-specific rules, prompts, context, and exceptions live here.\n"
        ),
        Path(".raiden/state/README.md"): (
            "# Local Live State\n\n"
            "Repo-local continuity state lives here.\n"
        ),
        Path(".raiden/state/CURRENT_STATE.md"): _build_current_state(findings),
        Path(".raiden/state/GOALS.md"): "# Goals\n\n",
        Path(".raiden/state/OPEN_LOOPS.md"): _build_open_loops(findings),
        Path(".raiden/state/DECISIONS.md"): "# Decisions\n\n",
        Path(".raiden/state/LEGACY_REVIEW.md"): _build_legacy_review(findings),
        Path(".raiden/state/WORK_LOG.md"): "# Work Log\n\n",
    }


def preview_init_instance(target: Path, *, force: bool = False) -> InitPreviewResult:
    """Preview the writes an instance initialization would perform."""
    findings = scan_legacy_artifacts(target)
    planned_writes: list[PlannedWrite] = []
    file_map = _instance_file_map(findings)

    agents_path = target / "AGENTS.md"
    replace_agents = any(artifact.path == "AGENTS.md" for artifact in findings)
    if agents_path.exists():
        action = "overwrite" if force or replace_agents else "preserve"
        reason = (
            "Replace legacy startup instructions with the RAIDEN bridge"
            if replace_agents
            else "Existing bridge or local file preserved without --force"
        )
    else:
        action = "create"
        reason = "Create the repo-root RAIDEN startup bridge"
    planned_writes.append(
        PlannedWrite(path="AGENTS.md", action=action, reason=reason)
    )

    if replace_agents or force:
        planned_writes.append(
            PlannedWrite(
                path=".raiden/local/legacy/AGENTS.legacy.md",
                action="create" if not (target / ".raiden/local/legacy/AGENTS.legacy.md").exists() else "overwrite",
                reason="Preserve the pre-RAIDEN AGENTS.md for operator review",
            )
        )

    for rel_path in file_map:
        if rel_path == Path("AGENTS.md"):
            continue
        full_path = target / rel_path
        if full_path.exists():
            action = "overwrite" if force else "preserve"
            reason = "Installer-owned file replaced because --force was requested" if force else "Existing file preserved without --force"
        else:
            action = "create"
            reason = "Create required RAIDEN Instance file"
        planned_writes.append(
            PlannedWrite(path=str(rel_path).replace("\\", "/"), action=action, reason=reason)
        )

    metadata_path = target / ".raiden" / "instance" / "metadata.json"
    metadata_action = "overwrite" if force and metadata_path.exists() else ("create" if not metadata_path.exists() else "preserve")
    metadata_reason = (
        "Metadata replaced because --force was requested"
        if force and metadata_path.exists()
        else ("Create required instance metadata" if not metadata_path.exists() else "Existing metadata preserved without --force")
    )
    planned_writes.append(
        PlannedWrite(
            path=".raiden/instance/metadata.json",
            action=metadata_action,
            reason=metadata_reason,
        )
    )

    return InitPreviewResult(
        legacy_artifacts=findings,
        planned_writes=planned_writes,
    )


def init_instance(target: Path, *, force: bool = False) -> InitApplyResult:
    """Create the current downstream RAIDEN Instance skeleton."""
    writes: list[Path] = []
    findings = scan_legacy_artifacts(target)

    writes.extend(_archive_existing_agents(target, force=force))

    file_map = _instance_file_map(findings)
    agents_path = target / "AGENTS.md"
    replace_agents = any(artifact.path == "AGENTS.md" for artifact in findings)
    if _write_text(agents_path, file_map[Path("AGENTS.md")], force=force or replace_agents):
        writes.append(agents_path)

    for rel_path, content in file_map.items():
        if rel_path == Path("AGENTS.md"):
            continue
        path = target / rel_path
        if _write_text(path, content, force=force):
            writes.append(path)

    for directory in (
        target / ".raiden" / "writ",
        target / ".raiden" / "local" / "prompts",
        target / ".raiden" / "local" / "rules",
        target / ".raiden" / "local" / "context",
        target / ".raiden" / "instance",
    ):
        directory.mkdir(parents=True, exist_ok=True)

    metadata_path = target / ".raiden" / "instance" / "metadata.json"
    if _write_json(metadata_path, _metadata(INITIAL_INSTALLED_VERSION), force=force):
        writes.append(metadata_path)

    return InitApplyResult(
        written_paths=[str(path) for path in writes],
        legacy_artifacts=findings,
    )


def doctor(target: Path) -> DoctorResult:
    """Check whether a target repo has the current minimum instance shape."""
    required_paths = [
        target / "AGENTS.md",
        target / ".raiden" / "README.md",
        target / ".raiden" / "writ",
        target / ".raiden" / "local",
        target / ".raiden" / "state",
        target / ".raiden" / "instance",
        target / ".raiden" / "instance" / "metadata.json",
    ]
    missing = [str(path) for path in required_paths if not path.exists()]

    problems: list[str] = []
    if missing:
        problems.extend(f"missing: {path}" for path in missing)

    metadata_path = target / ".raiden" / "instance" / "metadata.json"
    if metadata_path.exists():
        try:
            data = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            problems.append(f"invalid metadata JSON: {exc}")
        else:
            expected = _metadata(data.get("installed_edict_version", ""))
            for key, value in expected.items():
                if data.get(key) != value:
                    problems.append(
                        f"metadata {key!r} is {data.get(key)!r}, expected {value!r}"
                    )

    return DoctorResult(ok=not problems, problems=problems)
