"""RAIDEN Updater CLI — plan and apply managed-core updates.

Usage::

    python -m raiden_updater.cli plan  --instance <path> --package <path>
    python -m raiden_updater.cli apply --instance <path> --package <path>

The package manifest, instance metadata, installed baseline, and core version
comparison rules now reflect current local CLI updater canon.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .applier import ApplyError, apply_plan
from .planner import create_plan


def _format_plan(plan) -> str:  # noqa: ANN001
    """Format a PlanResult for human-readable terminal output."""
    lines: list[str] = []
    lines.append("=" * 60)
    lines.append("RAIDEN Updater — Plan Result")
    lines.append("=" * 60)

    lines.append(f"Compatible:         {plan.compatible}")
    lines.append(f"Compatibility:      {plan.compatibility_detail}")
    lines.append(f"Version comparison: {plan.version_comparison}")
    lines.append(f"Current version:    {plan.current_version}")
    lines.append(f"Target version:     {plan.target_version}")

    lines.append("")
    lines.append("--- Protected Paths ---")
    if plan.protected_paths:
        for p in plan.protected_paths:
            lines.append(f"  [protected] {p}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("--- File Actions ---")
    if plan.file_actions:
        for fa in plan.file_actions:
            lines.append(f"  [{fa.action:>9}] {fa.path}  — {fa.reason}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("--- Conflicts ---")
    if plan.conflicts:
        for c in plan.conflicts:
            lines.append(f"  [{c.conflict_type}] {c.path}: {c.detail}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("--- Anomalies ---")
    if plan.anomalies:
        for a in plan.anomalies:
            lines.append(f"  [{a.severity:>5}] {a.code}: {a.detail}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append(f"Can apply: {plan.can_apply}")
    if plan.block_reason:
        lines.append(f"Block reason: {plan.block_reason}")

    lines.append("=" * 60)
    return "\n".join(lines)


def cmd_plan(args: argparse.Namespace) -> int:
    """Execute the plan command."""
    instance_root = Path(args.instance).resolve()
    package_root = Path(args.package).resolve()

    plan = create_plan(instance_root, package_root)
    print(_format_plan(plan))

    return 0 if plan.can_apply or plan.block_reason == "Already up to date — no changes needed" else 1


def cmd_apply(args: argparse.Namespace) -> int:
    """Execute the apply command."""
    instance_root = Path(args.instance).resolve()
    package_root = Path(args.package).resolve()

    plan = create_plan(instance_root, package_root)
    print(_format_plan(plan))

    if not plan.can_apply:
        print(f"\nApply BLOCKED: {plan.block_reason}")
        return 1

    try:
        apply_plan(plan, instance_root, package_root)
    except ApplyError as exc:
        print(f"\nApply FAILED: {exc}")
        return 1

    print("\nApply SUCCEEDED — managed core updated, baseline recorded.")
    return 0


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="raiden-updater",
        description="RAIDEN Updater MVP — managed-core update CLI",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # plan
    plan_parser = subparsers.add_parser(
        "plan", help="Produce a dry-run update plan (no mutations)"
    )
    plan_parser.add_argument(
        "--instance", required=True,
        help="Path to the target repo root (parent of .raiden/)",
    )
    plan_parser.add_argument(
        "--package", required=True,
        help="Path to the Edict package directory",
    )

    # apply
    apply_parser = subparsers.add_parser(
        "apply", help="Apply an update (only if plan is conflict-free)"
    )
    apply_parser.add_argument(
        "--instance", required=True,
        help="Path to the target repo root (parent of .raiden/)",
    )
    apply_parser.add_argument(
        "--package", required=True,
        help="Path to the Edict package directory",
    )

    args = parser.parse_args(argv)

    if args.command == "plan":
        return cmd_plan(args)
    elif args.command == "apply":
        return cmd_apply(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
