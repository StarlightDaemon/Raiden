# RAIDEN Current Task Set Review Prompt

Token-lean internal review prompt for identifying the current active RAIDEN task
set from canon.

```text
Mode: review
Obj: identify the current RAIDEN task set still open from canon
Scope: root canon + directly relevant support files; no repo-wide mining
Read:
- /mnt/e/RAIDEN/SOURCE_OF_TRUTH.md
- /mnt/e/RAIDEN/CURRENT_STATE.md
- /mnt/e/RAIDEN/GOALS.md
- /mnt/e/RAIDEN/OPEN_LOOPS.md
- /mnt/e/RAIDEN/DECISIONS.md
- /mnt/e/RAIDEN/PAST_PRESENT_FUTURE.md
- /mnt/e/RAIDEN/TOOLKIT_INDEX.md
- /mnt/e/RAIDEN/INGRESS_POLICY.md
- /mnt/e/RAIDEN/SNAPSHOT_RETIREMENT_RULE.md
- if needed: /mnt/e/RAIDEN/reference-extracts/README.md
- if needed: /mnt/e/RAIDEN/reference-extracts/hardlinkorganizer/README.md
- if needed: /mnt/e/RAIDEN/reference-extracts/bind/README.md
- if needed: /mnt/e/RAIDEN/reference-reviews/CANONICAL_SOURCE_MAP.md
- if needed: /mnt/e/RAIDEN/reference-reviews/CROSS_REPO_MATRIX.md
- only if task status requires it: /mnt/e/RAIDEN/working/updater-system/README.md
- only if task status requires it: /mnt/e/RAIDEN/working/updater-system/BUILD_PLAN.md
Do:
- separate active now, open but paused, closed/not to reopen, optional later, prerequisite-bound work
- identify the single highest-value next active task
- list the next 1-3 supporting follow-on tasks
- call out blockers, sequencing risk, and canon ambiguity
No:
- do not treat review/extract files as canon unless adopted
- do not mine reference-repos unless canon leaves a real ambiguity
- do not reopen settled naming or architecture without contradiction
- do not collapse current-task review into a repo rewrite plan
Val:
- task set matches OPEN_LOOPS.md
- task set matches CURRENT_STATE.md
- active vs paused is explicit
- closed extraction work is not reopened without new evidence
Out:
- Executive Judgment
- Active Task Set: why active, dependencies, blocked/ready
- Paused But Still Open
- Closed Or Not To Reopen
- Immediate Next Task
- Supporting Follow-On Tasks
- Risks And Ambiguities
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
