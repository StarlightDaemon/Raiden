# Edict To Writ Compatibility Surface

## Purpose

This document defines the current high-level compatibility surface for a
managed `Edict` package and the `Writ` it installs.

It exists to reduce release-preparation ambiguity around package compatibility
without broadening beyond the current local CLI updater contract.

It does not define:

- exact compatibility markers
- downgrade policy beyond the current core `MAJOR.MINOR.PATCH` comparison
- package manifest extensions beyond the current updater contract
- updater commands

## Core Rule

Compatibility work for `Edict` should focus first on what must remain coherent
between:

- the central package-side `Edict` surface
- the installed `.raiden/writ/` managed core
- the surrounding `RAIDEN Instance` layer contract

At this stage, RAIDEN needs compatibility categories and boundaries, while the
current local CLI contract supplies only the first concrete comparison rules.

## Compatibility Questions RAIDEN Must Eventually Answer

Future package and release canon will need to answer at least these questions:

1. Can this package shape install into the expected `.raiden/writ/` location
   without violating the current instance structure?
2. Does this package still respect the managed-vs-local contract and avoid
   pulling local overlay or live-state material into managed core?
3. Does this package expect any managed files, directories, or support data
   that an older installed instance may not have yet?
4. Would applying this package require a migration or operator attention rather
   than a normal managed-core refresh?
5. Are any shared managed assets being moved, split, added, or retired in a
   way that later release tooling will need to detect explicitly?

## Current Compatibility Categories

### 1. Package-To-Instance Shape Compatibility

This category asks whether the package payload still maps cleanly into the
current downstream instance structure.

High-level concerns:

- the installed payload still belongs under `.raiden/writ/`
- the package does not assume local-only paths are managed-core payload
- the package does not require unresolved project-adjacent deployment shapes

### 2. Managed-Vs-Local Boundary Compatibility

This category asks whether the package still obeys RAIDEN's three-layer model.

High-level concerns:

- managed files remain managed
- local overlay remains outside the package
- local live state remains outside the package
- later instance-support metadata stays distinct from the managed payload unless
  canon explicitly promotes it

### 3. Managed Payload Ownership Compatibility

This category asks whether included files are still clearly RAIDEN-owned and
appropriate for central update.

High-level concerns:

- law and boundary artifacts remain centrally owned
- files that require routine repo-local editing do not leak into the package
- target-specific prompts, context, and exceptions stay out of the managed
  payload

### 4. Installed-Surface Continuity Compatibility

This category asks whether a new package revision preserves a coherent
installed managed-core surface for downstream repos.

High-level concerns:

- an installed `.raiden/writ/` still has a clear managed index
- managed guidance remains interpretable after package changes
- later release work can identify when a change is a normal refresh versus a
  structural shift

### 5. Release Transition Compatibility

This category asks whether moving from one package revision to another is a
simple managed-core update or a more significant transition.

High-level concerns:

- additive managed files versus removed managed files
- reorganized managed paths versus unchanged managed paths
- compatibility notes or migration notes that may be needed later
- operator-visible breaks that later tooling must report instead of silently
  flattening

## Current Practical Use

Use this document when:

- reviewing whether a new `Edict` example or package artifact hardens too much
- deciding whether a proposed managed file belongs in the package surface
- identifying what later updater canon must classify as compatibility-relevant
- improving release-prep documentation without inventing metadata schema

## What Currently Counts As Compatible Enough

For current release-preparation work, a package surface is compatible enough to
keep moving if all of the following are true:

- it maps cleanly to `.raiden/writ/`
- it does not absorb `.raiden/local/` or `.raiden/state/` materials
- it does not depend on unresolved manifest or updater behavior
- its managed files are clearly RAIDEN-owned

This is a release-prep threshold, not a final install/update rule.

## Still Deferred

The following remain intentionally deferred:

- exact compatibility marker shape
- versioning and comparison extensions beyond the current core
  `MAJOR.MINOR.PATCH` comparison
- downgrade and rollback policy
- baseline/install-state extensions beyond the current updater contract
- migration-record format
- release artifact format

Those belong to later package, updater, and metadata canon.
