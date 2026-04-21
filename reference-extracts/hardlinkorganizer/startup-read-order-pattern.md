# Startup Read-Order Pattern

## Purpose

This extract preserves the `HardlinkOrganizer` startup pattern where an agent
is pointed at a specific live repo root and given a constrained read order
before widening into the rest of the project.

## Observed Pattern

Observed startup rules:

- declare the authoritative live repo root first
- warn against working from deprecated or mirrored locations
- define the first files to read in order
- distinguish project-local authority from parent-repo summary material
- point execution work back to the continuity layer before touching code

## Why It Matters To RAIDEN

This is a strong operational pattern for downstream deployment because it
reduces ambiguity about:

- where the live instance actually is
- what an agent should read first
- which local artifacts outrank older or broader summary material

It is especially relevant to `RAIDEN Instance` bootstrapping and any future
downstream startup template.

## Reusable Pattern

Preserve these behaviors:

1. name the authoritative repo root explicitly
2. state known deprecated locations when confusion is likely
3. give a short read order for startup
4. direct agents to the local continuity layer before broader context
5. keep code entry points secondary to startup and authority guidance

## RAIDEN-Relevant Implication

This pattern is useful for a future downstream startup template and for
clarifying how a deployed instance should direct agents toward local overlay and
live-state files without mistaking parent or historical material for local
authority.

## What Not To Reuse Literally

Do not promote directly:

- environment-specific path values
- product-specific code entry points
- references to deprecated nested locations that only matter to
  `HardlinkOrganizer`

## Provenance

- Primary sources:
  - `reference-repos/HardlinkOrganizer/AGENTS.md`
  - `reference-repos/HardlinkOrganizer/agent-ledger/README.md`
- Supporting sources:
  - `reference-reviews/HardlinkOrganizer/REPO_TOOLING_REVIEW.md`
  - `reference-reviews/HardlinkOrganizer/IMPORT_CANDIDATES.md`
