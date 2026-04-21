# Shared Prompt Assets

## Purpose

This directory is the canonical shared prompt asset home for the central RAIDEN
toolkit layer.

It holds reusable prompts that are:

- not tied to one downstream repo
- stable enough to version later
- useful across more than one task family

Repo-local operational prompts do not belong here. They belong in the local
overlay of a downstream `RAIDEN Instance`.

## Current Asset Set

| File | Role |
|---|---|
| `GOVERNANCE.md` | shared prompt authoring, promotion, and drift rules |
| `CATALOG.md` | current central prompt inventory and status map |
| `bounded-task-template.md` | reusable one-slice task dispatch template |
| `compact-task-template.md` | reusable token-lean internal execution template |
| `handoff-template.md` | reusable review or transfer handoff template |
| `pause-point-template.md` | reusable pause-point export template |
| `continuation-state-template.md` | reusable carried-forward state template |
| `completion-template.md` | reusable closeout and completion report template |
| `validation-template.md` | reusable validation-check template |
| `compact-review-template.md` | reusable token-lean review template |
| `read-only-audit-review-template.md` | reusable full-state audit and review template |

## Working Rule

Keep prompt assets:

- reusable
- concise
- role-aware
- independent from one repo's filesystem layout
- explicit about whether the active surface is readable or compressed

Do not turn this directory into a dump of session prompts or repo-specific
instructions.

When this directory grows:

- add reusable prompts to `CATALOG.md`
- keep behavioral rules in `GOVERNANCE.md`
- avoid embedding updater-specific metadata requirements here before package work
  is canonized
