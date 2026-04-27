# Raiden Workspace Audit Report

Date: 2026-04-26
Produced by: Claude Sonnet 4.6 (Claude Code)
Status: Working artifact — non-canonical

---

## 1. Purpose & Scope

**What RAIDEN is trying to accomplish:**

RAIDEN exists because the operator's actual working environment fails in two directions simultaneously: long chat sessions degrade under context accumulation, and IDE-connected agent tooling burns token budgets rapidly during coding work. The result is repeated waste — the same project state, conventions, and decisions get re-explained at the start of every work cycle.

RAIDEN's answer is to build *durable infrastructure* that eliminates that repeated waste:

- **Governance canon**: stable docs that define authority, naming, and boundaries so agents don't re-derive them
- **Shared prompt templates**: reusable handoff, pause-point, bounded-task, and continuation formats so operators don't author them from scratch each time
- **Downstream instance model**: a standard `.raiden/` control plane structure that target repos adopt, separating managed RAIDEN core from local state
- **Updater tooling**: a CLI + local web surface for safely installing and refreshing the managed core in downstream repos without clobbering local overlay or state

**"Better orchestration" concretely means**: an agent starting a work cycle in any repo running a RAIDEN Instance can read `AGENTS.md` → `.raiden/README.md` → `.raiden/state/CURRENT_STATE.md` and know exactly where it is, what has been decided, and what is in scope — without reconstructing context from raw chat history.

---

## 2. Architecture Overview

**Repo layout:**

```
RAIDEN/
├── [Root canonical docs]          ← authority layer; all binding governance
│   README.md, SOURCE_OF_TRUTH.md, REPOSITORY_MAP.md, AGENT_BOUNDARIES.md,
│   MANAGED_VS_LOCAL.md, ARTIFACT_AUDIENCE.md, CURRENT_STATE.md,
│   DECISIONS.md, GOALS.md, OPEN_LOOPS.md, OPERATING_INTENT.md,
│   INGRESS_POLICY.md, RELEASE_READY_CHECKLIST.md, PAST_PRESENT_FUTURE.md,
│   SNAPSHOT_RETIREMENT_RULE.md, PROMPT_ASSET_INDEX.md, TOOLKIT_INDEX.md,
│   SOURCE_HISTORY_INDEX.md, WORKBOOK.md
│
├── toolkit/                       ← canonical implementation subtree
│   ├── prompts/                   ← shared prompt asset library (9 templates)
│   ├── edict/                     ← central package surface + example-package/
│   ├── instance/                  ← downstream instance structure docs
│   ├── guide/                     ← operator helper script (raiden_guide.py)
│   └── updater/                   ← Python CLI + local web API backend
│       ├── raiden_updater/        ← Python package (plan, apply, install, serve)
│       ├── fixtures/              ← sample_instance + sample_package for testing
│       ├── tests/                 ← pytest test suite
│       └── web/                   ← React/Vite local browser UI scaffold
│
├── reference-reviews/             ← non-canonical prototype analysis
├── reference-extracts/            ← non-canonical compact extracted patterns
├── reference-repos/               ← prototype snapshots (all retired; now empty)
├── Source_info/                   ← preserved historical source (non-canonical)
├── working/                       ← non-canonical session working artifacts
└── .codex/config.toml             ← Codex agent configuration
```

**Where the "agent" sits within this:**

RAIDEN is not a running process. It is a framework repo. When an AI agent is invoked in this workspace, it *is* RAIDEN operating on RAIDEN. The `AGENTS.md` file at the root provides agent orientation for this repo. The `toolkit/updater/` Python code is the only operational software; everything else is documentation and governance.

---

## 3. Tool Surface

These are the executable operations available in the repo. All are in Python; no other executable tooling was found.

---

### `raiden_updater` CLI (`toolkit/updater/raiden_updater/cli.py`)

