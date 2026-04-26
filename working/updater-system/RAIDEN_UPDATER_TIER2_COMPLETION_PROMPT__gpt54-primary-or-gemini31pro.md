# RAIDEN Updater Tier 2 Completion Prompt

## Status

This is a retained non-canonical working prompt for the next bounded updater
work block after the first updater MVP and first updater-shape canon promotion.

Do not treat this file as root canon.

## Recommended Target

Primary target:

- model: `gpt-5.4`
- reasoning: `high`

Strong alternative:

- model: `Gemini 3.1 Pro`
- reasoning: `high`

Run rule:

- choose the model and reasoning level before launch
- keep the run model-bound and reasoning-bound
- do not assume safe mid-run switching
- if the first pass leaves material ambiguity, launch a second bounded pass
  rather than stretching the same run indefinitely

## Why This Target

This task is no longer MVP invention. It is a mixed canon-and-implementation
closure pass across a narrow but sensitive surface:

- validate which provisional updater choices are now ready for promotion
- refine the ones that are not yet stable enough
- make one explicit policy decision where the MVP intentionally deferred it
- align implementation, docs, tests, and canon together

`gpt-5.4` at high reasoning is the best primary fit because it is strongest for
mixed reasoning/coding/documentation work in this environment and this pass
needs careful file-level execution after a planning/review cycle.

`Gemini 3.1 Pro` at high reasoning is the best alternative when a long-context
comparative review across canon, updater code, tests, and evaluation notes is
preferred before implementation.

## Operator Goal

Finish the remaining post-MVP updater work in one disciplined cycle if
possible.

That means:

1. review the current updater canon, implementation, and Tier 2 evaluation
2. decide what is ready for canon promotion now
3. decide what needs one more implementation/policy refinement first
4. implement the narrow remaining changes
5. promote the validated choices into canon
6. review the result again through tests and consistency checks

## Current Target Surface

The remaining work to close is:

- manifest field-level canonization if the field set is now stable enough
- semver parsing/comparison canonization if the current behavior is now stable
  enough
- anomaly-threshold refinement, especially the high-change-ratio rule for small
  packages
- intentional design decision for managed-file removals:
  - stay manual/operator-driven
  - or gain a safe auto-removal path

This pass should not reopen the basic updater shape.

## Runtime Notes

- start from root canon first
- use `working/updater-system/` only as retained working input
- use the actual implementation under `toolkit/updater/` as evidence, not as
  automatic canon
- if one area is not ready for promotion, keep it provisional rather than
  forcing weak canon
- prefer the smallest durable canon and code changes that close real remaining
  ambiguity

## Exact Copyable Prompt

