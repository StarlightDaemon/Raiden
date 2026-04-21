# Snapshot Retirement Rule

## Purpose

This file defines when imported prototype repo snapshots under `reference-repos/` may be reduced or removed without losing RAIDEN's usable reference value.

The rule is:

- extraction first
- retirement second

Review completion alone is not enough.

## Scope

This rule applies to imported prototype snapshots kept under `reference-repos/`.

It does not apply to:

- root canonical RAIDEN docs
- `Source_info/` preserved early source history
- `reference-reviews/` review and synthesis artifacts

## Core Model

Prototype evidence moves through three states.

### State 1: Full Snapshot Retained

The full imported repo remains under `reference-repos/`.

Use this state when:

- review is incomplete
- synthesis is incomplete
- direct reread is still likely
- useful patterns have not yet been preserved elsewhere

### State 2: Extracted Reference Retained

The repo's high-value reusable material has been preserved in RAIDEN-owned extracted references under `reference-extracts/`.

The full snapshot may still exist temporarily, but it is no longer the preferred reread surface.

This is the normal transition state before retirement.

### State 3: Full Snapshot Retired

The bulky raw snapshot has been removed from `reference-repos/`.

What remains:

- per-repo reviews
- import candidates
- synthesis coverage
- extracted references
- source-history/index records of the retirement

## Required Principle

A full prototype snapshot becomes eligible for retirement only after its reusable value has been preserved in one or both of these places:

- root RAIDEN canon
- `reference-extracts/`

If the useful pattern still only lives inside the raw repo, the snapshot is not ready for retirement.

## What To Preserve Before Retirement

Preserve only the high-signal reusable material, such as:

- artifact-role models
- current-state or handoff patterns
- prompt-interface patterns
- governance-sidecar patterns
- structure guidance
- update or audit patterns
- compact examples that explain how a pattern works

Do not preserve:

- full product code
- build outputs
- bulky product-specific history
- repo-specific implementation detail with no RAIDEN reuse value

## Retirement Eligibility

A prototype snapshot becomes eligible for full retirement only when all of the following are true:

1. `REPO_TOOLING_REVIEW.md` exists for that repo
2. `IMPORT_CANDIDATES.md` exists for that repo
3. the repo's role is represented in `reference-reviews/CROSS_REPO_MATRIX.md`
4. the repo's role is represented in `reference-reviews/CANONICAL_SOURCE_MAP.md`
5. any reusable material still needed has been preserved in root canon or `reference-extracts/`
6. no open loop still depends on rereading the raw snapshot
7. the operator approves retirement

## Retirement Actions

When a snapshot is retired:

1. remove the raw repo snapshot from `reference-repos/`
2. keep:
   - per-repo review artifacts
   - import candidates
   - synthesis artifacts
   - extracted references
3. update `SOURCE_HISTORY_INDEX.md` to record:
   - that the repo was reviewed
   - whether extracted references were created
   - that the full snapshot was retired

## Retention Exceptions

A snapshot may be kept longer even after review if it is:

- the only strong source for a pattern not yet extracted
- still needed for an open structural decision
- likely to be reread during updater or toolkit-surface design
- explicitly retained by operator choice

## Re-Import Rule

If raw evidence is needed again later:

- the repo may be re-imported
- the earlier reviews remain historical context
- the re-imported copy should be treated as a fresh evidence snapshot if it differs materially

## Current Operating Expectation

Until extracted-reference coverage is broader, reviewed prototype snapshots should be assumed to remain in State 1 or State 2.

Do not retire a large snapshot only because:

- it has already been reviewed
- the repo is inconveniently large
- a narrower summary exists but does not preserve the needed patterns

## Current First Pilot

`CTRL` is the first pilot for the extracted-reference layer because:

- it has high reuse value for artifact policy and handoff discipline
- much of its raw codebase is not needed for RAIDEN canon
- it is a strong example of why extraction should happen before retirement
