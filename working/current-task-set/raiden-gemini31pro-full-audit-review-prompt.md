# RAIDEN Gemini 3.1 Pro Full Audit Review Prompt

Use this as the immediate filled-in prompt for a read-only full audit of
RAIDEN's current state.

```text
Mode: review
Obj: perform a full read-only structural audit of current RAIDEN state
Scope: root canon + toolkit subtree + directly relevant review artifacts
Read:
- /mnt/e/RAIDEN/SOURCE_OF_TRUTH.md
- /mnt/e/RAIDEN/CURRENT_STATE.md
- /mnt/e/RAIDEN/GOALS.md
- /mnt/e/RAIDEN/OPEN_LOOPS.md
- /mnt/e/RAIDEN/DECISIONS.md
- /mnt/e/RAIDEN/PAST_PRESENT_FUTURE.md
- /mnt/e/RAIDEN/RELEASE_READY_CHECKLIST.md
- /mnt/e/RAIDEN/TOOLKIT_INDEX.md
- /mnt/e/RAIDEN/MANAGED_VS_LOCAL.md
- /mnt/e/RAIDEN/PROMPT_ASSET_INDEX.md
- /mnt/e/RAIDEN/SNAPSHOT_RETIREMENT_RULE.md
- /mnt/e/RAIDEN/SOURCE_HISTORY_INDEX.md
- /mnt/e/RAIDEN/toolkit/README.md
- /mnt/e/RAIDEN/toolkit/edict/README.md
- /mnt/e/RAIDEN/toolkit/edict/PACKAGE_BOUNDARY.md
- /mnt/e/RAIDEN/toolkit/edict/LIFECYCLE.md
- /mnt/e/RAIDEN/toolkit/instance/README.md
- /mnt/e/RAIDEN/toolkit/instance/STRUCTURE.md
- /mnt/e/RAIDEN/toolkit/instance/PROMPT_MAPPING.md
- /mnt/e/RAIDEN/toolkit/prompts/README.md
- /mnt/e/RAIDEN/toolkit/prompts/GOVERNANCE.md
- /mnt/e/RAIDEN/toolkit/prompts/CATALOG.md
- /mnt/e/RAIDEN/reference-reviews/CROSS_REPO_MATRIX.md
- /mnt/e/RAIDEN/reference-reviews/CANONICAL_SOURCE_MAP.md
- /mnt/e/RAIDEN/reference-reviews/2026-04-18__snapshot_retirement_readiness_assessment.md
- if needed: /mnt/e/RAIDEN/reference-extracts/hardlinkorganizer/
- if needed: /mnt/e/RAIDEN/reference-extracts/bind/
- if needed: /mnt/e/RAIDEN/reference-extracts/ctrl/
- if needed: relevant per-repo files under /mnt/e/RAIDEN/reference-reviews/
Check:
- authority clarity vs evidence/extract/working-artifact confusion
- continuity-file agreement on active, paused, closed, deferred work
- release-ready checklist usefulness as updater gate
- whether toolkit subtree is materially useful vs nominal
- downstream RAIDEN Instance coherence and scope fit
- contradictions across root canon, toolkit docs, and review artifacts
- whether current task order is correct with updater work deferred
- whether key canon artifacts are still missing
- whether retirement-readiness judgments for CTRL, HardlinkOrganizer, and BIND are well supported
- highest-leverage risks if work continues unchanged
No:
- read-only only
- do not read imported prototype repos unless review/extract evidence is insufficient
- do not turn the review into a rewrite plan
- do not reopen settled naming or architecture without contradiction
Out:
- Executive Judgment
- Findings first, ordered by severity/leverage
- each finding: title / why it matters / evidence / recommended adjustment
- What Is Strong
- Weak Or Unclear Areas
- Priority Review
- Recommended Adjustments
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
