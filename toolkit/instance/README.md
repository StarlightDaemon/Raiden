# RAIDEN Instance Docs

## Purpose

This directory defines the first-pass canonical structure of a downstream
`RAIDEN Instance`.

It exists to make the downstream form concrete enough for release-readiness
preparation without freezing updater delivery mechanics too early.

## Current Scope

- `STRUCTURE.md`
  - default physical layout and placement rules for a deployed instance
- `PROMPT_MAPPING.md`
  - how central shared prompts relate to downstream local operational prompts

## Current Non-Goals

This directory does not yet define:

- package or instance metadata extensions beyond the current local CLI updater
  contract
- package manifest extensions beyond the current updater contract
- final archive/bundle format
- remote distribution mechanics

Those remain deferred until a later updater or package pass has direct
evidence for them.
