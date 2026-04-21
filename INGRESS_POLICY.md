# Ingress Policy

## Purpose

This file defines how external repository material enters RAIDEN for review, extraction, and possible promotion.

The goal is to keep RAIDEN's intake process:

- readable
- bounded
- provenance-safe
- low-noise

Ingress is a controlled evidence process, not a bulk import habit.

## Scope

This policy applies to:

- imported prototype repos
- external repo snapshots used for comparison
- future repo evidence brought in to support toolkit, updater, or downstream-instance design

It does not apply to:

- normal edits to RAIDEN canon
- `Source_info/` preserved early RAIDEN source history

## Core Principle

Import first.
Review next.
Extract only if needed.
Retire when safe.

Extraction is conditional, not automatic.

## Ingress Flow

### 1. Snapshot Intake

External repo material enters RAIDEN as a read-only reference snapshot under `reference-repos/`.

Required handling:

- keep the repo isolated from RAIDEN canon
- treat the snapshot as evidence, not authority
- prefer a clean snapshot without transient bulk when practical
- preserve basic provenance if known

Minimum provenance to record when available:

- original repo name or source path
- snapshot date
- branch or commit if known
- notable exclusions if any

## 2. Triage Review

Every imported repo should receive a first-pass review before deeper extraction or promotion work.

The first-pass review should focus on:

- authority surfaces
- governance/control artifacts
- state-tracking patterns
- prompt assets
- navigation artifacts
- toolkit-structure evidence

Do not start by mining product code unless the code is the only evidence for a claimed tooling behavior.

## 3. Per-Repo Review Artifacts

The standard minimum review outputs are:

- `REPO_TOOLING_REVIEW.md`
- `IMPORT_CANDIDATES.md`

These live under `reference-reviews/<repo-name>/`.

Their job is to explain:

- what the repo contributes
- what should be reused
- what should stay historical only
- what must not be copied wholesale

## 4. Synthesis

High-value reviewed repos should be represented in the current RAIDEN synthesis layer:

- `reference-reviews/CROSS_REPO_MATRIX.md`
- `reference-reviews/CANONICAL_SOURCE_MAP.md`

This is where RAIDEN decides whether a pattern is:

- primary source material
- supporting source material
- historical-only evidence

## 5. Optional Extraction

Extraction into `reference-extracts/` is optional and should happen only when needed.

Use extraction when all of the following are true:

- the raw repo is large or noisy
- the repo contains reusable patterns RAIDEN still needs
- those patterns are not yet safely preserved in canon
- keeping the full snapshot as the main reread surface would create unnecessary storage or search burden

Do not extract by default just because a repo was reviewed.

Good extraction targets include:

- artifact-policy patterns
- handoff patterns
- structure guidance
- governance-sidecar patterns
- update or audit patterns

Bad extraction targets include:

- full product source trees
- build outputs
- repo-specific product history
- implementation detail with no RAIDEN reuse value

## 6. Promotion Boundary

Nothing imported through ingress becomes RAIDEN canon by default.

Promotion requires the normal canon path:

1. review
2. comparison when relevant
3. synthesis or explicit decision
4. adoption into a root canonical RAIDEN artifact

## 7. Retirement Boundary

Imported snapshots may only be reduced or removed according to `SNAPSHOT_RETIREMENT_RULE.md`.

The short rule is:

- review alone does not justify retirement
- extraction is only needed when reusable value would otherwise be lost
- retire the full snapshot only after the useful value is preserved elsewhere

## 8. Working Rules

- keep imported evidence out of the RAIDEN root
- do not treat imported wording as canonical by proximity
- prefer pattern extraction over code retention when the product code is not needed
- avoid duplicate intake of the same repo unless a fresh snapshot is materially needed
- if a repo is re-imported later, treat it as a new evidence snapshot

## 9. Current RAIDEN Reading Order

For external repo evidence:

1. start in `reference-reviews/`
2. use `reference-extracts/` when compact preserved patterns exist
3. return to `reference-repos/` only when raw reread is still necessary

For actual authority:

1. return to root canonical RAIDEN docs

## 10. Current Practical Expectation

The current heavy prototype intake was an early normalization phase.

Future intake should usually be narrower:

- import only when there is a real comparison or design reason
- review before extracting
- extract only where it materially reduces risk or clutter
- retire snapshots once the retirement rule is satisfied
