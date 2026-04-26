# RAIDEN Worktree Cleanup And Release Staging Prompt

Use this as the filled-in handoff prompt for cleaning and organizing the dirty
RAIDEN worktree before a possible 1.0 release decision.

This is a non-canonical working artifact. It is not root canon and should not
be treated as adopted RAIDEN law unless promoted into canonical docs.

Recommended runtime:

- model: `gpt-5.5`
- reasoning: `high`
- use `xhigh` only if the first pass finds conflicting release-canon claims,
  unclear provenance, or a staging plan that cannot be made safely bounded

## Planning Summary

Current observed worktree state:

- many root canonical docs are modified
- many toolkit and instance docs are modified
- `toolkit/updater/` is untracked and includes source, tests, fixtures,
  `.pytest_cache/`, and `__pycache__/` files
- reference review/extract changes are present
- multiple working prompts and evaluation fixtures are untracked under
  `working/`
- `.gitignore` currently ignores `reference-repos/` and `.codex.placeholder`
  only, so generated Python cache files are visible as untracked files

Initial cleanup buckets:

- release-canon bucket: root docs, `TOOLKIT_INDEX.md`,
  `MANAGED_VS_LOCAL.md`, `RELEASE_READY_CHECKLIST.md`, and directly related
  toolkit docs
- updater bucket: `toolkit/updater/` source, tests, fixtures, README, and
  directly related canon/doc changes
- reference/disposition bucket: `reference-extracts/`,
  `reference-reviews/`, `SOURCE_HISTORY_INDEX.md`, `INGRESS_POLICY.md`, and
  snapshot/legacy disposition docs
- working-only bucket: `working/current-task-set/`,
  `working/updater-system/`, `working/evaluation-*`, and setup helper scripts
- generated/noise bucket: Python `__pycache__/`, `.pyc`, and
  `.pytest_cache/`

## First Plan

1. Read root canon and release-state docs.
2. Inventory dirty tracked files, untracked files, generated files, and
   apparent thematic change groups.
3. Remove or ignore generated cache artifacts after preview.
4. Review each thematic bucket with targeted diffs.
5. Decide whether each bucket is release-required, release-supporting,
   working-only, or should remain unstaged/deferred.
6. Update only minimal organization metadata such as `.gitignore` or a working
   staging ledger if needed.
7. Run available validation.
8. Produce a staging/commit plan or, if explicitly authorized, create small
   thematic commits.

## Refined Plan

Do not start by staging everything. The first real task is to shrink noise and
make provenance auditable.

Refined execution order:

1. Establish ground truth with `git status --short`, `git diff --stat`,
   `git diff --name-only`, and `git ls-files --others --exclude-standard`.
2. Preview generated-file cleanup with `find` and/or `git clean -ndX`; do not
   delete anything until the removal list is explicit.
3. Add narrow ignore rules for Python/test generated artifacts if they are
   absent: `__pycache__/`, `*.py[cod]`, `.pytest_cache/`.
4. Remove generated cache artifacts only after approval or under an explicit
   operator instruction in the active prompt.
5. Classify all remaining files into buckets, using targeted diffs rather than
   broad assumptions.
6. For each bucket, decide:
   - include in 1.0 release set
   - keep as working-only and do not stage for release
   - defer pending operator review
   - discard only with explicit operator approval
7. Validate release-canon consistency against `SOURCE_OF_TRUTH.md`,
   `CURRENT_STATE.md`, `DECISIONS.md`, `OPEN_LOOPS.md`,
   `RELEASE_READY_CHECKLIST.md`, `MANAGED_VS_LOCAL.md`, and `TOOLKIT_INDEX.md`.
8. Validate updater behavior with available tests. If pytest is unavailable,
   report that directly and run compile/targeted smoke checks.
9. Produce the final cleanup report and exact staging/commit plan.

## Copyable Prompt

