# CTRL Extracts

## Purpose

This folder contains the first RAIDEN-owned extracted references taken from `CTRL`.

The goal is to preserve the parts of `CTRL` that matter to RAIDEN without keeping the full browser-extension repo as the only place those patterns exist.

## Current Extract Set

| File | Pattern | Status |
|---|---|---|
| `artifact-policy-pattern.md` | durable local state vs session-shaped execution artifacts | Active |
| `current-state-handoff-pattern.md` | reset a new agent against the actual current repo baseline | Active |
| `project-structure-pattern.md` | human-plus-agent-readable structure guidance and local/public split discipline | Active |

## Source Provenance

Primary source files:

- `reference-repos/CTRL/agent-ledger/2026-04-13__local_artifact_policy.md`
- `reference-repos/CTRL/reports/2026-03-08__current_state_repo_agent_handoff.md`
- `reference-repos/CTRL/reports/2026-04-10__next_main_rebuild_handoff.md`
- `reference-repos/CTRL/docs/PROJECT_SOP.md`
- `reference-repos/CTRL/docs/reference/project_structure_guide.md`

Supporting interpretation:

- `reference-reviews/CTRL/REPO_TOOLING_REVIEW.md`
- `reference-reviews/CTRL/IMPORT_CANDIDATES.md`

## Current Retirement Status

- extracted references exist
- the full `CTRL` snapshot remains retained for now
- `CTRL` is not yet retired from `reference-repos/`

This folder moves `CTRL` into the extracted-reference stage, but not yet full retirement.
