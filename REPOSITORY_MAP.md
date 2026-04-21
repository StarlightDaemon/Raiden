# Repository Map

## Purpose

This file is the navigation spine for RAIDEN.

Use it to distinguish:

- canon
- evidence
- extracted references
- preserved source history
- review outputs

## Structural Layers

### 1. Canon Layer

RAIDEN's canonical layer currently includes root-level Markdown/text files and
the explicitly designated `toolkit/` subtree.

Key root files:

| Path | Role |
|---|---|
| `README.md` | repository identity and top-level framing |
| `OPERATING_INTENT.md` | canonical mission-and-operating-intent layer |
| `SOURCE_OF_TRUTH.md` | authority order and promotion rules |
| `REPOSITORY_MAP.md` | navigation and structural map |
| `AGENT_BOUNDARIES.md` | role definitions and write boundaries |
| `ARTIFACT_AUDIENCE.md` | artifact audience, intended-role, and non-use classification rules |
| `MANAGED_VS_LOCAL.md` | update boundary between managed RAIDEN core and downstream local layers |
| `INGRESS_POLICY.md` | intake, review, optional extraction, and retirement rules for external repo evidence |
| `CURRENT_STATE.md` | current RAIDEN repo state |
| `PAST_PRESENT_FUTURE.md` | canonical planning view of completed work, current phase, and next trajectory |
| `RELEASE_READY_CHECKLIST.md` | canonical release-preparation gate before updater canon resumes |
| `GOALS.md` | active normalization goals |
| `OPEN_LOOPS.md` | pending work and unresolved items |
| `DECISIONS.md` | durable decision record |
| `WORKBOOK.md` | synthesis and extraction workspace |
| `SOURCE_HISTORY_INDEX.md` | preserved source-history index |
| `PROMPT_ASSET_INDEX.md` | canonical prompt asset map and placement policy |
| `TOOLKIT_INDEX.md` | canonical toolkit/component map |

Canonical toolkit subtree:

| Path | Role |
|---|---|
| `toolkit/` | canonical central toolkit subtree for shared prompt assets and the first managed `Edict` package surface |

### 2. Preserved Source Layer

| Path | Role |
|---|---|
| `Source_info/` | preserved early RAIDEN source material, drafts, and chat-export style inputs |

This directory is retained for provenance. It is not authoritative by default.

### 3. Prototype Snapshot Layer

| Path | Role |
|---|---|
| `reference-repos/` | imported prototype repo snapshots reviewed as read-only evidence |

These repos are temporary evidence holdings. Do not treat them as RAIDEN canon.

### 4. Review And Synthesis Layer

| Path | Role |
|---|---|
| `reference-reviews/` | per-repo reviews, import candidates, cross-repo synthesis, and comparison artifacts |
| `reference-reviews/templates/` | reusable review templates |

This layer is where source evidence is assessed before promotion into canon.

### 5. Extracted Reference Layer

| Path | Role |
|---|---|
| `reference-extracts/` | compact RAIDEN-owned extracted references preserved from large prototype repos |

This layer preserves reusable patterns after review without keeping every full prototype repo as the preferred reread surface forever.

## Current Operating Flow

1. External repo evidence enters through `reference-repos/` under `INGRESS_POLICY.md`
2. Comparative review and synthesis happen in `reference-reviews/`
3. High-value patterns may be preserved in `reference-extracts/` when extraction is justified
4. Canonical RAIDEN conclusions are written to root-level files
5. Full prototype snapshots may be retired only after the retirement rule is satisfied

## Working Rules

- Do not mix imported prototype files into the RAIDEN root.
- Do not treat `reference-reviews/` as canon unless a root file adopts the result.
- Do not treat `reference-extracts/` as canon unless a root file adopts the result.
- Keep root files concise and durable.
- Preserve provenance links back to reviewed source material whenever material is promoted.
- Use `ARTIFACT_AUDIENCE.md` when deciding who a file is for, not only whether it is canonical.

## Current Expansion State

RAIDEN now has a first explicit toolkit subtree under `toolkit/`.

As that subtree grows, this map should continue to distinguish:

- central RAIDEN canon
- toolkit/package implementation
- downstream embedded-instance templates

The root canonical docs remain the primary operating layer for authority and interpretation.
