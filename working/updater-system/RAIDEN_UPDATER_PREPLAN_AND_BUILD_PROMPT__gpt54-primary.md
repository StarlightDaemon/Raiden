# RAIDEN Updater Preplan And Build Prompt

## Status

This is a retained non-canonical working prompt for updater planning and
implementation work after operator approval to resume updater-shape canon.

Do not treat this file as root canon.

## Recommended Target

Primary target:

- model: `gpt-5.4`
- reasoning: `medium` for the first bounded pass

Escalation target if the first pass leaves material ambiguity,
contradiction, premature stopping, or weak implementation judgment:

- model: `gpt-5.4`
- reasoning: `high`

Strong alternatives when the active host favors them:

- `Claude Opus 4.1` at high reasoning for planning-heavy or critique-heavy
  review passes
- `Gemini 2.5 Pro` at high reasoning for very long-context comparative review
  across updater docs, fixtures, and implementation surfaces

Run rule:

- choose the model and reasoning level before launch
- treat the run as model-bound and reasoning-bound
- do not assume safe mid-run switching
- if the first pass fails materially, launch a new pass with a stronger profile
  rather than steering the same weak run repeatedly

## Why This Target

`gpt-5.4` is the best primary fit for the full updater cycle because OpenAI's
official March 5, 2026 release describes it as the frontier model for agentic,
coding, and professional workflows, with native computer-use capability and
state-of-the-art tool use. That matches RAIDEN's need for a model that can:

- review canon carefully
- refine an implementation plan
- make bounded code changes
- verify behavior through tests and fixtures

`Claude Opus 4.1` is a strong alternative for critique-heavy planning and
coding review. Anthropic's August 5, 2025 release describes it as their most
capable model for agentic tasks, real-world coding, and reasoning.

`Gemini 2.5 Pro` remains a strong long-context alternative when the task is
especially document-heavy or codebase-heavy. Google's Gemini API docs describe
it as their state-of-the-art thinking model for complex code and large
codebases with a 1,048,576-token context window.

## Operator Goal

Run one disciplined updater cycle that does all of the following in order:

1. review the current canon and retained updater planning bundle
2. produce a narrow preplan
3. refine that preplan after a second internal review pass
4. build the updater MVP only within the approved narrow scope
5. review the implementation again through validation and self-audit
6. leave a readable final report plus a compact review block

The pass should avoid jumping straight from old draft ideas to implementation.

## Runtime Notes

- start from canon and use `working/updater-system/` only as retained planning
  input, not as adopted law
- treat this as a bounded updater MVP, not a distribution platform
- prefer deterministic local CLI behavior, typed models, fixtures, and tests
  over broader packaging polish
- if canon still leaves one narrow implementation choice unresolved, pick the
  smallest safe provisional option and label it as provisional
- if the implementation uncovers a real canon contradiction, stop and report it
  instead of forcing a weak build

## Exact Copyable Prompt

