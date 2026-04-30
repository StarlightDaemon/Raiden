# Current State

## Summary

RAIDEN is now in the **first downstream deployment phase**.

The repo has moved past initial intake and broad prototype comparison. Authority order is defined, reviewed prototype patterns are synthesized, and the first canonical root governance/navigation layer is in place.

RAIDEN is not yet a finished toolkit implementation. It is currently a structured central framework repo with:

- preserved source history
- completed prototype evidence review and retirement
- completed cross-repo synthesis
- initial canonical root docs
- completed continuity canon
- completed first support-layer canon
- a defined prototype snapshot retirement rule
- an initial extracted-reference layer
- an initial canonical toolkit subtree

## Confirmed Current State

- `RAIDEN` is the canonical central toolkit/framework repository.
- `Source_info/` is preserved source history, not active canon.
- imported prototype repos under `reference-repos/` are treated as read-only evidence by process.
- per-repo reviews now exist for:
  - `HardlinkOrganizer`
  - `Starlight Architect`
  - `StarlightDaemonDev`
  - `BIND`
  - `CTRL`
  - `ARC`
  - `ARC-RC`
- P0 synthesis is complete in:
  - `reference-reviews/CROSS_REPO_MATRIX.md`
  - `reference-reviews/CANONICAL_SOURCE_MAP.md`
- P1-B continuity canon is complete:
  - `CURRENT_STATE.md`
  - `GOALS.md`
  - `OPEN_LOOPS.md`
  - `DECISIONS.md`
- P1-A canonical docs are complete:
  - `SOURCE_OF_TRUTH.md`
  - `REPOSITORY_MAP.md`
  - `AGENT_BOUNDARIES.md`
- the canonical mission-and-operating-intent layer now exists in:
  - `OPERATING_INTENT.md`
- external evidence intake is now governed by `INGRESS_POLICY.md`, including a pre-intake go/no-go gate (§0) that requires a bounded design reason before any import
- the managed-vs-local update boundary is now defined in `MANAGED_VS_LOCAL.md`
- support-layer canon now includes:
  - `ARTIFACT_AUDIENCE.md`
  - `PROMPT_ASSET_INDEX.md`
  - `SOURCE_HISTORY_INDEX.md`
  - `TOOLKIT_INDEX.md`
- central prompt governance now includes a readable-versus-compressed surface rule and compact internal execution templates under `toolkit/prompts/`
- the default downstream `RAIDEN Instance` folder structure is now defined under `toolkit/instance/`
- the release-preparation gate is now defined in `RELEASE_READY_CHECKLIST.md`
- the first explicit canonical toolkit subtree now exists under `toolkit/`
- a consolidated past/current/future planning view now exists in `PAST_PRESENT_FUTURE.md`
- prototype snapshot retirement is now governed by `SNAPSHOT_RETIREMENT_RULE.md`
- `reference-extracts/` now exists as a compact non-canonical extracted-reference layer
- `CTRL` has the first pilot extracted-reference set under `reference-extracts/ctrl/`
- `CTRL` has now been fully retired from `reference-repos/` after extraction preserved its reusable RAIDEN value
- `HardlinkOrganizer` now has extracted references under `reference-extracts/hardlinkorganizer/`
- `BIND` now has extracted references under `reference-extracts/bind/`
- `HardlinkOrganizer`, `BIND`, `ARC`, and `ARC-RC` have now been fully retired from `reference-repos/` after review/disposition closure and operator approval
- empty `Agent Ledger` has now been removed from `reference-repos/` after verification confirmed it held no evidence value
- downstream naming is now fixed:
  - `RAIDEN` = central governing agent
  - `Edict` = central managed instruction/package surface
  - `RAIDEN Instance` = downstream deployed form
  - `Writ` = installed managed core artifact
