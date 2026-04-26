# Edict Package Surface

## Purpose

This directory is the first central `Edict` package surface in the canonical
RAIDEN toolkit subtree.

`Edict` is the central RAIDEN-authored managed instruction/package surface.
Its installable `payload/` becomes a downstream `Writ` inside a
`RAIDEN Instance`.
This directory is the central RAIDEN-side home for package-surface material
that will later be consumed by an updater or packaging flow.

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
- the current local CLI manifest contract where package-facing docs need it
- versioned package examples later
- updater-facing compatibility rules later

## Current Materialized Example

The first minimal package skeleton now lives at:

- `toolkit/edict/example-package/`

Its role is to show the smallest useful central package-side shape before
manifest mechanics are defined.

`payload` is a technical package term for the installable subset of an `Edict`.
After install, that payload becomes the downstream `Writ`.

The current minimum canonical installed payload for release-prep is defined in:

- `MINIMUM_PAYLOAD.md`

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
- `payload/` is the technical installable subset of an `Edict`
- `payload/` maps directly to `.raiden/writ/` in a downstream `RAIDEN Instance`
- the current `payload/` file set is the minimum canonical installed `Writ`
  payload for current release-prep

The example is intentionally small. It demonstrates a real managed payload
surface without freezing:

- package manifest extensions beyond the current updater contract
- package archive format
- updater commands
- final internal package taxonomy beyond this example

Current status in canon:

- the `toolkit/edict/` surface is currently assessed as `Release-Ready` in the
  present RAIDEN release-prep sense
- this is a release-prep maturity assessment, not a statement that updater or
  package metadata canon is complete

## Current Non-Goals

This directory does not yet define:

- package manifest extensions beyond the current updater contract
- final package archive format
- updater command behavior beyond the current local CLI surface
- instance-side metadata extensions beyond the current local CLI contract

Those remain deferred until later package, updater, or distribution work has
direct evidence for them.

## Updater MVP Connection

The first updater MVP (D-0032) under `toolkit/updater/` consumes a
`manifest.json` file at the package root adjacent to `payload/`.

This manifest location now matches current updater canon for the local CLI
surface. The broader package ecosystem beyond that narrow manifest contract
remains intentionally deferred.

## Working Rule

Treat this directory as the central package-side boundary for managed core
materials.

Do not place downstream local overlay or live-state artifacts here.

The example package must remain clearly separate from:

- `.raiden/local/`
- `.raiden/state/`
- `.raiden/instance/`

Use:

- `PACKAGE_BOUNDARY.md` for what belongs in the central `Edict` and what may
  issue into a downstream `Writ`
- `PACKAGE_TO_INSTANCE_MAPPING.md` for how the current central example maps to
  installed `.raiden/writ/` and which instance paths remain outside the
  managed package
- `MINIMUM_PAYLOAD.md` for the current minimum canonical installed managed-core
  target used during release preparation
- `COMPATIBILITY.md` for the high-level compatibility surface that later
  updater and package work may classify more precisely
- `RELEASE_NOTES_AND_MIGRATION_POSITION.md` for the current default placement
  of release-support notes relative to the managed payload
- `LIFECYCLE.md` for how a managed package moves from draft to installed state
  and what currently counts as release-ready
- `RELEASE_REVIEW_CHECKLIST.md` for a compact current-canon review pass over
  `Draft`, `Candidate`, and `Release-Ready`
