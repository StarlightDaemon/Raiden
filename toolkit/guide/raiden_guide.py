"""Guided RAIDEN setup helper.

This is an operator-facing wrapper around the current local CLI updater flow.
It scaffolds a downstream RAIDEN Instance and then delegates install/update
planning and applying to ``raiden_updater``.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


TOOLKIT_ROOT = Path(__file__).resolve().parents[1]
UPDATER_ROOT = TOOLKIT_ROOT / "updater"
if str(UPDATER_ROOT) not in sys.path:
    sys.path.insert(0, str(UPDATER_ROOT))

from raiden_updater.applier import ApplyError, apply_plan  # noqa: E402
from raiden_updater.cli import _format_plan  # noqa: E402
from raiden_updater.planner import create_plan  # noqa: E402


INSTANCE_SCHEMA_VERSION = "1"
INSTANCE_FORM_TYPE = "raiden-instance"
INITIAL_INSTALLED_VERSION = "0.0.0"


def _write_text(path: Path, content: str, *, force: bool) -> bool:
    """Write text if missing or forced. Return True when a write happened."""
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def _write_json(path: Path, data: dict, *, force: bool) -> bool:
    """Write JSON if missing or forced. Return True when a write happened."""
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return True


def _metadata(installed_version: str) -> dict:
    return {
        "instance_schema_version": INSTANCE_SCHEMA_VERSION,
        "instance_form_type": INSTANCE_FORM_TYPE,
        "installed_edict_version": installed_version,
        "managed_roots": [".raiden/writ"],
        "overlay_roots": [".raiden/local"],
        "live_state_roots": [".raiden/state"],
    }


def init_instance(target: Path, *, force: bool = False) -> list[Path]:
    """Create the current downstream RAIDEN Instance skeleton."""
    writes: list[Path] = []

    files = {
        target / "AGENTS.md": (
            "# Agent Startup\n\n"
            "Read `.raiden/README.md` before doing repo-local work.\n"
        ),
        target / ".raiden" / "README.md": (
            "# RAIDEN Instance\n\n"
            "This directory is the local RAIDEN Instance control plane.\n\n"
            "Read order:\n"
            "1. `.raiden/state/CURRENT_STATE.md`\n"
            "2. `.raiden/state/OPEN_LOOPS.md`\n"
            "3. `.raiden/local/README.md`\n"
            "4. `.raiden/writ/README.md`\n"
        ),
        target / ".raiden" / "local" / "README.md": (
            "# Local Overlay\n\n"
            "Repo-specific rules, prompts, context, and exceptions live here.\n"
        ),
        target / ".raiden" / "state" / "README.md": (
            "# Local Live State\n\n"
            "Repo-local continuity state lives here.\n"
        ),
        target / ".raiden" / "state" / "CURRENT_STATE.md": (
            "# Current State\n\n"
            "- Initial RAIDEN Instance scaffold created.\n"
        ),
        target / ".raiden" / "state" / "GOALS.md": "# Goals\n\n",
        target / ".raiden" / "state" / "OPEN_LOOPS.md": "# Open Loops\n\n",
        target / ".raiden" / "state" / "DECISIONS.md": "# Decisions\n\n",
        target / ".raiden" / "state" / "WORK_LOG.md": "# Work Log\n\n",
    }

    for path, content in files.items():
        if _write_text(path, content, force=force):
            writes.append(path)

    for directory in (
        target / ".raiden" / "writ",
        target / ".raiden" / "local" / "prompts",
        target / ".raiden" / "local" / "rules",
        target / ".raiden" / "local" / "context",
        target / ".raiden" / "instance",
    ):
        directory.mkdir(parents=True, exist_ok=True)

    metadata_path = target / ".raiden" / "instance" / "metadata.json"
    if _write_json(metadata_path, _metadata(INITIAL_INSTALLED_VERSION), force=force):
        writes.append(metadata_path)

    return writes


def doctor(target: Path) -> tuple[bool, list[str]]:
    """Check whether a target repo has the current minimum instance shape."""
    required_paths = [
        target / "AGENTS.md",
        target / ".raiden" / "README.md",
        target / ".raiden" / "writ",
        target / ".raiden" / "local",
        target / ".raiden" / "state",
        target / ".raiden" / "instance",
        target / ".raiden" / "instance" / "metadata.json",
    ]
    missing = [str(path) for path in required_paths if not path.exists()]

    problems: list[str] = []
    if missing:
        problems.extend(f"missing: {path}" for path in missing)

    metadata_path = target / ".raiden" / "instance" / "metadata.json"
    if metadata_path.exists():
        try:
            data = json.loads(metadata_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            problems.append(f"invalid metadata JSON: {exc}")
        else:
            expected = _metadata(data.get("installed_edict_version", ""))
            for key, value in expected.items():
                if data.get(key) != value:
                    problems.append(f"metadata {key!r} is {data.get(key)!r}, expected {value!r}")

    return not problems, problems


def print_steps() -> None:
    """Print the current operator guide."""
    print(
        """RAIDEN guided setup flow

