# Agent Boundaries

## Purpose

This file defines the major agent roles RAIDEN recognizes and the boundaries between them.

RAIDEN is a central toolkit/framework repo. Not every agent working with RAIDEN is doing the same kind of work.

## Boundary Principles

1. Roles are defined by scope, not model name.
2. Evidence review and canonical writing are different activities.
3. No agent may treat prototype material as canon without explicit promotion.
4. Imported reference repos are read-only by process.
5. Durable state belongs in durable artifacts, not only in chat or transient prompts.
6. Artifact audience and intended role must match the agent using or writing the file; see `ARTIFACT_AUDIENCE.md`.

## Core Roles

### 1. Operator

The human operator sets priorities, approves major direction changes, and resolves high-level ambiguity.

Operator-only powers:

- approve destructive cleanup
- choose canonical naming
- approve major governance changes when needed
- decide when evidence is sufficient to retire imported snapshots

### 2. Reference Review Agent

This agent inspects `Source_info/` and `reference-repos/` and writes assessments into `reference-reviews/`.

Allowed:

- inventory artifacts
- compare prototype patterns
- write reviews, matrices, and source maps

Not allowed:

- treat reviewed prototypes as canon by default
- edit imported prototype repos
- skip comparison when multiple competing patterns exist

### 3. Canonical Structuring Agent

This agent writes or updates root-level RAIDEN canonical docs.

Allowed:

- create and maintain canonical Markdown/text artifacts
- adopt reviewed patterns into RAIDEN canon
- normalize naming and hierarchy

Not allowed:

- promote source material without review
- silently overwrite authority order
- treat a temporary review artifact as canon unless adopted

### 4. Downstream Embedded-Instance Agent

This is a future repo-local agent operating inside a product repo that uses RAIDEN outputs.

Expected scope:

- maintain local continuity artifacts
- track local state, goals, loops, decisions, and work history
- follow the local startup/read-order rules for that repo

Boundary:

- local repo state is not central RAIDEN canon
- local adaptations can inform RAIDEN later, but only through review and promotion

### 5. Implementation Agent

This agent changes product code or operational code inside a target repo.

Expected scope:

- implement one bounded task at a time
- follow the target repo's local control plane and prompts
- report outcomes clearly

Boundary:

- implementation work does not rewrite governance by default
- product-specific expediency does not automatically become toolkit policy

### 6. Audit / Review Agent

This agent verifies claims, identifies drift, and checks conformance against the current source of truth.

Expected scope:

- compare implementation against intended behavior
- surface contradictions and missing evidence
- produce bounded audit or review artifacts

Boundary:

- audits report findings; they do not silently redefine canon

### 7. Research Agent

This agent gathers research, external references, or exploratory findings for future use.

Expected scope:

- generate research notes
- preserve provenance
- feed structured findings into the workbook or source-history layer

Boundary:

- research is evidence, not canon
- exploratory notes require synthesis before adoption

## Artifact Ownership By Role

| Role | Primary Write Surface | Should Not Write Directly |
|---|---|---|
| Operator | decisions through direct instruction | imported repos unless intentionally acting outside RAIDEN review flow |
| Reference Review Agent | `reference-reviews/` | root canon as if review alone were adoption |
| Canonical Structuring Agent | root canonical `.md` files | imported prototype repos |
| Downstream Embedded-Instance Agent | future repo-local control plane | RAIDEN root canon unless feeding back through review |
| Implementation Agent | target implementation repo | RAIDEN canon unless specifically tasked |
| Audit / Review Agent | bounded audit/review artifacts | source-of-truth changes without explicit adoption |
| Research Agent | workbook, source-history, research artifacts | canonical docs without synthesis |

## Promotion Path

The normal path from idea to canon is:

1. source evidence
2. review or comparison
3. synthesis
4. explicit adoption into a canonical RAIDEN file

The normal path from RAIDEN canon to downstream use is:

1. canonical RAIDEN rule or pattern
2. toolkit/package or embedded-instance template
3. repo-local adaptation

## Current Practical Reading

For current RAIDEN work:

- `HardlinkOrganizer` is the strongest source for embedded local continuity structure
- `Starlight Architect` is the strongest source for formal boundary logic
- `BIND` is the strongest source for prompt-interface and sidecar governance patterns
- `CTRL` is the strongest source for local artifact split discipline
- `ARC` and `ARC-RC` are supporting sources for simple role memos and producer/consumer boundaries

These sources inform RAIDEN boundary design, but none of them override RAIDEN canon directly.
