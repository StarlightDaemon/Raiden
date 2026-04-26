# Source History Index

## Purpose

This file indexes preserved source-history materials that informed RAIDEN canon.

It exists to:

- preserve provenance
- reduce the need to keep re-reading raw source material
- make clear what is retained, why it is retained, and whether it is authoritative

Nothing indexed here is canonical by default unless a root-level RAIDEN document explicitly adopts it.

## 1. Preserved Root Source History

These files live under `Source_info/` and are retained as early RAIDEN source material.

| File | Current Role | Status | Canonicality | Notes |
|---|---|---|---|---|
| `Source_info/Agent Ledger Development.md` | toolkit architecture source | Retained | Non-canonical | contains scaffold, naming, and central/local split proposals |
| `Source_info/Repo-wide Governance Review.md` | ledger/toolkit design source | Retained | Non-canonical | richest mixed source document; strong but noisy |
| `Source_info/Governance Document Review.md` | governance protocol source | Retained | Non-canonical | strong source for prompt-governance and protocol ideas |
| `Source_info/Programming Chat Instructions.md` | prompt-discipline source | Retained | Non-canonical | concise operational guardrail material |
| `Source_info/Orchestration Agent Planning.md` | orchestrator-role prototype | Retained | Non-canonical | useful role-boundary lineage |
| `Source_info/Architect Ghost.md` | advisory-role prototype | Retained | Non-canonical | useful for boundary patterns only |
| `Source_info/deep-research-report (2).md` | safeguard/control critique | Retained | Non-canonical | useful control critique; contains external formatting residue |
| `Source_info/Raiden Agent Clarity.md` | identity/role-definition source | Retained | Non-canonical | defines present-day RAIDEN vs future RAIDEN; intended for RAIDEN concept formation, not downstream work |
| `Source_info/Raiden Foundational Operating Brief Prompt.md` | mission and efficiency-constraint source | Retained | Non-canonical | strong source for why RAIDEN exists, token/budget constraints, and infrastructure-first operating intent |

## 2. Reviewed Prototype Sources

These repos were imported into `reference-repos/` and assessed through RAIDEN reviews.

They are preserved as evidence sources, not canon.

| Repo | Current Review Status | Primary Relevance | Extract Status | Retirement Status |
|---|---|---|---|---|
| `HardlinkOrganizer` | Reviewed | embedded local control plane and prompt-library structure | extract set created | full snapshot retired 2026-04-23; extracted references retained |
| `Starlight Architect` | Reviewed | original governance architecture and formal boundary logic | not needed (value preserved in canon and review artifacts) | full snapshot retired 2026-04-24; no extract needed |
| `StarlightDaemonDev` | Reviewed | host/meta-workspace structure | not needed (value preserved in canon and review artifacts) | full snapshot retired 2026-04-24; no extract needed |
| `BIND` | Reviewed | governance sidecar, remote audit, prompt interfaces | extract set created | full snapshot retired 2026-04-23; extracted references retained |
| `CTRL` | Reviewed | artifact policy and handoff discipline | pilot extraction created | full snapshot retired 2026-04-23; extracted references retained |
| `ARC` | Reviewed | simple role-boundary pattern | not needed (narrow value in canon) | full snapshot retired 2026-04-23; no extract needed |
| `ARC-RC` | Reviewed | research-index and producer/consumer boundary pattern | not needed (narrow value in canon) | full snapshot retired 2026-04-23; no extract needed |
| `Stargate` | Scanned (broad reviews only) | project-registry and stewardship patterns | extract set created | full snapshot retired 2026-04-24; extracted references retained |
| `StarlightDaemon` | Scanned (broad reviews only) | historical prompt/audit lineage | not needed (mostly provenance) | full snapshot retired 2026-04-24; no extract needed |
| `Agent Ledger` | Scanned (broad reviews only) | none (empty import) | n/a | removed 2026-04-23 after empty import was confirmed |
| `Afterglows` | Scanned (broad reviews only) | low evidence value | n/a | removed by operator direction 2026-04-23 |
| `Nullsector` | Scanned (broad reviews only) | low evidence value | n/a | removed by operator direction 2026-04-23 |
| `local-vpn-extract` | Scanned (broad reviews only) | very low evidence value | n/a | removed by operator direction 2026-04-23 |

Primary reviewed sources have per-repo `REPO_TOOLING_REVIEW.md` and `IMPORT_CANDIDATES.md`
under `reference-reviews/`. Legacy holdings are tracked in
`reference-reviews/LEGACY_HOLDINGS_TRIAGE.md`. The unified register is at
`reference-reviews/REFERENCE_REPO_DISPOSITION_REGISTER.md`.

## 3. Extracted References

The extracted-reference layer preserves high-value reusable patterns in smaller RAIDEN-owned documents after review.

Current extracted-reference coverage:

| Extract Folder | Source Repo | Current Role | Canonicality |
|---|---|---|---|
| `reference-extracts/ctrl/` | `CTRL` | pilot extraction for artifact policy, handoff, and structure guidance | Non-canonical |
| `reference-extracts/hardlinkorganizer/` | `HardlinkOrganizer` | extracted references for embedded-instance structure, continuity roles, prompts, and startup guidance | Non-canonical |
| `reference-extracts/bind/` | `BIND` | extracted references for governance sidecar, remote audit, maturity model, prompt interface, and remediation patterns | Non-canonical |
| `reference-extracts/stargate/` | `Stargate` | extracted references for registry and stewardship pattern | Non-canonical |

These extracts are a bridge layer:

- narrower than raw prototype snapshots
- more durable than ad hoc review notes
- still subordinate to root canon

## 4. Review Artifacts

The main durable review/synthesis surfaces are:

- `reference-reviews/HIGH_LEVEL_OVERVIEW.md`
- `reference-reviews/ALL_REPOS_EXPANDED_REVIEW.md`
- per-repo `REPO_TOOLING_REVIEW.md`
- per-repo `IMPORT_CANDIDATES.md`
- `reference-reviews/CROSS_REPO_MATRIX.md`
- `reference-reviews/CANONICAL_SOURCE_MAP.md`

These are not root canon by default, but they are the main bridge between raw evidence and adopted canon.

## 5. Promotion Rules

A source-history item is retained for one or more of these reasons:

- provenance
- unresolved comparison value
- potential future extraction
- historical explanation of why RAIDEN canon looks the way it does

A source-history item should not be treated as live authority just because:

- it is detailed
- it is earlier
- it was once used in another repo
- it contains a more elaborate process than current canon

## 6. Retirement Intent

Source-history retention is intentional, but not necessarily permanent.

For imported prototype snapshots, retirement should be based on `SNAPSHOT_RETIREMENT_RULE.md`.
Initial intake and review handling should follow `INGRESS_POLICY.md`.

For `Source_info/`, retention should continue until RAIDEN is confident that:

- provenance value is preserved
- canonical extracts are stable
- no unresolved synthesis question depends on rereading the originals

## 7. Current Practical Reading

If an agent needs:

- raw early RAIDEN thought lineage: start in `Source_info/`
- structured comparison of reviewed prototypes: start in `reference-reviews/`
- compact preserved prototype patterns: start in `reference-extracts/`
- actual current authority: return to root canonical docs
