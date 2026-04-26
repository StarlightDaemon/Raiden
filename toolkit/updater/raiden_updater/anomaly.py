"""Anomaly classification for the RAIDEN updater.

Detects conditions that are unusual enough to deserve operator attention.
Anomalies are classified as ``warn`` (proceed with caution) or ``block``
(refuse to apply).

The high-change ratio warning is intentionally constrained so small managed
packages do not warn on routine updates.
"""

from __future__ import annotations

from .models import (
    Anomaly,
    FileAction,
    InstanceMetadata,
    PackageManifest,
)


# ---------------------------------------------------------------------------
# Thresholds
# ---------------------------------------------------------------------------

#: Warn if more than this fraction of managed files are changing.
HIGH_CHANGE_RATIO = 0.50

#: Require at least this many managed files before the ratio warning applies.
HIGH_CHANGE_RATIO_MIN_TOTAL_FILES = 8

#: Warn if more than this many files change in absolute terms.
HIGH_CHANGE_COUNT = 10


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def classify_anomalies(
    metadata: InstanceMetadata,
    manifest: PackageManifest,
    file_actions: list[FileAction],
) -> list[Anomaly]:
    """Return a list of anomalies detected in the planned update.

    Parameters
    ----------
    metadata:
        The current instance metadata.
    manifest:
        The target package manifest.
    file_actions:
        The planned file actions from the planner.
    """
    anomalies: list[Anomaly] = []

    # --- Check for writes into overlay or live-state roots -----------------
    protected_roots = set(metadata.overlay_roots + metadata.live_state_roots)
    for entry in manifest.managed_files:
        for root in protected_roots:
            # Normalize: if a managed file path starts with a protected root
            # relative prefix, that's a boundary violation.
            if entry.path.startswith(root) or root.endswith(entry.path):
                anomalies.append(Anomaly(
                    code="protected_path_write",
                    severity="block",
                    detail=(
                        f"Package managed file {entry.path!r} collides with "
                        f"protected root {root!r}"
                    ),
                ))

    # --- Check for high change ratio --------------------------------------
    changing = [a for a in file_actions if a.action != "unchanged"]
    total = len(file_actions)
    if total >= HIGH_CHANGE_RATIO_MIN_TOTAL_FILES:
        ratio = len(changing) / total
        if ratio > HIGH_CHANGE_RATIO:
            anomalies.append(Anomaly(
                code="high_change_ratio",
                severity="warn",
                detail=(
                    f"{len(changing)}/{total} managed files "
                    f"({ratio:.0%}) are changing"
                ),
            ))

    # --- Check for high absolute change count ------------------------------
    if len(changing) > HIGH_CHANGE_COUNT:
        anomalies.append(Anomaly(
            code="high_change_count",
            severity="warn",
            detail=f"{len(changing)} managed files are changing",
        ))

    # --- Check for files in baseline but absent from new package -----------
    # Removals remain operator-visible even when they are apply-safe.
    removed = [a for a in file_actions if a.action == "remove"]
    if removed:
        anomalies.append(Anomaly(
            code="managed_file_removal",
            severity="warn",
            detail=(
                f"{len(removed)} managed file(s) in the installed baseline "
                f"are absent from the new package: "
                f"{', '.join(a.path for a in removed)}"
            ),
        ))

    return anomalies
