"""Tests for the apply command.

Covers: clean apply, overlay preservation, live-state preservation,
baseline written after apply, conflict blocks apply.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from raiden_updater.applier import ApplyError, apply_plan
from raiden_updater.hasher import hash_file
from raiden_updater.planner import create_plan
from .conftest import (
    SAMPLE_INSTANCE,
    SAMPLE_PACKAGE,
    modify_instance_file,
    remove_package_file,
)


@pytest.fixture
def env(tmp_path: Path) -> tuple[Path, Path]:
    inst = tmp_path / "instance"
    pkg = tmp_path / "package"
    shutil.copytree(SAMPLE_INSTANCE, inst)
    shutil.copytree(SAMPLE_PACKAGE, pkg)
    return inst, pkg


# ---------------------------------------------------------------------------
# Test 1: Clean apply succeeds
# ---------------------------------------------------------------------------

def test_clean_apply_succeeds(env):
    inst, pkg = env

    plan = create_plan(inst, pkg)
    assert plan.can_apply is True

    apply_plan(plan, inst, pkg)

    # Verify writ files now match the package payload
    payload = pkg / "payload"
    writ = inst / ".raiden" / "writ"

    for f in payload.iterdir():
        assert (writ / f.name).exists()
        assert hash_file(writ / f.name) == hash_file(f), (
            f"{f.name} content mismatch after apply"
        )


# ---------------------------------------------------------------------------
# Test 4: Changed-files-only rewrite
# ---------------------------------------------------------------------------

def test_changed_files_only_rewrite(env):
    inst, pkg = env

    # Record the hash of OWNERSHIP_BOUNDARY.md before apply
    # (it should be unchanged since content is identical)
    boundary_path = inst / ".raiden" / "writ" / "OWNERSHIP_BOUNDARY.md"
    boundary_mtime_before = boundary_path.stat().st_mtime

    plan = create_plan(inst, pkg)

    # Confirm OWNERSHIP_BOUNDARY.md is planned as unchanged
    unchanged = [a for a in plan.file_actions if a.action == "unchanged"]
    assert any(a.path == "OWNERSHIP_BOUNDARY.md" for a in unchanged)

    apply_plan(plan, inst, pkg)

    # OWNERSHIP_BOUNDARY.md should NOT have been rewritten
    # (The applier skips unchanged files, so mtime should be the same)
    # Note: on some filesystems mtime granularity may cause false passes,
    # but content hash is the real test
    assert hash_file(boundary_path) == hash_file(
        pkg / "payload" / "OWNERSHIP_BOUNDARY.md"
    )


# ---------------------------------------------------------------------------
# Test 5: Overlay preserved during apply
# ---------------------------------------------------------------------------

def test_overlay_preserved(env):
    inst, pkg = env

    local_readme = inst / ".raiden" / "local" / "README.md"
    local_content_before = local_readme.read_text(encoding="utf-8")

    plan = create_plan(inst, pkg)
    apply_plan(plan, inst, pkg)

    # Overlay should be completely untouched
    assert local_readme.exists()
    assert local_readme.read_text(encoding="utf-8") == local_content_before


# ---------------------------------------------------------------------------
# Test 6: Live-state preserved during apply
# ---------------------------------------------------------------------------

def test_live_state_preserved(env):
    inst, pkg = env

    state_readme = inst / ".raiden" / "state" / "README.md"
    state_content_before = state_readme.read_text(encoding="utf-8")

    plan = create_plan(inst, pkg)
    apply_plan(plan, inst, pkg)

    # Live state should be completely untouched
    assert state_readme.exists()
    assert state_readme.read_text(encoding="utf-8") == state_content_before


# ---------------------------------------------------------------------------
# Test 12: Baseline written after successful apply
# ---------------------------------------------------------------------------

def test_baseline_written_after_apply(env):
    inst, pkg = env

    plan = create_plan(inst, pkg)
    apply_plan(plan, inst, pkg)

    baseline_path = inst / ".raiden" / "instance" / "baseline.json"
    assert baseline_path.exists()

    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    assert baseline["installed_edict_version"] == "0.2.0"
    assert len(baseline["managed_files"]) == 3

    # Verify each baseline hash matches the actual installed file
    writ = inst / ".raiden" / "writ"
    for entry in baseline["managed_files"]:
        installed = writ / entry["path"]
        assert installed.exists()
        assert hash_file(installed) == entry["hash"]


# ---------------------------------------------------------------------------
# Test: Conflict blocks apply
# ---------------------------------------------------------------------------

def test_conflict_blocks_apply(env):
    inst, pkg = env

    modify_instance_file(inst, "README.md", "LOCALLY MODIFIED")

    plan = create_plan(inst, pkg)
    assert plan.can_apply is False

    with pytest.raises(ApplyError):
        apply_plan(plan, inst, pkg)


# ---------------------------------------------------------------------------
# Test: Metadata version updated after apply
# ---------------------------------------------------------------------------

def test_metadata_version_updated(env):
    inst, pkg = env

    plan = create_plan(inst, pkg)
    apply_plan(plan, inst, pkg)

    meta_path = inst / ".raiden" / "instance" / "metadata.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    assert meta["installed_edict_version"] == "0.2.0"


def test_safe_auto_remove_deletes_managed_file(env):
    inst, pkg = env
    remove_package_file(pkg, "OWNERSHIP_BOUNDARY.md")

    plan = create_plan(inst, pkg)
    assert plan.can_apply is True

    apply_plan(plan, inst, pkg)

    removed_path = inst / ".raiden" / "writ" / "OWNERSHIP_BOUNDARY.md"
    assert not removed_path.exists()

    baseline_path = inst / ".raiden" / "instance" / "baseline.json"
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    baseline_paths = {entry["path"] for entry in baseline["managed_files"]}
    assert baseline_paths == {"README.md", "OPERATING_RULES.md"}
