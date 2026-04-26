# Prompt Library Pattern

## Purpose

This extract preserves the `HardlinkOrganizer` pattern of using a bounded local
prompt library to dispatch narrow work slices without turning prompts into the
main continuity surface.

## Observed Pattern

Observed prompt-layer behavior:

- prompt assets live under `agent-prompts/`
- prompt files are narrow and task-shaped
- a micro prompt exists to dispatch another agent to exactly one prompt file
- the prompt layer includes a root lock so agents work from the intended repo
- the prompt README describes a specific usage sequence instead of acting as a
  general notebook

## Why It Matters To RAIDEN

This is strong evidence for how a downstream instance can support prompt-driven
execution while keeping durable state elsewhere.

The pattern cleanly separates:

- continuity files that persist project truth
- prompt files that package bounded execution slices

That separation aligns well with RAIDEN's distinction between reusable prompt
governance and repo-local operational prompts.

## Reusable Pattern

Preserve these ideas:

1. keep prompt assets in a dedicated prompt subtree
2. make prompt files narrow and bounded
3. provide a micro-dispatch template for one-slice handoff
4. keep prompt execution anchored to a declared repo root
5. avoid using prompt files as the durable source of project state

## RAIDEN-Relevant Implication

This pattern is useful for the future downstream prompt surface of a
`RAIDEN Instance`, especially where local prompts should survive updates but
remain separate from managed governance files.

## What Not To Reuse Literally

Do not promote directly:

- repo-specific prompt filenames and milestone numbering
- absolute filesystem root locks
- product-specific execution slices

## Provenance

- Primary sources from the retired `HardlinkOrganizer` snapshot:
  - `reference-repos/HardlinkOrganizer/agent-prompts/README.md`
  - `reference-repos/HardlinkOrganizer/agent-prompts/micro-prompt-template.md`
  - `reference-repos/HardlinkOrganizer/AGENTS.md`
- Supporting sources:
  - `reference-reviews/HardlinkOrganizer/REPO_TOOLING_REVIEW.md`
  - `reference-reviews/HardlinkOrganizer/IMPORT_CANDIDATES.md`
