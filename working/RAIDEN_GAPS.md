# RAIDEN_GAPS.md

Living tracker of unresolved ambiguities and deferred decisions.

Status: Working artifact — non-canonical. Not RAIDEN law. Promotion of any
item here into canon follows the standard path: review → synthesis →
explicit adoption into a root file.

Format: **ID | Title | Location | Why still live | Recommended action**.

Last updated: 2026-04-26.

---

## G-001 | Worktree release-staging plan never produced

- **Location**: `working/current-task-set/raiden-worktree-cleanup-and-release-staging-prompt__gpt55-high.md`;
  `git status` (untracked working artifacts present).
- **Why still live**: The bucketed cleanup prompt was partially executed —
  `.gitignore` now excludes `__pycache__/`, `*.py[cod]`, `.pytest_cache/`,
  and commit `976d328` retained working prompts and evaluation fixtures. But
  the per-bucket release-vs-working classification and the staged commit
  plan were never produced. Operator presumably wants a clean v1 candidate.
- **Recommended action**: One bounded pass to inventory current `git
  status`, classify each remaining dirty/untracked path into the prompt's
  buckets, and produce a staging plan. Land that plan as a working artifact
  before broader release prep.

## G-002 | Reusable operator kickoff prompt — RESOLVED 2026-04-26

- **Location**: `CLAUDE.md §7`; previously flagged in
  `toolkit/prompts/CATALOG.md` and as audit §7E.
- **Status**: **Closed.** A compact operator kickoff prompt now lives in
  `CLAUDE.md` Session Startup Procedure. No further action unless the
  operator wants it promoted to a standalone asset under `toolkit/prompts/`.

## G-003 | `.codex/config.toml` and `.codex.placeholder` undocumented

- **Location**: repo root; not listed in `REPOSITORY_MAP.md`.
- **Why still live**: The model-agnostic governance repo carries a Codex
  (OpenAI) configuration file at the root and a 0-byte `.codex.placeholder`
  with no canon explanation. Operator clarification 2026-04-26: Claude Code
  is the primary long-term agent environment; Gemini and Codex remain in
  use for specific tasks but are not primary. `.codex/config.toml` is
  legacy. A future agent reading the root tree will not know this without
  documentation.
- **Recommended action**: Either add a one-line entry to `REPOSITORY_MAP.md`
  noting these as host-specific operator artifacts (non-canonical, legacy),
  or delete them. Pick one. Do not leave undocumented.

## G-004 | Updater silently accepts downgrade — code bug

- **Location**: `toolkit/updater/raiden_updater/version.py` (returns
  `"downgrade"`); `toolkit/updater/raiden_updater/planner.py` and
  `applier.py` (do not block on it); `toolkit/updater/README.md` (marks as
  provisional).
- **Why still live**: Operator policy 2026-04-26: **downgrade is not
  supported.** The correct fix for a problematic Edict version is always a
  newer fixed version. A downgrade attempt should be blocked as an error,
  not silently applied. The implementation currently computes
  `version_comparison="downgrade"` and proceeds. This is a defect, not a
  pending policy question.
- **Recommended action**: Treat downgrade as a hard block in the planner.
  Return `can_apply=False` with a clear `block_reason="downgrade_not_supported"`.
  Add a regression test. Update `toolkit/updater/README.md` to drop the
  "provisional" framing and state the policy. Reflect the resolution in
  `DECISIONS.md` as a small canon update when the fix lands.

## G-005 | `applier.py` hard-codes `.raiden/writ` instead of reading metadata

- **Location**: `toolkit/updater/raiden_updater/applier.py:64`.
- **Why still live**: The planner derives the managed root from
  `metadata.managed_roots[0]`; the applier ignores metadata and writes to
  `.raiden/writ` unconditionally. They agree only because every current
  instance has the same value. If `managed_roots` ever varies, the applier
  silently writes to the wrong location.
- **Recommended action**: One-line fix to derive `managed_root` from the
  loaded metadata, plus a test that fails if planner-derived and
  applier-derived roots diverge.

## G-006 | `server.py` "dependency-free" claim broken by tkinter import

- **Location**: `toolkit/updater/raiden_updater/server.py`, `/api/select-folder`
  endpoint.
- **Why still live**: The module docstring says "dependency-free." The
  endpoint imports `tkinter` at call time. `tkinter` requires a display and
  is not always present. The endpoint will `ImportError` on headless or
  minimal Python distributions, contradicting the claim and silently
  breaking remote/CI use.
