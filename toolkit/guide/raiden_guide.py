"""Guided RAIDEN setup helper.

This is an operator-facing wrapper around the current local CLI installer flow.
It delegates instance setup and install/update planning/applying to the shared
``raiden_updater`` service layer.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


TOOLKIT_ROOT = Path(__file__).resolve().parents[1]
UPDATER_ROOT = TOOLKIT_ROOT / "updater"
if str(UPDATER_ROOT) not in sys.path:
    sys.path.insert(0, str(UPDATER_ROOT))

from raiden_updater.applier import ApplyError, apply_plan  # noqa: E402
from raiden_updater.cli import _format_plan  # noqa: E402
from raiden_updater.installer import (  # noqa: E402
    LEGACY_REVIEW_RELATIVE_PATH,
    doctor,
    init_instance,
)
from raiden_updater.planner import create_plan  # noqa: E402


def print_steps() -> None:
    """Print the current operator guide."""
    print(
        """RAIDEN guided installer flow

1. Choose a target repo.
   Example: mkdir -p /tmp/raiden-trial

2. Initialize the RAIDEN Instance skeleton.
   python3 toolkit/guide/raiden_guide.py init --target /tmp/raiden-trial

3. Preview install or update-mode install from an Edict package.
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
    result = init_instance(target, force=args.force)
    print(f"Initialized RAIDEN Instance skeleton at: {target}")
    if result.written_paths:
        print("Files written:")
        for path in result.written_paths:
            print(f"- {path}")
    else:
        print("No files written; existing files were preserved.")
    if result.legacy_artifacts:
        print("Legacy artifacts detected:")
        for artifact in result.legacy_artifacts:
            print(f"- {artifact.path} [{artifact.status}] {artifact.reason}")
        print(f"Review file: {target / LEGACY_REVIEW_RELATIVE_PATH}")
    return 0


def cmd_doctor(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    result = doctor(target)
    if result.ok:
        print(f"RAIDEN Instance check passed: {target}")
        return 0
    print(f"RAIDEN Instance check failed: {target}")
    for problem in result.problems:
        print(f"- {problem}")
    return 1


def cmd_install(args: argparse.Namespace) -> int:
    target = Path(args.target).resolve()
    package = Path(args.package).resolve()

    target.mkdir(parents=True, exist_ok=True)
    init_result = init_instance(target, force=False)

    plan = create_plan(target, package)
    print(_format_plan(plan))
    if init_result.legacy_artifacts:
        print("\nLegacy artifacts detected:")
        for artifact in init_result.legacy_artifacts:
            print(f"- {artifact.path} [{artifact.status}] {artifact.reason}")
        print(f"Review file: {target / LEGACY_REVIEW_RELATIVE_PATH}")

    if not args.apply:
        print("\nDry run only. Re-run with --apply to install or install an update.")
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
        description="Step-by-step helper for the current RAIDEN Instance installer flow.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    steps_parser = subparsers.add_parser("steps", help="Print the setup flow")
    steps_parser.set_defaults(func=cmd_steps)

    init_parser = subparsers.add_parser("init", help="Create a RAIDEN Instance skeleton")
    init_parser.add_argument("--target", required=True, help="Target repo root")
    init_parser.add_argument("--force", action="store_true", help="Overwrite existing guide-created files")
    init_parser.set_defaults(func=cmd_init)

    install_parser = subparsers.add_parser("install", help="Plan or apply an Edict package install")
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
