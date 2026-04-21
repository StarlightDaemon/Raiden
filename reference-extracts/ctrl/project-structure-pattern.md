# CTRL Project Structure Pattern

## Pattern Summary

`CTRL` contributes a strong structure-guidance pattern aimed at keeping a product repo readable to both humans and agents.

The reusable parts are:

- intentional documentation entrypoints
- explicit local-vs-public artifact separation
- a project structure guide that explains purpose, not just paths
- a repo organization standard that keeps implementation areas and support artifacts distinct

## Why It Matters To RAIDEN

RAIDEN needs structure guidance that future agents can read quickly without guessing where:

- public docs belong
- local operational artifacts belong
- state and policy artifacts belong

`CTRL` is useful here because it treats structure as something that must be explained, not merely implied by folders.

## Recommended RAIDEN Use

Preserve the principle that a repo should expose:

- clear navigation entrypoints
- clear distinctions between outward-facing docs and local operational artifacts
- explicit explanations of why structure exists, not only where files live

Use the idea, but normalize it into RAIDEN's simpler canonical hierarchy.

## Cautions

- much of `CTRL`'s structure guidance is still product-specific
- some references inside the repo point to local practices and report flows that RAIDEN should not copy wholesale
- structure guidance should stay compact enough to remain readable

## Provenance

Primary sources:

- `reference-repos/CTRL/docs/PROJECT_SOP.md`
- `reference-repos/CTRL/docs/reference/project_structure_guide.md`

Supporting review:

- `reference-reviews/CTRL/REPO_TOOLING_REVIEW.md`
- `reference-reviews/CTRL/IMPORT_CANDIDATES.md`
