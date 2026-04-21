# ARC Import Candidates

## Candidate Summary

| Candidate | Source Path | Apparent Function | Proposed RAIDEN Target | Confidence | Notes |
|---|---|---|---|---|---|
| Role mission statement pattern | `FRONTEND_AGENT.md` | Define one agent role, scope, and goals | future role templates / `AGENT_BOUNDARIES.md` inputs | High | main value of the repo |
| Forbidden actions table | `FRONTEND_AGENT.md` | Explicit out-of-scope guardrails | role-boundary templates | High | concise and reusable |
| Directory ownership map | `FRONTEND_AGENT.md` | Map owned vs read-only paths | role template support material | Medium-high | useful in split-repo systems |
| Producer/consumer sync wording | `FRONTEND_AGENT.md`, `README.md` | Clarify that data comes from upstream repo | downstream embedded-instance guidance | Medium-high | useful for central/local split language |

## Promotion Rules

- Promote the **role-boundary structure**, not ARC’s frontend design specifics.
- Keep this repo classified as a narrow role-pattern source, not a toolkit source.
- Merge only after comparison with stronger agent-boundary artifacts from other repos.

## Promote Soon

- forbidden-actions table pattern
- directory ownership map pattern

## Hold For Comparison

- mission-statement wording
- success-metrics pattern

## Merge With Existing RAIDEN Material

- merge with `AGENT_BOUNDARIES.md` drafting
- compare with `ARC-RC`, `Starlight Architect`, and `HardlinkOrganizer` role rules

## Keep As Historical Reference Only

- ARC frontend design standards
- ARC static-site architecture details
