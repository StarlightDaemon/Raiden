"""Load and validate RAIDEN updater metadata files.

Handles JSON deserialization and structural validation for:
- InstanceMetadata  (.raiden/instance/metadata.json)
- PackageManifest   (manifest.json at package root)
- InstalledBaseline (.raiden/instance/baseline.json)
"""

from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
from typing import Any

from .models import (
    InstalledBaseline,
    InstanceMetadata,
    ManagedFileEntry,
    PackageManifest,
)


class LoadError(Exception):
    """Raised when a metadata file cannot be loaded or validated."""


INSTANCE_METADATA_KEYS = {
    "instance_schema_version",
    "instance_form_type",
    "installed_edict_version",
    "managed_roots",
    "overlay_roots",
    "live_state_roots",
}

INSTALLED_BASELINE_KEYS = {
    "installed_edict_version",
    "installed_at",
    "managed_files",
}

MANAGED_FILE_KEYS = {"path", "hash"}

SUPPORTED_INSTANCE_FORM_TYPE = "raiden-instance"
SUPPORTED_MANAGED_ROOTS = [".raiden/writ"]
SUPPORTED_OVERLAY_ROOTS = [".raiden/local"]
SUPPORTED_LIVE_STATE_ROOTS = [".raiden/state"]


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _read_json(path: Path) -> Any:
    """Read and parse a JSON file, wrapping errors."""
    if not path.exists():
        raise LoadError(f"File not found: {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as exc:
        raise LoadError(f"Invalid JSON in {path}: {exc}") from exc


def _require_keys(data: dict, keys: list[str], context: str) -> None:
    """Raise LoadError if any required key is missing."""
    missing = [k for k in keys if k not in data]
    if missing:
        raise LoadError(
            f"Missing required keys in {context}: {', '.join(missing)}"
        )


def _require_exact_keys(data: dict, keys: set[str], context: str) -> None:
    """Raise LoadError unless *data* has exactly the expected keys."""
    missing = sorted(keys - set(data))
    unknown = sorted(set(data) - keys)
    details: list[str] = []
    if missing:
        details.append(f"missing required keys: {', '.join(missing)}")
    if unknown:
        details.append(f"unknown keys: {', '.join(unknown)}")
    if details:
        raise LoadError(f"Invalid keys in {context}: {'; '.join(details)}")


def _require_string(data: dict, key: str, context: str) -> str:
    """Return a required string field."""
    value = data[key]
    if not isinstance(value, str) or value == "":
        raise LoadError(f"{key} must be a non-empty string in {context}")
    return value


def _require_string_list(
    data: dict,
    key: str,
    context: str,
    *,
    expected: list[str] | None = None,
) -> list[str]:
    """Return a required list of strings, optionally fixed to *expected*."""
    value = data[key]
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item for item in value
    ):
        raise LoadError(f"{key} must be a list of non-empty strings in {context}")
    if expected is not None and value != expected:
        raise LoadError(
            f"{key} must be {expected!r} for the current local CLI in {context}"
        )
    return value


def _validate_managed_file_path(value: Any, context: str) -> str:
    """Validate a managed-file path as a safe relative POSIX path."""
    if not isinstance(value, str) or value == "":
        raise LoadError(f"managed file path must be a non-empty string in {context}")
    if "\\" in value:
        raise LoadError(f"managed file path must use POSIX separators in {context}")
    if value.endswith("/"):
        raise LoadError(f"managed file path must identify a file in {context}")

    path = PurePosixPath(value)
    if path.is_absolute() or path == PurePosixPath(".") or ".." in path.parts:
        raise LoadError(f"managed file path must be relative in {context}")
    return value


def _validate_sha256(value: Any, context: str) -> str:
    """Validate a SHA-256 hex digest string."""
    if not isinstance(value, str) or len(value) != 64:
        raise LoadError(f"managed file hash must be a SHA-256 hex digest in {context}")
    try:
        int(value, 16)
    except ValueError as exc:
        raise LoadError(
            f"managed file hash must be a SHA-256 hex digest in {context}"
        ) from exc
    return value


