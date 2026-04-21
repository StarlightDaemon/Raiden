# Edict Lifecycle

## Purpose

This document describes the current high-level lifecycle of a managed `Edict`
package without defining the updater implementation or manifest schema.

It gives RAIDEN a shared vocabulary for package-state discussions before the
full updater shape is canonized.

## Lifecycle Stages

### 1. Draft

Central RAIDEN materials are being prepared, normalized, or reorganized into a
managed-core package candidate.

Typical activity:

- clarify boundary
- prepare package-side docs
- identify what belongs in managed core versus local layers

At this stage, package shape is still being formed.

Typical signs that a package is still in `Draft`:

- the managed payload is not yet materialized even as an example
- ownership is still being argued file by file
- package-to-instance mapping is still implicit or unstable
- release-readiness would depend on unresolved boundary cleanup

### 2. Candidate

A coherent managed-core package shape exists conceptually and is being checked
for consistency against:

- root canon
- managed-vs-local rules
- downstream preservation requirements

Typical activity:

- review package boundary
- confirm shared assets are correctly typed
- identify compatibility questions that must be answered later

`Candidate` means the package surface is coherent enough to review as one
managed unit, but not yet strong enough to treat as release-ready.

Typical signs that a package is in `Candidate`:

- a real managed payload example exists
- package-to-instance mapping is explicit
- managed-vs-local separation is mostly clear
- remaining work is about release confidence and compatibility framing rather
  than basic package identity

### 3. Release-Ready

The package surface is stable enough that an updater or installer could target
it once the remaining metadata and compatibility canon exists.

Release-ready does not mean released. It means:

- boundary is coherent
- managed ownership is clear
- no obvious local-only material has leaked into the package surface

For current RAIDEN canon, `Release-Ready` also means:

- the managed payload has a real example surface that a later updater could
  target
- package-to-instance mapping is explicit
- compatibility questions are described clearly enough that later updater work
  will not need to rediscover the package boundary from scratch
- release-prep review no longer depends on naming or prompt-home ambiguity

`Release-Ready` does not yet require:

- final manifest schema
- final package archive format
- exact version comparison rules
- final updater command surface

Those remain later updater-shape concerns.

### 4. Installed

A downstream `RAIDEN Instance` is using a released `Edict` managed core.

At this stage, the managed core must remain distinct from:

- local overlay
- local live state

### 5. Updated

A later managed-core revision replaces or refreshes the installed one under the
managed-vs-local contract.

The exact update mechanism is still deferred, but any future updater must:

- update managed core
- preserve local overlay
- preserve local live state
- stop on conflict if managed files were locally modified

### 6. Replaced Or Retired

An older managed package revision may later be superseded or retired once
package/update rules are mature enough to support that safely.

## Current Release Threshold

For the current `toolkit/edict/` surface, the practical release-prep threshold
is:

1. a real managed payload example exists
2. managed ownership is explicit
3. package-to-instance mapping is explicit
4. compatibility categories are documented
5. no local overlay or live-state materials are mixed into the package surface

If one of those is still missing, the package surface is not yet
`Release-Ready` in the current canon sense even if it looks structurally
plausible.

Use `RELEASE_REVIEW_CHECKLIST.md` for a compact review pass over that
threshold.

## What Release Language Must Not Pretend Yet

Current release language must not pretend that RAIDEN has already settled:

- release artifact naming
- manifest markers
- migration record format
- rollback behavior
- updater implementation details

Those remain intentionally deferred.

## Current Responsibilities By Layer

Central RAIDEN is responsible for:

- package boundary definition
- managed ownership definition
- shared asset preparation
- future compatibility and release rules

Downstream repos are responsible for:

- local overlay content
- local live state content
- not silently treating local edits as managed-core updates

## Current Deferred Questions

The lifecycle still leaves these unresolved:

- exact version comparison rules
- downgrade policy
- required compatibility markers
- baseline/install-state record shape
- release artifact format

Those belong to later updater and metadata canon, not this stage.
