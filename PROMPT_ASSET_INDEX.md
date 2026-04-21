# Prompt Asset Index

## Purpose

This file defines RAIDEN's prompt-asset model and the placement policy for the
materialized `toolkit/prompts/` subtree.

It answers:

- what kinds of prompt assets RAIDEN recognizes
- where they belong
- what is central versus local
- which reviewed prototype sources inform the model

This file is an index and policy layer, not a prompt dump.

## Canonical Prompt Model

RAIDEN now uses a two-level prompt model:

### 1. Central Shared Prompt Layer

This belongs to the central RAIDEN toolkit layer.

It will hold:

- canonical prompt rules
- reusable handoff prompts
- reusable completion/report prompts
- reusable bounded-task prompt templates
- reusable compact internal execution templates
- shared prompt metadata and versioning rules

This layer is managed by RAIDEN.

### 2. Downstream Local Prompt Layer

This belongs to the deployed downstream repo subtree.

It will hold:

- repo-local operational prompts
- prompts tied to local continuity state
- prompts tied to local tools, risks, or constraints
- repo-specific execution slices

This layer is local to the target repo and must survive RAIDEN updates.

## Current Canonical Placement Rule

Now that the first toolkit subtree exists:

- prompt **policy and indexing** remain in RAIDEN root canon
- prompt **assets themselves** belong under `toolkit/prompts/`
- repo-local operational prompts belong under `.raiden/local/prompts/` in a deployed downstream instance, not in RAIDEN root canon

## Prompt Asset Categories

| Category | Canonical Home | Purpose | Notes |
|---|---|---|---|
| Prompt governance rules | central toolkit | define how prompts are written, versioned, and used | source-of-truth layer |
| Shared handoff prompts | central toolkit | initialize other agents for reusable task shapes | should be normalized and reusable |
| Shared completion prompts | central toolkit | standardize bounded closeout/report outputs | should not become report sprawl by default |
| Bounded task templates | central toolkit | one-slice task dispatch patterns | strongest lineage from `HardlinkOrganizer` |
| Compact internal templates | central toolkit | token-lean execution, pause-point, continuation, validation, and review scaffolds | machine-oriented by design, still must remain operationally lossless |
| Repo-local operational prompts | downstream local subtree | drive local implementation, review, or audit work | local-only, not RAIDEN canon |
| Session-only prompts | local/transient | one-off use in a current session | should not be mistaken for durable assets |

## Source Lineage

Primary reviewed source inputs:

- `HardlinkOrganizer`
  - strongest source for prompt-library layout
  - strongest source for bounded execution slices
  - strongest source for micro-dispatch template patterns

- `BIND`
  - strongest source for handoff prompt interface
  - strongest source for completion/closeout prompt interface
  - strongest source for sidecar-style prompt governance

- `CTRL`
  - strongest source for current-state handoff discipline
  - useful caution against letting reports and prompts blur together

Supporting influences:

- `Starlight Architect` for older formal handoff lineage
- `ARC` and `ARC-RC` for role memo and bounded mission-style instruction patterns

## Inclusion Rules

A prompt asset belongs in the central shared layer only if it is:

1. reusable across more than one target repo or task family
2. not dependent on one repo's local filesystem or project identity
3. structurally stable enough to version and index

A prompt asset belongs in the downstream local layer if it depends on:

- local repo state
- local project naming
- local implementation details
- local exceptions or constraints

## Anti-Drift Rules

- Do not store all prompts at the RAIDEN root.
- Do not mix central reusable prompts with target-repo operational prompts.
- Do not let report artifacts become the accidental prompt registry.
- Do not treat session-only prompts as durable assets without explicit promotion.

## Future Required Metadata

Prompt assets under `toolkit/prompts/` should eventually carry:

- prompt ID
- category
- owning layer (`central` or `local`)
- surface (`human-facing`, `agent-facing`, or `mixed`)
- version
- intended role
- expected inputs
- expected outputs
- compatibility notes where needed

## Current Status

- canonical placement policy: defined
- source lineage: defined
- toolkit-subtree physical home: materialized under `toolkit/prompts/`
- downstream local prompt area naming: defined at `.raiden/local/prompts/`

## Still Deferred

The following remain deferred:

- version manifest shape for prompt bundles

Those should be resolved alongside further updater and package drafting.
