# Starlight Architect Import Candidates

## Candidate Summary

| Candidate | Source Path | Apparent Function | Proposed RAIDEN Target | Confidence | Notes |
|---|---|---|---|---|---|
| Project registry concept | `infrastructure/PROJECTREGISTRY.md` | Canonical portfolio/project index | RAIDEN root navigation / catalog layer | High | foundational ancestor pattern |
| Audit ledger concept | `infrastructure/AUDITLEDGER.md` | Central audit status tracking | RAIDEN state-tracking model | High | likely concept source for later ledger thinking |
| Handoff queue concept | `infrastructure/HANDOFFQUEUE.md` | Cross-agent routing queue | RAIDEN open-work / routing patterns | Medium-high | compare against `OPEN_LOOPS` model |
| Exported continuity report | `reports/ECOSYSTEM_HANDOFF.md` | Portable system-of-record snapshot | RAIDEN handoff/export artifact pattern | High | strong continuity idea |
| Agent boundary model | `infrastructure/HANDSHAKE_PROTOCOL.md` | Cross-domain consent and shared-resource rules | `AGENT_BOUNDARIES.md` and coordination policy | High | one of the strongest reusable abstractions |
| Context-aware audit briefs | `infrastructure/AGENT_AUDIT_BRIEFS.md` | Project-sensitive audit directives | optional context-layer pattern | Medium-high | useful to avoid rigid one-size-fits-all governance |
| Central/local maturity model | `infrastructure/INTEGRATION_STRATEGY.md` | Vendored kit -> CI gate -> managed package evolution | RAIDEN central toolkit vs embedded-instance model | High | key bridge concept |
| Workspace boundary / immutability policy | `infrastructure/PROJECT_LOCATION_RULES.md` | Movement constraints and boundary control | generalized workspace-boundary policy | Medium | useful concept, but path-specific here |
| Subagent workspace maps | `agents/tron/workspace-map.md`, `agents/clu/workspace-map.md` | Agent-local navigation | optional specialized-agent navigation template | Medium | helpful but secondary |

## Promotion Rules

- Promote the **concepts and patterns**, not Starlight-specific identities.
- Strip Carbon-specific, CLU/TRON-specific, and `/mnt/e/`-specific assumptions.
- Normalize naming before promotion; do not carry forward mixed underscore/no-underscore variants.
- Treat report-heavy operational history as evidence, not as the default future RAIDEN workflow.
- Compare all promoted concepts against `HardlinkOrganizer` to determine whether they belong at RAIDEN root level or only in a future central orchestration layer.

## Promote Soon

- project registry concept
- audit ledger concept
- exported continuity handoff artifact concept
- handshake / cross-boundary coordination model
- central/local maturity model from `INTEGRATION_STRATEGY.md`

## Hold For Comparison

- handoff queue vs open loops relationship
- audit-brief context layer
- workspace immutability policy
- subagent workspace-map conventions

## Merge With Existing RAIDEN Material

- merge registry and continuity concepts into RAIDEN root source-of-truth/navigation planning
- merge boundary logic into RAIDEN agent-boundary work
- merge central/local evolution thinking with existing RAIDEN canonical-central-repo framing

## Keep As Historical Reference Only

- literal Starlight project registry contents
- CLU/TRON identity and Carbon-domain prose
- migration backups and acknowledgments
- path-specific immutability rules in their original form