```text
Mode: review-plan-refine-impl-review
Obj: clean and organize the dirty RAIDEN worktree into a release-ready staging state
Scope: worktree cleanup, generated-file cleanup, release staging, and directly necessary organization metadata only
Repo: /mnt/e/RAIDEN

Read first:
- /mnt/e/RAIDEN/README.md
- /mnt/e/RAIDEN/SOURCE_OF_TRUTH.md
- /mnt/e/RAIDEN/CURRENT_STATE.md
- /mnt/e/RAIDEN/DECISIONS.md
- /mnt/e/RAIDEN/OPEN_LOOPS.md
- /mnt/e/RAIDEN/RELEASE_READY_CHECKLIST.md
- /mnt/e/RAIDEN/MANAGED_VS_LOCAL.md
- /mnt/e/RAIDEN/TOOLKIT_INDEX.md
- /mnt/e/RAIDEN/REPOSITORY_MAP.md
- /mnt/e/RAIDEN/AGENT_BOUNDARIES.md
- /mnt/e/RAIDEN/toolkit/README.md
- /mnt/e/RAIDEN/toolkit/instance/README.md
- /mnt/e/RAIDEN/toolkit/instance/STRUCTURE.md
- /mnt/e/RAIDEN/toolkit/updater/README.md if present

Start inventory:
- run `git status --short`
- run `git diff --stat`
- run `git diff --name-only`
- run `git ls-files --others --exclude-standard`
- inspect `.gitignore`
- identify generated files such as `__pycache__/`, `.pyc`, and `.pytest_cache/`

Do:
- classify every dirty or untracked path into exactly one bucket:
  release-canon, updater/toolkit, reference/disposition, working-only, generated/noise, or unresolved
- identify which changes appear directly release-relevant for a 1.0 candidate
- identify which changes should remain working-only and not be staged for release
- identify generated/noise files that should be removed or ignored
- update `.gitignore` only if narrow generated-file ignore rules are missing
- remove generated/noise artifacts only after previewing the exact list and only if operator approval or the active environment allows it
- do targeted diffs for each bucket before deciding its treatment
- preserve user-authored work unless it is explicitly classified and approved for removal
- keep reference-repos untouched
- keep canon/root updates narrow and evidence-backed
- run available validation after organization
- produce exact staging commands or a staged state if commits are explicitly authorized

Cleanup buckets to consider:
- release-canon: root canon/continuity docs and directly affected toolkit index/boundary docs
- updater/toolkit: `toolkit/updater/`, updater tests/fixtures, updater docs, and directly related instance/updater docs
- reference/disposition: `reference-extracts/`, `reference-reviews/`, source-history/disposition docs
- working-only: `working/current-task-set/`, `working/updater-system/`, `working/evaluation-*`, setup helper scripts
- generated/noise: `__pycache__/`, `*.pyc`, `.pytest_cache/`

Plan:
- first produce a cleanup plan with file buckets and proposed action for each bucket
- critique the plan for overbroad deletion, accidental canon promotion, and commit mixing
- refine the plan until every file has a clear action and evidence level

Implementation rules:
- do not use `git reset --hard`
- do not use `git checkout --` to discard files unless the operator explicitly approves the exact path list
- do not delete untracked working artifacts unless the operator explicitly approves the exact path list
- do not commit unless this run has explicit commit authorization
- if committing is authorized, create small thematic commits rather than one bulk commit
- do not edit `reference-repos/`
- do not broaden into new canon design unless cleanup reveals a direct contradiction

Recommended commit grouping if commits are authorized:
- commit 1: ignore/generated cleanup only
- commit 2: release-canon and continuity alignment
- commit 3: toolkit/Edict/Instance/Writ surface
- commit 4: updater local CLI implementation, fixtures, tests, and docs
- commit 5: reference extraction/disposition updates
- commit 6: working prompts/evaluation artifacts only if intentionally retained

Validation:
- `git status --short` after cleanup
- `git diff --stat` or staged diff stat for each staged group
- targeted diff review for every staged group
- `python3 -m compileall toolkit/updater/raiden_updater toolkit/updater/tests` if updater exists
- `python3 -m pytest toolkit/updater/tests -q` if pytest is available
- search for stale claims:
  - `rg -n "provisional|deferred|manifest-field|metadata field|baseline field|1.0|v1|release-ready" README.md CURRENT_STATE.md DECISIONS.md OPEN_LOOPS.md RELEASE_READY_CHECKLIST.md TOOLKIT_INDEX.md MANAGED_VS_LOCAL.md toolkit`
- confirm no generated Python caches remain tracked or untracked unless intentionally ignored

No:
- do not collapse all changes into one release commit
- do not stage generated caches
- do not silently discard user work
- do not treat working prompts as canon
- do not promote reference/extract content into canon by proximity
- do not reopen settled naming, manifest core semantics, anomaly thresholds, or missing-baseline policy unless a direct contradiction is found
- do not edit unrelated files just to make the tree look tidy

Stop:
- stop when the dirty tree is organized into an explicit release staging state:
  either clean, staged in reviewed groups, or intentionally dirty with each remaining path explained

Out:
- Executive Judgment
- Dirty Tree Classification
- Refined Cleanup Plan
- Generated/Noise Cleanup
- Release-Candidate File Set
- Deferred Or Working-Only File Set
- Staging Or Commit Plan
- Validation Results
- Remaining Risks
- Exact Next Command
- Confidence: observed evidence / strong inference / weak inference / unresolved ambiguity

Code Block For Review:
```text
Obj: Clean and organize RAIDEN dirty worktree
Scope: worktree cleanup + release staging only
Done:
- <inventory completed>
- <plan created>
- <plan refined>
- <generated cleanup completed or explicitly deferred>
- <release buckets reviewed>
- <validation completed>
Open:
- <exact remaining dirty paths or none>
Dec:
- <bucket decisions and commit/staging decisions>
Val:
- <commands run and results>
Blk:
- <none or exact blocker>
Next:
- <single next command or task>
Confidence:
- <observed evidence / strong inference / weak inference / unresolved ambiguity>
```
```
