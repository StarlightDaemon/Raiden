# RAIDEN Edict-Writ Ambiguity Follow-Up Prompt

Use this as the next filled-in prompt for any tooling agent that should reduce
the remaining package-side `Edict` to installed `Writ` ambiguity without
reopening deferred updater canon.

`RAIDEN` should first select the best target agent for this task, then use this
file to build the prompt for that chosen target.

Available target agents include:

- Gemini 3.1 Pro
- Gemini 3 Flash
- Claude Sonnet 4.6
- Claude Opus 4.6
- GPT-OSS-120b
- GPT-5.4
- GPT-5.2-Codex
- GPT-5.1-Codex-Max
- GPT-5.4-Mini
- GPT-5.3-Codex
- GPT-5.2
- GPT-5.1-Codex-Mini

## Recommended Runtime

First choose a target agent and pass type:

- fast pass
  - use when the goal is to identify 1-3 precise ambiguity gaps and draft the
    smallest doc changes that resolve them
- planning pass
  - use when the first fast pass still leaves uncertainty about what is truly
    ambiguous versus already settled

Select the model and reasoning level before launch.
Assume the active agent is model-bound and reasoning-bound for the full run
unless the host explicitly proves otherwise.
Do not plan around switching models or reasoning levels mid-task.

Choose a specific target agent in the wrapper metadata before using the prompt
body.
Do not launch this as a generic cross-model prompt if `RAIDEN` can make a
reasoned target selection first.

Escalate reasoning only if the first pass still shows:

- contradiction between root canon and `toolkit/edict/`
- weak confidence about what is release-blocking now
- multiple plausible doc-change paths with materially different canon impact

## Intent

The goal is not to re-audit the whole repo and not to design the updater.

The goal is to:

1. identify the exact remaining ambiguity in the central `Edict` package
   surface and its issued downstream `Writ`
2. decide which ambiguity is real enough to matter for release-prep
3. propose the smallest canon-safe doc updates that remove that ambiguity
4. either draft those updates directly or produce patch-ready wording and file
   targets

## Target Selection Notes

`RAIDEN` should prefer the target agent that is strongest at:

- bounded canon review
- contradiction detection across a narrow document set
- identifying the smallest valid doc change set
- avoiding accidental reopening of deferred updater mechanics

The wrapper metadata for the launched prompt should name:

- selected target agent
- selected reasoning level
- selected pass type: fast or planning
- short selection rationale

The fenced prompt body remains the executable text for the chosen target agent.

## Working Theory To Test

Current canon suggests the package surface is mostly coherent, but still leaves
some release-prep ambiguity around the central `Edict` to downstream `Writ`
model.

Do not assume that broad package work is still needed.
Test whether the remaining gap is actually:

- terminology drift
- placement drift
- missing cross-reference
- unclear ownership boundary
- unclear "minimum current managed core" statement
- unclear release-prep threshold language

## Read First

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

Only if needed for continuity alignment:

- /mnt/e/raiden/OPEN_LOOPS.md
- /mnt/e/raiden/AGENTS.md

Do not read outside this set unless a canonical contradiction cannot be
resolved otherwise.

## Core Questions

Answer these in order:

1. What exact ambiguity still exists in the current `Edict` -> `Writ` story?
2. Is that ambiguity in root canon, toolkit canon, example-package material,
   or only in wording/cross-reference drift?
3. Which ambiguity is actually release-blocking now, versus merely unresolved
   for later updater canon?
4. What is the smallest set of file edits that would remove the active
   ambiguity without broadening canon?
5. After those edits, would the release checklist's remaining package-surface
   gap be materially closed, or only narrowed?

## Do

- identify only the ambiguity that is still active now
- separate real blockers from already-settled deferred questions
- prefer narrow doc alignment over new structure
- propose the smallest coherent edit set
- keep central `Edict`, installable `payload`, and downstream `Writ`
  explicitly distinct
- preserve the rule that updater-shape and manifest-field canon remain deferred
- if the docs are already strong enough, say so and identify the checklist line
  that should be updated instead of inventing more package docs

## No

- do not reopen updater design, command surface, manifests, archive format, or
  distribution mechanics
- do not broaden the package surface unless a current release-prep ambiguity
  cannot be resolved otherwise
- do not treat working files as canon
- do not mine `reference-repos/`, `reference-reviews/`, or
  `reference-extracts/` unless root canon is contradictory
- do not recommend broad repo cleanup when one or two targeted doc updates are
  enough
- do not confuse "still deferred" with "still ambiguous enough to block
  release-prep"

## Preferred Output

- Executive Judgment
- Actual Remaining Ambiguity
- Not Actually A Current Blocker
- Minimal Change Set
- for each proposed change: file / why this file / exact ambiguity resolved
- Draft Text Or Patch Plan
- Release-Gate Impact
- Risks If Left Unchanged
- Confidence: observed evidence / strong inference / weak inference /
  unresolved ambiguity

## If Writing Changes

If the environment allows editing, make only the smallest canon-safe changes
needed.

Preferred edit style:

- adjust existing wording before adding new sections
- add one short clarifying paragraph before adding a new file
- add cross-references before creating new taxonomy
- keep ASCII Markdown
- preserve current naming exactly: `RAIDEN`, `Edict`, `RAIDEN Instance`,
  `Writ`

## Validation

Before concluding, verify:

- root canon and `toolkit/edict/` still agree
- `Edict` remains the central authored package surface
- `payload/` remains the technical installable subset
- `.raiden/writ/` remains the downstream installed managed core
- no local overlay, live-state, or instance-support material leaks into the
  package payload
- updater deferral is preserved
- any claimed blocker is traceable to current canon, not to deferred future
  mechanics

## Prompt Body

Use the fenced block below as the exact copyable prompt body.

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
