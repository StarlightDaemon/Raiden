"""Tests for version parsing and compatibility checks."""

from __future__ import annotations

import pytest

from raiden_updater.version import Version, compare_versions, parse_version
from raiden_updater.compatibility import check_schema_compatibility
from raiden_updater.models import InstanceMetadata, PackageManifest, ManagedFileEntry


# ---------------------------------------------------------------------------
# Version parsing
# ---------------------------------------------------------------------------

def test_parse_version_valid():
    v = parse_version("1.2.3")
    assert v == Version(1, 2, 3)


def test_parse_version_invalid_format():
    with pytest.raises(ValueError):
        parse_version("1.2")


def test_parse_version_non_integer():
    with pytest.raises(ValueError):
        parse_version("1.2.x")


def test_parse_version_rejects_prerelease_suffix():
    with pytest.raises(ValueError):
        parse_version("1.2.3-alpha")


def test_parse_version_rejects_leading_zero_component():
    with pytest.raises(ValueError):
        parse_version("01.2.3")


def test_parse_version_rejects_negative_component():
    with pytest.raises(ValueError):
        parse_version("-1.2.3")


# ---------------------------------------------------------------------------
# Version comparison
# ---------------------------------------------------------------------------

def test_compare_upgrade():
    assert compare_versions("0.1.0", "0.2.0") == "upgrade"


def test_compare_same():
    assert compare_versions("0.2.0", "0.2.0") == "same"


def test_compare_downgrade():
    assert compare_versions("0.2.0", "0.1.0") == "downgrade"


# ---------------------------------------------------------------------------
# Schema compatibility
# ---------------------------------------------------------------------------

def _make_meta(schema: str = "1") -> InstanceMetadata:
    return InstanceMetadata(
        instance_schema_version=schema,
        instance_form_type="raiden-instance",
        installed_edict_version="0.1.0",
        managed_roots=[".raiden/writ"],
        overlay_roots=[".raiden/local"],
        live_state_roots=[".raiden/state"],
    )


def _make_manifest(schemas: list[str] | None = None) -> PackageManifest:
    return PackageManifest(
        package_type="edict",
        edict_version="0.2.0",
        compatible_instance_schemas=schemas or ["1"],
        managed_files=[ManagedFileEntry(path="README.md", hash="abc")],
        created_at="2026-04-24T00:00:00Z",
    )


def test_schema_compatible():
    ok, _ = check_schema_compatibility(_make_meta("1"), _make_manifest(["1"]))
    assert ok is True


def test_schema_incompatible():
    ok, detail = check_schema_compatibility(
        _make_meta("1"), _make_manifest(["2"])
    )
    assert ok is False
    assert "NOT" in detail
