# CTRL Current-State Handoff Pattern

## Pattern Summary

`CTRL` shows a useful handoff style built around resetting a follow-on agent to the actual repo baseline rather than to a stale plan or broad historical narrative.

The handoff pattern emphasizes:

- what is already true now
- what was intentionally excluded
- what remains safe next work
- where the durable state lives

## Why It Matters To RAIDEN

This is one of the best practical examples of a handoff document that reduces re-derivation cost for a new agent inside a live product repo.

It complements RAIDEN's own continuity layer by showing how a bounded handoff can:

- restate the current baseline
- point back to the durable source of truth
- constrain follow-on scope

## Recommended RAIDEN Use

Preserve the pattern for:

- repo-agent handoffs
- local closeout follow-up notes
- bounded transition prompts

The preferred RAIDEN adaptation is:

- durable state in the canonical local state layer
- handoff documents that summarize only what a follow-on agent needs for the next bounded slice

## Cautions

- do not let handoffs become the long-term source of truth
- do not copy large volumes of dated handoff files by default
- keep the handoff tied to the durable state surface instead of replacing it

## Provenance

Historical primary sources at extraction time:

- `reference-repos/CTRL/reports/2026-03-08__current_state_repo_agent_handoff.md`
- `reference-repos/CTRL/reports/2026-04-10__next_main_rebuild_handoff.md`

Supporting review:

- `reference-reviews/CTRL/REPO_TOOLING_REVIEW.md`
- `reference-reviews/CTRL/IMPORT_CANDIDATES.md`
