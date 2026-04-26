# RAIDEN Snapshot Retirement Full Assessment Prompt For Gemini 3.1 Pro High

Use this as the target-specific working prompt for a `Gemini 3.1 Pro`
high-reasoning pass on whether any retained raw snapshot is now clearly safe to
retire from `reference-repos/`.

## Target Selection

- selected target agent: `Gemini 3.1 Pro`
- selected reasoning level: `high`
- selected pass type: `planning`
- run rule: choose this configuration before launch and keep it fixed for the
  full run

## Why This Target

`RAIDEN` selected `Gemini 3.1 Pro` high for this pass because the task is:

- a high-context read-only assessment across canon, prior assessments, and
  extracted-reference coverage
- comparative rather than implementation-heavy
- sensitive to whether raw-reread arguments still hold after recent canon
  progress
- best served by a careful reassessment of retained evidence value rather than
  a narrow doc-only edit pass

This pass is not primarily about:

- code changes
- package implementation
- updater design

The strongest fit is a high-level review model that can hold the retirement
rule, the prior readiness assessment, and the current canon state together and
judge whether any repo has now moved from plausible reread value to clearly
retireable.

## Runtime Notes

- do not switch model or reasoning level mid-run
- if the pass still leaves material uncertainty about one repo, prefer a
  repo-by-repo judgment rather than a forced all-or-nothing answer
- findings must distinguish:
  - clearly safe to retire now
  - not yet safe to retire
  - unclear and needing one narrower follow-up check

## Expected Standard

This pass should:

- reassess `CTRL`, `HardlinkOrganizer`, and `BIND`
- use the actual retirement rule, not intuition
- test whether recent canon progress removed earlier reread justifications
- identify whether at least one repo now satisfies the checklist's open item
- recommend the smallest justified next action:
  - retire one repo now
  - keep all for now
  - extract one missing pattern first, then retire
  - perform one narrower reread before deciding

## Copyable Prompt Body

Use the fenced block below as the exact copyable prompt body for the selected
target.

```text
Obj: perform a full retirement-readiness reassessment and determine whether at least one retained raw snapshot is now clearly safe to retire from `reference-repos/`
Scope: retirement canon + current readiness assessment + extracted-reference coverage + directly relevant continuity files only
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
- /mnt/e/raiden/reference-extracts/README.md
- /mnt/e/raiden/reference-reviews/2026-04-18__snapshot_retirement_readiness_assessment.md
Then read:
- /mnt/e/raiden/reference-extracts/ctrl/README.md
- /mnt/e/raiden/reference-extracts/hardlinkorganizer/README.md
- /mnt/e/raiden/reference-extracts/bind/README.md
- /mnt/e/raiden/reference-reviews/CTRL/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/CTRL/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-reviews/HardlinkOrganizer/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/HardlinkOrganizer/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-reviews/BIND/REPO_TOOLING_REVIEW.md
- /mnt/e/raiden/reference-reviews/BIND/IMPORT_CANDIDATES.md
- /mnt/e/raiden/reference-reviews/CROSS_REPO_MATRIX.md
- /mnt/e/raiden/reference-reviews/CANONICAL_SOURCE_MAP.md
Only if needed for a specific unresolved retirement claim, reread narrow raw-snapshot files under:
- /mnt/e/raiden/reference-repos/CTRL
- /mnt/e/raiden/reference-repos/HardlinkOrganizer
- /mnt/e/raiden/reference-repos/BIND
Do:
- reassess the retirement eligibility of `CTRL`, `HardlinkOrganizer`, and `BIND` against the actual criteria in `SNAPSHOT_RETIREMENT_RULE.md`
- identify what has changed since the earlier readiness assessment and whether those changes weaken any prior retention argument
- determine for each repo:
- clearly safe to retire now
- not yet safe to retire
- or unclear pending one narrower follow-up check
- if one repo is now clearly safe to retire, say which one and why
- if none are clearly safe, say whether the blocker is:
- missing preserved value
- plausible raw reread still needed
- operator approval only
- or mixed reasons
- recommend the smallest justified next step for each repo
- if the evidence supports it, propose the narrow doc/status updates needed to reflect a newly safe retirement candidate
No:
- do not retire anything directly
- do not edit `reference-repos/`
- do not treat extracted references as automatically complete just because they exist
- do not reopen updater canon beyond retirement-readiness relevance
- do not broaden this into general repo cleanup
- do not force a retirement recommendation when the evidence is still materially ambiguous
Val:
- every judgment is tied to the actual retirement criteria
- prior assessment reasoning is checked against current canon rather than repeated by inertia
- extracted-reference coverage is evaluated for replacement value, not just presence
- any recommendation to retire at least one raw snapshot is backed by clear evidence that raw reread is no longer plausibly needed
- if no repo is ready, the blocker is stated precisely enough to guide the next bounded pass
Out:
- Executive Judgment
- Repo-By-Repo Assessment
- for each repo: criteria status / what changed since prior assessment / current blocker or retirement basis
- Is At Least One Raw Snapshot Clearly Safe To Retire Now?
- Recommended Next Action
- If A Repo Is Ready: exact status/doc updates that should follow
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
