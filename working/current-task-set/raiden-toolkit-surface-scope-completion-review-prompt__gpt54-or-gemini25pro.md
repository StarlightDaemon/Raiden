# RAIDEN Toolkit Surface Scoped Completion And Review Prompt For GPT-5.4 Or Gemini 2.5 Pro

Use this as the full-scope working prompt for the current active release-prep
task:

- deepen the initial `toolkit/` and package surface where added docs reduce
  release ambiguity

This pass should plan, review, implement only the smallest justified doc
changes, and leave a clear report for operator review.

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
  rather than widening scope

## Why This Target

This task is a bounded canon-sensitive completion-and-review pass across a
small but interdependent doc surface.

The agent needs to:

- review the current `toolkit/` surface against release-prep canon
- separate real release ambiguity from already-deferred updater questions
- identify the smallest useful completion scope
- make only the doc changes that materially reduce current ambiguity
- output a readable final report and a compact code block suitable for review

This is not broad research, not updater design, and not a repo-wide rewrite.

## Operator Goal

Push the current `toolkit/` surface closer to a scoped completion state for
release-prep review.

Desired outcome:

- any real remaining `toolkit/` or package-surface ambiguity is identified
- only the smallest justified docs are added or refined
- continuity/checklist docs are updated only if the toolkit review changes the
  release-prep judgment
- the pass ends with a clear closure-style report and a compact review block

## Runtime Notes

- prefer narrow, additive documentation over broad restructuring
- focus on `toolkit/edict/`, `toolkit/instance/`, and `toolkit/README.md`
  first; touch prompts only if they directly affect current release ambiguity
- if the current toolkit surface is already sufficient in one area, prefer
  checklist/continuity alignment over inventing more docs
- do not treat non-canonical working files as authority
- keep edits reviewable and avoid creating new categories unless current canon
  clearly requires them

## Exact Copyable Prompt

```text
Mode: review-plan-impl
Obj: deepen the initial `toolkit/` and package surface only where added documentation materially reduces current release ambiguity, then leave a clear scoped-completion report for review
Scope: root release-prep canon + `toolkit/` subtree + only directly affected continuity/checklist docs
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
- /mnt/e/raiden/MANAGED_VS_LOCAL.md
- /mnt/e/raiden/TOOLKIT_INDEX.md
Then read the live toolkit surface:
- /mnt/e/raiden/toolkit/README.md
- /mnt/e/raiden/toolkit/edict/README.md
- /mnt/e/raiden/toolkit/edict/PACKAGE_BOUNDARY.md
- /mnt/e/raiden/toolkit/edict/PACKAGE_TO_INSTANCE_MAPPING.md
- /mnt/e/raiden/toolkit/edict/MINIMUM_PAYLOAD.md
- /mnt/e/raiden/toolkit/edict/COMPATIBILITY.md
- /mnt/e/raiden/toolkit/edict/LIFECYCLE.md
- /mnt/e/raiden/toolkit/edict/RELEASE_REVIEW_CHECKLIST.md
- /mnt/e/raiden/toolkit/edict/RELEASE_NOTES_AND_MIGRATION_POSITION.md
- /mnt/e/raiden/toolkit/instance/README.md
- /mnt/e/raiden/toolkit/instance/STRUCTURE.md
- /mnt/e/raiden/toolkit/instance/PROMPT_MAPPING.md
- /mnt/e/raiden/toolkit/prompts/README.md
- /mnt/e/raiden/toolkit/prompts/GOVERNANCE.md
- /mnt/e/raiden/toolkit/prompts/CATALOG.md
If needed for a specific ambiguity claim, read:
- /mnt/e/raiden/reference-extracts/hardlinkorganizer/embedded-instance-structure-pattern.md
- /mnt/e/raiden/reference-extracts/hardlinkorganizer/continuity-file-roles-pattern.md
- /mnt/e/raiden/reference-extracts/bind/integration-maturity-model-pattern.md
- /mnt/e/raiden/reference-extracts/stargate/registry-and-stewardship-pattern.md
Do:
- identify the actual remaining release-prep ambiguities in the current `toolkit/` surface
- separate true current blockers from intentionally deferred updater, manifest, packaging, distribution, or rollback questions
- choose a scoped completion target for this pass:
- no toolkit doc changes needed; continuity/checklist alignment only
- one narrow doc addition or clarification
- a small coordinated doc set across `toolkit/edict/` and/or `toolkit/instance/`
- prefer the smallest completion scope that materially improves release-readiness clarity
- if editing is justified, implement only the smallest doc changes needed
- update root continuity/checklist docs only if the toolkit judgment materially changes
- leave the `toolkit/` surface more reviewable and less ambiguous than before
Primary questions to answer:
- is the central `Edict` package surface clear enough for release-prep without adding more package taxonomy?
- is the minimum installed `Writ` payload explicit enough for later updater work to have a stable target?
- is the downstream `RAIDEN Instance` relationship to the central toolkit clear enough for current release-prep?
- are there any release-facing gaps in lifecycle, ownership, compatibility, or mapping language that still cause real ambiguity now?
- if ambiguity remains, is it best solved by a toolkit doc change or by continuity/checklist wording?
No:
- do not reopen updater-shape canon
- do not define exact manifest fields
- do not define package archive/bundle format
- do not define version comparison semantics, rollback, downgrade, or distribution behavior
- do not move local overlay or live-state materials into the managed package
- do not reopen naming, authority order, or managed-vs-local contract
- do not broaden into repo-wide planning or broad cleanup
- do not create documentation just to make the subtree look fuller
Val:
- every claimed ambiguity is grounded in current canon
- `Edict`, `payload`, `RAIDEN Instance`, and `Writ` remain distinct and explicit
- updater deferral is preserved
- any new toolkit docs stay within current release-prep scope
- any continuity/checklist change is justified by actual toolkit-state change, not by preference
- touched files agree with `CURRENT_STATE.md`, `RELEASE_READY_CHECKLIST.md`, and `TOOLKIT_INDEX.md`
Stop:
- stop when the smallest justified completion scope is implemented and the remaining ambiguity is either materially reduced or explicitly classified as deferred/not-current
Out:
- Readable Report:
- Executive Judgment
- Actual Remaining Ambiguities
- Scoped Completion Plan Chosen
- Changes Made
- Why These Changes And Not More
- Release-Gate Impact
- Remaining Deferred Questions
- Validation Performed
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
- Code Block For Review:
```text
Obj: toolkit surface scoped completion review
Scope: `toolkit/` + directly affected release-prep canon only
Done:
- <smallest justified toolkit/doc changes completed>
Open:
- <none or exact remaining non-deferred ambiguity>
Dec:
- <scoped completion judgment and why>
Val:
- <consistency checks performed>
Blk:
- <none or exact blocker>
Next:
- <single best next task after this pass>
Confidence:
- <observed evidence / strong inference / weak inference / unresolved ambiguity>
```
```
