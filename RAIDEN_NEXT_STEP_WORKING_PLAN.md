# RAIDEN Next-Step Working Plan

## 1. Executive Assessment

RAIDEN is in a good canonicalization state: authority order, naming, boundary rules, ingress, retirement, and first extracted-reference mechanics are already established in root canon. The repo is no longer blocked on broad synthesis. It is now blocked on turning the adopted managed-core versus local-layer contract into the first practical updater model and the smallest packageable surface that can support it.

The next step should not be a large toolkit subtree buildout. It should be a narrow updater-design pass that defines how a `RAIDEN Instance` identifies its installed managed core, how the `Edict` is versioned, and how managed-file conflicts are detected before any overwrite occurs.

## 2. Immediate Priority

The single most important next work block is to define the first concrete updater shape and its required instance metadata contract.

Why this is next:

- `MANAGED_VS_LOCAL.md` and `DECISIONS.md` already fix the safety contract, but not the implementation shape.
- `TOOLKIT_INDEX.md` explicitly leaves version-manifest fields, downstream folder names, and updater shape undefined.
- Future toolkit materialization, downstream deployment, and snapshot-retirement readiness all depend on knowing what a managed update unit actually is.

## 3. Updater Design Recommendation

Recommend the first updater shape as: a local CLI updater that applies a manifest-driven managed-core package for the `Edict`.

Why this fits the current canon:

- The canon already supports multiple future update shapes, but requires one stable safety contract across them. A CLI is the simplest way to implement that contract first without committing to UI or distribution mechanics too early.
- A CLI can operate directly against a local repo tree, compare managed files against recorded metadata, stop on conflict, and preserve overlay/live-state layers deterministically.
- A manifest-driven package is still needed, but it should be the package format the CLI consumes, not the first user-facing update mode by itself.
- A drag-and-drop bundle flow is better treated as a later wrapper around the same package and manifest once the metadata model is stable.

What files or metadata it requires:

- `toolkit_core_version`: version of the managed RAIDEN core being installed.
- `instance_schema_version`: version of the `RAIDEN Instance` layout/metadata contract.
- `instance_form_type`: at minimum enough typing to distinguish central toolkit material from downstream instance material, because canon requires both forms to be typed and versioned.
- `managed_file_manifest`: list of managed paths in the `Edict`, with per-file content hashes or equivalent integrity values.
- `installed_from_version`: the previously installed managed-core version, so upgrade paths and compatibility checks are explicit.
- `compatibility_range` or equivalent: what instance schema versions a package can safely update.
- `conflict_detection_state`: enough recorded baseline to detect when a managed file was locally modified since installation.
- `overlay_roots` and `live_state_roots`: explicit non-managed paths the updater must preserve untouched.

Minimum behavioral contract for the first updater:

- validate instance metadata
- validate package metadata
- compare managed-file hashes against the recorded baseline
- stop and report conflicts on any managed-file local modification
- replace only managed-core files
- leave overlay and live-state files unchanged
- record the newly installed version and managed-file baseline

What risks this avoids:

- avoids overcommitting to drag-and-drop packaging before the manifest and conflict model exist
- avoids confusing the package artifact with the update mechanism
- avoids locking RAIDEN into a sidecar-only or embedded-only deployment assumption too early
- avoids silent overwrite behavior that would violate existing canon
- avoids premature validator/audit automation before the install/update contract is defined

What it should not try to do yet:

- no GUI or drag-and-drop updater UX
- no remote distribution or publishing workflow
- no automatic merge resolution for locally modified managed files
- no full audit/report pipeline as a default path
- no attempt to materialize the entire future toolkit subtree
- no attempt to standardize every downstream prompt or validator surface in the same pass

## 4. Secondary Work

After updater design, the next supporting tasks should be:

1. Define the instance metadata and manifest spec in canonical form.
   This is the minimal prerequisite for safe updates, version checks, and future package materialization.

2. Extract `HardlinkOrganizer` into `reference-extracts/`.
   RAIDEN needs a compact preserved reference for downstream instance structure, file-role separation, and prompt-library layout before deeper instance-shape drafting.

3. Draft the smallest first toolkit surface around the managed `Edict`.
   The first materialized surface should be only the managed-core package definition, instance metadata contract, and a minimal downstream scaffold boundary, not a full package ecosystem.

## 5. Extraction Recommendations

`HardlinkOrganizer` should be extracted next. `BIND` should follow immediately after.

Why `HardlinkOrganizer` is first:

- It is the strongest practical source for the downstream embedded-instance model.
- Its value is directly upstream of updater design because it shows the continuity files, prompt-library split, and local control-plane shape that a `RAIDEN Instance` will need to preserve.
- It is the highest-leverage source for deciding which files belong to managed core versus overlay versus live state in a real repo-local deployment.

