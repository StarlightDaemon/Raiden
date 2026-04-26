"""Tests for the plan command.

Covers: clean plan, conflict stop, no-op, schema incompatibility,
malformed manifest, dry-run no mutation, and delta-only detection.
"""

from __future__ import annotations

import json
from pathlib import Path

from raiden_updater.planner import create_plan
from .conftest import (
    SAMPLE_INSTANCE,
    SAMPLE_PACKAGE,
    corrupt_manifest,
    modify_instance_file,
    remove_package_file,
    set_manifest_field,
    set_metadata_field,
)

import shutil
import pytest


@pytest.fixture
def env(tmp_path: Path) -> tuple[Path, Path]:
    inst = tmp_path / "instance"
    pkg = tmp_path / "package"
    shutil.copytree(SAMPLE_INSTANCE, inst)
    shutil.copytree(SAMPLE_PACKAGE, pkg)
    return inst, pkg


# ---------------------------------------------------------------------------
# Test 1: Clean plan succeeds
# ---------------------------------------------------------------------------

def test_clean_plan_can_apply(env):
    inst, pkg = env
    plan = create_plan(inst, pkg)

    assert plan.compatible is True
    assert plan.version_comparison == "upgrade"
    assert plan.can_apply is True
    assert plan.block_reason is None
    assert len(plan.conflicts) == 0

    # Should have 2 updates (README.md, OPERATING_RULES.md) and 1 unchanged
    actions_by_type = {}
    for a in plan.file_actions:
        actions_by_type.setdefault(a.action, []).append(a.path)

    assert "update" in actions_by_type
    assert "unchanged" in actions_by_type
    assert "OWNERSHIP_BOUNDARY.md" in actions_by_type["unchanged"]


# ---------------------------------------------------------------------------
# Test 2: Conflict stops apply
# ---------------------------------------------------------------------------

def test_conflict_blocks_plan(env):
    inst, pkg = env
    # Locally modify a managed file so its hash no longer matches baseline
    modify_instance_file(inst, "README.md", "LOCALLY MODIFIED CONTENT")

    plan = create_plan(inst, pkg)

    assert plan.can_apply is False
    assert len(plan.conflicts) > 0
    assert plan.conflicts[0].conflict_type == "local_modification"


# ---------------------------------------------------------------------------
# Test 3: No-op when already current
# ---------------------------------------------------------------------------

def test_noop_when_already_current(env):
    inst, pkg = env
    # Make the instance already at 0.2.0 by updating metadata and matching
    # all file content
    set_metadata_field(inst, "installed_edict_version", "0.2.0")

    # Copy package payload files into writ so hashes match
    writ = inst / ".raiden" / "writ"
    payload = pkg / "payload"
    for f in payload.iterdir():
        shutil.copy2(f, writ / f.name)

    # Update baseline to match current hashes
    from raiden_updater.hasher import hash_file
    baseline_entries = []
    for f in sorted(writ.iterdir()):
        baseline_entries.append({
            "path": f.name,
            "hash": hash_file(f),
        })
    baseline_path = inst / ".raiden" / "instance" / "baseline.json"
    baseline_path.write_text(json.dumps({
        "installed_edict_version": "0.2.0",
        "installed_at": "2026-04-24T00:00:00Z",
        "managed_files": baseline_entries,
    }, indent=2), encoding="utf-8")

    plan = create_plan(inst, pkg)

    assert plan.version_comparison == "same"
    assert plan.can_apply is False
    assert "up to date" in plan.block_reason.lower()


# ---------------------------------------------------------------------------
# Test 4: Changed-files-only (delta detection)
# ---------------------------------------------------------------------------

def test_delta_only_detection(env):
    inst, pkg = env
    plan = create_plan(inst, pkg)

    update_actions = [a for a in plan.file_actions if a.action == "update"]
    unchanged_actions = [a for a in plan.file_actions if a.action == "unchanged"]

    # README.md and OPERATING_RULES.md should update
    assert len(update_actions) == 2
    update_paths = {a.path for a in update_actions}
    assert "README.md" in update_paths
    assert "OPERATING_RULES.md" in update_paths

    # OWNERSHIP_BOUNDARY.md should be unchanged
    assert len(unchanged_actions) == 1
    assert unchanged_actions[0].path == "OWNERSHIP_BOUNDARY.md"


