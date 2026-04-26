# HardlinkOrganizer Extracts

## Purpose

This folder contains RAIDEN-owned extracted references taken from
`HardlinkOrganizer`.

The goal is to preserve the parts of `HardlinkOrganizer` that matter to RAIDEN
without keeping the full project snapshot as the preferred reread surface for
downstream-instance structure and continuity patterns.

## Current Extract Set

| File | Pattern | Status |
|---|---|---|
| `embedded-instance-structure-pattern.md` | repo-local embedded control-plane layout | Active |
| `continuity-file-roles-pattern.md` | durable separation of current state, goals, loops, decisions, and work history | Active |
| `prompt-library-pattern.md` | bounded prompt-library and micro-dispatch model | Active |
| `startup-read-order-pattern.md` | agent startup, root-lock, and read-order pattern | Active |

## Source Provenance

Primary source files came from these historical paths in the retired
`HardlinkOrganizer` snapshot:

- `reference-repos/HardlinkOrganizer/AGENTS.md`
- `reference-repos/HardlinkOrganizer/agent-ledger/README.md`
- `reference-repos/HardlinkOrganizer/agent-ledger/AGENT_LEDGER_STANDARD.md`
- `reference-repos/HardlinkOrganizer/agent-ledger/CURRENT_STATE.md`
- `reference-repos/HardlinkOrganizer/agent-ledger/GOALS.md`
- `reference-repos/HardlinkOrganizer/agent-ledger/OPEN_LOOPS.md`
- `reference-repos/HardlinkOrganizer/agent-ledger/DECISIONS.md`
- `reference-repos/HardlinkOrganizer/agent-ledger/WORK_LOG.md`
- `reference-repos/HardlinkOrganizer/agent-prompts/README.md`
- `reference-repos/HardlinkOrganizer/agent-prompts/micro-prompt-template.md`

Supporting interpretation:

- `reference-reviews/HardlinkOrganizer/REPO_TOOLING_REVIEW.md`
- `reference-reviews/HardlinkOrganizer/IMPORT_CANDIDATES.md`

## Current Retirement Status

- extracted references now exist
- the full `HardlinkOrganizer` snapshot was retired from `reference-repos/` on 2026-04-23
- the extracted references in this folder are now the preferred compact RAIDEN-owned reread surface for these patterns

This folder now preserves the reusable `HardlinkOrganizer` patterns after full
snapshot retirement.
