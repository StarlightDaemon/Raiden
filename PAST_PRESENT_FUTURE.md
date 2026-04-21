# Past, Present, Future

## Purpose

This file gives a compact full-form planning view of RAIDEN across:

- past work already completed
- present operating state
- future work still ahead

Use it when a new agent needs orientation quickly without reconstructing the repo history from chat or raw prototype evidence.

Root canonical docs remain the source of truth for authority and rules. This file is a canonical planning view, not a replacement for them.

## 1. Past

### What RAIDEN Started As

RAIDEN began as a preservation and normalization workspace.

At the start, the repo mainly held:

- early transcript-derived working material in `Source_info/`
- incomplete or drifting concept language
- no stable root authority layer
- no clear separation between source evidence and canonical repo artifacts

### What Was Done

RAIDEN then moved through an intentional preparation phase:

1. root scaffold and review spaces were created
2. major prototype repos were imported under `reference-repos/` as read-only evidence
3. broad and per-repo reviews were completed
4. cross-repo synthesis was completed
5. root canonical authority docs were written
6. continuity docs were refreshed into a usable live operating layer
7. support-layer canon was established
8. managed-vs-local update boundaries were defined
9. downstream naming was fixed
10. snapshot-retirement and ingress rules were added
11. the first extracted-reference pilot was created from `CTRL`

### What The Past Phase Produced

The key outputs of the completed preparation phase are:

- authority order
- repository navigation
- role boundaries
- continuity tracking
- source-history indexing
- toolkit naming and conceptual structure
- evidence intake rules
- retirement rules
- an extracted-reference bridge layer

### What Is No Longer True

These earlier conditions should no longer be assumed:

- prototype repos are not the main operating surface
- downstream naming is not unresolved
- support-layer canon is not missing
- evidence intake is not ad hoc
- raw prototype snapshots are not the only retention option

## 2. Present

### Current Phase

RAIDEN is in the **canonicalization phase**.

It is now a structured central toolkit/framework repo, but not yet a fully materialized toolkit implementation.

### What Is True Now

- RAIDEN is the canonical central toolkit/framework repo
- root canonical docs define current authority
- the repo has completed prototype review and synthesis coverage for the main sources
- the first canonical `toolkit/` subtree now exists
- a central-versus-downstream model is established
- the naming stack is fixed:
  - `RAIDEN`
  - `RAIDEN Instance`
  - `Edict`
- managed core versus local overlay versus live state boundaries are defined
- ingress, extraction, and snapshot-retirement rules exist
- `reference-extracts/ctrl/` is the first pilot extracted-reference set

### Current Strongest Source Assignments

- `HardlinkOrganizer` = embedded continuity and prompt-library structure
- `Starlight Architect` = original governance architecture and formal boundaries
- `StarlightDaemonDev` = host/meta-workspace structure
- `BIND` = governance sidecar, remote audit, prompt interfaces
- `CTRL` = artifact policy and handoff discipline
- `ARC` and `ARC-RC` = role memos and producer/consumer patterns

### Current Open Work

The main remaining work is narrower and more concrete than before:

- decide which reviewed snapshots are candidates for retirement after extraction
- expand the initial toolkit subtree around shared prompts and the managed `Edict` package surface
- continue release-readiness preparation for toolkit/package material before updater canon resumes, using `RELEASE_READY_CHECKLIST.md` as the gate

### Current Constraint

RAIDEN must continue to treat:

- `Source_info/` as preserved source history
- `reference-repos/` as evidence only
- `reference-reviews/` as analysis unless adopted
- `reference-extracts/` as compact preserved references unless adopted

## 3. Future

### Near-Term Future

The next work block should focus on turning the current conceptual model into the first practical implementation-facing layer.

Recommended order:

1. deepen the initial toolkit subtree/package surface
2. assess whether extracted repos can move toward retirement readiness
3. continue release-readiness preparation for toolkit/package material
4. return to updater-shape canon only after that preparation is substantially complete

### Medium-Term Future

After release-readiness preparation and extract/retirement work are clearer, RAIDEN should:

- define version/manifests for managed core updates
- define concrete downstream instance folder structure
- define how central prompt assets map into deployed repo-local operational prompts
- define how an updater enforces managed-versus-local boundaries

### Long-Term Future

RAIDEN should eventually support two stable forms:

- a central toolkit/package/sidecar-capable form
- a downstream `RAIDEN Instance` form with an `Edict` managed core

At that point, large raw prototype snapshots should no longer be the main reference surface for ongoing work.

## 4. Immediate Next-Step Recommendation

If a new agent is starting from the current repo state, the best next focus is:

### Primary next task

Deepen the initial toolkit/package surface until RAIDEN is substantially closer
to release-ready state.

### Why this is next

Current operator direction is to keep updater work deferred while RAIDEN still
has material toolkit/package preparation work left.

That means the highest-value active work is:

- deeper toolkit/package documentation
- clearer managed-core boundary and lifecycle material
- retirement-readiness assessment
- other release-preparation work tracked in `RELEASE_READY_CHECKLIST.md` that reduces ambiguity before updater canon

The updater question remains open, but it should resume after RAIDEN is closer
to release-ready package state.

### Secondary next task

Assess whether reviewed snapshots can move toward retirement readiness without
losing reread value still needed for toolkit/package preparation.

## 5. Reading Order For A New Agent

If an agent needs to start work from this file, read next in this order:

1. `SOURCE_OF_TRUTH.md`
2. `CURRENT_STATE.md`
3. `DECISIONS.md`
4. `MANAGED_VS_LOCAL.md`
5. `INGRESS_POLICY.md`
6. `SNAPSHOT_RETIREMENT_RULE.md`
7. `TOOLKIT_INDEX.md`
8. `reference-reviews/CANONICAL_SOURCE_MAP.md`
9. `reference-reviews/CROSS_REPO_MATRIX.md`

## 6. Current Confidence

- Observed evidence: high
- Structural direction: high
- Toolkit implementation completeness: low
- Updater design completeness: low
- Snapshot-retirement readiness across all repos: low-to-medium
