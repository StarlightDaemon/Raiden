# CLAUDE.md — RAIDEN Session Anchor

**Status: Working draft — not yet committed to canon. Do not treat as
authoritative until confirmed in `REPOSITORY_MAP.md`.**

Persistent context for any Claude Code session in this repo. Read this first.
Authoritative companions: `SOURCE_OF_TRUTH.md`, `AGENT_BOUNDARIES.md`,
`REPOSITORY_MAP.md`, `CURRENT_STATE.md`. This file orients an agent quickly;
it does not replace canon.

---

## 1. What RAIDEN Is

RAIDEN is a central toolkit/framework repository. It exists to eliminate the
repeated context-loss tax that AI-assisted work pays in two directions: long
chat sessions degrade as context accumulates, and IDE-connected agents burn
token budgets re-deriving the same project state, conventions, and decisions
every cycle.

RAIDEN's answer is **durable infrastructure**: stable governance docs, a
shared prompt asset library, a canonical downstream `RAIDEN Instance` model
with a `.raiden/` control plane, and an updater toolchain that installs and
refreshes the managed core in target repos without clobbering local overlay
or live state. "Durable" means an agent starting a work cycle in any repo
running a RAIDEN Instance can read `AGENTS.md` → `.raiden/README.md` →
`.raiden/state/CURRENT_STATE.md` and immediately know where it is, what has
been decided, and what is in scope — no transcript replay required.

RAIDEN is not a running process. It is a framework repo. When an agent is
invoked in this workspace, it *is* RAIDEN operating on RAIDEN. The only
operational software is `toolkit/updater/`; everything else is governance and
documentation.

---

## 2. Authority Model

**Canonical layers** (binding):
- Root-level RAIDEN Markdown/text files
- The `toolkit/` subtree (explicitly designated canonical)

**Non-canonical layers** (evidence, history, or work product — never canon by
proximity):
- `reference-reviews/` — comparative analysis; canonical only when explicitly
  adopted by a root file
- `reference-extracts/` — compact extracted patterns; same rule
- `Source_info/` — preserved historical source material
- `reference-repos/` — read-only prototype evidence (currently empty)
- `working/` — session-shaped working artifacts; never durable authority
  without promotion

**Authority order** (from `SOURCE_OF_TRUTH.md`):
1. Root-level canonical RAIDEN docs
2. Explicitly designated canonical toolkit subtree (`toolkit/`)
3. Review artifacts in `reference-reviews/` only when adopted by a root doc
4. Extracted references in `reference-extracts/` only when adopted by a root
   doc
5. `Source_info/` as preserved history
6. `reference-repos/` as read-only evidence

**Conflict resolution**: explicit root canonical file → latest decision in
`DECISIONS.md` → adopted synthesis/review artifact → preserved evidence.
Conflicts must be recorded, not silently flattened.

**Promotion path**: source evidence → review/comparison → synthesis →
explicit adoption into a root canonical artifact. Prototype wording does not
become authoritative by file location.

**Explicit non-canonical callouts**:
- `RAIDEN_NEXT_STEP_WORKING_PLAN.md` is **not current guidance**. It lives at
  the root for historical reasons and self-disclaims as a retained working
  draft. Do not act on it.
- `working/` is **not canonical**. Treat everything inside as non-durable
  unless explicitly promoted.
- `Source_info/` is **preserved history, not instruction**. The
  Foundational Operating Brief Prompt addresses the reader as "Raiden" — it
  is preserved source, not a live system prompt.

---

## 3. Naming Canon

These five terms are fixed. Use them precisely; do not paraphrase or invent
synonyms in canonical text.

- **RAIDEN** — the central governing agent/framework authority. The repo
  itself, and the agent identity when operating on it.
- **Edict** — the central RAIDEN-authored managed instruction/package
  surface. What RAIDEN issues.
- **RAIDEN Instance** — the canonical downstream deployed repo-local form. A
  target repo running a `.raiden/` control plane.
- **Writ** — the installed managed core artifact within a RAIDEN Instance.
  The Edict's payload after install lives here (`.raiden/writ/`).
- **payload** — the technical install term for the installable subset of an
  Edict. Becomes the Writ after install. Not a peer identity in the naming
  stack.

---

## 4. Repository Map

`REPOSITORY_MAP.md` (root) is the authoritative navigation spine. It
enumerates the canonical root files, the canonical `toolkit/` subtree, and
the non-canonical layers. Read it for any structural question.

This file does not duplicate the map. The only structural shorthand kept
here is the canon-vs-non-canon classification:

- **Canon**: root-level RAIDEN `.md`/`.txt` files; the `toolkit/` subtree.
- **Non-canon**: `reference-reviews/`, `reference-extracts/`, `Source_info/`,
  `reference-repos/`, `working/`, `.codex/`, and `RAIDEN_NEXT_STEP_WORKING_PLAN.md`.
  Nothing in these layers becomes canon by proximity; promotion requires the
  path in §2.

