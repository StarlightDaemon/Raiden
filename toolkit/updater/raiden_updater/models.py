"""Typed data models for the RAIDEN updater.

The package manifest, instance metadata, and installed baseline field sets
reflect the current local CLI updater canon.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Shared sub-models
# ---------------------------------------------------------------------------

@dataclass
class ManagedFileEntry:
    """A single managed file with its relative path and content hash."""

    path: str       # relative to writ root, e.g. "README.md"
    hash: str       # SHA-256 hex digest


# ---------------------------------------------------------------------------
# Instance metadata  (.raiden/instance/metadata.json, current local CLI canon)
# ---------------------------------------------------------------------------

@dataclass
class InstanceMetadata:
    """Typed model for the instance-side metadata record.

    Lives at ``.raiden/instance/metadata.json`` within a RAIDEN Instance.
    """

    instance_schema_version: str      # e.g. "1"
    instance_form_type: str           # "raiden-instance"
    installed_edict_version: str      # e.g. "0.1.0"
    managed_roots: list[str]          # e.g. [".raiden/writ"]
    overlay_roots: list[str]          # e.g. [".raiden/local"]
    live_state_roots: list[str]       # e.g. [".raiden/state"]


# ---------------------------------------------------------------------------
# Package manifest  (manifest.json at package root, current canon)
# ---------------------------------------------------------------------------

@dataclass
class PackageManifest:
    """Typed model for an Edict package manifest.

    Lives at the root of a package directory adjacent to ``payload/``.
    """

    package_type: str                         # "edict"
    edict_version: str                        # e.g. "0.2.0"
    compatible_instance_schemas: list[str]    # e.g. ["1"]
    managed_files: list[ManagedFileEntry]
    created_at: str                           # ISO-8601


# ---------------------------------------------------------------------------
# Installed baseline  (.raiden/instance/baseline.json, current local CLI canon)
# ---------------------------------------------------------------------------

@dataclass
class InstalledBaseline:
    """Typed model for the installed baseline record.

    Records the state of managed files at the time they were last installed
    or updated. Lives at ``.raiden/instance/baseline.json``.
    """

    installed_edict_version: str
    installed_at: str                         # ISO-8601
    managed_files: list[ManagedFileEntry]


# ---------------------------------------------------------------------------
# Plan result  (in-memory, returned by planner)
# ---------------------------------------------------------------------------

@dataclass
class FileAction:
    """A planned action for a single managed file."""

    path: str
    action: str      # "update", "add", "unchanged"
    reason: str


@dataclass
class Conflict:
    """A blocking conflict discovered during planning."""

    path: str
    conflict_type: str   # "local_modification", "path_collision",
                         # "missing_baseline", "missing_metadata"
    detail: str


@dataclass
class Anomaly:
    """An anomalous condition detected during planning."""

    code: str        # e.g. "high_change_ratio", "schema_mismatch"
    severity: str    # "warn" or "block"
    detail: str


@dataclass
class PlanResult:
    """Complete result of a plan operation."""

    compatible: bool
    compatibility_detail: str
    version_comparison: str         # "upgrade", "same", "downgrade"
    current_version: str
    target_version: str
    file_actions: list[FileAction]  = field(default_factory=list)
    conflicts: list[Conflict]       = field(default_factory=list)
    anomalies: list[Anomaly]        = field(default_factory=list)
    protected_paths: list[str]      = field(default_factory=list)
    can_apply: bool                 = False
    block_reason: Optional[str]     = None
