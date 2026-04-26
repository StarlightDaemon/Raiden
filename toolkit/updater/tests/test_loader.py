"""Tests for package-manifest loading and validation."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from raiden_updater.loader import (
    LoadError,
    load_installed_baseline,
    load_instance_metadata,
    load_package_manifest,
)
from .conftest import SAMPLE_INSTANCE, SAMPLE_PACKAGE


@pytest.fixture
def package_root(tmp_path: Path) -> Path:
    dest = tmp_path / "package"
    shutil.copytree(SAMPLE_PACKAGE, dest)
    return dest


@pytest.fixture
def instance_root(tmp_path: Path) -> Path:
    dest = tmp_path / "instance"
    shutil.copytree(SAMPLE_INSTANCE, dest)
    return dest


def _metadata_path(instance_root: Path) -> Path:
    return instance_root / ".raiden" / "instance" / "metadata.json"


def _baseline_path(instance_root: Path) -> Path:
    return instance_root / ".raiden" / "instance" / "baseline.json"


def test_load_instance_metadata_reads_current_canon_fields(instance_root: Path):
    metadata = load_instance_metadata(instance_root)

    assert metadata.instance_schema_version == "1"
    assert metadata.instance_form_type == "raiden-instance"
    assert metadata.installed_edict_version == "0.1.0"
    assert metadata.managed_roots == [".raiden/writ"]
    assert metadata.overlay_roots == [".raiden/local"]
    assert metadata.live_state_roots == [".raiden/state"]


@pytest.mark.parametrize(
    "missing_key",
    [
        "instance_schema_version",
        "instance_form_type",
        "installed_edict_version",
        "managed_roots",
        "overlay_roots",
        "live_state_roots",
    ],
)
def test_load_instance_metadata_requires_current_canon_fields(
    instance_root: Path,
    missing_key: str,
):
    metadata_path = _metadata_path(instance_root)
    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    del data[missing_key]
    metadata_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_instance_metadata(instance_root)


def test_load_instance_metadata_rejects_unknown_extra_fields(
    instance_root: Path,
):
    metadata_path = _metadata_path(instance_root)
    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    data["future_extension"] = "unsupported"
    metadata_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_instance_metadata(instance_root)


def test_load_instance_metadata_rejects_unsupported_roots(
    instance_root: Path,
):
    metadata_path = _metadata_path(instance_root)
    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    data["managed_roots"] = [".raiden/other"]
    metadata_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_instance_metadata(instance_root)


def test_load_instance_metadata_rejects_non_list_roots(
    instance_root: Path,
):
    metadata_path = _metadata_path(instance_root)
    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    data["managed_roots"] = ".raiden/writ"
    metadata_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_instance_metadata(instance_root)


def test_load_installed_baseline_reads_current_canon_fields(
    instance_root: Path,
):
    baseline = load_installed_baseline(instance_root)

    assert baseline is not None
    assert baseline.installed_edict_version == "0.1.0"
    assert baseline.installed_at == "2026-04-20T00:00:00Z"
    assert [entry.path for entry in baseline.managed_files] == [
        "README.md",
        "OPERATING_RULES.md",
        "OWNERSHIP_BOUNDARY.md",
    ]


@pytest.mark.parametrize(
    "missing_key",
    ["installed_edict_version", "installed_at", "managed_files"],
)
def test_load_installed_baseline_requires_current_canon_fields(
    instance_root: Path,
    missing_key: str,
):
    baseline_path = _baseline_path(instance_root)
    data = json.loads(baseline_path.read_text(encoding="utf-8"))
    del data[missing_key]
    baseline_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_installed_baseline(instance_root)


def test_load_installed_baseline_rejects_unknown_extra_fields(
    instance_root: Path,
):
    baseline_path = _baseline_path(instance_root)
    data = json.loads(baseline_path.read_text(encoding="utf-8"))
    data["future_extension"] = "unsupported"
    baseline_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_installed_baseline(instance_root)


def test_load_installed_baseline_rejects_invalid_hash(instance_root: Path):
    baseline_path = _baseline_path(instance_root)
    data = json.loads(baseline_path.read_text(encoding="utf-8"))
    data["managed_files"][0]["hash"] = "not-a-sha256"
    baseline_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_installed_baseline(instance_root)


def test_load_installed_baseline_rejects_duplicate_paths(instance_root: Path):
    baseline_path = _baseline_path(instance_root)
    data = json.loads(baseline_path.read_text(encoding="utf-8"))
    data["managed_files"].append(dict(data["managed_files"][0]))
    baseline_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_installed_baseline(instance_root)


def test_load_package_manifest_reads_current_canon_fields(package_root: Path):
    manifest = load_package_manifest(package_root)

    assert manifest.package_type == "edict"
    assert manifest.edict_version == "0.2.0"
    assert manifest.compatible_instance_schemas == ["1"]
    assert manifest.created_at == "2026-04-24T00:00:00Z"
    assert [entry.path for entry in manifest.managed_files] == [
        "README.md",
        "OPERATING_RULES.md",
        "OWNERSHIP_BOUNDARY.md",
    ]


@pytest.mark.parametrize(
    "missing_key",
    [
        "package_type",
        "edict_version",
        "compatible_instance_schemas",
        "managed_files",
        "created_at",
    ],
)
def test_load_package_manifest_requires_current_canon_fields(
    package_root: Path,
    missing_key: str,
):
    manifest_path = package_root / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    del data[missing_key]
    manifest_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_package_manifest(package_root)


def test_load_package_manifest_rejects_non_edict_package_type(
    package_root: Path,
):
    manifest_path = package_root / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["package_type"] = "other"
    manifest_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    with pytest.raises(LoadError):
        load_package_manifest(package_root)