```text
Mode: review-plan-refine-impl-promote-review
Obj: complete the remaining post-MVP updater work by deciding which Tier 2 provisional items should be promoted now, refining the ones that are not yet stable enough, implementing any needed narrow changes, and aligning canon, docs, and tests
Scope: updater Tier 2 surface only — directly affected canon, updater code, tests, fixtures, and local docs
Read first:
- /mnt/e/raiden/README.md
- /mnt/e/raiden/SOURCE_OF_TRUTH.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/DECISIONS.md
- /mnt/e/raiden/OPEN_LOOPS.md
- /mnt/e/raiden/RELEASE_READY_CHECKLIST.md
- /mnt/e/raiden/MANAGED_VS_LOCAL.md
- /mnt/e/raiden/TOOLKIT_INDEX.md
- /mnt/e/raiden/toolkit/edict/README.md
- /mnt/e/raiden/toolkit/instance/STRUCTURE.md
- /mnt/e/raiden/toolkit/updater/README.md
Then read the implementation and test surface:
- /mnt/e/raiden/toolkit/updater/raiden_updater/models.py
- /mnt/e/raiden/toolkit/updater/raiden_updater/loader.py
- /mnt/e/raiden/toolkit/updater/raiden_updater/version.py
- /mnt/e/raiden/toolkit/updater/raiden_updater/compatibility.py
- /mnt/e/raiden/toolkit/updater/raiden_updater/anomaly.py
- /mnt/e/raiden/toolkit/updater/raiden_updater/planner.py
- /mnt/e/raiden/toolkit/updater/raiden_updater/applier.py
- /mnt/e/raiden/toolkit/updater/raiden_updater/cli.py
- /mnt/e/raiden/toolkit/updater/tests/
- /mnt/e/raiden/toolkit/updater/fixtures/
Then read retained working inputs only as non-canonical evidence:
- /mnt/e/raiden/working/updater-system/BUILD_PLAN.md
- /mnt/e/raiden/working/updater-system/RAIDEN_UPDATER_PREPLAN_AND_BUILD_PROMPT__gpt54-primary.md
Use the Tier 2 evaluation result as direct task guidance:
- manifest fields and semver semantics appear stable enough for promotion
- the 50 percent anomaly ratio is too noisy for small packages and likely needs a minimum file-count constraint
- removal policy is still intentionally unresolved and needs an explicit design decision
Do this in order:
1. Review:
- identify the exact remaining Tier 2 provisional items
- classify them as:
- ready for canon promotion now
- needs one narrow implementation refinement first
- still should remain provisional
- identify whether the current removal behavior should remain manual or gain a safe auto-removal path
2. Plan:
- produce a narrow completion plan with:
- canon files to update
- implementation files to update
- tests/fixtures to add or revise
- exact policy decisions needed
- explicit non-goals
3. Refine:
- critique the first plan
- shrink any unnecessary canon spread
- ensure each promotion claim is backed by implementation evidence or evaluation evidence
- ensure each unpromoted item remains explicitly provisional
4. Implement and promote:
- make the narrow code/doc/test changes needed
- promote validated manifest fields and semver semantics if the evidence supports it
- refine anomaly thresholds if the current ratio rule is too noisy
- make and implement one explicit managed-file removal policy decision
- update canon and local docs only where directly affected
5. Review again:
- run tests
- confirm the updated behavior matches the promoted canon
- confirm deferred items are still clearly marked deferred
- check all changed docs for cross-reference consistency
Primary questions to answer:
- which manifest fields are now stable enough to become canon?
- are current semver parsing and comparison semantics stable enough to become canon?
- what anomaly rule should replace or constrain the current 50 percent change-ratio warning for small packages?
- should managed-file removals remain manual/operator-visible, or should RAIDEN support a safe auto-removal path now?
- if auto-removal is promoted, what is the minimum safe contract?
No:
- do not reopen the choice of local CLI as the first updater shape
- do not broaden into remote distribution, registry resolution, publishing, GUI flows, or drag-and-drop UX
- do not turn manifest canonization into a full package ecosystem design
- do not rewrite unrelated root docs
- do not preserve provisional implementation details as canon unless the evidence now justifies promotion
- do not leave the code, tests, and canon disagreeing about removal behavior or anomaly policy
Val:
- every promotion claim is grounded in current implementation and evaluation evidence
- every non-promoted item is still clearly marked provisional
- tests cover any changed manifest semantics, anomaly behavior, or removal behavior
- affected canon files agree with affected updater docs and implementation behavior
- no unrelated files are modified
Stop:
- stop when the remaining Tier 2 updater work is either promoted, refined, or explicitly left provisional with a clear reason
Out:
- Readable Report:
- Executive Judgment
- Tier 2 Classification
- Completion Plan
- Policy Decisions Made
- Changes Made
- What Was Promoted Into Canon
- What Remains Provisional
- Validation And Tests
- Risks And Follow-On Work
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
- Code Block For Review:
```text
Obj: Evaluate updater MVP Tier 2 provisional items
Scope: updater Tier 2 canon + implementation surface only
Done:
- <review completed>
- <plan created>
- <plan refined>
- <changes implemented>
- <canon promotions completed>
- <validation completed>
Open:
- <none or exact remaining provisional item>
Dec:
- <manifest/semver/anomaly/removal decisions>
Val:
- <tests and consistency checks completed>
Blk:
- <none or exact blocker>
Next:
- <single best next task>
Confidence:
- <observed evidence / strong inference / weak inference / unresolved ambiguity>
```
```
