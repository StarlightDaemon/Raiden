# Edict Package Lifecycle

## Purpose

This document describes the current high-level lifecycle of a central `Edict`
package without defining package distribution mechanics.

It gives RAIDEN a shared vocabulary for package-state discussions around the
current local CLI updater surface and later package/distribution work.

`Edict` is the central package-side surface. `Writ` is the installed
downstream issued form.

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

The package surface is stable enough that the current local CLI updater can
target it, while broader package and distribution mechanics remain deferred.

Release-ready does not mean released. It means:

- boundary is coherent
- managed ownership is clear
- no obvious local-only material has leaked into the package surface

For current RAIDEN canon, `Release-Ready` also means:

- the managed payload has a real example surface that the local CLI updater can
  target
- package-to-instance mapping is explicit
- compatibility questions are described clearly enough that later package work
  will not need to rediscover the package boundary from scratch
- release-prep review no longer depends on naming or prompt-home ambiguity

`Release-Ready` does not yet require:

- package manifest extensions beyond the current updater contract
- final package archive format
- final downgrade policy or prerelease/build version semantics
- final updater command surface

Those remain later package and distribution concerns.

### 4. Installed

A downstream `RAIDEN Instance` is using a released `Writ` issued from an
`Edict`.

At this stage, the managed core must remain distinct from:

- local overlay
- local live state

### 5. Updated

A later managed `Writ` revision replaces or refreshes the installed one under
the managed-vs-local contract.

The current local CLI updater is the first concrete update mechanism. Any
future updater shape must still:

- update managed core
- preserve local overlay
- preserve local live state
- stop on conflict if managed files were locally modified

### 6. Replaced Or Retired

An older `Edict` package revision or issued `Writ` revision may later be
superseded or retired once package/update rules are mature enough to support
that safely.

## Current Release Threshold

For the current `toolkit/edict/` surface, the practical release-prep threshold
is:

1. a real managed payload example exists
2. the minimum installed managed payload is explicit
3. managed ownership is explicit
4. package-to-instance mapping is explicit
5. compatibility categories are documented
6. no local overlay or live-state materials are mixed into the package surface

If one of those is still missing, the package surface is not yet
`Release-Ready` in the current canon sense even if it looks structurally
plausible.

Use `RELEASE_REVIEW_CHECKLIST.md` for a compact review pass over that
threshold.

## Current Canon Assessment

The current `toolkit/edict/` package surface should presently be treated as
`Release-Ready` in the current RAIDEN release-prep sense.

Why this assessment currently holds:

- a real managed payload example exists under `example-package/payload/`
- the minimum installed managed payload is explicit in `MINIMUM_PAYLOAD.md`
- managed ownership and managed-versus-local boundaries are explicit
- package-to-instance mapping is explicit
- compatibility categories are documented
- release-support positioning is explicit
- no obvious local-only material has leaked into the managed payload

This assessment is intentionally narrow.
It means later package or updater work does not need to rediscover the present managed
package target from scratch.

It does not mean RAIDEN has already settled:

- release artifact format
- migration-record shape
- rollback behavior
- updater command behavior

## What Release Language Must Not Pretend Yet

Current release language must not pretend that RAIDEN has already settled:

- release artifact naming
- manifest markers
- migration record format
- rollback behavior
- updater implementation details beyond the current local CLI surface

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
- not silently treating local edits as `Writ` updates

## Current Deferred Questions

The lifecycle still leaves these unresolved:

- downgrade policy
- manifest extensions beyond the current updater contract
- baseline/install-state extensions beyond the current updater contract
- release artifact format

Those belong to later package, updater, and metadata canon, not this stage.
