# RAIDEN Instance Structure

## Purpose

This document defines the first-pass canonical folder structure for a deployed
downstream `RAIDEN Instance`.

It answers:

- where the instance lives in a target repo
- how the managed, local, and live-state layers are separated physically
- which files and subtrees are required versus optional

It defines the current local CLI updater metadata fields, but not broader
metadata extensions or package archives.

## Default Root Shape

The default physical shape of a downstream instance is:

```text
<target-repo>/
├── README.md
├── AGENTS.md
└── .raiden/
    ├── README.md
    ├── writ/
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
- `.raiden/writ/`
  - installed managed core owned by RAIDEN
- `.raiden/local/`
  - repo-local overlay area
- `.raiden/state/`
  - repo-local live continuity state
- `.raiden/instance/`
  - reserved support area for instance typing and install/update support data

## Layer Mapping

### 1. Managed Core

Path:

- `.raiden/writ/`

Role:

- the issued `Writ`
- RAIDEN-owned law and governed reusable material after deployment

Should contain:

- managed governance/law artifacts
- managed shared assets intended to deploy with the instance
- package-side materials that remain RAIDEN-owned after install

Current minimum installed contents for release-prep:

```text
.raiden/writ/
├── README.md
├── OPERATING_RULES.md
└── OWNERSHIP_BOUNDARY.md
```

These files are the current minimum canonical managed payload.
See `toolkit/edict/MINIMUM_PAYLOAD.md` for the package-side definition and
mapping.

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

Current files:

- `metadata.json`
  - instance typing and installed version tracking
- `baseline.json`
  - installed-state record of managed files at last update time

These files were introduced by the first updater MVP (D-0032). Their current
field sets are now canonical for the local CLI updater.

Current `metadata.json` fields:

- `instance_schema_version`
- `instance_form_type`
- `installed_edict_version`
- `managed_roots`
- `overlay_roots`
- `live_state_roots`

Current `baseline.json` fields:

- `installed_edict_version`
- `installed_at`
- `managed_files`

Each baseline `managed_files` entry contains exactly:

- `path`
- `hash`

Unknown extra fields in these current local CLI metadata files are rejected.
Missing `baseline.json` is allowed only for an initial install into a fresh
managed root with no existing files.

This keeps updater-related support material out of live state and out of the
managed `Writ` tree while still reserving a stable home for it.

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

- package or instance metadata extensions beyond the current local CLI updater
  contract
- package manifest extensions beyond the current updater contract
- whether all managed files deploy under `writ/` only or also project-adjacent
  root paths later
- package archive or bundle layout

Those belong to later updater and package canon.