def _parse_managed_files(raw: Any, context: str) -> list[ManagedFileEntry]:
    """Parse a list of managed-file entries from raw JSON data."""
    if not isinstance(raw, list):
        raise LoadError(f"managed_files must be a list in {context}")
    entries: list[ManagedFileEntry] = []
    seen_paths: set[str] = set()
    for i, item in enumerate(raw):
        if not isinstance(item, dict):
            raise LoadError(
                f"managed_files[{i}] must be an object in {context}"
            )
        _require_exact_keys(item, MANAGED_FILE_KEYS, f"{context} managed_files[{i}]")
        entry_path = _validate_managed_file_path(
            item["path"], f"{context} managed_files[{i}]"
        )
        if entry_path in seen_paths:
            raise LoadError(
                f"duplicate managed file path {entry_path!r} in {context}"
            )
        seen_paths.add(entry_path)
        entries.append(ManagedFileEntry(
            path=entry_path,
            hash=_validate_sha256(item["hash"], f"{context} managed_files[{i}]"),
        ))
    return entries


# ---------------------------------------------------------------------------
# Public loaders
# ---------------------------------------------------------------------------

def load_instance_metadata(instance_root: Path) -> InstanceMetadata:
    """Load and validate ``.raiden/instance/metadata.json``.

    Parameters
    ----------
    instance_root:
        Path to the target repository root (parent of ``.raiden/``).
    """
    path = instance_root / ".raiden" / "instance" / "metadata.json"
    data = _read_json(path)
    if not isinstance(data, dict):
        raise LoadError(f"Expected object in {path}")

    _require_exact_keys(data, INSTANCE_METADATA_KEYS, str(path))

    instance_form_type = _require_string(data, "instance_form_type", str(path))
    if instance_form_type != SUPPORTED_INSTANCE_FORM_TYPE:
        raise LoadError(
            "instance_form_type must be "
            f"{SUPPORTED_INSTANCE_FORM_TYPE!r} in {path}"
        )

    return InstanceMetadata(
        instance_schema_version=_require_string(
            data, "instance_schema_version", str(path)
        ),
        instance_form_type=instance_form_type,
        installed_edict_version=_require_string(
            data, "installed_edict_version", str(path)
        ),
        managed_roots=_require_string_list(
            data,
            "managed_roots",
            str(path),
            expected=SUPPORTED_MANAGED_ROOTS,
        ),
        overlay_roots=_require_string_list(
            data,
            "overlay_roots",
            str(path),
            expected=SUPPORTED_OVERLAY_ROOTS,
        ),
        live_state_roots=_require_string_list(
            data,
            "live_state_roots",
            str(path),
            expected=SUPPORTED_LIVE_STATE_ROOTS,
        ),
    )


def load_package_manifest(package_root: Path) -> PackageManifest:
    """Load and validate ``manifest.json`` from a package directory.

    Parameters
    ----------
    package_root:
        Path to the package root (directory containing ``manifest.json``
        and ``payload/``).
    """
    path = package_root / "manifest.json"
    data = _read_json(path)
    if not isinstance(data, dict):
        raise LoadError(f"Expected object in {path}")

    _require_keys(
        data,
        [
            "package_type",
            "edict_version",
            "compatible_instance_schemas",
            "managed_files",
            "created_at",
        ],
        str(path),
    )

    if data["package_type"] != "edict":
        raise LoadError(
            f"Unsupported package_type {data['package_type']!r} in {path}"
        )

    return PackageManifest(
        package_type=_require_string(data, "package_type", str(path)),
        edict_version=_require_string(data, "edict_version", str(path)),
        compatible_instance_schemas=_require_string_list(
            data, "compatible_instance_schemas", str(path)
        ),
        managed_files=_parse_managed_files(data["managed_files"], str(path)),
        created_at=_require_string(data, "created_at", str(path)),
    )


def load_installed_baseline(instance_root: Path) -> InstalledBaseline | None:
    """Load ``.raiden/instance/baseline.json`` if it exists.

    Returns ``None`` if the baseline file does not exist (e.g. fresh
    instance that has never been updated via the updater).
    """
    path = instance_root / ".raiden" / "instance" / "baseline.json"
    if not path.exists():
        return None

    data = _read_json(path)
    if not isinstance(data, dict):
        raise LoadError(f"Expected object in {path}")

    _require_exact_keys(data, INSTALLED_BASELINE_KEYS, str(path))

    return InstalledBaseline(
        installed_edict_version=_require_string(
            data, "installed_edict_version", str(path)
        ),
        installed_at=_require_string(data, "installed_at", str(path)),
        managed_files=_parse_managed_files(data["managed_files"], str(path)),
    )
