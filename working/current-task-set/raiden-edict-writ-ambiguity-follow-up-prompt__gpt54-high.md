# RAIDEN Edict-Writ Ambiguity Follow-Up Prompt For GPT-5.4 High

Use this as the target-specific working prompt for a `GPT-5.4` high-reasoning
pass on the remaining `Edict` -> `Writ` ambiguity.

## Target Selection

- selected target agent: `GPT-5.4`
- selected reasoning level: `high`
- selected pass type: `planning`
- run rule: choose this configuration before launch and keep it fixed for the
  full run

## Why This Target

`RAIDEN` selected `GPT-5.4` high for this pass because the task is:

- a bounded canon review rather than broad repo mining
- ambiguity-reduction work across a narrow but interdependent document set
- sensitive to small wording contradictions and checklist drift
- likely to benefit from one strong reasoning pass more than multiple weak
  retries

This pass is not primarily about:

- heavy implementation
- long exploratory research
- broad cross-repo comparison

So the strongest fit is a careful high-reasoning review/synthesis pass that can
identify the smallest canon-safe doc change set.

## Runtime Notes

- do not switch model or reasoning level mid-run
- if this pass still leaves material ambiguity, start a new pass rather than
  trying to salvage the same run
- if the result shows only checklist drift and no real package-surface gap,
  prefer a narrow continuity/checklist adjustment over adding new package docs

## Expected Standard

This pass should:

- identify the exact remaining active ambiguity
- separate real blockers from deferred updater questions
- prefer the smallest valid doc changes
- avoid inventing more package structure than current canon supports

## Copyable Prompt Body

Use the fenced block below as the exact copyable prompt body for the selected
target.

```text
Obj: reduce the remaining package-side `Edict` -> installed `Writ` ambiguity in current RAIDEN canon without reopening deferred updater canon
Scope: root canon + directly relevant `toolkit/edict/` and downstream-instance docs only
Read:
- /mnt/e/raiden/README.md
- /mnt/e/raiden/SOURCE_OF_TRUTH.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/DECISIONS.md
- /mnt/e/raiden/PAST_PRESENT_FUTURE.md
- /mnt/e/raiden/RELEASE_READY_CHECKLIST.md
- /mnt/e/raiden/MANAGED_VS_LOCAL.md
- /mnt/e/raiden/TOOLKIT_INDEX.md
- /mnt/e/raiden/toolkit/README.md
- /mnt/e/raiden/toolkit/edict/README.md
- /mnt/e/raiden/toolkit/edict/PACKAGE_BOUNDARY.md
- /mnt/e/raiden/toolkit/edict/PACKAGE_TO_INSTANCE_MAPPING.md
- /mnt/e/raiden/toolkit/edict/MINIMUM_PAYLOAD.md
- /mnt/e/raiden/toolkit/edict/COMPATIBILITY.md
- /mnt/e/raiden/toolkit/edict/LIFECYCLE.md
- /mnt/e/raiden/toolkit/edict/RELEASE_REVIEW_CHECKLIST.md
- /mnt/e/raiden/toolkit/edict/RELEASE_NOTES_AND_MIGRATION_POSITION.md
- /mnt/e/raiden/toolkit/edict/example-package/README.md
- /mnt/e/raiden/toolkit/edict/example-package/payload/README.md
- /mnt/e/raiden/toolkit/edict/example-package/payload/OPERATING_RULES.md
- /mnt/e/raiden/toolkit/edict/example-package/payload/OWNERSHIP_BOUNDARY.md
- /mnt/e/raiden/toolkit/instance/README.md
- /mnt/e/raiden/toolkit/instance/STRUCTURE.md
- only if continuity alignment requires it: /mnt/e/raiden/OPEN_LOOPS.md
Do:
- identify the exact remaining `Edict` -> `Writ` ambiguity that still matters for release-prep
- separate true blockers from intentionally deferred updater/metadata questions
- determine whether the current blocker is a wording gap, mapping gap, ownership gap, threshold-language gap, or checklist drift
- propose the smallest canon-safe edit set that would materially reduce or close the blocker
- if the docs are already sufficient, recommend which checklist or continuity statement should be updated instead of adding more package docs
- if editing is allowed, make only the smallest necessary doc changes
No:
- do not reopen updater shape, manifest fields, package archive format, version comparison semantics, rollback policy, or distribution design
- do not invent broader package taxonomy unless current canon forces it
- do not use non-canonical working files as authority
- do not turn this into a broad repo rewrite or a new architecture plan
Val:
- any claimed ambiguity is grounded in current canon
- central `Edict` vs installed `Writ` stays explicit
- `payload/` vs `.raiden/writ/` mapping stays explicit
- updater deferral is preserved
- proposed edits are narrow and release-prep focused
Out:
- Executive Judgment
- Actual Remaining Ambiguity
- Not Actually A Current Blocker
- Minimal Change Set
- for each proposed change: file / rationale / expected effect
- Draft Text Or Patch Summary
- Release-Gate Impact
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
