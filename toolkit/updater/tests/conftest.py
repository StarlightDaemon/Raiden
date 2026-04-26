"""Shared test fixtures and helpers for the RAIDEN updater test suite."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

# Path to the static fixtures directory
FIXTURES_DIR = Path(__file__).resolve().parent.parent / "fixtures"
SAMPLE_PACKAGE = FIXTURES_DIR / "sample_package"
SAMPLE_INSTANCE = FIXTURES_DIR / "sample_instance"


@pytest.fixture
def tmp_instance(tmp_path: Path) -> Path:
    """Copy the sample instance into a temp directory and return its root."""
    dest = tmp_path / "instance"
    shutil.copytree(SAMPLE_INSTANCE, dest)
    return dest


@pytest.fixture
def tmp_package(tmp_path: Path) -> Path:
    """Copy the sample package into a temp directory and return its root."""
    dest = tmp_path / "package"
    shutil.copytree(SAMPLE_PACKAGE, dest)
    return dest


@pytest.fixture
def tmp_instance_and_package(tmp_path: Path) -> tuple[Path, Path]:
    """Provide both instance and package in a shared temp root."""
    inst = tmp_path / "instance"
    pkg = tmp_path / "package"
    shutil.copytree(SAMPLE_INSTANCE, inst)
    shutil.copytree(SAMPLE_PACKAGE, pkg)
    return inst, pkg


# ---------------------------------------------------------------------------
# Helpers for creating variant fixtures on the fly
# ---------------------------------------------------------------------------

def modify_instance_file(instance_root: Path, rel_path: str, content: str) -> None:
    """Overwrite a file inside the instance writ."""
    target = instance_root / ".raiden" / "writ" / rel_path
    target.write_text(content, encoding="utf-8")


def set_metadata_field(instance_root: Path, key: str, value) -> None:
    """Patch a single field in instance metadata.json."""
    meta_path = instance_root / ".raiden" / "instance" / "metadata.json"
    data = json.loads(meta_path.read_text(encoding="utf-8"))
    data[key] = value
    meta_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def set_manifest_field(package_root: Path, key: str, value) -> None:
    """Patch a single field in the package manifest.json."""
    manifest_path = package_root / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data[key] = value
    manifest_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def remove_package_file(package_root: Path, rel_path: str) -> None:
    """Remove a managed file from the package payload and manifest."""
    payload_path = package_root / "payload" / rel_path
    if payload_path.exists():
        payload_path.unlink()

    manifest_path = package_root / "manifest.json"
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    data["managed_files"] = [
        entry for entry in data["managed_files"]
        if entry["path"] != rel_path
    ]
    manifest_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def corrupt_manifest(package_root: Path) -> None:
    """Replace the package manifest with invalid JSON."""
    manifest_path = package_root / "manifest.json"
    manifest_path.write_text("{{{INVALID JSON", encoding="utf-8")
