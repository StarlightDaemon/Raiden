# RAIDEN Legacy Snapshot Triage Prompt For Gemini 3.1 Pro High

Use this as the target-specific working prompt for a `Gemini 3.1 Pro`
high-reasoning pass on the next-best retirement-related review: triaging the
legacy or lower-priority snapshot holdings that still sit in
`reference-repos/` but are not yet normalized into the main retirement
workflow.

## Target Selection

- selected target agent: `Gemini 3.1 Pro`
- selected reasoning level: `high`
- selected pass type: `planning`
- run rule: choose this configuration before launch and keep it fixed for the
  full run

## Why This Target

`RAIDEN` selected `Gemini 3.1 Pro` high for this pass because the task is:

- a high-context read-only classification review across canon, high-level repo
  reviews, and a mixed set of lower-priority retained snapshots
- more comparative and triage-oriented than implementation-heavy
- sensitive to distinctions between:
  - primary evidence still worth normalizing
  - stale low-priority holdings safe for later cleanup
  - repos that should remain retained for a specific reason
- better served by one broad synthesis pass than by a narrow one-repo-at-a-time
  prompt

This pass is not primarily about:

- package implementation
- updater design
- immediate deletion of any repo

The strongest fit is a model that can hold the broader repo set together and
produce a disciplined disposition map rather than a binary retire/keep answer.

## Runtime Notes

- do not switch model or reasoning level mid-run
- if one repo remains ambiguous, prefer classifying it as "needs one narrower
  follow-up review" rather than forcing a weak disposition
- keep the review read-only
- this pass should recommend workflow paths, not execute cleanup

## Expected Standard

This pass should:

- triage the non-primary snapshot holdings still under `reference-repos/`
- identify which of them should:
  - enter the full retirement workflow
  - remain retained for a clear reason
  - or be treated as low-priority legacy evidence that can be cleaned up after
    minimal documentation
- avoid overpromoting weak sources into the main canon pipeline
- produce the smallest defensible next-step map for reducing `reference-repos/`
  over time

## Copyable Prompt Body

Use the fenced block below as the exact copyable prompt body for the selected
target.

```text
Obj: perform the next-best retirement-related review by triaging the lower-priority or legacy snapshot holdings still under `reference-repos/` and determining the right workflow path for each
Scope: retirement canon + current source-history indexing + high-level repo reviews + only the specific legacy snapshot set under review
Read first:
- /mnt/e/raiden/README.md
- /mnt/e/raiden/SOURCE_OF_TRUTH.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/OPEN_LOOPS.md
- /mnt/e/raiden/DECISIONS.md
- /mnt/e/raiden/PAST_PRESENT_FUTURE.md
- /mnt/e/raiden/RELEASE_READY_CHECKLIST.md
- /mnt/e/raiden/INGRESS_POLICY.md
- /mnt/e/raiden/SNAPSHOT_RETIREMENT_RULE.md
- /mnt/e/raiden/SOURCE_HISTORY_INDEX.md
- /mnt/e/raiden/reference-reviews/HIGH_LEVEL_OVERVIEW.md
- /mnt/e/raiden/reference-reviews/ALL_REPOS_EXPANDED_REVIEW.md
- /mnt/e/raiden/reference-reviews/CROSS_REPO_MATRIX.md
- /mnt/e/raiden/reference-reviews/CANONICAL_SOURCE_MAP.md
Review this legacy snapshot set:
- /mnt/e/raiden/reference-repos/Afterglows
- /mnt/e/raiden/reference-repos/Agent Ledger
- /mnt/e/raiden/reference-repos/Nullsector
- /mnt/e/raiden/reference-repos/Stargate
- /mnt/e/raiden/reference-repos/StarlightDaemon
- /mnt/e/raiden/reference-repos/local-vpn-extract
Only if needed for a specific disposition claim, do narrow raw rereads inside those repos.
Do:
- determine whether each repo should be classified as:
- promote into the full retirement workflow later
- retain for a specific evidence reason
- low-priority legacy evidence safe for bounded cleanup after minimal documentation
- or unclear and needing one narrower follow-up review
- do not assume every retained snapshot deserves full extraction or full retirement-readiness work
- identify whether any of these repos are only lingering from early broad intake and are no longer materially useful to active RAIDEN work
- distinguish canonical-source relevance from mere historical presence
- recommend the smallest justified next action for each repo
- if helpful, recommend one grouped next step for the whole legacy set
No:
- do not delete any repo
- do not edit `reference-repos/`
- do not force low-value repos into the main canon pipeline just because they exist
- do not treat broad early review mentions as proof of ongoing evidence value
- do not reopen updater, package, or downstream-structure design
- do not broaden this into a full reassessment of `HardlinkOrganizer`, `BIND`, `Starlight Architect`, `StarlightDaemonDev`, `ARC`, or `ARC-RC`
Val:
- every disposition is tied to current canon and the retirement rule
- recommendations distinguish primary reviewed sources from secondary legacy holdings
- low-priority cleanup recommendations are not confused with formal retirement eligibility under the main rule
- any repo recommended for further normalization has a concrete reason
- any repo recommended for later cleanup has low enough evidence value that keeping it adds more noise than value
Out:
- Executive Judgment
- Repo-By-Repo Disposition
- for each repo: current apparent value / recommended workflow path / rationale / confidence
- Which Repos Should Enter The Full Retirement Workflow?
- Which Repos Look Like Legacy Holdings Safe For Bounded Cleanup After Minimal Documentation?
- Recommended Next Step
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
