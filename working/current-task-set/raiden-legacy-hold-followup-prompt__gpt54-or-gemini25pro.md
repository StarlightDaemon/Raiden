# RAIDEN Legacy-Hold Follow-Up Prompt For GPT-5.4 Or Gemini 2.5 Pro

Use this as the bounded follow-up prompt for the only remaining
`reference-repos/` legacy holds:

- `Stargate`
- `StarlightDaemon`

This prompt is for deciding the smallest justified next handling for those two
repos without reopening the already-closed primary retirement workflow.

## Recommended Target

Preferred target:

- model: `gpt-5.4`
- reasoning: `high`

Acceptable alternative:

- model: `Gemini 2.5 Pro` or `Gemini 3.1 Pro`
- reasoning: `high`

Run rule:

- choose model and reasoning before launch
- keep that choice fixed for the full pass
- if the first pass leaves material ambiguity, rerun with stronger reasoning
  rather than switching goals mid-pass

## Why This Target

This is a bounded canon-sensitive review, not a broad repo survey and not an
implementation task.

The agent needs to:

- distinguish legacy-hold follow-up from the closed primary retirement effort
- judge whether `Stargate` and `StarlightDaemon` still justify retention
- avoid overpromoting weak evidence into the main review/extract pipeline
- recommend the smallest durable next step

`gpt-5.4` high is the best default because the task is mostly disciplined
reading, classification, and sequencing against current canon. A strong Gemini
reasoning model is also suitable if that is the preferred runtime.

## Operator Goal

Resolve what follow-up, if any, is actually warranted for the two remaining
legacy holds.

Desired outcome:

- either confirm that both should remain legacy holds for now with no further
  action
- or identify one narrow next action for one or both repos, such as:
  - a bounded review
  - a very small extract need
  - a future cleanup/retirement path after minimal documentation

Do not turn this into a broad new retirement campaign.

## Runtime Notes

- keep the pass read-heavy and judgment-focused
- prefer narrow raw rereads only when a specific disposition claim depends on
  them
- do not treat existence in `reference-repos/` as proof that a repo deserves
  full normalization
- do not recommend deletion in this pass unless canon and evidence make the
  path unusually clear; default to recommending a workflow path, not executing
  cleanup

## Exact Copyable Prompt

```text
Mode: review
Obj: determine the smallest justified follow-up for the only remaining legacy holds in `reference-repos/` (`Stargate` and `StarlightDaemon`) without reopening the already-closed primary retirement workflow
Scope: root canon + retirement/disposition review artifacts + only the two legacy-hold repos and their directly relevant evidence
Read first:
- /mnt/e/raiden/README.md
- /mnt/e/raiden/SOURCE_OF_TRUTH.md
- /mnt/e/raiden/REPOSITORY_MAP.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/GOALS.md
- /mnt/e/raiden/OPEN_LOOPS.md
- /mnt/e/raiden/DECISIONS.md
- /mnt/e/raiden/PAST_PRESENT_FUTURE.md
- /mnt/e/raiden/RELEASE_READY_CHECKLIST.md
- /mnt/e/raiden/INGRESS_POLICY.md
- /mnt/e/raiden/SNAPSHOT_RETIREMENT_RULE.md
- /mnt/e/raiden/reference-reviews/LEGACY_HOLDINGS_TRIAGE.md
- /mnt/e/raiden/reference-reviews/REFERENCE_REPO_DISPOSITION_REGISTER.md
- /mnt/e/raiden/reference-reviews/HIGH_LEVEL_OVERVIEW.md
- /mnt/e/raiden/reference-reviews/ALL_REPOS_EXPANDED_REVIEW.md
Then review the legacy-hold targets:
- /mnt/e/raiden/reference-repos/Stargate
- /mnt/e/raiden/reference-repos/StarlightDaemon
Only if needed for a specific claim, do narrow rereads inside those repos.
Do:
- determine whether `Stargate` should:
- remain a legacy hold with no further action now
- enter one bounded review/extract/retirement path later for its registry/stewardship value
- or be treated as low enough value that future cleanup after minimal documentation is the better path
- determine whether `StarlightDaemon` should:
- remain a historical-provenance legacy hold with no further action now
- receive one bounded provenance-preservation follow-up
- or be treated as low enough active value that future cleanup after minimal documentation is the better path
- distinguish active RAIDEN value from mere ancestry or historical interest
- identify whether either repo is still materially useful to current RAIDEN work
- recommend the smallest justified next step for each repo
- say clearly whether this is release-relevant, cleanliness-only, provenance-only, or optional-later work
- if useful, recommend one grouped handling strategy for both legacy holds together
Importance rules:
- preserve the judgment that primary retirement-review work is already closed
- do not rank this work above active release-prep work unless current canon explicitly requires it
- prefer bounded documentation and disposition clarity over broad new extraction work
- do not force a repo into the full retirement workflow without a concrete canon-backed reason
No:
- do not edit or delete `reference-repos/`
- do not reopen `HardlinkOrganizer`, `BIND`, `ARC`, `ARC-RC`, `Starlight Architect`, or `StarlightDaemonDev`
- do not reopen updater canon or package-surface design
- do not confuse legacy-hold follow-up with a release blocker
- do not treat review artifacts as canon unless root canon explicitly adopts them
Val:
- conclusions match `CURRENT_STATE.md` and preserve the statement that only legacy holds remain
- conclusions match `REFERENCE_REPO_DISPOSITION_REGISTER.md` and preserve closure of the primary retirement workflow
- any recommendation for further normalization has a specific evidence reason
- any recommendation for later cleanup explains why retention adds more noise than value
Out:
- Executive Judgment
- Repo-By-Repo Assessment
- for each repo: current value / why retained / recommended next handling / why now-or-not-now / confidence
- Is Any Legacy-Hold Work Worth Doing Soon?
- If Yes: Single Best Next Task
- If No: Clear Deferral Recommendation
- Risks And Ambiguities
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