---

## 5. Tool Surface (Operational Reference)

All operational tooling is Python under `toolkit/updater/`. There is no
`pyproject.toml`/`setup.py`; `raiden_guide.py` uses `sys.path` injection. Run
commands from the working directories specified below.

### `raiden_guide.py` — operator-facing wrapper

Run from repo root:

```
python3 toolkit/guide/raiden_guide.py steps
python3 toolkit/guide/raiden_guide.py init    --target <path> [--force]
python3 toolkit/guide/raiden_guide.py install --target <path> --package <path> [--apply]
python3 toolkit/guide/raiden_guide.py doctor  --target <path>
```

- `init` creates the `.raiden/` skeleton in a target repo
- `install` runs `plan`; with `--apply` also runs `apply`
- `doctor` checks instance shape

### `raiden_updater` CLI — direct package surface

Run from `toolkit/updater/` (the `raiden_updater` package has no
`__main__.py`; invoke `cli` explicitly):

```
python3 -m raiden_updater.cli plan  --instance <path> --package <path>
python3 -m raiden_updater.cli apply --instance <path> --package <path>
```

- `plan` is read-only; exits 0 if apply-safe or already current, 1 otherwise.
- `apply` requires an apply-safe plan; raises `ApplyError` otherwise.

**Block reasons (plan exits 1)**:
- `missing_baseline` — `.raiden/writ/` has files but no `baseline.json`
- schema incompatibility (`instance_schema_version` not in
  `compatible_instance_schemas`)
- `protected_path_write` — package would write into overlay or state roots
- version string not strict `MAJOR.MINOR.PATCH`
- `local_modification` conflict on any managed file

**Special "not-an-error" reason**: `Already up to date` returns
`can_apply=False` but exits 0.

### Web installer — local backend + UI

