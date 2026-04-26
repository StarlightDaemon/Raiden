# Reference Repo Disposition Register

## Purpose

This register gives every repo that was ever imported into `reference-repos/`
a single-line disposition status.

It exists so that the retirement-review effort has one defensible summary
artifact showing no retained repo is left in an undefined state.

This is a review artifact, not root canon.

## Governing Rule

Retirement eligibility follows `SNAPSHOT_RETIREMENT_RULE.md`.
Legacy holdings follow `LEGACY_HOLDINGS_TRIAGE.md`.

## Register Date

2026-04-23

## Disposition Key

| State | Meaning |
|---|---|
| Retired | Full snapshot removed from `reference-repos/`; reviews, extracts, and synthesis retained |
| Retirement-eligible | All retirement criteria met except operator approval; recommend retirement |
| Retained (State 2) | Extract exists; full snapshot still retained for a stated reason |
| Retained (State 1) | Full snapshot retained; no extract yet; specific blocker identified |
| Legacy hold | Retained outside the primary retirement workflow for a narrow stated reason |
| Removed (legacy) | Low-value snapshot removed by operator direction |
| Empty / unresolved | Imported directory with no meaningful content |

## Primary Reviewed Sources

These repos went through the primary reviewed-source workflow.
They are now all retired.

| Repo | Review | Candidates | Synthesis | Extract | Disposition | Reason |
|---|---|---|---|---|---|---|
| `CTRL` | Yes | Yes | Yes | Yes | **Retired** | Retired 2026-04-23 after review, extraction, and operator approval satisfied all 7 retirement criteria |
| `HardlinkOrganizer` | Yes | Yes | Yes | Yes | **Retired** | Retired 2026-04-23 after operator approval; extract set preserves embedded-instance, continuity, prompt, and startup patterns |
| `BIND` | Yes | Yes | Yes | Yes | **Retired** | Retired 2026-04-23 after operator approval; extract set preserves governance sidecar, maturity model, remote audit, prompt interface, and remediation patterns |
| `ARC` | Yes | Yes | Yes | No | **Retired** | Retired 2026-04-23 after operator approval; extraction was unnecessary because the repo's narrow role-boundary value is already represented in canon |
| `ARC-RC` | Yes | Yes | Yes | No | **Retired** | Retired 2026-04-23 after operator approval; extraction was unnecessary because the repo's narrow role-memo and research-index value is already represented in canon |
| `Starlight Architect` | Yes | Yes | Yes | No | **Retired** | Retired 2026-04-24 after operator approval; no extract needed because canon and review artifacts already preserve its RAIDEN-relevant governance, registry, handoff, boundary, and central/local maturity concepts |
| `StarlightDaemonDev` | Yes | Yes | Yes | No | **Retired** | Retired 2026-04-24 after operator approval; no extract needed because canon and review artifacts already preserve its RAIDEN-relevant host-workspace structure, category boundaries, repo-map conventions, startup patterns, and tool-catalog concepts |

## Legacy Holdings

These repos were retained outside the primary retirement workflow.
They do not have per-repo `REPO_TOOLING_REVIEW.md` or `IMPORT_CANDIDATES.md`
and are not represented in the primary synthesis maps.

| Repo | Broad Review Coverage | Legacy Triage | Disposition | Reason |
|---|---|---|---|---|
| `Stargate` | Yes (HIGH_LEVEL_OVERVIEW, ALL_REPOS_EXPANDED_REVIEW) | Yes | **Retired** | Retired 2026-04-24 after extracting registry, stewardship, and prototype-sprawl control patterns to `reference-extracts/stargate/` |
| `StarlightDaemon` | Yes (HIGH_LEVEL_OVERVIEW, ALL_REPOS_EXPANDED_REVIEW) | Yes | **Retired** | Retired 2026-04-24; provenance value preserved in index docs; raw snapshot no longer needed |
| `Agent Ledger` | Yes (HIGH_LEVEL_OVERVIEW, ALL_REPOS_EXPANDED_REVIEW) | Yes | **Removed (legacy)** | Removed 2026-04-23 after verification confirmed the imported directory was empty and held no evidence content |

## Already Removed

These repos were removed from `reference-repos/` by operator direction during
earlier triage passes.

| Repo | Removal Reason | Date |
|---|---|---|
| `Afterglows` | Low evidence value; no strong governance/control-plane reuse value | 2026-04-23 |
| `Nullsector` | Low evidence value; no governance-tooling artifacts | 2026-04-23 |
| `local-vpn-extract` | Very low evidence value; narrow utility extract | 2026-04-23 |
| `Agent Ledger` | Empty import; no evidence content to preserve | 2026-04-23 |

## Retirement-Readiness Summary

| Category | Count |
|---|---|
| Already retired | 9 (`CTRL`, `HardlinkOrganizer`, `BIND`, `ARC`, `ARC-RC`, `Starlight Architect`, `StarlightDaemonDev`, `Stargate`, `StarlightDaemon`) |
| Legacy hold | 0 |
| Already removed (legacy) | 4 (`Afterglows`, `Nullsector`, `local-vpn-extract`, `Agent Ledger`) |
| **Total repos ever imported** | **13** |

## What Blocks Full Closure

The primary retirement-review effort is now fully closed.

All 7 primary reviewed sources and 2 legacy holds are now retired. No repo remains in an
undefined or blocked state.

