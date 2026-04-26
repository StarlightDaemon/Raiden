# CTRL Artifact Policy Pattern

## Pattern Summary

`CTRL` contributes a strong local artifact split:

- durable local state belongs in `agent-ledger/`
- session-shaped prompts, handoffs, and execution artifacts belong in `reports/`

The important reusable idea is the function split, not the exact folder names.

## Why It Matters To RAIDEN

This is one of the clearest practical examples in the reviewed set of separating:

- durable continuity
- bounded execution support

That split helps prevent:

- duplicate closeout summaries
- prompt sprawl becoming accidental authority
- reports being mistaken for the canonical local state

## Recommended RAIDEN Use

Reuse the policy logic:

- one durable local state surface
- one execution-support surface
- explicit instruction that durable state wins when both mention the same work item

Do not copy `CTRL`'s exact `reports/` sprawl as the default operating style.

## Cautions

- `CTRL` is report-heavy, so preserve the principle without inheriting the volume
- older `CTRL` materials do not follow the split perfectly; this is a mature local rule, not proof that the repo always operated this way
- RAIDEN should keep clearer canonical names than `CTRL`'s mixed public-docs, local-ledger, and report surfaces

## Provenance

Historical primary source at extraction time:

- `reference-repos/CTRL/agent-ledger/2026-04-13__local_artifact_policy.md`

Supporting review:

- `reference-reviews/CTRL/REPO_TOOLING_REVIEW.md`
- `reference-reviews/CTRL/IMPORT_CANDIDATES.md`
