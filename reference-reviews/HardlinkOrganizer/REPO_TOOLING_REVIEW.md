# HardlinkOrganizer Repo Tooling Review

## 1. Repo Identity

- Repo name: `HardlinkOrganizer`
- Snapshot location: `/mnt/e/RAIDEN/reference-repos/HardlinkOrganizer`
- Apparent live root referenced by the repo: `/mnt/e/HardlinkOrganizer`
- Review framing: strongest current live product implementation of the newer embedded toolkit model

## 2. Executive Summary

`HardlinkOrganizer` is the clearest current example of a **project-local embedded control plane** among the imported repos.

Observed evidence shows a coherent shallow structure built around:

- a product-facing root `README.md`
- a project-local `agent-ledger/` as the continuity and governance layer
- a separate `agent-prompts/` library for bounded execution slices
- a `notes/` area for planning and transition material
- product-specific packaging and release support material under `packaging/unraid/`

This makes `HardlinkOrganizer` highly relevant to RAIDEN as a source for the **downstream embedded instance pattern**.

It is not a clean generic template yet. Several parts are still tightly coupled to this project and to its extraction history, and some materials contain environment-specific or time-sensitive assumptions that RAIDEN should not promote directly.

## 3. Artifact Inventory

| Item | Location | Category | Apparent Purpose | Status | Reusability | Notes |
|---|---|---|---|---|---|---|
| Product front page | `README.md` | Navigation artifact | Product identity, entrypoints, repo map | Active | High | Good model for pairing product brief with control-plane pointers |
| Agent guide | `AGENTS.md` | Agent-facing artifact | Agent startup order, authority, root lock | Active | High | Strong downstream pattern, but absolute-path-coupled |
| Ledger index | `agent-ledger/README.md` | Navigation artifact | Defines local control plane and file map | Active | High | Strong embedded-ledger entrypoint |
| Ledger standard | `agent-ledger/AGENT_LEDGER_STANDARD.md` | Governance/control artifact | Minimal standard for evidence, provenance, loops, terminology | Active | High | Good minimal standard, but lighter than some older variants |
| Governance | `agent-ledger/GOVERNANCE.md` | Governance/control artifact | Read-only governance constraints | Active | High | Practical short form |
| Terms registry | `agent-ledger/TERMS.md` | Governance/control artifact | Local terminology and acronym control | Active | High | Useful and concise |
| Current state | `agent-ledger/CURRENT_STATE.md` | State-tracking artifact | Evidence-based state summary | Active | High | Good example of current-state file in active use |
| Goals | `agent-ledger/GOALS.md` | State-tracking artifact | Current goals and priorities | Active | High | Strong canonical role separation from current state |
| Open loops | `agent-ledger/OPEN_LOOPS.md` | State-tracking artifact | Entry point for execution work | Active | High | Coarse but clear |
| Decisions | `agent-ledger/DECISIONS.md` | State-tracking artifact | Decision log and rationale | Active | High | Strong practical decision record |
| Work log | `agent-ledger/WORK_LOG.md` | State-tracking artifact | Chronological durable work history | Active | High | Useful for execution lineage |
| Exceptions | `agent-ledger/EXCEPTIONS.md` | Governance/control artifact | Exception tracking | Active | Medium-high | Present, but not exercised yet |
| Snapshots scaffold | `agent-ledger/SNAPSHOTS/` | State-tracking artifact | Point-in-time captures | Scaffold only | Medium | Structure exists but appears unused in this snapshot |
| Prompt library | `agent-prompts/` | Prompt asset | Narrow execution prompts and templates | Active | High | Strong pattern for bounded execution support |
| Notes index | `notes/README.md` | Planning artifact | Index of local planning notes | Active | Medium-high | Useful support pattern |
| Packaging guide | `packaging/unraid/README.md` | Operational artifact | Deployment and release support | Active | Medium | Valuable operational pattern, but product-specific |
| Extraction plan | `notes/PROJECT_WORKSPACE_EXTRACTION_PLAN.md` | Planning artifact | Workspace promotion/extraction history | Historical-active | Medium | Useful transition pattern, not canonical as-is |

