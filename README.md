# RAIDEN

RAIDEN is the canonical central toolkit/framework repository for reusable AI-agent governance, repository-structure, and execution-support artifacts.

## What This Repo Is

RAIDEN is the central canon, not a product application and not a loose notes dump.
It exists to hold:

- root-level canonical governance and continuity docs
- the first explicit canonical `toolkit/` subtree
- review outputs and extracted references that support canon formation
- preserved source history used for provenance and synthesis

RAIDEN uses this naming stack:

- `RAIDEN` = central governing agent/framework authority
- `RAIDEN Instance` = downstream deployed repo-local form
- `Edict` = managed core artifact within a `RAIDEN Instance`

## Current State

The repository is in the canonicalization and release-preparation phase.

Current published state includes:

- canonical root scaffold and authority order
- canonical operating-intent layer
- initial canonical `toolkit/` subtree
- continuity canon such as current state, goals, open loops, and decisions
- extracted references and comparative reviews that support future canon work

Not yet done:

- final updater-shape canon
- final manifest-field canon
- broader package/release mechanics beyond the current first-pass toolkit surface

## Published Layout

Key published areas:

- `README.md` - top-level repository framing
- `SOURCE_OF_TRUTH.md` - authority order and promotion rules
- `REPOSITORY_MAP.md` - navigation and structural layers
- `CURRENT_STATE.md` - current repo status
- `DECISIONS.md` - durable decision log
- `AGENT_BOUNDARIES.md` - role and write-boundary rules
- `MANAGED_VS_LOCAL.md` - managed-core versus local-layer contract
- `toolkit/` - canonical reusable toolkit/package and instance materials
- `reference-reviews/` - comparative assessments and synthesis artifacts
- `reference-extracts/` - compact preserved reference patterns
- `Source_info/` - preserved historical source material
- `working/` - temporary working bundles and planning artifacts

Local-only area:

- `reference-repos/` - imported prototype snapshots used as evidence in local operator workspaces; intentionally excluded from this published GitHub repo

## Authority Model

RAIDEN canon follows this order:

1. root-level canonical RAIDEN documents
2. explicitly designated canonical toolkit surfaces such as `toolkit/`
3. review or extract artifacts only when explicitly adopted by root canon
4. preserved historical or prototype evidence

Working rule:

Imported prototypes and source-history material are evidence inputs, not canon.
Nothing becomes authoritative by proximity.
Material is promoted only after review, comparison when relevant, and explicit adoption into canonical RAIDEN artifacts.

## How To Read The Repo

If you are new to RAIDEN, start with:

1. `README.md`
2. `SOURCE_OF_TRUTH.md`
3. `REPOSITORY_MAP.md`
4. `CURRENT_STATE.md`
5. `DECISIONS.md`
6. `AGENT_BOUNDARIES.md`
7. `MANAGED_VS_LOCAL.md`
8. `RELEASE_READY_CHECKLIST.md`

## Editing Expectations

- Prefer concise ASCII Markdown.
- Keep canonical naming exact.
- Keep root canon concise and durable.
- Do not treat `reference-reviews/`, `reference-extracts/`, or `Source_info/` as canon unless canon explicitly adopts the result.
- Do not edit local-only prototype snapshots as part of published repo work.
- Prefer narrow, reviewable diffs over sweeping rewrites.

## Validation

There is no top-level automated test suite at present.

For repository changes, validate by:

- rereading touched files against `SOURCE_OF_TRUTH.md`, `REPOSITORY_MAP.md`, and `CURRENT_STATE.md`
- checking that canonical versus non-canonical status remains consistent
- confirming related boundary and release-readiness docs still agree when scope touches those areas

## Scope Guardrail

This repository publishes RAIDEN canon and supporting RAIDEN-owned materials.
It is not the place to silently convert prototype wording, local workspace state, or unreviewed external structures into central law.
