# RAIDEN Prompt: Starlight Architect + StarlightDaemonDev Retirement Closure

## Runtime Metadata

- Operator: `RAIDEN`
- Selected target agent: `Claude Opus 4.6 (thinking)`
- Selected reasoning level: `high`
- Selected pass type: `planning`
- Run-fixed note: choose model and reasoning before launch; do not assume they can be changed mid-run

## Why This Target

This task is a bounded high-judgment closure pass, not a broad repo survey.
`Starlight Architect` and `StarlightDaemonDev` are the only remaining primary
reviewed sources still blocking full retirement-review closure. The agent needs
to decide, carefully and minimally, whether each repo needs a narrow extract
set or whether current canon already preserves enough value to mark it
retirement-eligible without new extracts. `Claude Opus 4.6 (thinking)` at high
reasoning is the best fit for that synthesis-heavy, low-noise judgment.

## Operator Goal

Leave the retirement-review effort defensibly closed if possible today. That
means:

- either move `Starlight Architect` and `StarlightDaemonDev` to
  retirement-eligible with evidence-backed reasoning
- or create only the smallest missing extract/disposition surface needed to
  make that judgment

Do not broaden into unrelated retirement work.

## Exact Copyable Prompt

```text
Obj: close the remaining primary reference-repo retirement-review blockers by reassessing `Starlight Architect` and `StarlightDaemonDev`, deciding whether each still needs extraction, and making the smallest justified review/extract/disposition updates needed to leave the retirement-review effort fully closed if possible
Scope: root retirement canon + current disposition/indexing surfaces + only `Starlight Architect` and `StarlightDaemonDev` and their directly relevant review artifacts
Read first:
- /mnt/e/raiden/README.md
- /mnt/e/raiden/SOURCE_OF_TRUTH.md
- /mnt/e/raiden/REPOSITORY_MAP.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/DECISIONS.md
- /mnt/e/raiden/PAST_PRESENT_FUTURE.md
- /mnt/e/raiden/RELEASE_READY_CHECKLIST.md
- /mnt/e/raiden/INGRESS_POLICY.md
- /mnt/e/raiden/SNAPSHOT_RETIREMENT_RULE.md
- /mnt/e/raiden/SOURCE_HISTORY_INDEX.md
- /mnt/e/raiden/reference-reviews/REFERENCE_REPO_DISPOSITION_REGISTER.md
- /mnt/e/raiden/reference-reviews/2026-04-18__snapshot_retirement_readiness_assessment.md
- /mnt/e/raiden/reference-reviews/CROSS_REPO_MATRIX.md
- /mnt/e/raiden/reference-reviews/CANONICAL_SOURCE_MAP.md
- /mnt/e/raiden/reference-reviews/ALL_REPOS_EXPANDED_REVIEW.md
- /mnt/e/raiden/reference-reviews/HIGH_LEVEL_OVERVIEW.md
Then read:
- /mnt/e/raiden/reference-reviews/Starlight Architect/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/Starlight Architect/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-reviews/StarlightDaemonDev/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/StarlightDaemonDev/IMPORT_CANDIDATES.md
Only if needed for a specific extraction or retirement claim, do narrow rereads inside:
- /mnt/e/raiden/reference-repos/Starlight Architect
- /mnt/e/raiden/reference-repos/StarlightDaemonDev
Do:
- reassess both repos against the actual retirement rule, not against inertia from earlier reviews
- determine whether each repo is best handled as:
- retirement-eligible now without extracts
- retirement-eligible after one very small extract set
- or still retained with one precise blocker that cannot be closed today
- prefer the smallest durable closure path
- do not assume extraction is required just because no extract exists yet
- if a very small extract set is genuinely needed, create only the minimum RAIDEN-owned extract surface needed to preserve still-active value
- if current canon/review synthesis already preserves enough value, update the disposition/index surfaces accordingly instead of creating unnecessary extracts
- align all directly affected continuity/review/index files to the post-pass state
- if one or both repos become retirement-eligible, say so clearly but do not delete them unless fresh operator approval is explicitly granted in this run
- if full retirement-review closure still cannot be achieved, state the exact smallest blocker that remains after this pass
No:
- do not reopen updater canon
- do not reopen package-surface design beyond direct retirement relevance
- do not broaden into `Stargate`, `StarlightDaemon`, or already retired repos
- do not create broad extract suites when one compact pattern file would do
- do not force retirement-eligibility if plausible raw reread value still materially remains
- do not edit or delete `reference-repos/` in this pass without explicit fresh operator approval
Val:
- every judgment is tied to `SNAPSHOT_RETIREMENT_RULE.md`
- any new extract is justified by still-active value, not by completionism
- any decision that no extract is needed is backed by specific canon/review coverage already present
- `SOURCE_HISTORY_INDEX.md`, `CURRENT_STATE.md`, and `REFERENCE_REPO_DISPOSITION_REGISTER.md` remain consistent after the pass
- if closure is not reached, the blocker is narrow and explicit
Out:
- Readable Output:
- Executive Judgment
- Repo-By-Repo Assessment
- Changes Made
- Is The Retirement-Review Effort Now Fully Closed?
- If Not Closed: Exact Remaining Blocker
- Recommended Operator Action
- Code Block For Agent Review:
```text
Obj: starlight retirement closure
Scope: `Starlight Architect` and `StarlightDaemonDev` only
Done:
- <review/extract/disposition work completed>
Open:
- <none or exact remaining blocker>
Dec:
- <repo-by-repo disposition decisions>
Val:
- <validation checks completed>
Blk:
- <none or exact blocker>
Next:
- <operator action or final bounded follow-up>
Confidence:
- <observed evidence / strong inference / weak inference / unresolved ambiguity>
```
```
