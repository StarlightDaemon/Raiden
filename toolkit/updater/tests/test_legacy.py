from pathlib import Path

from raiden_updater.legacy import archive_legacy_artifacts, scan_legacy_artifacts


def test_scan_legacy_artifacts_none(tmp_path: Path):
    """Test scanning when no legacy artifacts exist."""
    result = scan_legacy_artifacts(tmp_path)
    assert not result.has_legacy
    assert result.found_paths == []


def test_scan_legacy_artifacts_found(tmp_path: Path):
    """Test scanning when some legacy artifacts exist."""
    (tmp_path / "AGENTS.md").write_text("Old agents doc")
    (tmp_path / "agent-prompts").mkdir()
    (tmp_path / "agent-prompts" / "test.txt").write_text("test")

    result = scan_legacy_artifacts(tmp_path)
    assert result.has_legacy
    assert set(result.found_paths) == {"AGENTS.md", "agent-prompts"}


def test_archive_legacy_artifacts(tmp_path: Path):
    """Test compatibility archiving preserves legacy context via init flow."""
    (tmp_path / "AGENTS.md").write_text("Old agents doc")
    (tmp_path / "agent-ledger").mkdir()
    (tmp_path / "agent-ledger" / "record.txt").write_text("record")

    report = archive_legacy_artifacts(tmp_path)

    assert report is not None
    assert report.exists()
    report_text = report.read_text()
    assert "# Legacy Review" in report_text
    assert "`AGENTS.md`" in report_text
    assert "`agent-ledger`" in report_text

    # Verify startup bridge replaced and prior AGENTS preserved for review
    assert (tmp_path / "AGENTS.md").exists()
    assert "Read `.raiden/README.md` before doing repo-local work." in (
        tmp_path / "AGENTS.md"
    ).read_text()
    assert (tmp_path / ".raiden" / "local" / "legacy" / "AGENTS.legacy.md").read_text() == "Old agents doc"


def test_archive_legacy_artifacts_none(tmp_path: Path):
    """Test archiving does nothing if no legacy artifacts exist."""
    archive_dir = archive_legacy_artifacts(tmp_path)
    assert archive_dir is None
    assert not (tmp_path / ".raiden" / "legacy_archive").exists()
