# Revised Snapshot Retirement Rule Concept

## Purpose

This document revises the earlier prototype snapshot retirement idea.

The earlier logic was:

- review completed
- import candidates completed
- synthesis coverage completed
- no unresolved reread questions
- then snapshot may be retired

That is too coarse for large prototype repos.

It assumes a repo can move directly from:

- full raw snapshot

to:

- retired

For several repos, especially large product repos like `CTRL`, that would discard too much useful reference material too early.

The revised concept introduces an intermediate extracted-reference state.

## Core Revision

Prototype retirement should be based on:

**extraction first, retirement second**

RAIDEN should not keep large full-product snapshots forever.
But it also should not delete them immediately after review if they still contain small high-value patterns that have not yet been preserved in a thinner form.

## New Three-State Model

### State 1: Full Snapshot Retained

The imported prototype repo remains in `reference-repos/`.

Use this state when:

- review is still incomplete
- synthesis is still incomplete
- the repo may need direct reread
- reusable patterns have not yet been normalized into smaller artifacts

### State 2: Extracted Reference Retained

The full prototype repo is no longer the primary reference surface.

Instead, RAIDEN keeps:

- per-repo review artifacts
- import candidates
- compact extracted reference documents for the useful patterns

The full snapshot may still exist temporarily, but it is now a candidate for retirement because its real value has been preserved in thinner RAIDEN-owned reference artifacts.

### State 3: Full Snapshot Retired

The bulky raw repo snapshot is removed from `reference-repos/`.

What remains:

- per-repo review artifacts
- import candidates
- synthesis coverage
- extracted reference artifacts
- source-history/index references showing it was reviewed and retired

This is the preferred end state for large snapshots once extraction is mature.

## New Retirement Principle

A full prototype snapshot should only be retired after:

1. its reusable value has been preserved in RAIDEN canon or RAIDEN-owned extracted references
2. the remaining raw product code and product-specific material are no longer needed for active reread

This is the key shift.

The threshold is not just “review exists.”
The threshold is “review exists and the useful parts have been preserved elsewhere.”

## Proposed New Layer

To support this model, RAIDEN should eventually add a compact extracted-reference layer, for example:

- `reference-extracts/`

This layer would sit between:

- `reference-repos/` raw evidence
- root canon

## Proposed Shape Of `reference-extracts/`

Example layout:

```text
reference-extracts/
├── hardlinkorganizer/
│   ├── embedded-instance-pattern.md
│   └── prompt-library-pattern.md
├── ctrl/
│   ├── artifact-policy-pattern.md
│   ├── handoff-pattern.md
│   └── project-space-audit-pattern.md
├── bind/
│   ├── governance-sidecar-pattern.md
│   ├── remote-audit-pattern.md
│   └── maturity-model-pattern.md
```

The extracted-reference layer should contain:

- normalized summaries
- structural patterns
- important caveats
- provenance links back to the reviewed source

It should not contain:

- full product code
- build outputs
- bulky repo-specific operational noise

## What Extraction Means

Extraction does **not** mean copying whole repos into another place.

Extraction means preserving only the high-signal reusable parts, such as:

- structure models
- artifact role models
- agent-boundary patterns
- prompt-interface patterns
- update or audit patterns
- compact examples of especially valuable artifacts

## Example: `CTRL`

Useful to preserve:

- local artifact policy
- current-state handoff pattern
- project-space audit pattern
- selected structure/SOP ideas

Not useful to preserve long term:

- browser extension source
- product adapter code
- most release/audit noise
- local build/test artifacts

`CTRL` is a strong example of why extraction is necessary before retirement.

## Example: `HardlinkOrganizer`

Useful to preserve:

- embedded local control-plane shape
- prompt-library pattern
- continuity file-role separation
- startup/read-order model

Not useful to preserve long term:

- hardlink product code
- Unraid packaging specifics
- product roadmap details

## Example: `BIND`

Useful to preserve:

- sidecar governance-kit pattern
- remote-audit pattern
- handoff/completion prompt interfaces
- maturity-model language

Not useful to preserve long term:

- product implementation code
- Carbon-specific product details
- most release/remediation history

## Revised Retirement Eligibility Rule

A prototype snapshot becomes eligible for full retirement only when all of the following are true:

1. `REPO_TOOLING_REVIEW.md` exists
2. `IMPORT_CANDIDATES.md` exists
3. the repo's role is represented in `CROSS_REPO_MATRIX.md`
4. the repo's role is represented in `CANONICAL_SOURCE_MAP.md`
5. any high-value reusable material has been preserved in:
   - root canon
   - or `reference-extracts/`
6. no open loop still requires direct reread of the raw snapshot
7. operator approval is given

This is the revised core rule.

## Retirement Actions

When a full snapshot is retired:

1. remove the bulky raw repo from `reference-repos/`
2. keep:
   - per-repo review artifacts
   - import candidates
   - synthesis artifacts
   - extracted references
3. update source-history/indexing to record:
   - that the repo was reviewed
   - that the full snapshot was retired
   - what extracted references replaced its active reread role

## Re-Import Rule

If direct raw evidence is needed again later:

- the repo may be re-imported
- the new import should be treated as a fresh evidence snapshot
- earlier reviews remain historical context, not automatic proof that the new snapshot is identical

## Why This Revised Model Is Better

### 1. Less storage bloat

Large product repos do not stay forever just because one or two patterns remain useful.

### 2. Less search noise

Future agents are less likely to search into irrelevant product code and confuse evidence with canon.

### 3. Better pattern preservation

The reusable parts are preserved in RAIDEN-owned artifacts rather than hidden inside product repos.

### 4. Safer deletion threshold

The repo only disappears after its useful structural value is preserved.

## Recommended Sequence

If adopting this concept later, the safest order is:

1. define `reference-extracts/` as a recognized layer
2. create extracted references for the largest/highest-noise reviewed repos
3. update source-history/indexing to reflect extracted-reference coverage
4. retire the first full raw snapshots only after the extraction layer is proven usable

## Candidate Early Extraction Targets

Best first candidates:

1. `CTRL`
   - very high report/code noise ratio relative to long-term reusable value

2. `BIND`
   - strong patterns, but too much product-specific and duplicated governance material

3. `HardlinkOrganizer`
   - very high value, but the reusable portion is structurally smaller than the full product repo

## Review Questions

Before adopting this into canon, the useful review questions are:

1. Should `reference-extracts/` become a formal RAIDEN layer?
2. Should all reviewed repos require extraction before retirement, or only the large/noisy ones?
3. How minimal can an extracted reference be before it stops being trustworthy?
4. Which already-reviewed repo is the best first pilot for this model?

## Bottom Line

The revised retirement rule concept is:

- keep full snapshots while they are still needed as raw evidence
- preserve reusable patterns in thinner RAIDEN-owned extracted references
- retire the bulky raw snapshots only after extraction is complete and reread demand is gone

That is safer and cleaner than review-only retirement.
