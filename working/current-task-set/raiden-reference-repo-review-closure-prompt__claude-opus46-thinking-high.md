# RAIDEN Reference-Repo Review Closure Prompt For Claude Opus 4.6 Thinking High

Use this as the target-specific working prompt for a `Claude Opus 4.6`
thinking-high pass on completing the remaining review/disposition work needed
to bring the `reference-repos/` retirement-review effort to a defensible close.

## Target Selection

- selected target agent: `Claude Opus 4.6`
- selected reasoning level: `high`
- selected pass type: `planning`
- run rule: choose this configuration before launch and keep it fixed for the
  full run

## Why This Target

`RAIDEN` selected `Claude Opus 4.6` thinking-high for this pass because the
task is:

- full-scope and cross-cutting rather than one-repo narrow
- a mix of review completion, disposition judgment, continuity alignment, and
  light documentation work
- sensitive to overclaiming closure where the retirement rule does not yet
  permit it
- best served by one deep synthesis pass that can separate:
  - primary reviewed sources
  - legacy holdings
  - repos ready for retirement
  - repos that still need extraction, reassessment, or explicit retention

This pass is not primarily about:

- code implementation
- updater design
- broad product analysis unrelated to retirement/disposition

The strongest fit is a high-caution reasoning model that can finish the review
work, make defensible repo-by-repo calls, and align the necessary artifacts
without forcing weak conclusions.

## Runtime Notes

- do not switch model or reasoning level mid-run
- if one repo remains materially ambiguous, mark it explicitly rather than
  weakening the whole review
- the goal is to finish the review/disposition work, not to guarantee that
  every remaining raw snapshot can be retired today
- if closure cannot be defensibly claimed, state the exact smallest blocker

## Expected Standard

This pass should:

- complete the remaining review/disposition work for all retained
  `reference-repos/`
- leave no retained snapshot in an unreviewed or undefined state
- distinguish:
  - ready to retire
  - retained with clear blocker
  - legacy holding retained for narrow reason
  - unresolved item needing one explicit follow-up
- update only the minimal artifacts needed to reflect the finished review state

## Copyable Prompt Body

Use the fenced block below as the exact copyable prompt body for the selected
target.

```text
Obj: complete the remaining reference-repo review/disposition work and leave the `reference-repos/` retirement-review effort in a defensible closed or near-closed state today
Scope: retirement canon + source-history index + current review artifacts + remaining retained `reference-repos/` only
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
- /mnt/e/raiden/reference-reviews/2026-04-18__snapshot_retirement_readiness_assessment.md
- /mnt/e/raiden/reference-reviews/LEGACY_HOLDINGS_TRIAGE.md
- /mnt/e/raiden/reference-reviews/HIGH_LEVEL_OVERVIEW.md
- /mnt/e/raiden/reference-reviews/ALL_REPOS_EXPANDED_REVIEW.md
- /mnt/e/raiden/reference-reviews/CROSS_REPO_MATRIX.md
- /mnt/e/raiden/reference-reviews/CANONICAL_SOURCE_MAP.md
- /mnt/e/raiden/reference-extracts/README.md
Then review the remaining retained reference repos and directly relevant artifacts:
- /mnt/e/raiden/reference-repos/ARC
- /mnt/e/raiden/reference-repos/ARC-RC
- /mnt/e/raiden/reference-repos/Agent Ledger
- /mnt/e/raiden/reference-repos/BIND
- /mnt/e/raiden/reference-repos/HardlinkOrganizer
- /mnt/e/raiden/reference-repos/Stargate
- /mnt/e/raiden/reference-repos/Starlight Architect
- /mnt/e/raiden/reference-repos/StarlightDaemon
- /mnt/e/raiden/reference-repos/StarlightDaemonDev
- /mnt/e/raiden/reference-reviews/ARC/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/ARC/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-reviews/ARC-RC/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/ARC-RC/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-reviews/BIND/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/BIND/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-reviews/HardlinkOrganizer/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/HardlinkOrganizer/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-reviews/Starlight Architect/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/Starlight Architect/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-reviews/StarlightDaemonDev/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/StarlightDaemonDev/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-extracts/ctrl/README.md
- /mnt/e/raiden/reference-extracts/hardlinkorganizer/README.md
- /mnt/e/raiden/reference-extracts/bind/README.md
Only if needed for a specific retirement or disposition claim, do narrow rereads inside the raw retained repos.
Do:
- complete the remaining review/disposition work for every repo still present under `reference-repos/`
- determine for each repo whether it is:
- ready to retire now
- retained with a precise current blocker under `SNAPSHOT_RETIREMENT_RULE.md`
- a legacy holding retained for a narrow reason
- or unresolved and needing one explicit follow-up review
- create or update only the minimal review/disposition artifacts needed so no retained repo is left in an undefined state
- if a repo lacks the review/disposition surface needed for defensible handling today, create the smallest such artifact
- align `SOURCE_HISTORY_INDEX.md` and any directly affected review/disposition artifacts to the post-review state
- if a repo is clearly ready to retire, say so, but do not delete it unless operator approval has already been explicitly granted for that repo
- if today cannot defensibly close the full retirement-review effort, state the exact smallest blocker that remains after this pass
No:
- do not edit or delete `reference-repos/` except where explicit operator approval already exists for a named repo
- do not reopen updater, package, or downstream-instance design beyond direct retirement relevance
- do not promote low-value legacy holdings into the full canon pipeline without a concrete reason
- do not create heavy new process layers when a narrow review/disposition artifact is enough
- do not force retirement recommendations where raw reread value is still plausibly active
Val:
- every repo still in `reference-repos/` ends the pass with a defined disposition
- every retirement-ready claim is tied to the actual retirement rule
- every retained repo has a precise reason for retention
- legacy holdings and primary reviewed sources are not conflated
- continuity/indexing updates match the actual post-pass state
- if closure is not achieved, the remaining blocker is minimal and explicit
Out:
- Readable Output:
- Executive Judgment
- Repo-By-Repo Disposition
- What Was Completed In This Pass
- What Still Blocks Full Closure, If Anything
- Recommended Final Operator Action
- Code Block For Agent Review:
```text
Obj: reference-repo review closure
Scope: all remaining retained reference repos
Done:
- <completed review/disposition work>
Open:
- <remaining blocker only if one still exists>
Dec:
- <repo-by-repo disposition decisions>
Val:
- <validation checks completed>
Blk:
- <none or exact blocker>
Next:
- <final operator action or next bounded pass>
Confidence:
- <observed evidence / strong inference / weak inference / unresolved ambiguity>
```
```
