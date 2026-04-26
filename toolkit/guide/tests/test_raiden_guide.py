from __future__ import annotations

import sys
import importlib.util
from pathlib import Path


GUIDE_PATH = Path(__file__).resolve().parents[1] / "raiden_guide.py"
SPEC = importlib.util.spec_from_file_location("raiden_guide", GUIDE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
raiden_guide = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = raiden_guide
SPEC.loader.exec_module(raiden_guide)


def test_init_without_legacy_creates_clean_state(tmp_path: Path) -> None:
    result = raiden_guide.init_instance(tmp_path)

    assert result.written_paths
    assert result.legacy_artifacts == []

    legacy_review = tmp_path / ".raiden" / "state" / "LEGACY_REVIEW.md"
    current_state = tmp_path / ".raiden" / "state" / "CURRENT_STATE.md"
    open_loops = tmp_path / ".raiden" / "state" / "OPEN_LOOPS.md"

    assert "No legacy repo-agent artifacts were detected" in legacy_review.read_text(encoding="utf-8")
    assert "Legacy repo-agent artifacts detected" not in current_state.read_text(encoding="utf-8")
    assert open_loops.read_text(encoding="utf-8") == "# Open Loops\n"


def test_init_with_legacy_agents_archives_and_replaces_startup(tmp_path: Path) -> None:
    original_agents = "# Old Agent Startup\n\nRead agent-ledger first.\n"
    (tmp_path / "AGENTS.md").write_text(original_agents, encoding="utf-8")
    (tmp_path / "agent-ledger").mkdir()
    (tmp_path / "agent-prompts").mkdir()

    result = raiden_guide.init_instance(tmp_path)

    assert {artifact.path for artifact in result.legacy_artifacts} == {
        "AGENTS.md",
        "agent-ledger",
        "agent-prompts",
    }

    new_agents = (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
    archived_agents = (
        tmp_path / ".raiden" / "local" / "legacy" / "AGENTS.legacy.md"
    ).read_text(encoding="utf-8")
    legacy_review = (tmp_path / ".raiden" / "state" / "LEGACY_REVIEW.md").read_text(encoding="utf-8")
    readme = (tmp_path / ".raiden" / "README.md").read_text(encoding="utf-8")
    current_state = (tmp_path / ".raiden" / "state" / "CURRENT_STATE.md").read_text(encoding="utf-8")
    open_loops = (tmp_path / ".raiden" / "state" / "OPEN_LOOPS.md").read_text(encoding="utf-8")

    assert "Read `.raiden/README.md` before doing repo-local work." in new_agents
    assert archived_agents == original_agents
    assert "`AGENTS.md`" in legacy_review
    assert "`agent-ledger`" in legacy_review
    assert "`agent-prompts`" in legacy_review
    assert "LEGACY_REVIEW.md" in readme
    assert "Legacy repo-agent artifacts detected" in current_state
    assert "Review legacy repo-agent artifacts listed in `.raiden/state/LEGACY_REVIEW.md`." in open_loops
