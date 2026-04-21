# Shared Prompt Catalog

## Purpose

This file is the inventory for the current central shared prompt set under
`toolkit/prompts/`.

It exists so future agents can see:

- what prompt assets already exist
- what role each one serves
- which lineage most strongly informed it
- whether the asset is active or only provisional

## Current Inventory

| Prompt ID | File | Category | Role | Primary Lineage | Status |
|---|---|---|---|---|---|
| `raiden.shared.bounded-task.v1` | `bounded-task-template.md` | bounded task | one-slice execution template | `HardlinkOrganizer` | Active |
| `raiden.shared.compact-task.v1` | `compact-task-template.md` | compact task | token-lean internal execution template | `HardlinkOrganizer`, `CTRL` | Active |
| `raiden.shared.handoff.v1` | `handoff-template.md` | handoff | bounded work transfer template | `BIND` | Active |
| `raiden.shared.pause-point.v1` | `pause-point-template.md` | pause-point | cycle stop/export template | `CTRL`, `BIND` | Active |
| `raiden.shared.continuation-state.v1` | `continuation-state-template.md` | continuation | compact carried-forward state template | `CTRL`, `HardlinkOrganizer` | Active |
| `raiden.shared.completion.v1` | `completion-template.md` | completion | concise closeout template | `BIND` | Active |
| `raiden.shared.validation.v1` | `validation-template.md` | validation | compact validation-check template | `CTRL` | Active |
| `raiden.shared.compact-review.v1` | `compact-review-template.md` | review | token-lean bounded review template | `BIND`, `CTRL` | Active |
| `raiden.shared.readonly-audit-review.v1` | `read-only-audit-review-template.md` | audit/review | full-state read-only audit and structural review template | `BIND`, `CTRL`, `Starlight Architect` | Active |

## Inclusion Threshold

Add a prompt to this catalog only when it is:

- reusable
- normalized into RAIDEN wording
- intended to persist beyond one session

Do not catalog:

- session-only prompts
- downstream local prompts
- raw prototype prompts

## Current Gaps

Useful future additions may include:

- a reusable operator kickoff prompt

These are gaps, not approvals. Add them only when the wording is stable enough
to reuse.
