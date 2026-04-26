# Artifact Audience

## Purpose

This file defines how RAIDEN classifies artifact audience and intended role.

The goal is to prevent:

- authority bleed
- audience confusion
- downstream misuse of upstream concept material
- source-history material being mistaken for live operating law

Audience is separate from canonicality.

- Canonicality answers: "is this authoritative?"
- Audience answers: "who is this for?"
- Intended role answers: "what job does this artifact perform?"

All three should stay explicit.

## Core Rule

Every durable RAIDEN artifact should be classifiable by:

1. canonicality
2. primary audience
3. intended role
4. non-use boundary when misuse would be likely

For some surfaces this can be defined at the directory or index level.
For others it should be stated inside the file itself.

## Audience Classes

Use these audience labels when assigning artifact purpose:

### 1. Operator

Human-facing material used to understand state, make decisions, and steer RAIDEN.

Examples:

- `README.md`
- `CURRENT_STATE.md`
- `GOALS.md`
- `OPEN_LOOPS.md`
- `DECISIONS.md`

### 2. RAIDEN Core

Material used to define RAIDEN itself: identity, authority, rules, structure, synthesis, and long-term shape.

Examples:

- `SOURCE_OF_TRUTH.md`
- `REPOSITORY_MAP.md`
- `AGENT_BOUNDARIES.md`
- `ARTIFACT_AUDIENCE.md`
- selected `Source_info/` files retained for concept formation

### 3. Canonical Structuring / Synthesis

Material used by agents turning evidence into durable RAIDEN canon.

Examples:

- `WORKBOOK.md`
- `SOURCE_HISTORY_INDEX.md`
- `reference-reviews/CANONICAL_SOURCE_MAP.md`
- `reference-reviews/CROSS_REPO_MATRIX.md`

### 4. Reference Review

Material used to inspect evidence, compare prototypes, and record findings before promotion.

Examples:

- `reference-reviews/`
- `reference-repos/`
- `reference-extracts/`

### 5. Toolkit / Package Maintainer

Material used to implement and maintain RAIDEN's reusable toolkit/package surfaces.

Examples:

- `toolkit/`
- `TOOLKIT_INDEX.md`
- `PROMPT_ASSET_INDEX.md`

### 6. Downstream RAIDEN Instance

Material intended for a deployed repo-local RAIDEN form rather than central RAIDEN canon.

Examples:

- `toolkit/instance/`
- downstream `Writ` surfaces
- local startup/read-order artifacts once emitted into a target repo

### 7. Implementation Agent

Material intended to guide bounded implementation work inside a target repo.

Examples:

- implementation prompts
- task handoff packages
- local execution instructions in a downstream repo

### 8. Audit / Review Agent

Material used to verify conformance, surface drift, and check claims against the current source of truth.

Examples:

- audit templates
- review prompts
- exception/drift reports

### 9. Research / Intake

Material retained to preserve provenance, exploratory findings, or future extraction value.

Examples:

- `Source_info/`
- raw research notes
- imported external evidence before synthesis

## Intended Role Labels

Use concise role labels where practical. Common roles include:

- repository identity
- canonical rule
- canonical navigation
- continuity/state tracking
- source-history index
- identity/role-definition source
- reviewed evidence
- extracted reference
- toolkit implementation surface
- downstream deployment surface
- implementation handoff
- audit/review artifact
- research note

The role should describe the artifact's job, not merely its format.

## Layer Defaults

Unless a file explicitly says otherwise, use these default audience assumptions.

| Layer | Canonicality | Default Audience | Default Role | Default Non-Use |
|---|---|---|---|---|
| root canonical `.md` files | Canonical | Operator + RAIDEN Core | rule, state, navigation, or decision surface | not a substitute for downstream repo-local execution instructions unless explicitly packaged for that purpose |
| `toolkit/` | Canonical when explicitly designated | Toolkit / Package Maintainer + Downstream RAIDEN Instance | reusable package/prompt/instance surface | not root-level governance by itself |
| `Source_info/` | Non-canonical by default | RAIDEN Core + Canonical Structuring + Research / Intake | preserved source history and concept-formation input | not downstream operating law or implementation instruction by default |
| `reference-reviews/` | Non-canonical unless adopted | Reference Review + Canonical Structuring | assessment and synthesis | not canon by review alone |
| `reference-extracts/` | Non-canonical unless adopted | RAIDEN Core + Reference Review + Toolkit / Package Maintainer | compact reusable reference | not canon by extraction alone |
| `reference-repos/` | Non-canonical | Reference Review | raw evidence snapshot | not writable canon or direct copy source |
| `working/` | Non-canonical | active working agents only | temporary planning/work surface | not durable authority without promotion |

## Local Status Blocks

A local status block is strongly recommended when a file:

- lives outside root canon
- is likely to be opened directly
- contains prescriptive language
- could be mistaken for downstream instruction
- exists primarily for RAIDEN concept formation rather than deployment

Recommended fields:

- Source type
- Canonicality
- Intended role
- Primary audience
- Non-use

Example:

- Source type: preserved source input
- Canonicality: non-canonical
- Intended role: identity/role-definition source for RAIDEN concept formation
- Primary audience: RAIDEN Core and canonical synthesis
- Non-use: not for downstream execution agents or repo-local operating law

## Working Rules

- Do not assume "useful" means "for everyone."
- Do not assume "detailed" means "canonical."
- Do not route downstream agents through `Source_info/` unless a canonical file explicitly tells them to use a specific source file.
- If a source-history file is mainly for RAIDEN self-definition, say so in the file.
- If a file is meant for downstream implementation, place it in the proper downstream/package surface rather than the root source-history layer.

## Current Practical Use

When deciding whether an artifact should be read by a given agent, ask:

1. Is this file authoritative?
2. Is this file actually for this audience?
3. Is this file defining RAIDEN itself, or guiding downstream work?

If those answers are unclear, the file or its index should be updated before wider reuse.
