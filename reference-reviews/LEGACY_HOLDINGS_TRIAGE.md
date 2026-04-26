# Legacy Holdings Triage

## Purpose

This document records the disposition of lower-priority or legacy snapshot
holdings that were retained under `reference-repos/` during RAIDEN's earlier
broad intake phase but do not all justify promotion into the main
review-extract-retirement workflow used for primary source repos.

This is a review artifact, not root canon.

## Scope

This record covers:

- `Afterglows`
- `Agent Ledger`
- `Nullsector`
- `Stargate`
- `StarlightDaemon`
- `local-vpn-extract`

It does not replace the main retirement handling for primary reviewed sources
such as `HardlinkOrganizer`, `BIND`, `Starlight Architect`,
`StarlightDaemonDev`, `ARC`, or `ARC-RC`.

## Executive Judgment

The legacy holdings split into two groups:

1. low-value legacy snapshots that did not justify ongoing retention and were
   removed by operator direction
2. retained legacy snapshots with a narrow reason to keep them

## Disposition

### Removed By Operator Direction

These snapshots were not intended to remain active evidence sources for RAIDEN
and were removed from `reference-repos/`:

- `Afterglows`
- `Nullsector`
- `local-vpn-extract`
- `Agent Ledger`

Reason:

- low evidence value for current RAIDEN toolkit/governance canon, or no
  meaningful evidence content at all
- no strong ongoing governance or control-plane reuse value
- retention added more search noise than reference value

## Retained For Specific Reason

### `Stargate`

Disposition:

- retired (legacy hold closed 2026-04-24)
- raw snapshot removed

Reason:

- held project-registry, stewardship, and prototype-sprawl control patterns
- these patterns were extracted to `reference-extracts/stargate/`
- raw snapshot was large and no longer justified retention

### `StarlightDaemon`

Disposition:

- retired (legacy hold closed 2026-04-24)
- raw snapshot removed

Reason:

- contained early prompt/audit lineage and project-history residue that matters as historical context
- not a strong active toolkit source
- provenance value is preserved in canonical index docs; raw snapshot no longer needed

## Empty Import — Removed

### `Agent Ledger`

Disposition:

- confirmed empty import; removed

Observed state:

- direct directory check on 2026-04-23 confirmed the imported directory is
  still empty
- no meaningful evidence, no review artifacts, not represented in synthesis

Handling:

- removed from `reference-repos/` on 2026-04-23 after operator approval

## Review Status

This triage was reviewed and updated on 2026-04-24 and is now defensibly closed:

- `Afterglows`, `Nullsector`, `local-vpn-extract`: removed by operator direction
- `Stargate`: extracted relevant registry patterns and retired raw snapshot
- `StarlightDaemon`: retired; provenance preserved in index
- `Agent Ledger`: confirmed empty and removed

All legacy holdings have now been fully closed and the snapshots are removed. See also
`REFERENCE_REPO_DISPOSITION_REGISTER.md` for the unified register.

## Use Rule

Use this document to explain why some lower-priority snapshot holdings were not
promoted into the main retirement workflow and why some were removed or kept
for narrower reasons.

Do not treat this record as a substitute for the main retirement rule used for
the primary reviewed prototype sources.
