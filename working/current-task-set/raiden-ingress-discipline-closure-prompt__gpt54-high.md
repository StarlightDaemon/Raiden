# RAIDEN Ingress-Discipline Closure Prompt For GPT-5.4 High

Use this as the target-specific working prompt for a `GPT-5.4` high-reasoning
pass on closing the "future evidence intake stays narrow and policy-driven"
gap.

## Target Selection

- selected target agent: `GPT-5.4`
- selected reasoning level: `high`
- selected pass type: `planning`
- run rule: choose this configuration before launch and keep it fixed for the
  full run

## Why This Target

`RAIDEN` selected `GPT-5.4` high for this pass because the task is:

- a bounded canon-and-continuity review across a small document set
- focused on turning an existing policy into a practical closure condition
- sensitive to overbuilding process where a small operational rule may be
  enough
- likely to require careful distinction between real practice gaps and simple
  checklist drift

This pass is not primarily about:

- broad research
- large implementation work
- repo-wide restructuring

The best fit is a strong reasoning pass that can identify the smallest
canon-safe way to close the loop.

## Runtime Notes

- do not switch model or reasoning level mid-run
- if this pass still leaves material ambiguity about the smallest closure path,
  start a new pass rather than stretching the same run
- prefer a narrow operationalization of the existing policy over inventing a
  new heavyweight process

## Expected Standard

This pass should:

- determine what work is actually needed to close `LOOP-0014`
- distinguish policy already written from practice still unproven
- prefer the smallest durable operational surface that makes future intake
  auditable
- update continuity and checklist state only if the closure condition is
  actually met by the edits

## Copyable Prompt Body

Use the fenced block below as the exact copyable prompt body for the selected
target.

```text
Obj: close the remaining "future evidence intake stays narrow and policy-driven" gap by turning the existing ingress policy into a small practical operational surface and aligning continuity docs only as justified
Scope: ingress-policy canon + directly related continuity/checklist files only
Read:
- /mnt/e/raiden/README.md
- /mnt/e/raiden/SOURCE_OF_TRUTH.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/GOALS.md
- /mnt/e/raiden/OPEN_LOOPS.md
- /mnt/e/raiden/DECISIONS.md
- /mnt/e/raiden/PAST_PRESENT_FUTURE.md
- /mnt/e/raiden/RELEASE_READY_CHECKLIST.md
- /mnt/e/raiden/INGRESS_POLICY.md
- /mnt/e/raiden/SNAPSHOT_RETIREMENT_RULE.md
- /mnt/e/raiden/WORKBOOK.md
- /mnt/e/raiden/AGENT_BOUNDARIES.md
- /mnt/e/raiden/working/current-task-set/2026-04-20__session_pause_point.md
- only if needed for structure alignment: /mnt/e/raiden/REPOSITORY_MAP.md
Do:
- review the active ingress-policy gap and determine what is still missing in practice, not just in wording
- decide whether the smallest valid closure path is:
- checklist drift only
- continuity drift only
- one new narrow operational artifact
- one small addition to existing ingress canon
- or a combination of the above
- prefer the smallest durable mechanism that makes future external repo intake auditable and intentionally bounded
- if needed, implement that mechanism with narrow doc edits only
- update `OPEN_LOOPS.md` and `RELEASE_READY_CHECKLIST.md` only if the success condition is actually met after the edits
- align any directly affected continuity docs so they do not overstate or understate the new status
No:
- do not reopen updater work
- do not reopen package or downstream-structure questions
- do not create a heavy approval bureaucracy when a light intake gate or checklist is enough
- do not invent new canon layers if an existing file can carry the rule
- do not mine `reference-repos/`, `reference-reviews/`, or `reference-extracts/` unless a canon claim cannot be checked otherwise
- do not broaden this into retirement-readiness work beyond what the ingress issue directly requires
Val:
- any claimed remaining gap is grounded in current canon
- any claimed closure mechanism is operational, not only rhetorical
- ingress remains a controlled evidence process, not a bulk import habit
- imported evidence stays outside canon by default
- continuity and checklist status changes match the actual post-edit state
- updater deferral and current release-prep priorities remain intact
Out:
- Executive Judgment
- Smallest Closure Path
- Changes Made
- Why This Is Enough Or Not Yet Enough
- Status Recommendation For LOOP-0014
- Status Recommendation For RELEASE_READY_CHECKLIST.md section 5
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