**`plan`**
- Purpose: Dry-run diff between an Edict package and a downstream RAIDEN Instance. No filesystem writes.
- Input: `--instance <path>` (target repo root), `--package <path>` (Edict package dir containing `manifest.json` + `payload/`)
- Output: Human-readable plan result to stdout; exit 0 if apply-safe or already current, else exit 1
- Edge cases:
  - Blocks with `missing_baseline` if `.raiden/writ/` has files but no `baseline.json` exists (cannot distinguish safe updates from local modifications)
  - Blocks on schema incompatibility between `instance_schema_version` and `compatible_instance_schemas`
  - Blocks on `protected_path_write` if a package managed file would collide with overlay or state roots
  - Blocks if version strings aren't strict `MAJOR.MINOR.PATCH` format
  - Returns `can_apply=False` with `block_reason="Already up to date"` for no-op same-version installs (exit 0, treated as success by `cmd_plan`)

**`apply`**
- Purpose: Execute a conflict-free plan: copy payload files to `.raiden/writ/`, write new `baseline.json`, update `installed_edict_version` in `metadata.json`
- Input: Same as `plan`
- Output: Apply result to stdout; exit 0 on success
- Edge cases:
  - Raises `ApplyError` if plan is not apply-safe
  - **Hard-codes managed root path as `.raiden/writ`** regardless of what `metadata.managed_roots[0]` says (inconsistency with planner; see §6)
  - Safe auto-removal: removes baseline-tracked managed files absent from the new package only if the current file matches the baseline hash; blocks on conflict otherwise
  - `_prune_empty_dirs()` cleans up empty parent directories after removal, stopping at the managed root

---

### Installer Services (`toolkit/updater/raiden_updater/installer.py`)

**`build_repo_scan(target)`**
- Purpose: Summarize a target repo's readiness for install or update
- Output: `RepoScanResult` — legacy artifact list, whether `.raiden/` exists, whether `AGENTS.md` is a RAIDEN bridge
- Detects three specific legacy artifacts: a non-bridge `AGENTS.md`, an `agent-ledger/` dir, an `agent-prompts/` dir

**`preview_init_instance(target, force=False)`**
- Purpose: Dry-run of instance initialization — reports what would be written without doing it
- Output: `InitPreviewResult` — legacy artifacts + planned writes with actions (`create`, `overwrite`, `preserve`)

**`init_instance(target, force=False)`**
- Purpose: Create the downstream RAIDEN Instance skeleton under `.raiden/`
- Writes: `AGENTS.md` (bridge), `.raiden/README.md`, `.raiden/local/README.md`, `.raiden/state/{README,CURRENT_STATE,GOALS,OPEN_LOOPS,DECISIONS,WORK_LOG}.md`, `.raiden/state/LEGACY_REVIEW.md`, `.raiden/instance/metadata.json`
- Creates empty dirs: `.raiden/writ/`, `.raiden/local/prompts/`, `.raiden/local/rules/`, `.raiden/local/context/`, `.raiden/instance/`
- Preserves existing files unless `force=True` (or file is a legacy `AGENTS.md`)
- Archives a legacy `AGENTS.md` to `.raiden/local/legacy/AGENTS.legacy.md` before replacing it

**`doctor(target)`**
- Purpose: Check a repo has the minimum required instance shape
- Output: `DoctorResult` — `ok: bool` + list of problems (missing paths, wrong metadata field values)
- Checks exactly: `AGENTS.md`, `.raiden/README.md`, `.raiden/writ/`, `.raiden/local/`, `.raiden/state/`, `.raiden/instance/`, `.raiden/instance/metadata.json`

---

### Web API Server (`toolkit/updater/raiden_updater/server.py`)

Dependency-free `http.server` implementation; listens at `127.0.0.1:8080` by default.

| Endpoint | Purpose | Request body fields | Notable behavior |
|---|---|---|---|
| `POST /api/scan` | Build repo scan | `instance_root` | Returns `RepoScanResult` dict |
| `POST /api/init-preview` | Preview init | `instance_root`, optional `force` | Returns `InitPreviewResult` dict |
| `POST /api/init-apply` | Apply init | `instance_root`, optional `force` | Creates `instance_root` dir first if missing |
| `POST /api/plan` | Dry-run plan | `instance_root`, `package_root` | Returns `PlanResult` dict |
| `POST /api/apply` | Execute apply | `instance_root`, `package_root` | Returns `{success, applied_version}` |
| `POST /api/doctor` | Check instance | `instance_root` | Returns `DoctorResult` dict |
| `POST /api/select-folder` | Native folder picker | optional `title` | **Uses tkinter**; see §6 |

**CORS**: All endpoints send `Access-Control-Allow-Origin: *`.

---