1. Choose a target repo.
   Example: mkdir -p /tmp/raiden-trial

2. Initialize the RAIDEN Instance skeleton.
   python3 toolkit/guide/raiden_guide.py init --target /tmp/raiden-trial

3. Preview install/update from an Edict package.
   python3 toolkit/guide/raiden_guide.py install \\
     --target /tmp/raiden-trial \\
     --package toolkit/updater/fixtures/sample_package

4. Apply only after the plan is conflict-free.
   python3 toolkit/guide/raiden_guide.py install \\
     --target /tmp/raiden-trial \\
     --package toolkit/updater/fixtures/sample_package \\
     --apply

5. Check the resulting instance.
   python3 toolkit/guide/raiden_guide.py doctor --target /tmp/raiden-trial
"""
    )


def cmd_steps(_args: argparse.Namespace) -> int:
    print_steps()
    return 0


def cmd_init(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    writes = init_instance(target, force=args.force)
    print(f"Initialized RAIDEN Instance skeleton at: {target}")
    if writes:
        print("Files written:")
        for path in writes:
            print(f"- {path}")
    else:
        print("No files written; existing files were preserved.")
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    ok, problems = doctor(target)
    if ok:
        print(f"RAIDEN Instance check passed: {target}")
        return 0
    print(f"RAIDEN Instance check failed: {target}")
    for problem in problems:
        print(f"- {problem}")
    return 1


def cmd_install(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    package = Path(args.package).resolve()

    target.mkdir(parents=True, exist_ok=True)
    init_instance(target, force=False)

    plan = create_plan(target, package)
    print(_format_plan(plan))

    if not args.apply:
        print("\nDry run only. Re-run with --apply to install or update.")
        return 0 if plan.can_apply or _is_already_current(plan.block_reason) else 1

    if not plan.can_apply:
        print(f"\nApply blocked: {plan.block_reason}")
        return 1

    try:
        apply_plan(plan, target, package)
    except ApplyError as exc:
        print(f"\nApply failed: {exc}")
        return 1

    print("\nApply succeeded. RAIDEN Writ is installed under .raiden/writ/.")
    return 0


def _is_already_current(block_reason: str | None) -> bool:
    """Return True for the updater's already-current no-op plan."""
    return block_reason is not None and block_reason.startswith("Already up to date")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="raiden-guide",
        description="Step-by-step helper for the current RAIDEN Instance install flow.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    steps_parser = subparsers.add_parser("steps", help="Print the setup flow")
    steps_parser.set_defaults(func=cmd_steps)

    init_parser = subparsers.add_parser("init", help="Create a RAIDEN Instance skeleton")
    init_parser.add_argument("--target", required=True, help="Target repo root")
    init_parser.add_argument("--force", action="store_true", help="Overwrite existing guide-created files")
    init_parser.set_defaults(func=cmd_init)

    install_parser = subparsers.add_parser("install", help="Plan or apply an Edict package")
    install_parser.add_argument("--target", required=True, help="Target repo root")
    install_parser.add_argument("--package", required=True, help="Edict package root")
    install_parser.add_argument("--apply", action="store_true", help="Apply the plan")
    install_parser.set_defaults(func=cmd_install)

    doctor_parser = subparsers.add_parser("doctor", help="Check a RAIDEN Instance skeleton")
    doctor_parser.add_argument("--target", required=True, help="Target repo root")
    doctor_parser.set_defaults(func=cmd_doctor)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