- the initial toolkit/package surface has been deepened to reduce release ambiguity without overcommitting unresolved updater details
- the minimum canonical installed `Writ` payload is explicitly defined, providing a stable managed-core target for later updater canon
- the first updater MVP now exists under `toolkit/updater/` as a local CLI with `plan` and `apply` commands (D-0032)
- the updater enforces the four-point managed-core update contract: update managed core, preserve overlay, preserve live state, stop on locally modified managed files
- `.raiden/instance/metadata.json` and `.raiden/instance/baseline.json` are now the first named files inside the reserved instance support area
- updater Tier 2 canon now promotes the package-manifest field set, core `MAJOR.MINOR.PATCH` version comparison semantics, the refined anomaly threshold rule, and a safe auto-removal path for baseline-tracked unchanged managed files (D-0033)
- updater instance-side metadata and installed-baseline field contracts are now promoted for the current local CLI updater, including strict unknown-field rejection and an initial-install-only missing-baseline policy (D-0034)
- the installer direction is now fixed as a local web operator surface with no native OS GUI target, and install/update is now treated as one installer surface with update mode (D-0035)
- the updater package now includes a shared installer service layer and a dependency-free local web API backend so future browser UI work can reuse canonical init/plan/apply behavior instead of forking it
- the first local web installer UI scaffold now exists under `toolkit/updater/web/`, connected to the local JSON API for scan, init preview/apply, plan, apply, doctor, and native folder-selection convenience

- all tracked implementation defects and documentation gaps in the gap tracker have been resolved; `working/RAIDEN_GAPS.md` is fully closed as of 2026-04-29
- downgrade is now blocked by default in the updater; an `--allow-downgrade` operator override is available (D-0036, commit 7d4628d)
- the release-ready checklist is fully green and no open defects or documentation gaps remain; the repo is past the release-preparation gate

## Current Canonical Source Map

The working concept ownership is now:

- `HardlinkOrganizer` for embedded local continuity and prompt-library structure
- `Starlight Architect` for original governance architecture and formal boundary logic
- `StarlightDaemonDev` for host/meta-workspace repository structure
- `BIND` for sidecar governance, remote audit, and handoff/completion prompt interfaces
- `CTRL` for artifact policy and current-state handoff discipline
- `ARC` and `ARC-RC` for role memos, producer/consumer boundaries, and research-index patterns

## In Progress

- None active. The first updater MVP is complete and tested. The operator-surface direction is now fixed to local web, while remaining updater canon work stays limited to broader metadata extensions and package/distribution questions beyond the promoted local CLI surface.

## Temporarily On Hold

- metadata extensions beyond the current local CLI contract and prerelease/build version metadata remain outside the current promoted updater surface
- broader updater-shape canon beyond the current MVP scope is deferred until real downstream usage provides feedback
- native OS GUI variants for the installer/operator surface are out of current scope

## Not Yet Done

- broader updater metadata extensions beyond the promoted local CLI contract are not yet settled
- broader extracted-reference coverage is not needed for the retired primary reviewed repos whose RAIDEN-relevant value is already preserved in canon and review artifacts
- no legacy holds remain under `reference-repos/`; all legacy snapshots have been retired or removed

## Known Constraints

- much of the preserved source material began as transcript-heavy working material
- several strong patterns conflict in style even when they agree in function
- prototype-specific naming and ecosystem context must not leak into canon without normalization
- agents should be treated as token-blind by default; live context usage and remaining token headroom may be unavailable
- agents should be treated as model-bound for the duration of a work cycle unless the active environment explicitly supports safe switching at a stop point

## Current Risks

- root continuity files can drift if they are not updated as canon advances
- a future agent could still confuse review artifacts with canon if `SOURCE_OF_TRUTH.md` is not followed strictly
- long mixed-purpose work cycles can silently accumulate context pressure if pause-point and handoff discipline are weak

## Evidence

- `README.md`
- `SOURCE_OF_TRUTH.md`
- `REPOSITORY_MAP.md`
- `AGENT_BOUNDARIES.md`
- `ARTIFACT_AUDIENCE.md`
- `INGRESS_POLICY.md`
- `MANAGED_VS_LOCAL.md`
- `RELEASE_READY_CHECKLIST.md`
- `toolkit/README.md`
- `toolkit/instance/README.md`
- `SNAPSHOT_RETIREMENT_RULE.md`
- `reference-reviews/CROSS_REPO_MATRIX.md`
- `reference-reviews/CANONICAL_SOURCE_MAP.md`

## Last Updated

- Date: 2026-04-29
- Confidence: High
