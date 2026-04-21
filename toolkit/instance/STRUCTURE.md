# RAIDEN Instance Structure

## Purpose

This document defines the first-pass canonical folder structure for a deployed
downstream `RAIDEN Instance`.

It answers:

- where the instance lives in a target repo
- how the managed, local, and live-state layers are separated physically
- which files and subtrees are required versus optional

It does not define updater metadata fields or package archives.

## Default Root Shape

The default physical shape of a downstream instance is:

```text
<target-repo>/
├── README.md
├── AGENTS.md
└── .raiden/
    ├── README.md
    ├── edict/
    ├── local/
    ├── state/
    └── instance/
```

### Why This Shape

- `README.md` stays the product or repo front door.
- `AGENTS.md` stays at repo root as the startup bridge for agents.
- `.raiden/` keeps the control plane compact and explicit without taking over
  the whole repository.

This preserves the strongest reusable embedded-instance pattern from
`HardlinkOrganizer` while normalizing it into RAIDEN naming.

## Required Paths

### Repo Root

- `README.md`
  - the target repo's normal front door
  - not RAIDEN-managed by default
- `AGENTS.md`
  - the startup bridge into the local `RAIDEN Instance`
  - should direct agent read order into `.raiden/README.md`

### Instance Root

- `.raiden/README.md`
  - local instance index and navigation spine
- `.raiden/edict/`
  - managed core owned by RAIDEN
- `.raiden/local/`
  - repo-local overlay area
- `.raiden/state/`
  - repo-local live continuity state
- `.raiden/instance/`
  - reserved support area for instance typing and install/update support data

## Layer Mapping

### 1. Managed Core

Path:

- `.raiden/edict/`

Role:

- the managed `Edict`
- RAIDEN-owned law and governed reusable material after deployment

Should contain:

- managed governance/law artifacts
- managed shared assets intended to deploy with the instance
- package-side materials that remain RAIDEN-owned after install

Should not contain:

- repo-local prompts
- repo-local state
- local exceptions
- repo-specific context

### 2. Local Overlay

Path:

- `.raiden/local/`

Role:

- repo-specific extension layer that survives RAIDEN updates

Default contents:

```text
.raiden/local/
├── README.md
├── rules/
├── prompts/
├── context/
├── TERMS.md
└── EXCEPTIONS.md
```

Required:

- `README.md`
  - explains the local overlay and its local ownership
- `prompts/`
  - repo-local operational prompts

Expected but may begin empty:

- `rules/`
  - local constraints or local policy extensions
- `context/`
  - repo-specific working context that should survive updates

Optional:

- `TERMS.md`
  - local terminology control when needed
- `EXCEPTIONS.md`
  - explicit local deviations or approved exceptions

### 3. Local Live State

Path:

- `.raiden/state/`

Role:

- local continuity state for the target repo

Default contents:

```text
.raiden/state/
├── README.md
├── CURRENT_STATE.md
├── GOALS.md
├── OPEN_LOOPS.md
├── DECISIONS.md
├── WORK_LOG.md
└── SNAPSHOTS/
```

Required:

- `README.md`
- `CURRENT_STATE.md`
- `GOALS.md`
- `OPEN_LOOPS.md`
- `DECISIONS.md`
- `WORK_LOG.md`

Optional:

- `SNAPSHOTS/`
  - point-in-time captures, pause-point exports, or compact continuation packages if a downstream repo actually needs them

### 4. Instance Support Area

Path:

- `.raiden/instance/`

Role:

- reserved home for instance typing, installation state, and later
  update-support materials

Current rule:

- the directory is part of the canonical structure
- exact filenames inside it remain deferred until updater canon resumes

This keeps updater-related support material out of live state and out of the
managed `Edict` tree while still reserving a stable home for it.

## Startup And Reading Order

The downstream startup pattern is:

1. repo-root `AGENTS.md`
2. `.raiden/README.md`
3. `.raiden/state/CURRENT_STATE.md`
4. `.raiden/state/OPEN_LOOPS.md`
5. other local state, overlay, or managed materials as needed

This preserves a clear entrypoint while keeping local truth inside the instance
rather than scattering it across the repo root.

## What Must Stay Outside The Instance

The following should stay outside `.raiden/` by default:

- product code
- product docs
- build outputs
- product packaging assets
- historical prototype evidence

The instance is a local control plane, not the whole repo.

## Current Non-Goals

This structure does not yet define:

- exact updater metadata filenames
- exact manifest fields
- whether all managed files deploy under `edict/` only or also project-adjacent
  root paths later
- package archive or bundle layout

Those belong to later updater and package canon.
