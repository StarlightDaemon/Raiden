# Managed Vs Local

## Purpose

This document defines the update boundary between:

- RAIDEN-managed core materials
- repo-local overlay materials
- repo-local live state

It exists to ensure that future RAIDEN update mechanisms can refresh the right files without letting downstream repo agents silently rewrite RAIDEN law.

Current naming:

- `RAIDEN` = central governing agent/framework authority
- `RAIDEN Instance` = downstream deployed repo-local form
- `Edict` = managed core artifact within a `RAIDEN Instance`

## Core Rule

RAIDEN law is **managed**, not freely rewritten in downstream repos.

A downstream repo may:

- extend RAIDEN with local rules
- add local prompts
- track local state
- record local decisions and exceptions

A downstream repo may **not** silently rewrite RAIDEN-managed source-of-truth files as if they were local property.

## Three-Layer Model

### 1. Managed Core

This is the RAIDEN-owned layer.

Examples:

- source-of-truth files
- governance/law files
- core boundary definitions
- shared prompt rules and shared prompt assets
- updater metadata
- version manifests
- the `Edict` artifact set

Characteristics:

- updated by RAIDEN package/update flow
- versioned as a managed unit
- should not be manually rewritten by downstream repo agents during normal repo work

### 2. Local Overlay

This is the target-repo-owned extension layer.

Examples:

- local repo rules
- target-specific constraints
- local prompts for bounded work
- repo-specific context
- repo-specific exceptions

Characteristics:

- owned by the target repo
- preserved during RAIDEN updates
- can extend or constrain local use
- must not pretend to replace RAIDEN core law

### 3. Local Live State

This is the target repo's continuity layer within a `RAIDEN Instance`.

Examples:

- current state
- goals
- open loops
- local decisions
- work log

Characteristics:

- changes often
- belongs to the downstream repo instance
- should survive RAIDEN updates
- records local reality, not central RAIDEN canon

## Update Rule

RAIDEN updates should:

1. update the managed core
2. preserve the local overlay
3. preserve the local live state
4. refuse silent overwrite when a managed file was locally modified

If a managed file has local edits, the updater should:

- stop
- report the conflict
- require explicit resolution

It should not silently replace a locally edited law file.

## Downstream Agent Rule

A downstream repo agent may:

- write local rules in approved local-overlay artifacts
- write local prompts in repo-local prompt areas
- update local state and local decisions

A downstream repo agent may not:

- rewrite RAIDEN-managed source-of-truth or law files in place
- claim local edits to managed core files are canonical RAIDEN changes
- bypass the update boundary by moving core law into local notes

## Central Toolkit Rule

Shared prompt rules, governance rules, and canonical reusable prompt assets belong to the central RAIDEN toolkit layer.

Repo-local operational prompts belong to the downstream repo subtree after deployment.

This preserves a clean distinction between:

- reusable RAIDEN guidance
- target-specific operating prompts

## Versioning Requirement

Both supported RAIDEN forms must be clearly typed and versioned:

- central toolkit/package form
- downstream embedded-instance form

That versioning should make it easy to determine:

- what is installed
- what can be updated
- what is local-only
- what may break compatibility

## Future Update Shapes

The update mechanism could later take more than one form, for example:

- CLI updater
- drag-and-drop package/bundle updater
- manual import/update bundle

All update mechanisms must still obey the same contract:

- update managed core
- preserve local overlay
- preserve live state
- block silent overwrite of locally modified managed files

## Canonical Implication

RAIDEN central law is maintained in RAIDEN canon.

Downstream repos may adapt locally, but adaptation happens through overlay and local state layers, not through silent mutation of RAIDEN core law.

## Default Downstream Physical Layout

The default physical root of a downstream `RAIDEN Instance` is:

- repo-root `AGENTS.md` as the startup bridge
- a compact `.raiden/` subtree as the instance home

Within `.raiden/`, the first-pass canonical structure is:

- `edict/`
  - managed core owned by RAIDEN
- `local/`
  - repo-local overlay materials
- `state/`
  - repo-local live continuity state
- `instance/`
  - reserved home for instance typing and install/update support data

This layout is documented in more detail under `toolkit/instance/`.
