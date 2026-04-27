"""Compatibility wrappers for legacy-artifact inspection.

This shim wraps ``raiden_updater.installer.scan_legacy_artifacts`` and
``init_instance()`` behind a stable interface so that callers using the old
``raiden_updater.legacy`` import path continue to work after legacy detection
was consolidated into ``installer``. The original external consumer is unknown;
the shim was created defensively during that consolidation. It can be dropped
once no code outside this package imports ``raiden_updater.legacy`` directly
(verify with a repo-wide grep before removal).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .installer import LEGACY_REVIEW_RELATIVE_PATH, init_instance, scan_legacy_artifacts as _scan


@dataclass(frozen=True)
class LegacyScanResult:
    """Compatibility result for legacy scanning."""

    found_paths: list[str]
    has_legacy: bool


def scan_legacy_artifacts(instance_root: Path) -> LegacyScanResult:
    """Scan a repo root for legacy artifacts using canonical installer rules."""
    findings = _scan(instance_root)
    found_paths = [artifact.path for artifact in findings]
    return LegacyScanResult(
        found_paths=found_paths,
        has_legacy=bool(found_paths),
    )


def archive_legacy_artifacts(instance_root: Path) -> Path | None:
    """Preserve legacy startup material using the canonical installer flow.

    This does not perform a destructive standalone archive pass. It delegates to
    ``init_instance()`` so legacy handling stays consistent with the canonical
    startup bridge and local-state review behavior.
    """
    result = init_instance(instance_root, force=False)
    if not result.legacy_artifacts:
        return None
    return instance_root / LEGACY_REVIEW_RELATIVE_PATH
