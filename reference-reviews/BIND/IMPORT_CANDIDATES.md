# BIND Import Candidates

## Candidate Summary

| Candidate | Source Path | Apparent Function | Proposed RAIDEN Target | Confidence | Notes |
|---|---|---|---|---|---|
| Governance sidecar pattern | `.governance/` | Repo-adjacent governance kit and control surface | future RAIDEN sidecar/deployable-kit model | High | strongest sidecar example in current repo set |
| Integration maturity model | `.governance/INTEGRATION_STRATEGY.md` | Vendored kit -> CI gatekeeper -> managed package | RAIDEN toolkit rollout strategy | High | strong cross-repo recurring concept |
| Remote audit protocol | `.governance/REMOTE_AUDIT.md` | Evidence-bundle remote verification | future RAIDEN audit/verification protocol | High | high-value concept |
| Standard handoff prompt | `.governance/HANDOFF_PROMPT.md` | Agent kickoff into governed implementation | prompt asset library | High | portable after terminology cleanup |
| Completion report prompt | `.governance/COMPLETION_REPORT_PROMPT.md` | Standardized closeout artifact generation | prompt asset library | Medium-high | useful but more report-centric |
| Drift report template | `.governance/drift-report-template.md` | Controlled deviation handling | future `EXCEPTIONS` or drift template | Medium-high | good structured exception pattern |
| Validator tool pattern | `.governance/validator/` | Machine-checkable governance evidence | future RAIDEN validation tooling concept | Medium | pattern matters more than implementation |
| Remediation ledger pattern | `docs/remediation/BIND_1.0_REMEDIATION_LEDGER.md` | Narrow issue ledger for release-readiness corrections | optional bounded-work ledger pattern | Medium-high | useful alternative to full ledger |
| Release decision artifact | `docs/remediation/BIND_1.0_RELEASE_DECISIONS.md` | Scoped decision log | decision-log pattern | Medium | narrower than full repo decisions |

## Promotion Rules

- Promote **structure and protocol**, not Carbon-specific design rules.
- Prefer a single canonical home for any governance kit; do not inherit BIND's duplication across live, script, and reference copies.
- Treat report-heavy certification artifacts as optional support surfaces, not default RAIDEN workflow.
- Normalize Starlight-specific role labels before reuse.

## Promote Soon

- sidecar governance-kit concept
- integration maturity model
- remote audit protocol
- handoff prompt pattern

## Hold For Comparison

- completion report pattern
- drift report template
- validator tooling shape
- remediation-ledger conventions

## Merge With Existing RAIDEN Material

- merge maturity model with `Starlight Architect` lineage
- merge sidecar prompt interface with `CTRL` handoff/report discipline
- merge audit/evidence concept with RAIDEN governance drafting

## Keep As Historical Reference Only

- Carbon token files and design-compliance specifics
- BIND release-readiness and remediation history
- duplicated governance kit copies under `docs/reference/` and `scripts/`
