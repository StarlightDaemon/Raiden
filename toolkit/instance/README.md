# RAIDEN Instance Docs

## Purpose

This directory defines the first-pass canonical structure of a downstream
`RAIDEN Instance`.

It exists to make the downstream form concrete enough for release-readiness
preparation without freezing updater manifests or delivery mechanics too early.

## Current Scope

- `STRUCTURE.md`
  - default physical layout and placement rules for a deployed instance
- `PROMPT_MAPPING.md`
  - how central shared prompts relate to downstream local operational prompts

## Current Non-Goals

This directory does not yet define:

- exact updater metadata filenames
- package manifest field names
- final archive/bundle format
- remote distribution mechanics

Those remain deferred until updater canon resumes.
