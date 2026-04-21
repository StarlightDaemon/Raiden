# Source Of Truth

## Purpose

This file defines RAIDEN's authority order and promotion rules.

RAIDEN is the canonical central toolkit/framework repo. Imported prototypes and preserved source history are evidence inputs, not canon.

## Authority Order

1. Root-level canonical RAIDEN documents in this repository
2. Any future RAIDEN toolkit subtree or package surface that is explicitly marked canonical
3. Review artifacts in `reference-reviews/` only when a root-level canonical RAIDEN document explicitly adopts them
4. Extracted references in `reference-extracts/` only when a root-level canonical RAIDEN document explicitly adopts them
5. `Source_info/` as preserved historical source material
6. Imported prototype repos in `reference-repos/` as read-only reference evidence

## Canonical Material

Canonical by default:

- root-level RAIDEN Markdown/text artifacts
- the explicitly designated `toolkit/` subtree
- future RAIDEN toolkit/package artifacts only after explicit designation

Not canonical by default:

- `Source_info/`
- `reference-repos/`
- `reference-reviews/`
- `reference-extracts/`
- prototype prompts
- archived research
- local-only artifacts copied from other repos

## Conflict Rules

When materials disagree, resolve conflicts in this order:

1. explicit root-level RAIDEN canonical file
2. latest relevant RAIDEN decision recorded in `DECISIONS.md`
3. explicitly adopted synthesis or review artifact
4. preserved source evidence

Conflicts must be recorded, not silently flattened.

## Promotion Rules

No material becomes RAIDEN canon unless all of the following are true:

1. it was reviewed in RAIDEN
2. it was compared against competing patterns when relevant
3. its role was assigned in synthesis or by explicit decision
4. it was rewritten or adopted into a canonical RAIDEN artifact

Prototype wording, names, and assumptions do not become authoritative by proximity.

## Artifact Discipline

- Durable RAIDEN rules belong in root canonical docs.
- Canonical reusable toolkit/package artifacts belong under explicitly designated toolkit surfaces such as `toolkit/`.
- Comparative analysis belongs in `reference-reviews/`.
- Preserved prototype/source history belongs in `Source_info/` and `reference-repos/`.
- Session-shaped or temporary working artifacts should not be mistaken for canon unless promoted.
- Audience and intended-role classification follow `ARTIFACT_AUDIENCE.md`.
- Canonicality does not override audience; a file can be useful to RAIDEN core without being intended for downstream execution.

## Current Explicit Toolkit Designation

- `toolkit/` is the first explicitly designated canonical RAIDEN toolkit subtree.
- Root canonical docs remain the higher-order authority for rules and interpretation.

## Current Naming Rule

- `RAIDEN` is the canonical central governing agent/framework name.
- `RAIDEN Instance` is the canonical downstream repo-local deployed form.
- `Edict` is the canonical managed core artifact within a `RAIDEN Instance`.
