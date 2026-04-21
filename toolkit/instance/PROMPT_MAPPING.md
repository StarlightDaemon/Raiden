# Downstream Prompt Mapping

## Purpose

This document explains how central shared prompts relate to downstream local
operational prompts inside a deployed `RAIDEN Instance`.

It closes the gap between:

- central reusable prompt assets under `toolkit/prompts/`
- repo-local prompt usage under `.raiden/local/prompts/`

## Core Rule

Central shared prompts remain owned by RAIDEN.

Downstream local prompts remain owned by the target repo.

The downstream prompt surface should use central shared prompts as source
patterns or derivation points, not as a reason to mix reusable and local prompt
assets into one directory.

## Physical Mapping

Central home:

- `toolkit/prompts/`

Downstream local home:

- `.raiden/local/prompts/`

This means:

- reusable prompt assets stay in the central toolkit
- repo-specific prompts live only in the downstream local overlay

## Mapping By Prompt Type

| Central Prompt Type | Central Home | Downstream Use |
|---|---|---|
| Bounded task template | `toolkit/prompts/` | derive repo-specific execution prompts under `.raiden/local/prompts/` |
| Compact task template | `toolkit/prompts/` | derive token-lean execution prompts under `.raiden/local/prompts/` |
| Handoff template | `toolkit/prompts/` | derive repo-specific handoff prompts or startup slices under `.raiden/local/prompts/` |
| Pause-point template | `toolkit/prompts/` | export compact cycle-stop handoffs into local state snapshots or equivalent local state surfaces |
| Continuation-state template | `toolkit/prompts/` | carry forward compact working state in `.raiden/state/` or its snapshot/history area |
| Completion template | `toolkit/prompts/` | derive local completion/closeout prompts under `.raiden/local/prompts/` when needed |
| Validation template | `toolkit/prompts/` | derive local validation-check prompts under `.raiden/local/prompts/` |
| Compact review template | `toolkit/prompts/` | derive token-lean local review prompts under `.raiden/local/prompts/` |

## Allowed Downstream Adaptation

A downstream repo may:

- adapt a shared template to local tooling and naming
- create repo-specific execution prompts
- create local handoff prompts tied to local state
- create local audit or review prompts for repo-specific workflows
- store compact continuation exports in local live-state surfaces when they are operationally useful

A downstream repo should not:

- treat local prompts as if they were central reusable defaults
- copy central prompt files into root canon
- replace a shared RAIDEN prompt definition with a local rewrite

## Good Derivation Pattern

A good local prompt derivation:

- starts from a shared RAIDEN template or category
- adds repo-specific paths, tools, and risks
- stays inside `.raiden/local/prompts/`
- references local state files when necessary
- uses compressed machine-oriented language for internal execution layers when safe

## Anti-Drift Rule

If a prompt becomes reusable across multiple repos or task families, it should
be reconsidered for promotion back into `toolkit/prompts/` rather than left as
duplicated local prompt text across many instances.

## Current Non-Goals

This mapping does not yet define:

- exact subfolders under `.raiden/local/prompts/`
- prompt bundle metadata
- updater behavior for prompt deployment

Those remain local or deferred until later canon work requires more specificity.
