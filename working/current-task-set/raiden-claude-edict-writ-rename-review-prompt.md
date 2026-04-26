# RAIDEN Claude-Type Edict-Writ Rename Review Prompt

Use this as the immediate filled-in prompt for a Claude-type review agent to
audit the Edict/Writ naming change and verify that the rename was completed
cleanly enough for current canon.

Recommended runtime:

- model class: Claude-type long-context review model
- reasoning: moderate-to-high
- mode: read-only review only

Select the model and reasoning level before launch.
Assume the agent is fixed to that model/reasoning choice for the full run.
If the first pass is insufficient, rerun as a new pass with a stronger
setting; do not imply mid-run switching is available.

Review plan:

1. verify the live naming model in root canon
2. verify the central `Edict` to downstream `Writ` mapping in toolkit/package docs
3. verify the downstream path model now uses `.raiden/writ/` coherently
4. verify release-prep and continuity docs still agree after the rename
5. check directly affected non-canonical working prompts only for drift that
   could mislead later work

Use the fenced block below as the exact copyable prompt body.

```text
Mode: review
Obj: audit the Edict/Writ naming change and determine whether it is complete, coherent, and safe for current RAIDEN canon
Scope: root canon + directly affected canonical toolkit files + directly affected working prompts only for drift checks
Read first:
- /mnt/e/raiden/README.md
- /mnt/e/raiden/SOURCE_OF_TRUTH.md
- /mnt/e/raiden/DECISIONS.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/PAST_PRESENT_FUTURE.md
- /mnt/e/raiden/RELEASE_READY_CHECKLIST.md
- /mnt/e/raiden/MANAGED_VS_LOCAL.md
- /mnt/e/raiden/TOOLKIT_INDEX.md
- /mnt/e/raiden/REPOSITORY_MAP.md
- /mnt/e/raiden/AGENTS.md
- /mnt/e/raiden/ARTIFACT_AUDIENCE.md
Then read:
- /mnt/e/raiden/toolkit/README.md
- /mnt/e/raiden/toolkit/edict/README.md
- /mnt/e/raiden/toolkit/edict/PACKAGE_BOUNDARY.md
- /mnt/e/raiden/toolkit/edict/PACKAGE_TO_INSTANCE_MAPPING.md
- /mnt/e/raiden/toolkit/edict/MINIMUM_PAYLOAD.md
- /mnt/e/raiden/toolkit/edict/LIFECYCLE.md
- /mnt/e/raiden/toolkit/edict/COMPATIBILITY.md
- /mnt/e/raiden/toolkit/edict/RELEASE_REVIEW_CHECKLIST.md
- /mnt/e/raiden/toolkit/edict/RELEASE_NOTES_AND_MIGRATION_POSITION.md
- /mnt/e/raiden/toolkit/edict/example-package/README.md
- /mnt/e/raiden/toolkit/edict/example-package/payload/README.md
- /mnt/e/raiden/toolkit/edict/example-package/payload/OPERATING_RULES.md
- /mnt/e/raiden/toolkit/edict/example-package/payload/OWNERSHIP_BOUNDARY.md
- /mnt/e/raiden/toolkit/instance/README.md
- /mnt/e/raiden/toolkit/instance/STRUCTURE.md
- /mnt/e/raiden/toolkit/instance/PROMPT_MAPPING.md
- /mnt/e/raiden/toolkit/prompts/README.md
- /mnt/e/raiden/toolkit/prompts/GOVERNANCE.md
Only after the canonical pass, read these non-canonical drift checks:
- /mnt/e/raiden/working/updater-system/BUILD_PLAN.md
- /mnt/e/raiden/working/updater-system/BUILD_AGENT_PROMPT.md
- /mnt/e/raiden/working/current-task-set/raiden-edict-skeleton-review-and-build-prompt.md
Check:
- does root canon now define the naming stack as `RAIDEN`, `Edict`, `RAIDEN Instance`, `Writ`
- is `Edict` consistently the central RAIDEN-authored instruction/package surface rather than the downstream installed artifact
- is `Writ` consistently the downstream installed managed core inside a `RAIDEN Instance`
- is `payload` consistently treated as a technical package/install term rather than a peer identity in the naming stack
- do toolkit package docs map `payload/` to `.raiden/writ/` consistently
- do downstream instance docs use `.raiden/writ/` consistently instead of `.raiden/edict/`
- do release-prep docs still make sense after the rename, without reopening updater canon or weakening the current gate
- are any canonical docs still using the old meaning `Edict = downstream installed managed core`
- are any directly affected working prompts or updater drafts stale enough to mislead later work even though they are non-canonical
- did the rename introduce any new contradiction between root canon, toolkit docs, and downstream instance docs
- was the rename kept narrow and additive, or did it silently broaden structure beyond what canon currently supports
No:
- read-only only
- do not propose a replacement naming model unless current canon still contradicts itself
- do not reopen updater-shape, manifest-field, packaging, or distribution design
- do not treat non-canonical working files as authority
- do not mine reference-repos, reference-reviews, or reference-extracts unless a canonical claim cannot be checked otherwise
- do not turn this into a broad repo rewrite plan
Val:
- findings distinguish canonical blockers from non-canonical drift
- findings cite exact files and lines
- rename assessment is grounded in current canon, not old assumptions
- updater deferral is preserved
- central-versus-downstream distinction remains explicit
Out:
- Executive Judgment
- Findings First
- for each finding: severity / why it matters / evidence / recommended adjustment
- Canonically Correct And Strong
- Remaining Rename Gaps
- Non-Canonical Drift Worth Fixing
- Is The Rename Complete Enough For Current Release-Prep?
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
```