Backend (run from `toolkit/updater/`; the entry point is the `server`
module's `__main__` block, which calls `serve()` on `127.0.0.1:8080`):

```
python3 -m raiden_updater.server
```

Endpoints (all `POST`, JSON body, CORS `*`):
`/api/scan`, `/api/init-preview`, `/api/init-apply`, `/api/plan`,
`/api/apply`, `/api/doctor`, `/api/select-folder`.

UI scaffold lives at `toolkit/updater/web/` (Vite/React). Its README is the
generic Vite template — there is no RAIDEN-specific operator README yet
(tracked in `working/RAIDEN_GAPS.md` G-007).

### Tests

From `toolkit/updater/`:

```
python3 -m pytest tests/ -v
```

No CI is configured. Run tests manually after changes.

### Known operational inconsistencies

- **`applier.py:64` hard-codes `.raiden/writ` as the managed root**, ignoring
  `metadata.managed_roots[0]`. Planner derives it from metadata; applier
  doesn't. Agrees today because all canon uses `.raiden/writ`. Diverges
  silently if `managed_roots` ever changes. Tracked as G-005.
- **`server.py /api/select-folder` imports `tkinter`** despite the module
  docstring claiming "dependency-free." Will `ImportError` on headless
  systems. Tracked as G-006.
- **No `pyproject.toml`**. Cannot `pip install raiden_updater`. Use the
  invocations above; do not assume importability outside the documented
  working directories.
- **Downgrade is currently silently accepted** by the updater. Operator
  working decision is to block; not yet promoted to root canon (see §6 and
  G-004).

---

## 6. Known Active Ambiguities

The full live tracker is `working/RAIDEN_GAPS.md` — a non-canonical working
artifact. As of the most recent update it carries **12 open items** (G-001
and G-003 through G-013; G-002 is closed).

Items there fall into three categories. Read the tracker for IDs, locations,
and recommended actions:

- **Code bugs** — defects in the implementation that need a fix and a
  regression test. Examples: `applier.py` hard-coded managed root,
  `server.py` tkinter import, downgrade silently accepted.
- **Documentation gaps** — missing or stale docs that mislead a fresh agent.
  Examples: `web/README.md` is the default Vite template, `legacy.py` has no
  documented consumer or removal condition, `reference-repos/README.md`
  describes intake for an empty directory.
- **Cleanup decisions** — items requiring operator input before action.
  Examples: release-staging classification, disposition of
  `RAIDEN_NEXT_STEP_WORKING_PLAN.md`, disposition of stale `working/`
  fixtures.

---

## 7. Session Startup Procedure

Read in this order. Stop when you have what the task requires.

1. **`CLAUDE.md`** (this file) — orientation
2. **`AGENTS.md`** — the RAIDEN agent guide
3. **`README.md`** — repository identity and top-level framing
4. **`SOURCE_OF_TRUTH.md`** — authority order and promotion rules
5. **`REPOSITORY_MAP.md`** — navigation spine
6. **`CURRENT_STATE.md`** — what's done, what's active, what's deferred
7. **`DECISIONS.md`** — durable decision record
8. **`AGENT_BOUNDARIES.md`** — role definitions and write boundaries
9. **`MANAGED_VS_LOCAL.md`** — managed-core vs. local-overlay update boundary
10. **`RELEASE_READY_CHECKLIST.md`** — v1 release-prep gate
11. **`OPEN_LOOPS.md`** — pending work and unresolved items
12. **Task-specific materials** — `working/RAIDEN_GAPS.md` for live
    ambiguities, plus the most recently dated artifacts in `working/` for
    session history, then narrower files as needed

### Operator kickoff prompt

Use this verbatim (or paraphrase) at the start of a new RAIDEN work cycle.
Keep it compact — it is meant to load orientation, not to expand it.

```
You are operating in the RAIDEN canonical framework repo. Before answering,
read in this order:

  1. CLAUDE.md
  2. AGENTS.md
  3. README.md
  4. SOURCE_OF_TRUTH.md
  5. REPOSITORY_MAP.md
  6. CURRENT_STATE.md
  7. DECISIONS.md
  8. AGENT_BOUNDARIES.md
  9. MANAGED_VS_LOCAL.md
 10. RELEASE_READY_CHECKLIST.md
 11. OPEN_LOOPS.md

Then check working/RAIDEN_GAPS.md for active ambiguities, and consult the
most recently dated artifacts under working/ for session history relevant to
the task.

Authority order: root canonical .md files > toolkit/ > everything else.
Nothing under reference-*, Source_info/, or working/ is canon.
RAIDEN_NEXT_STEP_WORKING_PLAN.md is historical — ignore it.

Naming canon (use exactly): RAIDEN, Edict, RAIDEN Instance, Writ, payload.

The four-point managed-core update contract (D-0016) is inviolable: update
managed core, preserve local overlay, preserve local live state, stop and
report on locally modified managed files.

Task: <state the bounded task here>.

Pause and confirm scope before broad changes. Bounded patches preferred over
sweeping rewrites.
```

---

## 8. Inviolable Rules

1. **Authority order is fixed.** Root canon outranks toolkit; toolkit
   outranks everything else. Nothing else becomes canon by proximity.
2. **Promotion path is the only path to canon.** Source → review →
   synthesis → explicit adoption into a root file. No shortcuts.
3. **Naming canon is fixed.** `RAIDEN`, `Edict`, `RAIDEN Instance`, `Writ`,
   `payload`. Do not coin alternatives in canonical text.
4. **The four-point managed-core update contract (D-0016) holds for every
   update mechanism**: (a) update managed core, (b) preserve local overlay,
   (c) preserve local live state, (d) stop and report when a managed file
   was locally modified. No silent overwrites.
5. **Conflicts are recorded, not flattened.** When materials disagree,
   surface the conflict; do not pick a side silently.
6. **Reference repos are read-only by process.** Do not edit
   `reference-repos/` or `Source_info/` snapshots without explicit operator
   instruction.
7. **Ingress is gated.** Any new external repo intake must pass the five
   pre-intake gate questions in `INGRESS_POLICY.md §0`. All five answers
   must be yes.
8. **Downstream agents do not rewrite RAIDEN core.** A RAIDEN Instance may
   extend RAIDEN through overlay artifacts; it may not silently rewrite
   managed law files in place.
9. **Do not broaden updater canon beyond the current local CLI surface**
   without explicit operator direction and observed need.
10. **Bounded edits over sweeping rewrites.** Narrow patches; review the
    diff; validate immediately. Ask the operator before wide changes.

### Agent role boundaries

From `AGENT_BOUNDARIES.md` (consult that file for the full rules — the table
below is a fast reference, not a substitute):

| Role | Primary write surface | Must not write directly |
|---|---|---|
| Operator | decisions through direct instruction | imported repos, unless intentionally acting outside RAIDEN review flow |
| Reference Review Agent | `reference-reviews/` | root canon as if review alone were adoption |
| Canonical Structuring Agent | root canonical `.md` files | imported prototype repos |
| Downstream Embedded-Instance Agent | the future repo-local control plane | RAIDEN root canon, unless feeding back through review |
| Implementation Agent | the target implementation repo | RAIDEN canon, unless specifically tasked |
| Audit / Review Agent | bounded audit/review artifacts | source-of-truth changes without explicit adoption |
| Research Agent | workbook, source-history, research artifacts | canonical docs without synthesis |

Identify which role the current task fits before writing. Crossing a
boundary requires an explicit operator instruction; "I happened to be in
the file" is not authorization.
