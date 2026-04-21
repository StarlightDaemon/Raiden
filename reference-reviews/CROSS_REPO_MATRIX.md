# Cross Repo Matrix

Use this file to compare reviewed prototype repos by function before promoting patterns into RAIDEN canon.

| Repo | Source Of Truth Model | State Tracking | Decisions / Logging | Prompt Governance | Agent Boundaries | Navigation | Reusable Candidate Strength | Notes |
|---|---|---|---|---|---|---|---|---|
| `HardlinkOrganizer` | local embedded control plane via `AGENTS.md` + `agent-ledger/` | strong multi-file ledger | strong `DECISIONS.md` + `WORK_LOG.md` | strong via `agent-prompts/` | medium-high | strong | Very High | best current embedded-instance model |
| `Starlight Architect` | ecosystem rules + registry/audit/handoff hub | strong, hub-style | strong, report-heavy | medium | very high | medium-high | Very High | original conceptual governance prototype |
| `StarlightDaemonDev` | root README -> local `agent-ledger/` | medium-high | high | low | medium | very high | High | strongest host/meta-workspace scaffold, but drifted |
| `BIND` | product README + `.governance/` sidecar | medium, mostly remediation/report based | medium-high | very high | medium | medium | High | strongest sidecar governance-kit pattern |
| `CTRL` | product docs + thin local `agent-ledger/` + `reports/` | medium, split across local notes and reports | medium-high | high, but scattered | medium | high | High | strongest artifact-policy and handoff-discipline source |
| `ARC-RC` | role file + work rules + research index | low-medium | low-medium | medium | high | medium-high | Medium | strong producer/research role and research-index pattern |
| `ARC` | role memo + product README | low | low | low | medium-high | low-medium | Medium-low | narrow frontend role-boundary source |

## Synthesis Notes

- Compare by function, not file naming alone.
- No single repo should be copied wholesale into RAIDEN canon.
- Current primary concept winners are:
  - embedded local control plane: `HardlinkOrganizer`
  - original governance architecture: `Starlight Architect`
  - host/meta-workspace structure: `StarlightDaemonDev`
  - sidecar governance + remote audit: `BIND`
  - artifact policy + handoff discipline: `CTRL`
  - role memo and producer/consumer boundary patterns: `ARC`, `ARC-RC`

## Excluded From Primary Canon Map

These repos were scanned earlier but are not currently primary source candidates:

- `Afterglows`
- `Nullsector`
- `local-vpn-extract`
- `Stargate`
- `StarlightDaemon`
- `Agent Ledger` (empty or unresolved import)
