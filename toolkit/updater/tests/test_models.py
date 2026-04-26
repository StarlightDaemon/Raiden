"""Tests for data model validation and construction."""

from __future__ import annotations

from raiden_updater.models import (
    Anomaly,
    Conflict,
    FileAction,
    InstalledBaseline,
    InstanceMetadata,
    ManagedFileEntry,
    PackageManifest,
    PlanResult,
)


def test_managed_file_entry_creation():
    entry = ManagedFileEntry(path="README.md", hash="abc123")
    assert entry.path == "README.md"
    assert entry.hash == "abc123"


def test_instance_metadata_creation():
    meta = InstanceMetadata(
        instance_schema_version="1",
        instance_form_type="raiden-instance",
        installed_edict_version="0.1.0",
        managed_roots=[".raiden/writ"],
        overlay_roots=[".raiden/local"],
        live_state_roots=[".raiden/state"],
    )
    assert meta.instance_schema_version == "1"
    assert meta.managed_roots == [".raiden/writ"]


def test_package_manifest_creation():
    manifest = PackageManifest(
        package_type="edict",
        edict_version="0.2.0",
        compatible_instance_schemas=["1"],
        managed_files=[ManagedFileEntry(path="README.md", hash="abc")],
        created_at="2026-04-24T00:00:00Z",
    )
    assert manifest.edict_version == "0.2.0"
    assert len(manifest.managed_files) == 1


def test_plan_result_defaults():
    plan = PlanResult(
        compatible=True,
        compatibility_detail="ok",
        version_comparison="upgrade",
        current_version="0.1.0",
        target_version="0.2.0",
    )
    assert plan.can_apply is False  # default
    assert plan.file_actions == []
    assert plan.conflicts == []
    assert plan.anomalies == []
    assert plan.block_reason is None
