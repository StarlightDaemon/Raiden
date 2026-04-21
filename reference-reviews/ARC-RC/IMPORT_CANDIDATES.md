# ARC-RC Import Candidates

## Candidate Summary

| Candidate | Source Path | Apparent Function | Proposed RAIDEN Target | Confidence | Notes |
|---|---|---|---|---|---|
| Backend/research role memo | `DEVELOPER_AGENT.md` | Define backend research agent scope and forbidden actions | role templates / `AGENT_BOUNDARIES.md` inputs | High | strong counterpart to ARC |
| Agent work rules | `docs/research/AGENT-RULES.md` | Local rules for token use, copy-paste hygiene, research handling | optional RAIDEN operator/agent workflow guidance | High | useful but context-specific |
| Research index pattern | `docs/research/RESEARCH-INDEX.md` | Preserve research, decisions, and implementation knowledge | `SOURCE_HISTORY_INDEX.md`, `WORKBOOK.md`, or research index patterns | High | one of the better research-index examples |
| Research docs hub | `docs/research/README.md` | Navigation into knowledge base | optional research navigation pattern | Medium-high | useful despite drift |
| Output-zone boundary | `output/`, `README.md` | Separate generated deliverables from tooling internals | central/local export boundary guidance | Medium-high | strong producer/consumer pattern |
| Schema plus sync bridge | `schemas/product-collection.schema.json`, `.github/workflows/sync-to-catalog.yml` | Formal contract and downstream sync | contract + sync pattern | Medium-high | useful conceptually |
| Targeted audit artifact | `docs/policies/HARDCODED-AUDIT.md` | Narrow audit of hardcoded/drift issues | specialized audit template | Medium | good focused audit style |

## Promotion Rules

- Promote the **patterns** for role definition, research indexing, and export boundaries, not ARC-specific research operations.
- Do not promote any documentation that depends on missing `.agent/` or `.gemini/` paths without repair.
- Treat token-efficiency rules as optional operational guidance, not canonical governance, unless they survive comparison with other repos.

## Promote Soon

- backend/research role memo pattern
- research-index pattern
- output-zone boundary pattern

## Hold For Comparison

- agent work-rules document
- schema plus sync bridge pattern
- targeted audit style

## Merge With Existing RAIDEN Material

- merge role memo with `ARC` and broader agent-boundary drafting
- merge research-index ideas with RAIDEN source-history and workbook artifacts
- compare artifact-hygiene rules with `CTRL` and `BIND`

## Keep As Historical Reference Only

- ARC accessory research workflows
- n8n implementation specifics
- environment-specific backup guidance
- docs that rely on missing `.agent/` and `.gemini/` sidecars
