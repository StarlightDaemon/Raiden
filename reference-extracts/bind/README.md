# BIND Extracts

## Purpose

This folder contains RAIDEN-owned extracted references taken from `BIND`.

The goal is to preserve the parts of `BIND` that matter to RAIDEN without
keeping the full product snapshot as the preferred reread surface for
governance-sidecar, remote-audit, and maturity-model patterns.

## Current Extract Set

| File | Pattern | Status |
|---|---|---|
| `governance-sidecar-pattern.md` | repo-adjacent governance kit and authority surface | Active |
| `integration-maturity-model-pattern.md` | vendored kit to CI gatekeeper to managed package path | Active |
| `remote-audit-pattern.md` | evidence-bundle remote verification flow | Active |
| `prompt-interface-pattern.md` | governed handoff and completion prompt interface | Active |
| `bounded-remediation-ledger-pattern.md` | narrow issue ledger for release-readiness corrections | Active |

## Source Provenance

Primary source files:

- `reference-repos/BIND/.governance/README.md`
- `reference-repos/BIND/.governance/INTEGRATION_STRATEGY.md`
- `reference-repos/BIND/.governance/REMOTE_AUDIT.md`
- `reference-repos/BIND/.governance/HANDOFF_PROMPT.md`
- `reference-repos/BIND/.governance/COMPLETION_REPORT_PROMPT.md`
- `reference-repos/BIND/.governance/drift-report-template.md`
- `reference-repos/BIND/docs/remediation/BIND_1.0_REMEDIATION_LEDGER.md`

Supporting interpretation:

- `reference-reviews/BIND/REPO_TOOLING_REVIEW.md`
- `reference-reviews/BIND/IMPORT_CANDIDATES.md`

## Current Retirement Status

- extracted references now exist
- the full `BIND` snapshot remains retained for now
- `BIND` is not yet retired from `reference-repos/`

This folder moves `BIND` into the extracted-reference stage, but not yet full
retirement.
