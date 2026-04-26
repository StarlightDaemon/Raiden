"""Tests for anomaly classification."""

from __future__ import annotations

from raiden_updater.anomaly import classify_anomalies
from raiden_updater.models import (
    Anomaly,
    FileAction,
    InstanceMetadata,
    ManagedFileEntry,
    PackageManifest,
)


def _make_meta() -> InstanceMetadata:
    return InstanceMetadata(
        instance_schema_version="1",
        instance_form_type="raiden-instance",
        installed_edict_version="0.1.0",
        managed_roots=[".raiden/writ"],
        overlay_roots=[".raiden/local"],
        live_state_roots=[".raiden/state"],
    )


def _make_manifest(
    files: list[ManagedFileEntry] | None = None,
) -> PackageManifest:
    return PackageManifest(
        package_type="edict",
        edict_version="0.2.0",
        compatible_instance_schemas=["1"],
        managed_files=files or [ManagedFileEntry(path="README.md", hash="abc")],
        created_at="2026-04-24T00:00:00Z",
    )


# ---------------------------------------------------------------------------
# Test 9: Anomaly warn triggers
# ---------------------------------------------------------------------------

def test_high_change_ratio_warns_with_minimum_file_count():
    meta = _make_meta()
    manifest = _make_manifest([
        ManagedFileEntry(path=f"{name}.md", hash=name)
        for name in "abcdefgh"
    ])
    # 5 of 8 files are changing (>50% and at least 8 total)
    actions = [
        FileAction(path="a.md", action="update", reason="changed"),
        FileAction(path="b.md", action="update", reason="changed"),
        FileAction(path="c.md", action="update", reason="changed"),
        FileAction(path="d.md", action="update", reason="changed"),
        FileAction(path="e.md", action="update", reason="changed"),
        FileAction(path="f.md", action="unchanged", reason="same"),
        FileAction(path="g.md", action="unchanged", reason="same"),
        FileAction(path="h.md", action="unchanged", reason="same"),
    ]

    anomalies = classify_anomalies(meta, manifest, actions)

    warn_codes = [a.code for a in anomalies if a.severity == "warn"]
    assert "high_change_ratio" in warn_codes


def test_high_change_ratio_does_not_warn_for_small_package():
    meta = _make_meta()
    manifest = _make_manifest([
        ManagedFileEntry(path="a.md", hash="1"),
        ManagedFileEntry(path="b.md", hash="2"),
        ManagedFileEntry(path="c.md", hash="3"),
    ])
    actions = [
        FileAction(path="a.md", action="update", reason="changed"),
        FileAction(path="b.md", action="update", reason="changed"),
        FileAction(path="c.md", action="update", reason="changed"),
    ]

    anomalies = classify_anomalies(meta, manifest, actions)

    warn_codes = [a.code for a in anomalies if a.severity == "warn"]
    assert "high_change_ratio" not in warn_codes


# ---------------------------------------------------------------------------
# Test 10: Anomaly block prevents apply (protected path write)
# ---------------------------------------------------------------------------

def test_protected_path_write_blocks():
    meta = _make_meta()
    # Package tries to write a file whose path starts with a protected root
    manifest = _make_manifest([
        ManagedFileEntry(path=".raiden/local/evil.md", hash="bad"),
    ])
    actions = [
        FileAction(path=".raiden/local/evil.md", action="add", reason="new"),
    ]

    anomalies = classify_anomalies(meta, manifest, actions)

    block_codes = [a.code for a in anomalies if a.severity == "block"]
    assert "protected_path_write" in block_codes


# ---------------------------------------------------------------------------
# Test: Removal detected as warn
# ---------------------------------------------------------------------------

def test_removal_warned():
    meta = _make_meta()
    manifest = _make_manifest()
    actions = [
        FileAction(path="OLD_FILE.md", action="remove",
                   reason="absent from new package"),
    ]

    anomalies = classify_anomalies(meta, manifest, actions)

    warn_codes = [a.code for a in anomalies if a.severity == "warn"]
    assert "managed_file_removal" in warn_codes


# ---------------------------------------------------------------------------
# Test: No anomalies on clean small update
# ---------------------------------------------------------------------------

def test_no_anomalies_on_small_update():
    meta = _make_meta()
    manifest = _make_manifest([
        ManagedFileEntry(path="a.md", hash="1"),
        ManagedFileEntry(path="b.md", hash="2"),
        ManagedFileEntry(path="c.md", hash="3"),
    ])
    # Only 1 of 3 files is changing (<= 50%)
    actions = [
        FileAction(path="a.md", action="update", reason="changed"),
        FileAction(path="b.md", action="unchanged", reason="same"),
        FileAction(path="c.md", action="unchanged", reason="same"),
    ]

    anomalies = classify_anomalies(meta, manifest, actions)

    # Should be empty
    assert len(anomalies) == 0
