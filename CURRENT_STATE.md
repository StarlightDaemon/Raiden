# Current State

## Summary

RAIDEN is now in the **canonicalization phase**.

The repo has moved past initial intake and broad prototype comparison. Authority order is defined, reviewed prototype patterns are synthesized, and the first canonical root governance/navigation layer is in place.

RAIDEN is not yet a finished toolkit implementation. It is currently a structured central framework repo with:

- preserved source history
- imported prototype evidence snapshots
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
- external evidence intake is now governed by `INGRESS_POLICY.md`
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
- `HardlinkOrganizer` now has extracted references under `reference-extracts/hardlinkorganizer/`
- `BIND` now has extracted references under `reference-extracts/bind/`
- downstream naming is now fixed:
  - `RAIDEN` = central governing agent
  - `RAIDEN Instance` = downstream deployed form
  - `Edict` = managed core artifact

## Current Canonical Source Map

The working concept ownership is now:

- `HardlinkOrganizer` for embedded local continuity and prompt-library structure
- `Starlight Architect` for original governance architecture and formal boundary logic
- `StarlightDaemonDev` for host/meta-workspace repository structure
- `BIND` for sidecar governance, remote audit, and handoff/completion prompt interfaces
- `CTRL` for artifact policy and current-state handoff discipline
- `ARC` and `ARC-RC` for role memos, producer/consumer boundaries, and research-index patterns

## In Progress

- expanding the initial toolkit subtree around the adopted naming model without overcommitting unresolved updater details
- narrowing future evidence intake so imports happen only when there is a real design or comparison reason

## Temporarily On Hold

- updater work is intentionally paused after initial planning
- the current updater planning bundle lives under `working/updater-system/`
- the updater remains an open future work block, but it is not the active implementation focus right now
- current operator direction is to defer updater-shape canon until RAIDEN is substantially closer to release-ready toolkit/package state

## Not Yet Done

- no updater-shape canon or manifest-field canon exists yet
- no imported prototype snapshot has been fully retired from `reference-repos/` yet
- broader extracted-reference coverage remains optional for later repos such as `Starlight Architect`, but the default next high-value targets (`HardlinkOrganizer` and `BIND`) are now preserved

## Known Constraints

- much of the preserved source material began as transcript-heavy working material
- reviewed prototype repos are large and should not remain in `reference-repos/` indefinitely
- several strong patterns conflict in style even when they agree in function
- prototype-specific naming and ecosystem context must not leak into canon without normalization
- agents should be treated as token-blind by default; live context usage and remaining token headroom may be unavailable
- agents should be treated as model-bound for the duration of a work cycle unless the active environment explicitly supports safe switching at a stop point

## Current Risks

- root continuity files can drift if they are not updated as canon advances
- imported prototype snapshots may remain expensive to retain until extracted-reference coverage is broader
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

- Date: 2026-04-20
- Confidence: High