# ---------------------------------------------------------------------------
# Test 7: Incompatible schema rejected
# ---------------------------------------------------------------------------

def test_incompatible_schema(env):
    inst, pkg = env
    set_manifest_field(pkg, "compatible_instance_schemas", ["2"])

    plan = create_plan(inst, pkg)

    assert plan.compatible is False
    assert plan.can_apply is False
    assert any(c.conflict_type == "schema_incompatibility" for c in plan.conflicts)


# ---------------------------------------------------------------------------
# Test 8: Malformed manifest rejected
# ---------------------------------------------------------------------------

def test_malformed_manifest(env):
    inst, pkg = env
    corrupt_manifest(pkg)

    plan = create_plan(inst, pkg)

    assert plan.can_apply is False
    assert plan.compatible is False
    assert "manifest" in plan.block_reason.lower() or "json" in plan.block_reason.lower()


def test_invalid_version_blocks_plan(env):
    inst, pkg = env
    set_manifest_field(pkg, "edict_version", "0.2.0-alpha")

    plan = create_plan(inst, pkg)

    assert plan.can_apply is False
    assert any(c.conflict_type == "invalid_version" for c in plan.conflicts)


# ---------------------------------------------------------------------------
# Test 11: Dry-run (plan) produces no mutations
# ---------------------------------------------------------------------------

def test_plan_no_mutation(env):
    inst, pkg = env

    # Snapshot all files before plan
    before = {}
    for f in (inst / ".raiden").rglob("*"):
        if f.is_file():
            before[str(f.relative_to(inst))] = f.read_bytes()

    _ = create_plan(inst, pkg)

    # Verify no files changed
    for f in (inst / ".raiden").rglob("*"):
        if f.is_file():
            rel = str(f.relative_to(inst))
            assert rel in before, f"Unexpected new file: {rel}"
            assert f.read_bytes() == before[rel], f"File mutated: {rel}"

    # Verify no files deleted
    for rel in before:
        assert (inst / rel).exists(), f"File deleted: {rel}"


# ---------------------------------------------------------------------------
# Protected paths are listed in plan
# ---------------------------------------------------------------------------

def test_protected_paths_listed(env):
    inst, pkg = env
    plan = create_plan(inst, pkg)

    assert ".raiden/local" in plan.protected_paths
    assert ".raiden/state" in plan.protected_paths


def test_removal_is_planned_as_safe_auto_remove(env):
    inst, pkg = env
    remove_package_file(pkg, "OWNERSHIP_BOUNDARY.md")

    plan = create_plan(inst, pkg)

    remove_actions = [a for a in plan.file_actions if a.action == "remove"]
    assert any(a.path == "OWNERSHIP_BOUNDARY.md" for a in remove_actions)
    assert any(a.code == "managed_file_removal" for a in plan.anomalies)
    assert plan.can_apply is True


def test_locally_modified_removal_candidate_blocks_plan(env):
    inst, pkg = env
    modify_instance_file(inst, "OWNERSHIP_BOUNDARY.md", "LOCALLY MODIFIED")
    remove_package_file(pkg, "OWNERSHIP_BOUNDARY.md")

    plan = create_plan(inst, pkg)

    assert plan.can_apply is False
    assert any(
        c.path == "OWNERSHIP_BOUNDARY.md"
        and c.conflict_type == "local_modification"
        for c in plan.conflicts
    )


def test_missing_baseline_blocks_non_empty_managed_root(env):
    inst, pkg = env
    baseline_path = inst / ".raiden" / "instance" / "baseline.json"
    baseline_path.unlink()

    plan = create_plan(inst, pkg)

    assert plan.can_apply is False
    assert any(c.conflict_type == "missing_baseline" for c in plan.conflicts)


def test_missing_baseline_allowed_for_empty_managed_root(env):
    inst, pkg = env
    baseline_path = inst / ".raiden" / "instance" / "baseline.json"
    baseline_path.unlink()

    writ = inst / ".raiden" / "writ"
    shutil.rmtree(writ)
    writ.mkdir(parents=True)

    plan = create_plan(inst, pkg)

    assert plan.can_apply is True
    assert all(a.action == "add" for a in plan.file_actions)
    assert not plan.conflicts
