# Edict Package Surface

## Purpose

This directory is the first managed `Edict` package surface in the canonical
RAIDEN toolkit subtree.

`Edict` is the managed core artifact inside a downstream `RAIDEN Instance`.
This directory is the central RAIDEN-side home for package-surface material that
will later be consumed by an updater or packaging flow.

## Current Scope

Right now this surface exists to define boundary and provide the smallest real
package example, not full package mechanics.

It is the place where later work should add:

- managed-core package documentation
- package-boundary and ownership rules
- compatibility surface guidance
- lifecycle and release-shape guidance
- release-support positioning guidance
- compact release-readiness review guidance
- concrete package skeleton/examples that stay inside current canon
- manifest and metadata specs once updater canon resumes
- versioned package examples later
- updater-facing compatibility rules later

## Current Materialized Example

The first minimal package skeleton now lives at:

- `toolkit/edict/example-package/`

Its role is to show the smallest useful central package-side shape before
manifest mechanics are defined.

Current example structure:

```text
toolkit/edict/example-package/
├── README.md
└── payload/
    ├── README.md
    ├── OPERATING_RULES.md
    └── OWNERSHIP_BOUNDARY.md
```

Working interpretation:

- `example-package/` is the central package-side example root
- `payload/` is the part that maps to installed managed-core contents
- `payload/` maps directly to `.raiden/edict/` in a downstream `RAIDEN Instance`

The example is intentionally small. It demonstrates a real managed payload
surface without freezing:

- manifest field names
- package archive format
- updater commands
- final internal package taxonomy beyond this example

## Current Non-Goals

This directory does not yet define:

- exact manifest field names
- final package archive format
- updater command behavior
- downstream instance folder names

Those remain deferred until updater-shape work resumes.

## Working Rule

Treat this directory as the central package-side boundary for managed core
materials.

Do not place downstream local overlay or live-state artifacts here.

The example package must remain clearly separate from:

- `.raiden/local/`
- `.raiden/state/`
- `.raiden/instance/`

Use:

- `PACKAGE_BOUNDARY.md` for what belongs in the managed `Edict`
- `PACKAGE_TO_INSTANCE_MAPPING.md` for how the current central example maps to
  installed `.raiden/edict/` and which instance paths remain outside the
  managed package
- `COMPATIBILITY.md` for the high-level compatibility surface that later
  updater canon must classify more precisely
- `RELEASE_NOTES_AND_MIGRATION_POSITION.md` for the current default placement
  of release-support notes relative to the managed payload
- `LIFECYCLE.md` for how a managed package moves from draft to installed state
  and what currently counts as release-ready
- `RELEASE_REVIEW_CHECKLIST.md` for a compact current-canon review pass over
  `Draft`, `Candidate`, and `Release-Ready`
