# HardlinkOrganizer Import Candidates

## Candidate Summary

| Candidate | Source Path | Apparent Function | Proposed RAIDEN Target | Confidence | Notes |
|---|---|---|---|---|---|
| Embedded ledger directory shape | `agent-ledger/` | Repo-local control plane | future downstream embedded-instance model | High | strongest practical example in current repo set |
| Agent startup guide pattern | `AGENTS.md` | Agent read order and authority declaration | `AGENT_BOUNDARIES.md` or downstream startup template | High | normalize away absolute root paths |
| Ledger index pattern | `agent-ledger/README.md` | Local control-plane entrypoint | downstream ledger `README.md` template | High | concise and effective |
| File-role separation | `CURRENT_STATE.md`, `GOALS.md`, `OPEN_LOOPS.md`, `DECISIONS.md`, `WORK_LOG.md` | Durable separation of concerns | future embedded-instance artifact set | High | one of the repo’s strongest reusable traits |
| Minimal ledger standard | `agent-ledger/AGENT_LEDGER_STANDARD.md` | Evidence/provenance/loop/terms baseline | future RAIDEN downstream standard | Medium-high | useful, but may need supplementation |
| Governance short form | `agent-ledger/GOVERNANCE.md` | Read-only governance layer | future downstream governance template | Medium-high | practical, but intentionally light |
| Terms registry pattern | `agent-ledger/TERMS.md` | Terminology control | future downstream `TERMS.md` template | High | good balance of brevity and usefulness |
| Exceptions scaffold | `agent-ledger/EXCEPTIONS.md` | Exception tracking | future downstream `EXCEPTIONS.md` template | Medium | structure present, not stress-tested here |
| Prompt library layout | `agent-prompts/` | Narrow execution support | future `PROMPT_ASSET_INDEX.md` and downstream prompt-library conventions | High | strong bounded-execution pattern |
| Micro dispatch template | `agent-prompts/micro-prompt-template.md` | One-slice agent handoff | reusable prompt asset | High | very portable after path normalization |
| Notes index pattern | `notes/README.md` | Support-note navigation | optional local planning index pattern | Medium | useful but not core canon |

## Promotion Rules

- Promote **structure and roles**, not HardlinkOrganizer product content.
- Strip absolute filesystem path locks and replace them with abstract root placeholders.
- Remove or isolate volatile environment/session assumptions such as model availability.
- Keep extraction-history documents as reference examples, not canonical embedded templates.
- Compare governance and ledger wording against `Starlight Architect` and `StarlightDaemonDev` before final canon decisions.

## Promote Soon

- embedded local control-plane directory shape
- ledger file-role separation
- local control-plane README pattern
- agent startup/read-order pattern
- bounded prompt-library pattern
- micro-prompt dispatch template

## Hold For Comparison

- ledger standard wording
- governance wording
- exception handling wording
- loop granularity conventions

## Merge With Existing RAIDEN Material

- evidence/provenance rules with broader RAIDEN governance drafts
- local embedded-instance concept with existing RAIDEN central/local split thinking
- prompt-library conventions with RAIDEN prompt asset indexing work

## Keep As Historical Reference Only

- Unraid packaging guidance
- Community Apps release material
- hardlink-specific roadmap content
- workspace extraction plan details tied to this repo’s migration context