## 4. Authority Map

- Observed product front door: `README.md`
- Observed agent startup entry: `AGENTS.md`
- Observed local control plane: `agent-ledger/`
- Observed execution entrypoint: `agent-ledger/OPEN_LOOPS.md`
- Observed bounded prompt dispatch surface: `agent-prompts/`
- Observed support/planning archive: `notes/`

### Authority order inferred from the repo

1. `AGENTS.md` for agent startup and workspace authority
2. `agent-ledger/README.md` plus the rest of `agent-ledger/` for continuity, state, and execution governance
3. `README.md` for product framing and implementation entrypoints
4. `agent-prompts/` for bounded execution slices
5. `notes/` and `packaging/` for supporting context

### Strong finding

This authority structure is coherent and intentional. The repo clearly distinguishes:

- product summary
- control plane
- execution prompts
- planning/support notes

That separation is one of the strongest reasons this repo matters to RAIDEN.

## 5. Structural Classification

- Governance/control artifacts:
  - `agent-ledger/AGENT_LEDGER_STANDARD.md`
  - `agent-ledger/GOVERNANCE.md`
  - `agent-ledger/TERMS.md`
  - `agent-ledger/EXCEPTIONS.md`
- Agent-facing artifacts:
  - `AGENTS.md`
  - `agent-prompts/README.md`
  - prompt files under `agent-prompts/`
- State-tracking artifacts:
  - `agent-ledger/CURRENT_STATE.md`
  - `agent-ledger/GOALS.md`
  - `agent-ledger/OPEN_LOOPS.md`
  - `agent-ledger/DECISIONS.md`
  - `agent-ledger/WORK_LOG.md`
  - `agent-ledger/SNAPSHOTS/`
- Navigation artifacts:
  - `README.md`
  - `agent-ledger/README.md`
  - `notes/README.md`
- Planning artifacts:
  - `notes/HARDLINK_ORGANIZER_NEXT_STEPS.md`
  - `notes/HARDLINK_ORGANIZER_FEATURE_EXPANSION_PLAN.md`
  - `notes/PROJECT_WORKSPACE_EXTRACTION_PLAN.md`
- Prompt assets:
  - all files under `agent-prompts/`
- Toolkit definitions:
  - the repo-local ledger system as a whole
- Unknown/unresolved:
  - whether `SNAPSHOTS/` is expected to remain lightly used or was simply not exercised yet

## 6. Strengths

### 1. Strong embedded-instance shape

The repo provides the clearest imported example of a downstream local toolkit/control-plane instance that lives *inside* a working product repo without overtaking the whole repo structure.

### 2. Clear role separation

It separates:

- product readme
- agent bootstrapping
- continuity/state
- execution prompts
- planning notes

This is structurally better than repos where prompts, audits, and handoffs sprawl across the whole tree.

### 3. Practical rather than speculative

The ledger files are not just scaffolds; they reflect actual project status, open loops, decisions, and work history for a live product.

### 4. Bounded prompt surface

`agent-prompts/` is a strong pattern for handing narrow work slices to other agents without re-explaining the whole project each time.

### 5. Project portability intent

The repo repeatedly aims to make the workspace stand on its own, which aligns well with RAIDEN’s future need to define an embedded local instance pattern.

## 7. Weaknesses, Drift, And Risks

### 1. Absolute-path coupling

Many agent-facing artifacts hardcode the live root as `/mnt/e/HardlinkOrganizer` and `E:\\HardlinkOrganizer`.

This is useful operationally for the live repo, but too environment-specific to promote directly into RAIDEN canon without abstraction.

### 2. Extraction-history residue