```text
Mode: review-plan-refine-impl-review
Obj: plan, refine, build, and review the first practical RAIDEN updater MVP through a disciplined preplan-first workflow that stays aligned with current canon
Scope: updater implementation surface + directly affected canon and local docs only
Read first:
- /mnt/e/raiden/README.md
- /mnt/e/raiden/SOURCE_OF_TRUTH.md
- /mnt/e/raiden/REPOSITORY_MAP.md
- /mnt/e/raiden/CURRENT_STATE.md
- /mnt/e/raiden/DECISIONS.md
- /mnt/e/raiden/OPEN_LOOPS.md
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
- /mnt/e/raiden/toolkit/instance/README.md
- /mnt/e/raiden/toolkit/instance/STRUCTURE.md
Then read retained updater planning inputs as non-canonical working material:
- /mnt/e/raiden/working/updater-system/README.md
- /mnt/e/raiden/working/updater-system/BUILD_PLAN.md
- /mnt/e/raiden/working/updater-system/BUILD_AGENT_PROMPT.md
Do this in order:
1. Review:
- identify the actual canon-backed updater contract and the smallest viable updater MVP
- separate current canon requirements from provisional details in the retained build draft
- list any real contradictions, unresolved implementation choices, or places where the retained build plan overreaches canon
2. Preplan:
- produce a narrow implementation plan with:
- chosen implementation location
- exact files to create or edit
- data models to define
- fixture strategy
- test matrix
- validation sequence
- explicit non-goals
3. Refine:
- critique the first preplan before coding
- shrink any unnecessary scope
- convert any vague steps into concrete file-level actions
- confirm the refined plan still satisfies the managed/local contract
4. Build:
- implement the refined updater MVP
- add typed metadata/manifest/baseline models
- add plan/apply behavior
- add conflict detection
- add delta-only managed updates
- add anomaly warn/block behavior
- add sample package and instance fixtures
- add tests
- add only the minimum aligned docs needed to run and understand the MVP
5. Review again:
- run validation and tests
- compare the implementation back against canon and the refined plan
- identify anything that is provisional, intentionally deferred, or still weak
- if necessary, make one final narrow cleanup pass before stopping
Implementation target:
- build the first updater as a local CLI for `RAIDEN Instance` managed-core updates sourced from `Edict` packages
- preserve local overlay and live state
- stop on locally modified managed files
- prefer safety, determinism, and testability over packaging polish
Minimum implementation scope:
- typed instance metadata model
- typed package manifest model
- typed installed baseline model
- `plan` command
- `apply` command
- compatibility and version checks
- conflict model
- delta-only managed file updates
- anomaly warning/block classification
- fixture-based tests
No:
- do not reopen authority order, naming, managed-vs-local contract, or toolkit package boundary
- do not add remote download or registry resolution
- do not add drag-and-drop UX or GUI flows
- do not add auto-merge for conflicts
- do not expand into publishing/distribution systems
- do not silently harden unresolved manifest or archive questions into root canon
- do not rewrite unrelated repo docs
- do not skip the preplan/refine/review steps and jump straight to coding
Val:
- updater enforces: update managed core / preserve overlay / preserve live state / stop on locally modified managed files
- plan output shows compatibility, version comparison, managed changes, already-current files, protected paths, conflicts, and anomaly results
- apply runs only when the plan is conflict-free
- tests cover at least: clean apply, conflict stop, no-op current package, changed-files-only rewrite, overlay preservation, live-state preservation, schema incompatibility, malformed manifest rejection, anomaly warn/block, dry-run no mutation
- any docs added remain narrow and consistent with current canon
Stop:
- stop at a narrow testable MVP plus aligned docs and a reviewed final report
Out:
- Readable Report:
- Executive Judgment
- Canon-Backed Updater Contract
- Preplan
- Refined Plan
- What Was Built
- Validation And Tests
- Provisional Choices
- Deferred Questions
- Risks And Follow-On Work
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity
- Code Block For Review:
```text
Obj: RAIDEN updater preplan and build
Scope: updater MVP + directly affected canon/docs only
Done:
- <review completed>
- <preplan created>
- <plan refined>
- <implementation completed>
- <validation completed>
Open:
- <none or exact remaining issue>
Dec:
- <key updater design choices made>
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

## Source Notes

- OpenAI, "Introducing GPT-5.4," March 5, 2026:
  https://openai.com/index/introducing-gpt-5-4/
- OpenAI API model page for `gpt-5.4`:
  https://developers.openai.com/api/docs/models/gpt-5.4
- Anthropic, "Claude Opus 4.1," August 5, 2025:
  https://www.anthropic.com/news/claude-opus-4-1
- Anthropic models overview:
  https://docs.anthropic.com/en/docs/about-claude/models/all-models
- Google Gemini API model docs for `gemini-2.5-pro`:
  https://ai.google.dev/gemini-api/docs/models/gemini-v2
