# RAIDEN Toolkit Subtree

## Purpose

This directory is the first explicitly designated canonical RAIDEN toolkit
subtree.

It is the central non-root home for reusable toolkit/package artifacts that
belong to RAIDEN itself rather than to a downstream `RAIDEN Instance`.

Root canonical docs remain the higher-order authority for:

- source of truth
- decisions
- continuity state
- policy interpretation

This subtree exists to hold concrete toolkit materials that should not live at
the repo root once they become real assets.

## Current Scope

The first materialized surface is intentionally small:

- `prompts/`
  - shared prompt assets, cataloging, and governance owned by central RAIDEN
- `edict/`
  - the first central `Edict` package surface, boundary, lifecycle docs, and a
    minimal example package skeleton that maps into downstream `Writ` material
- `instance/`
  - downstream `RAIDEN Instance` structure and prompt-mapping docs
- `updater/`
  - first local CLI updater for `Edict` package to downstream `Writ` updates
- `guide/`
  - step-by-step helper for trying the current install and updater flow

## Current Non-Goals

This subtree does not yet settle:

- updater metadata extensions beyond the current local CLI contract
- package manifest extensions beyond the current local CLI contract
- package publish mechanics
- remote distribution

Those remain governed by root canon until later package or distribution work is
promoted.

## Working Rule

Files here are canonical only because this subtree is explicitly designated in
root canon.

Do not place:

- imported prototype files
- raw extracted references
- repo-local downstream prompts
- session-only planning artifacts

into this subtree.