Why `BIND` is second:

- It is the strongest source for governance sidecar structure, remote audit, handoff/completion prompt interfaces, and the vendored-kit to managed-package maturity model.
- Those patterns matter, but they are slightly less blocking than `HardlinkOrganizer` for the first updater because the first updater must first know how a repo-local instance is laid out and protected.

No other repo should move ahead of those two by default. If a later pass needs deeper authority or boundary logic, that should be a targeted reread of `Starlight Architect`, not the next extraction by default.

## 6. Risks And Preconditions

Blockers or missing preconditions:

- there is not yet a canonical instance metadata schema
- there is not yet a canonical managed-file manifest
- `TOOLKIT_INDEX.md` explicitly leaves exact downstream folder names and version-manifest field names unresolved
- the exact physical boundary of the `Edict` artifact set is still conceptual rather than materialized

Sequencing risks:

- materializing a toolkit subtree before the updater metadata is defined could freeze weak folder names or package boundaries
- extracting `BIND` first could bias the first implementation toward sidecar packaging before the downstream instance shape is nailed down
- defining versioning without file ownership metadata would produce nominal versions without safe update behavior

Operational risks:

- if managed-file conflicts are detected only by path membership and not by recorded file state, local edits may be overwritten or falsely treated as safe
- if overlay/live-state roots are not explicit, the first updater may blur managed and local boundaries despite the current canon

## 7. Proposed Artifact Changes

Recommended new canonical docs:

- `UPDATER_SHAPE.md`
  Purpose: choose the first supported updater form, define its behavioral contract, and state deferred update forms.
- `INSTANCE_METADATA_SPEC.md`
  Purpose: define required `RAIDEN Instance` metadata fields, version typing, managed-file tracking, and conflict rules.
- `EDICT_PACKAGE_SPEC.md`
  Purpose: define the smallest first managed-core package surface and its manifest expectations.

Recommended updates to existing canon:

- `TOOLKIT_INDEX.md`
  Add the first minimal materialized package surface and how it relates to `RAIDEN`, `RAIDEN Instance`, and `Edict`.
- `MANAGED_VS_LOCAL.md`
  Add the concrete metadata expectations once chosen, without changing the already-set safety contract.
- `OPEN_LOOPS.md`
  Split the updater work into a metadata/spec loop and a later implementation/materialization loop.
- `CURRENT_STATE.md`
  Record updater-shape selection once made and note extraction progress for `HardlinkOrganizer` and `BIND`.
- `SOURCE_HISTORY_INDEX.md`
  Update extract status as additional repos move into the extracted-reference layer.

Recommended new extracted-reference work:

- `reference-extracts/hardlinkorganizer/`
  Focus on embedded-instance structure, continuity-file roles, prompt-library layout, and startup/read-order patterns.
- `reference-extracts/bind/`
  Focus on sidecar governance shape, maturity-model language, remote-audit protocol, and prompt-interface patterns.

## 8. Confidence

Observed evidence:

- root canon already fixes authority order, naming, managed-versus-local boundaries, ingress policy, and snapshot-retirement rules
- the current open loops explicitly name updater shape and expanded extracted references as the remaining open work
- `TOOLKIT_INDEX.md` explicitly says updater shape, version-manifest fields, and exact downstream folder names are not yet defined
- `HardlinkOrganizer` is the strongest reviewed source for embedded local control-plane structure
- `BIND` is the strongest reviewed source for governance sidecar, remote audit, and maturity-model patterns

Strong inference:

- the first updater should be CLI-based because it is the narrowest implementation that can fully enforce the already-approved safety contract
- the first package surface should be manifest-driven and centered on the managed `Edict`, not on a full toolkit subtree
- `HardlinkOrganizer` extraction is more immediately useful than `BIND` extraction for first-pass updater design because updater safety depends first on instance layout and managed/local separation

Weak inference:

- the eventual package naming will likely revolve around an `Edict`-scoped managed-core bundle rather than a broader toolkit release unit
- the first metadata spec will probably need both per-file hashes and compatibility fields rather than version labels alone
- a later drag-and-drop updater can be treated as a wrapper around the same manifest and CLI engine

Unresolved ambiguity:

- the exact physical folder names for the downstream `RAIDEN Instance`
- the exact physical folder names for the future toolkit subtree
- whether the first materialized package surface should live as a dedicated subtree, a templates area, or another canonical package root
- the exact boundary of the first `Edict` artifact set
- how much of `BIND`'s remote-audit pattern should become early canon versus remain a later optional support layer