### Guide CLI (`toolkit/guide/raiden_guide.py`)

Operator-facing wrapper around the above services.

| Subcommand | Purpose |
|---|---|
| `steps` | Print the current guided setup flow to stdout |
| `init --target <path> [--force]` | Create RAIDEN Instance skeleton |
| `install --target <path> --package <path> [--apply]` | Plan (+ optionally apply) an Edict package |
| `doctor --target <path>` | Check minimum instance shape |

Uses `sys.path` injection to import `raiden_updater` without it being installed as a package.

---

### Internal Modules (engine behind `plan` and `apply`)

| Module | Key function | Notes |
|---|---|---|
| `loader.py` | `load_instance_metadata()`, `load_package_manifest()`, `load_installed_baseline()` | Strict exact-key validation; rejects unknown fields; validates SHA-256 format; validates POSIX relative paths |
| `hasher.py` | `hash_file(path)` | SHA-256, chunked 8KB reads |
| `version.py` | `compare_versions(current, target)` | Strict `MAJOR.MINOR.PATCH`; returns `"upgrade"/"same"/"downgrade"` |
| `anomaly.py` | `classify_anomalies()` | `high_change_ratio` (>50% and ≥8 files, warn), `high_change_count` (>10 files, warn), `protected_path_write` (block), `managed_file_removal` (warn) |
| `compatibility.py` | `check_schema_compatibility()` | Simple set-membership check of `instance_schema_version` in `compatible_instance_schemas` |

---

## 4. Data & Control Flow

**Representative flow: Fresh install in a target repo**

```
Operator
  ↓  python3 toolkit/guide/raiden_guide.py init --target /path/to/myrepo
  ↓
installer.scan_legacy_artifacts()
  → checks for AGENTS.md (non-bridge), agent-ledger/, agent-prompts/
  → archives legacy AGENTS.md to .raiden/local/legacy/ if found
  ↓
installer._instance_file_map()
  → generates all scaffold file contents (including CURRENT_STATE, GOALS etc.
    pre-populated with legacy scan results)
  ↓
installer.init_instance() writes:
  AGENTS.md (bridge)
  .raiden/README.md, local/README.md, state/README.md
  state/{CURRENT_STATE,GOALS,OPEN_LOOPS,DECISIONS,WORK_LOG,LEGACY_REVIEW}.md
  instance/metadata.json  (installed_edict_version: "0.0.0")
  Empty dirs: .raiden/writ/, .raiden/local/prompts/, rules/, context/, instance/

  ↓  python3 toolkit/guide/raiden_guide.py install --target /path/to/myrepo --package /path/to/edict-pkg
  ↓
planner.create_plan(instance_root, package_root)
  → loader.load_instance_metadata()  ← reads .raiden/instance/metadata.json
  → loader.load_package_manifest()   ← reads manifest.json
  → loader.load_installed_baseline() ← reads .raiden/instance/baseline.json
                                        (returns None on fresh install)
  → check_schema_compatibility()
  → compare_versions()
  → _managed_root_has_files() check  (blocks if writ/ has files but no baseline)
  → for each file in manifest.managed_files:
      check installed hash vs target hash vs baseline hash
      → FileAction: "add" | "update" | "unchanged"
      → Conflict: "local_modification" if locally changed
  → for each file in baseline but NOT in manifest:
      check if locally modified → Conflict or "remove" FileAction
  → classify_anomalies()
  → return PlanResult

  [--apply flag present and plan.can_apply is True]
  ↓
applier.apply_plan(plan, instance_root, package_root)
  → for each FileAction:
      "add" or "update": shutil.copy2(payload/<path>, .raiden/writ/<path>)
      "remove": dst.unlink() + prune empty dirs
      "unchanged": no-op
  → write new baseline.json
  → update metadata.json installed_edict_version
```

**Branching logic:**

- If `baseline.json` is missing and `.raiden/writ/` has files: **hard block** (cannot prove no local modifications)
- If `baseline.json` is missing and `.raiden/writ/` is empty: initial install allowed, no baseline check
- If any managed file has a current hash that differs from both target hash AND baseline hash: **conflict block** (local modification)
- If `protected_path_write` anomaly: **block**
- If conflicts exist: **block**; no partial apply
- If version is "downgrade": reported but **not blocked** (provisional policy; see §6)

