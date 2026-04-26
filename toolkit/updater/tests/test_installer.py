from __future__ import annotations

from pathlib import Path

from raiden_updater.installer import (
    build_repo_scan,
    doctor,
    init_instance,
    preview_init_instance,
)


def test_repo_scan_detects_legacy_without_bridge(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text("# Old Agent Startup\n", encoding="utf-8")
    (tmp_path / "agent-prompts").mkdir()

    result = build_repo_scan(tmp_path)

    assert result.has_instance_root is False
    assert result.has_bridge is False
    assert {artifact.path for artifact in result.legacy_artifacts} == {
        "AGENTS.md",
        "agent-prompts",
    }


def test_init_preview_preserves_existing_files_without_force(tmp_path: Path) -> None:
    (tmp_path / ".raiden" / "state").mkdir(parents=True)
    (tmp_path / ".raiden" / "state" / "GOALS.md").write_text("# Existing\n", encoding="utf-8")

    result = preview_init_instance(tmp_path, force=False)
    actions = {item.path: item.action for item in result.planned_writes}

    assert actions["AGENTS.md"] == "create"
    assert actions[".raiden/state/GOALS.md"] == "preserve"


def test_init_instance_replaces_legacy_agents_and_doctor_passes(tmp_path: Path) -> None:
    (tmp_path / "AGENTS.md").write_text("# Old Agent Startup\n", encoding="utf-8")
    (tmp_path / "agent-ledger").mkdir()

    init_result = init_instance(tmp_path)
    doctor_result = doctor(tmp_path)

    assert init_result.written_paths
    assert {artifact.path for artifact in init_result.legacy_artifacts} == {
        "AGENTS.md",
        "agent-ledger",
    }
    assert "Read `.raiden/README.md` before doing repo-local work." in (
        tmp_path / "AGENTS.md"
    ).read_text(encoding="utf-8")
    assert doctor_result.ok is True
    assert doctor_result.problems == []
