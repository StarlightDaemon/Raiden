# Workbook

This file is the active synthesis workspace for turning preserved source history and reviewed prototype repos into canonical RAIDEN artifacts.

## Current Focus

- keep the root continuity layer aligned with actual progress
- keep the concrete toolkit, instance, and updater surfaces aligned with canon
- keep broader updater metadata, downgrade, prerelease/build, and distribution
  questions deferred until real downstream usage provides evidence
- use `RELEASE_READY_CHECKLIST.md` to preserve the release-prep threshold that
  allowed the current local CLI updater work to proceed

## Current Phase

RAIDEN is in the **canonicalization and release-preparation phase**.

Completed phase work:

- root scaffold creation
- prototype intake
- per-repo reviews
- cross-repo synthesis
- P1-A authority and structure docs
- P1-B continuity canon refresh
- first support-layer canon
- prototype snapshot retirement rule
- first extracted-reference pilot
- pre-intake gate added to `INGRESS_POLICY.md` so future external repo intake
  stays bounded by a concrete go/no-go check rather than ad hoc import habit

Current phase work:

- maintain the promoted `RAIDEN` / `Edict` / `RAIDEN Instance` / `Writ`
  surface without broadening package or distribution canon prematurely
- keep future evidence intake narrow and policy-driven

Temporarily on hold:

- broader updater metadata extensions
- downgrade policy and prerelease/build version metadata
- package archive, publishing, and remote distribution mechanics

## Reviewed Prototype Coverage

Completed reviews:

- `HardlinkOrganizer`
- `Starlight Architect`
- `StarlightDaemonDev`
- `BIND`
- `CTRL`
- `ARC`
- `ARC-RC`

Strongest current source assignments are recorded in:

- `reference-reviews/CANONICAL_SOURCE_MAP.md`
- `reference-reviews/CROSS_REPO_MATRIX.md`

## Live Synthesis Notes

- `HardlinkOrganizer` is the best practical embedded-instance reference.
- `Starlight Architect` is the best original governance-architecture reference.
- `StarlightDaemonDev` is the best host/meta-workspace structure reference.
- `BIND` is the best governance-sidecar and remote-audit reference.
- `CTRL` is the best artifact-policy and handoff-discipline reference.
- `ARC` and `ARC-RC` are supporting role-boundary and research-index references.
- current naming stack is:
  - `RAIDEN` = central governing agent
  - `Edict` = central managed instruction/package surface
  - `RAIDEN Instance` = downstream deployed form
  - `Writ` = installed managed core artifact

## Active Unresolved Questions

- Which broader updater metadata extensions are justified by real downstream
  usage?
- Which package/distribution mechanics should remain deferred until there is a
  concrete release need?
