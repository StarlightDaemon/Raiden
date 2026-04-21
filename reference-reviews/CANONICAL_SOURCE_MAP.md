# Canonical Source Map

## Purpose

This document is the P0 synthesis artifact for reviewed prototype repos.

It answers:

- which reviewed repo is the primary source for each major RAIDEN concept
- which repos should only support or refine that concept
- which patterns should stay historical-only
- which reviewed source should feed each first-wave RAIDEN canonical document

This is a synthesis map, not final canon text.

## 1. P0 Synthesis Summary

The reviewed repos do not describe one single RAIDEN lineage. They describe several complementary lineages:

1. **Embedded local control plane**
   - strongest source: `HardlinkOrganizer`

2. **Original governance architecture**
   - strongest source: `Starlight Architect`

3. **Host/meta-workspace repository shape**
   - strongest source: `StarlightDaemonDev`

4. **Governance sidecar and remote audit**
   - strongest source: `BIND`

5. **Artifact policy and handoff discipline**
   - strongest source: `CTRL`

6. **Role memo and producer/consumer split**
   - strongest sources: `ARC`, `ARC-RC`

No reviewed repo should be promoted as RAIDEN canon wholesale. RAIDEN canon should be assembled by concept.

## 2. Canonical Source Ownership By Concept

| RAIDEN Concept | Primary Source | Supporting Sources | Confidence | Why |
|---|---|---|---|---|
| Embedded local control plane | `HardlinkOrganizer` | `StarlightDaemonDev`, `CTRL` | High | cleanest current example of a repo-local `agent-ledger/` plus prompts and state files |
| Original governance architecture | `Starlight Architect` | `BIND` | High | strongest ancestor for registry, audit, handoff, and agent-boundary logic |
| Host/meta-workspace structure | `StarlightDaemonDev` | `CTRL` | High | best root-level category scaffold around a ledger-governed workspace |
| Governance sidecar / vendored kit | `BIND` | `Starlight Architect` | High | clearest sidecar kit, remote audit, and vendored-kit to package maturity model |
| Artifact policy / local-vs-session split | `CTRL` | `HardlinkOrganizer` | High | strongest explicit split between durable local state and session-shaped artifacts |
| Agent boundaries / role memos | `Starlight Architect` | `ARC`, `ARC-RC`, `HardlinkOrganizer` | Medium-high | strongest formal boundary logic, with ARC pair adding simple role memo patterns |
| Prompt governance / handoff prompts | `BIND` | `HardlinkOrganizer`, `CTRL` | High | strongest explicit prompt-interface and remote-audit handoff patterns |
| Current-state and continuity files | `HardlinkOrganizer` | `StarlightDaemonDev`, `CTRL` | High | best live evidence of `CURRENT_STATE`, `GOALS`, `OPEN_LOOPS`, `DECISIONS`, `WORK_LOG` roles |
| Research/source-history indexing | `ARC-RC` | `CTRL`, `Source_info/` in RAIDEN | Medium-high | strongest research index and preservation pattern, though some drift exists |
| Producer/consumer export boundary | `ARC-RC` | `ARC`, `StarlightDaemonDev` | Medium-high | strongest explicit output-zone and downstream sync model |
| Exception / drift handling | `BIND` | `HardlinkOrganizer` | Medium | strongest drift-template idea; `HardlinkOrganizer` has cleaner `EXCEPTIONS` slot |
| Release/readiness bounded ledgers | `BIND` | `CTRL` | Medium | good narrow remediation-ledger model, but too report-heavy for default RAIDEN use |

## 3. RAIDEN Canonical Document Source Assignments

