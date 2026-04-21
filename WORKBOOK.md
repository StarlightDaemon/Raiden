# Workbook

This file is the active synthesis workspace for turning preserved source history and reviewed prototype repos into canonical RAIDEN artifacts.

## Current Focus

- keep the root continuity layer aligned with actual progress
- turn the conceptual toolkit model into a concrete subtree or package surface when ready
- continue release-readiness preparation work before updater canon resumes
- use `RELEASE_READY_CHECKLIST.md` to track what still blocks updater canon

## Current Phase

RAIDEN is in the **canonicalization phase**.

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

Current phase work:

- expand the initial `toolkit/` subtree without freezing unresolved updater metadata too early
- materialize toolkit/component structure using the adopted `RAIDEN` / `RAIDEN Instance` / `Edict` naming model
- keep future external repo intake narrow and policy-driven rather than repeating broad early snapshot imports

Temporarily on hold:

- the first practical updater approach remains an open work block, but active updater implementation planning is paused for now
- prepared non-canonical working artifacts live under `working/updater-system/`
- current operator direction is to keep updater-shape work deferred until RAIDEN is substantially closer to release-ready toolkit/package state

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
  - `RAIDEN Instance` = downstream deployed form
  - `Edict` = managed core artifact

## Active Unresolved Questions

- Which reviewed repos are now good candidates for retirement readiness assessment?
- Which release-readiness preparation tasks still need completion before updater canon should resume?