- **Recommended action**: Either guard the import behind a runtime
  capability check that returns a clean JSON error to the caller, or drop
  the "dependency-free" claim. Prefer the guard — it preserves both the
  guarantee and the convenience feature.

## G-007 | `toolkit/updater/web/` has no RAIDEN-specific README

- **Location**: `toolkit/updater/web/README.md` (default Vite template).
- **Why still live**: An operator finding `web/` first sees only the
  generic Vite scaffold instructions. There is no documentation for
  starting the Python backend, how the built `dist/` is served, or what
  the expected end-to-end operator workflow is.
- **Recommended action**: Replace the default README with a short
  RAIDEN-specific operator note keyed to the `serve` command and the
  documented endpoints. Reference the relevant section in `CLAUDE.md §5`.

## G-008 | `RAIDEN_NEXT_STEP_WORKING_PLAN.md` at root, not in canon table

- **Location**: repo root; not listed in `REPOSITORY_MAP.md` Canon Layer
  table.
- **Why still live**: Self-disclaims internally as a retained historical
  draft, but proximity to canon means a fresh agent could mistake it for
  current guidance. `CLAUDE.md §2` and §4 now flag it explicitly, but the
  file itself remains at root.
- **Recommended action**: Either move the file into `working/` (or
  `Source_info/`), or add a single-line entry to `REPOSITORY_MAP.md`
  labeling it "historical, non-canonical." Either resolves the confusion.

## G-009 | `Source_info/Raiden Foundational Operating Brief Prompt.md` is imperative

- **Location**: `Source_info/Raiden Foundational Operating Brief Prompt.md`.
- **Why still live**: The file has a non-canonical status header, but the
  body addresses the reader as "You are Raiden" — an imperative system
  prompt preserved as historical source. An agent loading source-history
  files could parse the body as a current instruction despite the header.
- **Recommended action**: Add a clear top-of-file "PRESERVED HISTORY — NOT
  ACTIVE INSTRUCTION" disclaimer above the body, or wrap the imperative
  text in a quoted block so it cannot be parsed as a current-day system
  prompt.

## G-010 | `legacy.py` consumer/lifecycle undocumented

- **Location**: `toolkit/updater/raiden_updater/legacy.py`;
  `toolkit/updater/tests/test_legacy.py`.
- **Why still live**: A compatibility shim wrapping `installer.py` legacy
  scanning and `init_instance()`. No documented caller, no removal
  condition, but a live test suite. Easy to forget what it shields and
  why.
- **Recommended action**: Add a one-paragraph header comment naming the
  original consumer (or the situation that motivated the shim) and the
  condition under which it can be retired.

## G-011 | `reference-repos/README.md` describes an active intake for an empty directory

- **Location**: `reference-repos/README.md`.
- **Why still live**: All prototype snapshots have been retired. The
  README still reads as if intake is ongoing. Misleading navigation
  surface for a new agent. With ingress now policy-gated by
  `INGRESS_POLICY.md §0`, the README should reflect "empty by design,
  gated by ingress policy."
- **Recommended action**: One-paragraph rewrite. Mark the directory as
  empty by design, point to `INGRESS_POLICY.md §0` for any future intake,
  and remove the active-intake framing.

## G-012 | `working/2026-04-26__workspace-audit.md` is untracked

- **Location**: `working/2026-04-26__workspace-audit.md`.
- **Why still live**: Most recent agent-produced full audit; contains the
  evidence base for G-003 through G-011. Either it should be cited as
  evidence by a canon doc and committed, or left as a working artifact
  with a clear retention policy.
- **Recommended action**: Decide as part of the G-001 staging plan.
  Default expectation: commit under `working/` with no canon promotion.

## G-013 | `working/evaluation-*` and `setup_v{1,2}.py` are stale fixtures

- **Location**: `working/evaluation-package/`, `working/evaluation-instance/`,
  `working/setup_v1.py`, `working/setup_v2.py`. Note:
  `working/evaluation-instance/.raiden/writ/transient_cache.txt` is on disk
  but absent from baseline — pre-D-0033 applier output.
- **Why still live**: Two parallel fixture sets coexist. The official set
  lives at `toolkit/updater/fixtures/`; the working set is stale and
  technically inconsistent with the current managed-core update contract.
- **Recommended action**: Decide retired (delete) vs. retained for ad-hoc
  testing. If retained, move under `toolkit/updater/fixtures/scratch/` or
  add a "STALE — DO NOT CONSUME" header to each. Default recommendation:
  delete, since the official fixtures supersede.