---

## 5. Conventions & Patterns

**Canonical naming stack** — must be used exactly:
- `RAIDEN` = central governing agent/framework authority
- `Edict` = central RAIDEN-authored managed instruction/package surface
- `RAIDEN Instance` = downstream deployed repo-local form
- `Writ` = installed managed core artifact within a RAIDEN Instance
- `payload` = technical term for installable subset of an Edict (becomes the Writ after install)

**Authority order** (explicit, non-negotiable):
1. Root-level canonical RAIDEN docs
2. `toolkit/` subtree (explicitly designated canonical)
3. `reference-reviews/` only if explicitly adopted by root
4. `reference-extracts/` only if explicitly adopted by root
5. `Source_info/` (preserved history, non-canonical)
6. `reference-repos/` (read-only evidence, non-canonical)

**Nothing becomes canonical by proximity.** Proximity to a canonical file does not transfer authority.

**Downstream instance startup reading order**:
1. `AGENTS.md` (startup bridge)
2. `.raiden/README.md`
3. `.raiden/state/CURRENT_STATE.md`
4. `.raiden/state/OPEN_LOOPS.md`
5. Other materials as needed

**Promotion path** (how ideas become canon): source evidence → review/comparison → synthesis → explicit adoption into a root canonical file.

**Two-tier language standard**: durable human-facing docs stay readable; agent-facing internal execution layers (prompts, pause-points, continuation payloads) may be compressed for token efficiency.

**Managed core update contract** (D-0016, inviolable for all update mechanisms):
1. Update managed core
2. Preserve local overlay
3. Preserve local live state
4. Stop and report if a managed file was locally modified

**Conflict rule**: never silently flatten conflicts; record and surface them.

**Ingress discipline**: `reference-repos/` is for bounded evidence snapshots only. Any future import requires a pre-intake go/no-go gate (five questions, all must be yes).

---

## 6. Ambiguities & Contradictions

**A. `applier.py` hard-codes managed root path**

`toolkit/updater/raiden_updater/applier.py:64` does `managed_root = instance_root / ".raiden" / "writ"` unconditionally, while the planner reads `metadata.managed_roots[0]`. These agree for all current canon (single managed root is always `.raiden/writ`), but if the metadata ever had a different root, the applier would silently write to the wrong location. The planner derives it correctly; the applier doesn't.

**B. `server.py` uses `tkinter` inside a "dependency-free" server**

The module docstring says "dependency-free." The `/api/select-folder` endpoint imports `tkinter` at call time. `tkinter` requires a display (not available in headless environments) and is not always present in Python distributions. The endpoint will raise `ImportError` or fail silently on headless/server systems. This makes the "dependency-free" claim partially false.

**C. `web/README.md` is a generic Vite template README**

It contains zero RAIDEN-specific content — just the default Vite+React scaffold README. There is no documentation of how to start the Python backend, how to serve the built UI, what the expected development workflow is, or how the two halves integrate. An operator who finds `web/` first will have no guidance.

**D. `RAIDEN_NEXT_STEP_WORKING_PLAN.md` lives at repo root alongside canonical docs**

Its own internal disclaimer says it's "retained as a historical working draft" and "not the current RAIDEN plan." However, `REPOSITORY_MAP.md` does not list this file in the Canon Layer table. The only protection against an agent treating it as current guidance is its own internal text. A newly loaded agent scanning root-level `.md` files could inadvertently act on it.

**E. `.codex/config.toml` contains `model = "gpt-5.4"`**

This is a Codex-agent (OpenAI) configuration. RAIDEN's governance is explicitly model-agnostic. The presence of this config raises questions: Is Codex the current primary operator environment? Is this still active? Does it conflict with Claude Code being used now? This is not documented anywhere in RAIDEN canon.

**F. `.codex.placeholder` is undocumented**

It's a 0-byte, `r-xr-xr-x` file at the repo root. No file in the repo explains what it is or what it guards.

**G. `working/` is not gitignored**

The `.gitignore` ignores `reference-repos/`, `__pycache__/`, `*.py[cod]`, `.pytest_cache/`, but not `working/`. The `working/current-task-set/` contains task-specific prompts and session artifacts from previous development cycles. `ARTIFACT_AUDIENCE.md` says `working/` is "not durable authority without promotion," but these files are tracked in git history and visible in the repo.