Some materials still carry transition logic from promotion out of `StarlightDaemonDev`.

That history is useful, but it should not be mistaken for the steady-state generic model.

### 3. Coarse loops vs many prompt slices

`OPEN_LOOPS.md` currently contains only a small number of broad loops, while `agent-prompts/` contains many narrow execution slices.

This works in practice, but it creates a structural tension:

- ledger loops are coarse strategic containers
- prompt files are fine-grained operational units

RAIDEN will need to decide how explicit that relationship should be.

### 4. Lightweight governance standard

The standard is practical and concise, which is a strength, but it is also lighter than some of the richer older variants seen elsewhere.

For example, it does not itself define:

- a stronger closure protocol
- snapshot usage expectations
- atomic update behavior in detail
- explicit loop-to-prompt linking rules

### 5. Snapshot layer not visibly exercised

The snapshot mechanism exists but appears unpopulated in this snapshot.

That means the structure is present, but its actual operational value here is not yet strongly demonstrated.

### 6. Environment-specific planning details inside state

`CURRENT_STATE.md` records model-pool availability and workspace-extraction defaults that may be accurate for the original live context, but those are volatile and should be treated carefully in RAIDEN extraction.

## 8. Reusable Components

### Likely reusable with minimal normalization

- shallow `agent-ledger/` file set
- `AGENTS.md` startup/read-order pattern
- separation of `agent-ledger/`, `agent-prompts/`, and `notes/`
- `agent-ledger/README.md` as embedded control-plane index
- `CURRENT_STATE` / `GOALS` / `OPEN_LOOPS` / `DECISIONS` / `WORK_LOG` role separation
- concise `TERMS.md` pattern
- micro-prompt dispatch template

### Reusable with moderate normalization

- `AGENT_LEDGER_STANDARD.md`
- `GOVERNANCE.md`
- `EXCEPTIONS.md`
- prompt-library organization and naming
- planning-note indexing

### Project-specific only or mostly project-specific

- Unraid packaging docs
- Community Apps release path
- hardlink workflow specifics
- destination management roadmap
- extraction plan details tied to this repo’s promotion history

## 9. RAIDEN Import View

### Retain as reference only

- most product-specific notes under `notes/`
- Unraid packaging and CA publishing material
- extraction-history specifics

### Candidate for promotion

- embedded local control-plane structure
- agent startup/read-order pattern
- ledger file-role separation
- bounded prompt library pattern
- micro-prompt dispatch pattern

### Candidate for merge with other repos

- governance and ledger standard language
- terminology management
- open-loops execution surface
- decision-log conventions

### Candidate for deprecation or caution

- direct promotion of absolute root locks and hardcoded filesystem paths
- direct promotion of time-sensitive model-availability state

## 10. Bottom-Line Assessment

`HardlinkOrganizer` is the strongest current **practical downstream implementation** of the newer agent-ledger/governed-workspace idea.

For RAIDEN, this repo is most valuable not because it is the conceptual origin, but because it shows the pattern working inside a live coding project with:

- real state
- real decisions
- real prompt slices
- real project-local continuity

It should be treated as a primary source for the future **repo-local embedded instance model**.

It should **not** be copied wholesale. RAIDEN should extract:

- the structure
- the role boundaries
- the file responsibilities
- the prompt-surface pattern

while stripping out:

- environment-specific paths
- project-specific release content
- extraction-history residue
- volatile session/model assumptions

## 11. Confidence

### Observed evidence

- full local ledger file set
- active prompt library
- agent guide
- product and planning docs

### Strong inference

- this is the best current live practical embedded-instance source among the imported repos
- its structure is more directly reusable than its content

### Weak inference

- if the live repo outside this snapshot has additional snapshots or more recent loops, operational maturity may be even stronger than shown here

### Unresolved ambiguity

- how the repo intended to formalize the relationship between coarse `OPEN_LOOPS` entries and narrow prompt files over time
