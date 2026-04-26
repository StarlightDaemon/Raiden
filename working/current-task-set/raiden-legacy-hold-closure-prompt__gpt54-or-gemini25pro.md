# RAIDEN Legacy-Hold Closure Prompt For GPT-5.4 Or Gemini 2.5 Pro

Use this prompt for a bounded closure pass on the last two legacy holdings in
`reference-repos/`:

- `Stargate`
- `StarlightDaemon`

The goal is not to reopen the primary retirement workflow.
The goal is to preserve any still-useful historical or governance value in the
smallest RAIDEN-owned form, then retire the raw snapshots if that preservation
is sufficient.

## Recommended Target

Preferred target:

- model: `gpt-5.4`
- reasoning: `high`

Acceptable alternative:

- model: `Gemini 2.5 Pro` or `Gemini 3.1 Pro`
- reasoning: `high`

Run rule:

- choose model and reasoning before launch
- keep that choice fixed for the full run
- if the first pass leaves material ambiguity, rerun with stronger reasoning
  rather than broadening scope

## Why This Target

This is a closure-and-normalization pass with light implementation judgment.
The agent needs to:

- determine whether either legacy repo still holds bounded value worth
  preserving
- avoid inflating low-value historical residue into a full new review pipeline
- create only the minimum extract/provenance surface needed
- align the affected review/index/continuity docs
- retire the raw snapshots if the evidence shows retention is no longer needed

This is more than read-only triage, but still narrower than a repo-wide
refactor or broad canon rewrite.

## Operator Goal

Close the issue for both legacy holds in one pass if possible.

Desired end state:

- any still-useful value from `Stargate` or `StarlightDaemon` is preserved in a
  compact RAIDEN-owned form
- the legacy-hold status is resolved into a clearer final disposition
- if nothing material remains in the raw snapshots after preservation, the raw
  repos are retired in the same pass

Prefer the smallest durable closure path.

## Runtime Notes

- keep the pass tightly scoped to these two repos and directly affected
  continuity/review/index files
- do narrow rereads inside the raw repos only when needed to justify an extract
  or retirement claim
- prefer one compact extract or provenance note over a broad extract suite
- do not preserve product code, duplicate prototypes, or UI assets unless they
  carry direct governance/provenance value for RAIDEN
- if one repo still has plausible unresolved value, close the other and leave
  one explicit blocker rather than forcing a weak retirement

## Exact Copyable Prompt

```text
Mode: review-and-close
Obj: close the remaining legacy-hold issue for `Stargate` and `StarlightDaemon` by preserving any still-useful RAIDEN-relevant value in the smallest RAIDEN-owned form and retiring the raw snapshots if that preservation makes continued retention unnecessary
Scope: root canon + legacy-hold review/index surfaces + only `Stargate` and `StarlightDaemon` and their directly relevant evidence
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
- /mnt/e/raiden/SOURCE_HISTORY_INDEX.md
- /mnt/e/raiden/reference-reviews/LEGACY_HOLDINGS_TRIAGE.md
- /mnt/e/raiden/reference-reviews/REFERENCE_REPO_DISPOSITION_REGISTER.md
- /mnt/e/raiden/reference-reviews/HIGH_LEVEL_OVERVIEW.md
- /mnt/e/raiden/reference-reviews/ALL_REPOS_EXPANDED_REVIEW.md
Then inspect only:
- /mnt/e/raiden/reference-repos/Stargate
- /mnt/e/raiden/reference-repos/StarlightDaemon
Do narrow rereads only where needed to support a specific extraction, provenance, or retirement judgment.
Do:
- determine whether `Stargate` still contains any bounded RAIDEN-relevant value worth preserving, especially around:
- registry discipline
- stewardship rules
- prototype-sprawl control
- handoff/archive separation
- determine whether `StarlightDaemon` still contains any bounded RAIDEN-relevant value worth preserving, especially around:
- early prompt/audit lineage
- lightweight startup/workflow patterns
- provenance of later RAIDEN-relevant concepts
- for each repo, decide whether the right closure path is:
- no extract needed; raw repo can be retired
- one minimal RAIDEN-owned extract or provenance note is needed first, then retire the raw repo
- retain temporarily because one narrow blocker still prevents safe retirement
- if an extract or provenance note is genuinely needed, create only the minimum durable artifact needed to preserve the still-useful value
- avoid preserving raw project/UI/product material that does not materially support RAIDEN governance, provenance, or source-history understanding
- update all directly affected docs so status is consistent after the pass
- if a repo becomes safe to retire in this pass, retire it from `reference-repos/`
- if one repo cannot be retired safely, state the exact smallest blocker and leave everything else closed
Preferred artifact strategy:
- use a compact RAIDEN-owned Markdown note rather than a large extract suite unless a larger extract is clearly necessary
- if the value is mostly provenance, prefer updating `SOURCE_HISTORY_INDEX.md` and/or `reference-reviews/LEGACY_HOLDINGS_TRIAGE.md`
- if the value is a reusable pattern, prefer a small file under `reference-extracts/` with clear provenance
Likely files to update if needed:
- /mnt/e/raiden/SOURCE_HISTORY_INDEX.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/PAST_PRESENT_FUTURE.md
- /mnt/e/raiden/reference-reviews/LEGACY_HOLDINGS_TRIAGE.md
- /mnt/e/raiden/reference-reviews/REFERENCE_REPO_DISPOSITION_REGISTER.md
- /mnt/e/raiden/reference-extracts/README.md
- a new narrowly scoped file under `/mnt/e/raiden/reference-extracts/` only if justified
Importance rules:
- preserve the fact that the primary retirement-review workflow is already closed
- prefer small durable preservation over broad archival perfectionism
- prefer retiring noise once its useful value is preserved
- do not let cleanliness work outrank active release-prep work more than necessary to finish this bounded closure
No:
- do not reopen the primary retirement workflow for already retired repos
- do not broaden into `HardlinkOrganizer`, `BIND`, `ARC`, `ARC-RC`, `Starlight Architect`, or `StarlightDaemonDev`
- do not reopen updater canon or package-surface design
- do not treat legacy-hold closure as a reason for broad root-canon rewrites
- do not preserve large product code trees, duplicate prototype branches, or bulky assets unless they carry direct RAIDEN value
- do not leave status drift between continuity docs and review/index docs
Val:
- every keep/extract/retire judgment is tied to current canon and source-history rules
- any new preserved artifact is clearly narrower and more durable than the raw snapshot it replaces
- if a raw repo is retired, its RAIDEN-relevant value is still findable through canon/review/extract/index surfaces
- `CURRENT_STATE.md`, `SOURCE_HISTORY_INDEX.md`, and `REFERENCE_REPO_DISPOSITION_REGISTER.md` agree after the pass
- if closure is not complete, the remaining blocker is narrow and explicit
Out:
- Executive Judgment
- Repo-By-Repo Closure Decision
- Changes Made
- What Was Preserved From Each Repo
- What Was Retired
- Is The Legacy-Hold Issue Now Closed?
- If Not Closed: Exact Remaining Blocker
- Recommended Operator Action
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
