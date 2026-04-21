# StarlightDaemonDev Import Candidates

## Candidate Summary

| Candidate | Source Path | Apparent Function | Proposed RAIDEN Target | Confidence | Notes |
|---|---|---|---|---|---|
| Root README to ledger startup pattern | `README.md` | Direct operators and agents to the control plane first | root `README.md` guidance and downstream host templates | High | concise and effective |
| Broad host-workspace category layout | top-level directories and `docs/repo-map.md` | Separate docs, inventory, runbooks, tools, packaging, website, templates, and archive | `REPOSITORY_MAP.md` and future RAIDEN workspace conventions | High | strongest host-structure contribution |
| Shallow root ledger shape | `agent-ledger/` | Repo-root continuity and governance layer | RAIDEN host-level state/governance pattern | High | structurally strong even if content drifted |
| Ledger standard short form | `agent-ledger/AGENT_LEDGER_STANDARD.md` | Evidence/provenance/loop baseline | future RAIDEN governance synthesis | Medium-high | compare with `HardlinkOrganizer` wording before canonizing |
| Standards and conventions layer | `docs/standards-and-conventions.md` | Naming, layout, documentation, and publication rules | future `GOVERNANCE` or host standards doc | High | good concise source |
| Repo map separation rules | `docs/repo-map.md` | Shared-vs-tool-scoped boundaries and category roles | `REPOSITORY_MAP.md` and toolkit structure guidance | High | especially useful for packaging and website boundaries |
| Tool catalog intake pattern | `docs/tool-catalog.md` | Classify tools by category, status, safety, inputs, outputs, dependencies | `TOOLKIT_INDEX.md` or host tool catalog pattern | High | strong reusable structure |
| Publication categories | `docs/standards-and-conventions.md`, `docs/tool-catalog.md` | Distinguish `internal-only`, `reusable`, `packaged`, `website-ready` | RAIDEN promotion-state vocabulary | Medium-high | useful classification layer |
| Inventory and runbook domain split | `inventory/README.md`, `runbooks/README.md` | Separate environment facts from procedures | future host support-artifact conventions | Medium-high | good category model, lightly exercised here |
| Archive and website category split | `archive/README.md`, `website/README.md` | Keep historical material apart from public-facing material | RAIDEN host structure conventions | Medium-high | useful for future repo hygiene |

## Promotion Rules

- Promote **host structure and category boundaries**, not `Hardlink Organizer` product state.
- Strip bootstrap-session specifics and model-availability notes from anything promoted.
- Do not copy the mixed host-and-product `OPEN_LOOPS.md` pattern into canon without comparison.
- Treat this repo as a **transitional lineage source**, not the final template.

## Promote Soon

- broad host-workspace category layout
- repo-map boundary rules
- standards-and-conventions short form
- root README to ledger startup pattern
- tool-catalog intake schema

## Hold For Comparison

- ledger standard wording
- governance wording
- host-level open-loop structure
- publication-category vocabulary

## Merge With Existing RAIDEN Material

- merge host-workspace layout with RAIDEN root scaffold
- merge ledger structure with `HardlinkOrganizer`’s cleaner embedded-instance pattern
- merge category-boundary logic with `Starlight Architect`’s older hub-level governance concepts

## Keep As Historical Reference Only

- host-level Hardlink Organizer implementation status
- product-specific open loops and decisions
- model-pool notes captured in current state
- imported `.git/` and cache residue from the copied live workspace