The earlier operator approvals for `HardlinkOrganizer`, `BIND`, `ARC`,
`ARC-RC`, and empty `Agent Ledger` were executed on 2026-04-23. Operator
approval for `Starlight Architect` and `StarlightDaemonDev` was executed on
2026-04-24.

## Reassessment Notes (2026-04-23)

### Why HardlinkOrganizer and BIND are now retirement-eligible

The earlier retirement assessment (2026-04-18) judged both repos as "not
ready" primarily because:

- active toolkit-surface and updater work made raw reread still plausible
- some comparison material was intentionally held rather than fully extracted

Since then:

- updater work has been explicitly deferred by operator direction
- extract sets were created and reviewed for both repos
- no open loop currently depends on rereading either raw snapshot
- the canonical toolkit surface has advanced past the comparison stage where
  raw reread was actively needed

The remaining marginal reread value (governance wording comparison, terms
control, drift-report structure details) does not justify indefinite retention
given that the extracts and canon now preserve the primary patterns.

### Why ARC and ARC-RC are retirement-eligible without extracts

Both repos contribute narrow, well-defined patterns (role boundaries,
research indexing, producer/consumer splits) that were fully absorbed into
RAIDEN canon during synthesis. Their value does not depend on detailed
structural patterns that would warrant a separate extract set. The
combination of:

- per-repo `REPO_TOOLING_REVIEW.md`
- per-repo `IMPORT_CANDIDATES.md`
- `CROSS_REPO_MATRIX.md` representation
- `CANONICAL_SOURCE_MAP.md` representation
- canon coverage in `AGENT_BOUNDARIES.md` and `SOURCE_HISTORY_INDEX.md`

preserves their full contribution to RAIDEN without needing the raw snapshots.

### Why Starlight Architect is retirement-eligible without extracts (2026-04-23)

`Starlight Architect` contributes original governance architecture, registry,
audit-ledger, handoff, boundary, and central/local maturity concepts. All of
these concepts were absorbed into RAIDEN canon during the synthesis and
canon-drafting phase:

- registry → `REPOSITORY_MAP.md` navigation/catalog model
- audit ledger → RAIDEN continuity and state-tracking model
- handoff/continuity export → RAIDEN handoff and continuity artifacts
- agent boundaries/handshake → `AGENT_BOUNDARIES.md`
- central/local maturity (vendored kit → CI → package) → `MANAGED_VS_LOCAL.md`
  and the Edict/Writ/RAIDEN Instance model

The remaining raw-snapshot value is ancestral historical detail (ecosystem-
specific governance prose, Carbon-domain content, literal CLU/TRON roles,
path-specific rules) that was explicitly flagged as "retain as reference only"
or "historical only" in the IMPORT_CANDIDATES and CANONICAL_SOURCE_MAP.

The combination of:

- per-repo `REPO_TOOLING_REVIEW.md` (308 lines of detailed review)
- per-repo `IMPORT_CANDIDATES.md` (52 lines of structured candidates)
- `CROSS_REPO_MATRIX.md` representation
- `CANONICAL_SOURCE_MAP.md` representation (primary source for 3 concept rows)
- `ALL_REPOS_EXPANDED_REVIEW.md` and `HIGH_LEVEL_OVERVIEW.md` coverage
- canon coverage in `AGENT_BOUNDARIES.md`, `MANAGED_VS_LOCAL.md`,
  `REPOSITORY_MAP.md`, `SOURCE_OF_TRUTH.md`, and `DECISIONS.md`

preserves the full RAIDEN-relevant contribution without needing the raw
snapshot or a separate extract set.

### Why StarlightDaemonDev is retirement-eligible without extracts (2026-04-23)

`StarlightDaemonDev` contributes host/meta-workspace structure, category
boundary rules, tool-catalog patterns, root-readme-to-ledger startup, and
publication-category thinking. All of these concepts were absorbed into RAIDEN
canon during synthesis:

- host-workspace category layout → `REPOSITORY_MAP.md`
- repo-map boundary rules → `REPOSITORY_MAP.md`
- standards and conventions → RAIDEN root governance model
- root-readme-to-ledger startup → `AGENTS.md` bridge model in
  `toolkit/instance/`
- tool-catalog intake schema → `TOOLKIT_INDEX.md`

The remaining raw-snapshot value is:

- Hardlink Organizer product-specific state recorded at host level
- bootstrap-thin category scaffolds (templates, website, inventory placeholders)
- model-pool and session-specific operational notes
- imported VCS/runtime residue

All of these were explicitly flagged as "retain as reference only" or
"mostly repo-specific or historical" in the review artifacts.

The combination of:

- per-repo `REPO_TOOLING_REVIEW.md` (291 lines of detailed review)
- per-repo `IMPORT_CANDIDATES.md` (52 lines of structured candidates)
- `CROSS_REPO_MATRIX.md` representation
- `CANONICAL_SOURCE_MAP.md` representation (primary source for 2 concept rows)
- `ALL_REPOS_EXPANDED_REVIEW.md` and `HIGH_LEVEL_OVERVIEW.md` coverage
- canon coverage in `REPOSITORY_MAP.md`, `TOOLKIT_INDEX.md`,
  `toolkit/instance/`, and `DECISIONS.md`

preserves the full RAIDEN-relevant contribution without needing the raw
snapshot or a separate extract set.