**H. `Source_info/Raiden Foundational Operating Brief Prompt.md` says "You are Raiden"**

This is a prompt-to-AI artifact preserved as source history. It directly addresses the reader as if they are Raiden receiving an instruction. An agent reading this file could interpret it as an active operational instruction rather than preserved historical source. The file does have a status block at the top (`Canonicality: non-canonical`) but the body is imperative.

**I. Two separate uses of `AGENTS.md` — this repo's development guide vs. downstream bridge**

In this RAIDEN development repo, `AGENTS.md` is an agent guide for working on RAIDEN itself. In the downstream model, `AGENTS.md` is the startup bridge that `init_instance()` writes to a target repo pointing into `.raiden/`. These are different things sharing the same filename. The distinction is clear in context, but could be confusing on first reading without knowing both roles exist.

**J. `legacy.py` purpose is unclear**

It wraps `installer.py`'s legacy scanning and `init_instance()` in a compatibility shim, but there's no documentation of who calls it, where the original callers are, when this surface was introduced, or when it will be removed. The test suite (`test_legacy.py`) exercises it, implying it's a tested interface, but there's no explanation of the consumer.

**K. Downgrade is reported but not blocked**

The updater computes `version_comparison="downgrade"` but does not block apply. This is listed as a "provisional choice" in `toolkit/updater/README.md`. Downgrade policy is explicitly deferred. An operator who runs `apply` on a lower-version package will succeed silently.

**L. `reference-repos/README.md` describes a workflow for a directory that is now empty**

All prototype snapshots have been retired. `reference-repos/README.md` still reads as if it is an active intake directory with instructions for copying repos into it. It is now misleading as written.

---

## 7. What I Need to Operate Effectively

**Gaps that would prevent reliable operation as the agent for this workspace:**

**A. No Python packaging setup**

`toolkit/updater/raiden_updater/` is a Python package with no `pyproject.toml`, `setup.py`, or `setup.cfg`. The `raiden_guide.py` uses `sys.path` injection to find it. Tests work because `pytest` runs from the `toolkit/updater/` directory. There is no documented way to install `raiden_updater` system-wide or into a virtualenv. If asked to "run the updater," I need to know the correct working directory and invocation path explicitly.

**B. No RAIDEN-specific web UI documentation**

`toolkit/updater/web/` has a built `dist/` and source in `src/`, but there is no documentation of how to start the Python backend alongside it, whether the built `dist/` is served by the Python backend, or what the expected end-to-end operator workflow is. The only guidance is the server's startup message at `http://127.0.0.1:8080`.

**C. No CI or test runner configuration**

There is no `tox.ini`, `.github/workflows/`, or equivalent. The tests can be run with `py -m pytest tests/ -v` from `toolkit/updater/`, as documented in the README. But there is no automated way to verify the test suite passes after a change, and no standardized dev environment setup is documented.

**D. Unclear active agent environment**

Both `AGENTS.md` (Claude Code context) and `.codex/config.toml` (Codex/GPT-5.4 context) are present. Which is the current primary operator environment? Are both in active use? This matters because `OPERATING_INTENT.md` says agents should be treated as model-bound for a work cycle, but the designated canonical model for RAIDEN work is not stated.

**E. No operator kickoff prompt**

`toolkit/prompts/CATALOG.md` explicitly lists "a reusable operator kickoff prompt" as a current gap. Starting a work session in RAIDEN requires reading multiple root docs to reconstruct current state. There is no compact standard entry prompt for beginning a new work cycle in this repo.

**F. `working/` status ambiguity**

The files in `working/current-task-set/` include historical task prompts from prior work cycles. It is not clear whether these should be treated as relevant historical context for ongoing work or ignored as stale session artifacts. They are tracked in git but marked as non-canonical by policy.

**G. Downgrade policy is undefined**

If asked to roll back a downstream instance to a prior Edict version, current canon says to report it but allows applying it. There is no guidance on whether the operator should be warned, whether conflicts need special handling, or whether downgrade is ever expected as a real operation vs. an error condition.

**H. `reference-repos/README.md` is now stale**

`reference-repos/` is empty. The README describes an active intake workflow that no longer applies. This is a minor navigation hazard for a new agent reading the directory.
