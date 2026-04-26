# RAIDEN GPT-5.4 Priority Task Review Prompt

Use this as the immediate filled-in handoff prompt for a read-only priority
review of RAIDEN's current task set.

Recommended runtime:

- model: `gpt-5.4`
- reasoning: `high`
- use `xhigh` only when the first review still leaves material task-order
  ambiguity, unresolved contradiction, or weak confidence

Select the model and reasoning level before launch.
Assume the agent is fixed to that model/reasoning choice for the full run.
If the first pass fails materially, start a new pass with a stronger setting;
do not plan around switching mid-run.

Use the fenced block below as the exact copyable prompt body.

```text
Mode: review
Obj: identify the current RAIDEN task set and rank it in order of importance from canon
Scope: root canon + directly relevant toolkit/support files; no repo-wide mining
Read:
- /mnt/e/raiden/README.md
- /mnt/e/raiden/SOURCE_OF_TRUTH.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/GOALS.md
- /mnt/e/raiden/OPEN_LOOPS.md
- /mnt/e/raiden/DECISIONS.md
- /mnt/e/raiden/PAST_PRESENT_FUTURE.md
- /mnt/e/raiden/RELEASE_READY_CHECKLIST.md
- /mnt/e/raiden/TOOLKIT_INDEX.md
- /mnt/e/raiden/MANAGED_VS_LOCAL.md
- /mnt/e/raiden/INGRESS_POLICY.md
- /mnt/e/raiden/SNAPSHOT_RETIREMENT_RULE.md
- /mnt/e/raiden/toolkit/prompts/GOVERNANCE.md
- if needed: /mnt/e/raiden/reference-extracts/README.md
- if needed: /mnt/e/raiden/reference-extracts/hardlinkorganizer/README.md
- if needed: /mnt/e/raiden/reference-extracts/bind/README.md
- if needed: /mnt/e/raiden/reference-reviews/2026-04-18__snapshot_retirement_readiness_assessment.md
- only if a status claim depends on them: /mnt/e/raiden/working/updater-system/README.md
- only if a status claim depends on them: /mnt/e/raiden/RAIDEN_NEXT_STEP_WORKING_PLAN.md
Do:
- identify active now, open but paused, closed/not to reopen, optional later, and prerequisite-bound work
- rank active and paused work in order of importance
- choose one single highest-priority next task
- list the next 2-5 follow-on tasks in descending importance
- explain why each task is above or below the others
- call out blockers, sequencing dependencies, and canon ambiguity
- separate what is operationally important now from what is merely unresolved
Importance rules:
- prioritize work that reduces current release ambiguity before deferred updater work
- do not rank paused updater work above active release-prep work unless canon now requires it
- prefer tasks that unblock other current work
- prefer canon-backed active work over speculative cleanup
- treat narrow continuity alignment as higher value than broad rewrite plans when drift is real
No:
- do not treat review/extract files as canon unless explicitly adopted
- do not mine reference-repos unless canon leaves a real ambiguity
- do not reopen settled naming, downstream structure, or updater design without contradiction
- do not collapse task review into a repo rewrite plan
- do not recommend updater planning/building before RAIDEN is materially closer to a v1 release state
Val:
- ranked task set matches CURRENT_STATE.md
- ranked task set matches OPEN_LOOPS.md
- ranked task set matches RELEASE_READY_CHECKLIST.md
- active vs paused is explicit
- updater deferral is preserved
- no completed downstream-structure work is mislisted as future active work
Out:
- Executive Judgment
- Priority-Ordered Task List
- for each task: status / why now / dependencies / blocked-or-ready
- Highest-Priority Next Task
- Follow-On Tasks
- Paused But Still Open
- Closed Or Not To Reopen
- Risks And Ambiguities
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