| RAIDEN File | Primary Source | Secondary Source | Notes |
|---|---|---|---|
| `SOURCE_OF_TRUTH.md` | `Starlight Architect` | `CTRL`, `BIND` | use Architect for authority hierarchy, CTRL for local artifact split, BIND for sidecar caveats |
| `REPOSITORY_MAP.md` | `StarlightDaemonDev` | `CTRL` | use StarlightDaemonDev for category scaffold; pull SOP clarity from CTRL |
| `AGENT_BOUNDARIES.md` | `Starlight Architect` | `ARC`, `ARC-RC`, `HardlinkOrganizer` | formal boundary logic first, then simplified role memo patterns |
| `PROMPT_ASSET_INDEX.md` | `HardlinkOrganizer` | `BIND`, `CTRL` | use HardlinkOrganizer prompt-library shape, BIND prompt interfaces, CTRL handoff artifact naming lessons |
| `CURRENT_STATE.md` | `HardlinkOrganizer` | `CTRL` | use HardlinkOrganizer structure; use CTRL handoff style to keep state grounded in present reality |
| `GOALS.md` | `HardlinkOrganizer` | `StarlightDaemonDev` | use embedded-instance goals separation with host-level goal framing where useful |
| `OPEN_LOOPS.md` | `HardlinkOrganizer` | `StarlightDaemonDev` | use loop-driven work intake, but avoid host/product mixing seen in StarlightDaemonDev |
| `DECISIONS.md` | `HardlinkOrganizer` | `BIND` | practical durable decision log plus bounded remediation decision patterns |
| `WORKBOOK.md` | `ARC-RC` | RAIDEN `Source_info/`, `CTRL` | use research-index and knowledge-preservation logic, but simplify and repair drift |
| `SOURCE_HISTORY_INDEX.md` | `ARC-RC` | RAIDEN `Source_info/` | use research/source catalog pattern for retained prototype/source files |
| `TOOLKIT_INDEX.md` | `StarlightDaemonDev` | `BIND`, `HardlinkOrganizer` | host-level tool catalog with sidecar and embedded-instance distinctions |
| `EXCEPTIONS` / drift handling doc | `BIND` | `HardlinkOrganizer` | use drift-report concept, but prefer a simpler normalized exception record |

## 4. Merge Patterns, Not Winners

Some areas should not have a single winner.

### 1. Governance maturity model

Merge:

- `Starlight Architect` integration thinking
- `BIND` vendored kit -> CI gatekeeper -> managed package path
- `HardlinkOrganizer` proof that a local embedded instance can stay practical

### 2. Artifact hierarchy

Merge:

- `StarlightDaemonDev` root workspace structure
- `CTRL` explicit local artifact split
- `HardlinkOrganizer` clean internal control-plane separation

### 3. Agent role definitions

Merge:

- `Starlight Architect` formal boundary logic
- `ARC`/`ARC-RC` simple mission-statement and forbidden-action tables
- `HardlinkOrganizer` practical startup/read-order control

### 4. Prompt and handoff surfaces

Merge:

- `BIND` standard handoff/completion prompts
- `HardlinkOrganizer` prompt-library layout
- `CTRL` current-state and local handoff artifacts

## 5. Historical-Only Or Cautionary Sources

These patterns should remain historical reference or be used only with strong caution.

| Source | Keep As | Reason |
|---|---|---|
| `Starlight Architect` Carbon-specific governance prose | historical only | too ecosystem-specific |
| `BIND` duplicate governance kit copies | cautionary | do not reproduce duplicated authority surfaces |
| `StarlightDaemonDev` host ledger dominated by `HardlinkOrganizer` product state | cautionary | shows drift from host role into product role |
| `CTRL` report volume as a default operating model | cautionary | useful history, but too noisy for canon |
| `ARC-RC` docs referencing missing `.agent/` and `.gemini/` paths | cautionary | documentation drift weakens authority |
| `ARC` frontend design standards | historical only | not toolkit-governance material |

## 6. First Canonical RAIDEN Draft Order

### P1-A: authority and structure

1. `SOURCE_OF_TRUTH.md`
2. `REPOSITORY_MAP.md`
3. `AGENT_BOUNDARIES.md`

### P1-B: live continuity set

4. `CURRENT_STATE.md`
5. `GOALS.md`
6. `OPEN_LOOPS.md`
7. `DECISIONS.md`

### P1-C: preservation and prompt support

8. `PROMPT_ASSET_INDEX.md`
9. `WORKBOOK.md`
10. `SOURCE_HISTORY_INDEX.md`
11. `TOOLKIT_INDEX.md`

## 7. Unresolved Synthesis Questions

These questions no longer block P0, but they do affect P1 drafting quality:

1. Should RAIDEN standardize both:
   - a **central toolkit/sidecar package model**
   - and a **repo-local embedded instance model**

2. Should prompt assets live:
   - in a dedicated root prompt area
   - or inside the future toolkit subtree only

3. Should RAIDEN’s exception handling look more like:
   - a simple `EXCEPTIONS.md`
   - or a richer drift-report workflow

4. Should RAIDEN’s source-history pattern preserve:
   - only indexes and reviews
   - or also normalized extracts from `Source_info/`

## 8. P0 Conclusion

P0 synthesis is complete enough to begin P1 drafting.

The working source map is:

- `HardlinkOrganizer` for embedded continuity and prompts
- `Starlight Architect` for original governance architecture and boundaries
- `StarlightDaemonDev` for root workspace structure
- `BIND` for sidecar governance, remote audit, and prompt interfaces
- `CTRL` for artifact policy and current-state handoff discipline
- `ARC` and `ARC-RC` for role memo patterns, research indexing, and producer/consumer boundaries

This should now be treated as the baseline map for RAIDEN canon drafting until a stronger conflicting source is found.
