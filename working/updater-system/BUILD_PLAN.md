# RAIDEN Updater System Build Plan

## Purpose

This is a non-canonical implementation planning artifact for the first RAIDEN updater build.

It translates the current RAIDEN canon into a narrow build target for an implementation agent without treating unresolved package and subtree questions as already settled.

## 1. Current Working Judgment

The first updater should be built as a local CLI that consumes a manifest-driven managed-core package for the `Edict`.

That choice is the narrowest implementation that satisfies current canon:

- update managed core
- preserve local overlay
- preserve local live state
- stop on locally modified managed files

The first build should prioritize safety, determinism, and testability over packaging polish.

It should also distinguish between:

- compatibility and version checks
- the minimal file delta actually required
- unusually large or structurally surprising changes that may indicate a broader issue

## 2. Build Objective

Build the first updater MVP for a `RAIDEN Instance` that can:

1. read instance metadata
2. read a managed-core package manifest
3. compare versions and compatibility before planning any update
4. compare the installed managed baseline against the current instance tree
5. produce a conflict-aware update plan
6. apply only the managed-file changes that are actually needed
7. flag unusually large or structurally surprising changes for operator review
8. preserve overlay and live-state paths untouched
9. record the new installed baseline after a successful update

## 3. MVP Scope

The MVP should include:

- a local CLI updater
- typed metadata models for instance state and package manifest
- version and compatibility checks
- conflict detection for managed files
- delta-only update planning
- change-size and anomaly classification
- a dry-run planning mode
- an apply mode
- fixture-based tests covering safe-update and conflict cases
- at least one sample package fixture and one sample instance fixture

The MVP should not include:

- remote download or registry resolution
- drag-and-drop UX
- GUI packaging
- auto-merge for conflicts
- report-heavy audit workflows
- full toolkit publishing mechanics
- validator ecosystems beyond update safety checks

## 4. Recommended Functional Shape

Recommended command surface:

- `inspect`
  Show parsed instance metadata, package metadata, and current compatibility state.
- `plan`
  Produce a dry-run result showing compatibility, which managed files would change, which changes are unnecessary because the installed file already matches the target package, which paths are protected as overlay/live state, whether conflicts block apply, and whether the change set looks unusually large.
- `apply`
  Execute the update only if the plan is conflict-free, then write the new installed baseline.

If the implementation needs an even smaller first cut, `inspect` may be folded into `plan`, but `plan` and `apply` should both exist.

## 5. Required Data Models

The implementation should define narrow explicit models for:

### Instance metadata

Minimum fields:

- `instance_schema_version`
- `instance_form_type`
- `installed_core_version`
- `installed_package_version` if package identity is separate from core version
- `managed_roots`
- `overlay_roots`
- `live_state_roots`
- `baseline_manifest_path` or equivalent installed-state reference

### Package manifest

Minimum fields:

- `package_type`
- `toolkit_core_version`
- `package_version`
- `compatible_instance_schema_versions`
- `managed_files`
- `package_created_at` or equivalent provenance field

For each managed file entry:

- relative path
- content hash
- file kind if needed

### Installed baseline record

Minimum fields:

- installed managed-core version
- installed package identifier if present
- installed package version if tracked separately
- managed file list with hashes recorded at install time
- install timestamp or revision marker

### Plan/apply result

Minimum fields:

- compatibility status
- version comparison result
- changed managed files
- unchanged managed files
- already-up-to-date files
- conflicts
- anomaly warnings
- skipped local paths
- apply outcome

## 6. Version And Delta Rules

The updater should check at least:

- whether the package is compatible with the instance schema version
- whether the target managed-core version is newer, equal, or older than the installed version
- whether the target package version is newer, equal, or older than the installed package version if both exist

Default behavior:

- block incompatible schema versions
- no-op or report already current when the installed managed core already matches the target package
- optionally require an explicit flag for downgrade behavior if downgrade support is allowed later

Delta behavior:

- only rewrite managed files whose current target content differs from the package content
- do not rewrite managed files that already match the target package hash
- still inspect all managed files for local-modification conflicts before apply

## 7. Large-Change And Anomaly Rules

The updater should include a simple anomaly pass during `plan`.

It does not need full audit intelligence. It should only detect conditions that are unusual enough to deserve operator attention.

Minimum anomaly signals:

- high managed-file change count
- high percentage of the managed set changing in one update
- many deletions
- changes spanning multiple managed roots or categories
- changes to especially sensitive metadata files
- version jumps larger than the expected immediate increment
- any package that changes instance metadata shape or baseline format

Recommended first behavior:

- classify anomalies as `warn` or `block`
- `warn` when the update is large but still structurally plausible
- `block` when the update implies a likely compatibility or packaging mistake

Examples:

- `warn`: 40 percent of managed files change in a planned major update
- `warn`: multiple managed roots are touched when the version change is larger than a patch increment
- `block`: package declares compatibility with a schema version that does not match the instance
- `block`: package attempts to write into overlay or live-state roots
- `block`: package deletes or replaces foundational metadata files without the expected schema/version markers

## 8. Conflict Model

The updater must treat these as blocking conflicts:

- a managed file exists in the installed baseline but its current content hash no longer matches the recorded installed hash
- a managed file expected by the new package collides with a protected overlay or live-state path
- instance metadata is missing or incompatible
- the installed baseline is missing when the command requires it and safe inference is not possible

The updater should not:

- overwrite a locally edited managed file
- infer that local modifications are safe
- mutate overlay files
- mutate live-state files

## 9. Suggested Build Sequence

1. Define data models and file-format expectations.
2. Build fixture directories for a sample `RAIDEN Instance` and sample package.
3. Implement manifest loading, version comparison, and compatibility validation.
4. Implement baseline loading and current-tree hashing.
5. Implement planning logic for delta-only updates and conflict reporting.
6. Implement anomaly classification for large or structurally surprising changes.
7. Implement apply logic.
8. Add tests for happy path, conflict stop, incompatible schema, no-op/already-current behavior, anomaly warnings, and overlay/live-state preservation.
9. Add minimal user-facing documentation for running the CLI locally.

## 10. Suggested Test Matrix

Minimum tests:

- applies a package when managed files match the installed baseline
- blocks apply when a managed file was locally edited
- no-ops when the installed version and managed hashes already match the target package
- rewrites only files whose target package content differs
- preserves overlay files during apply
- preserves live-state files during apply
- rejects incompatible instance schema versions
- rejects malformed package manifests
- warns on large but structurally valid change sets
- blocks on structurally invalid change sets
- writes updated installed baseline after successful apply
- dry-run reports planned managed changes without mutating files

Good additional tests if time permits:

- missing installed baseline handling
- newly added managed file
- removed managed file
- managed path collision with protected local path

## 11. Recommended Documentation Outputs

The implementation agent should be prepared to create or update:

- a narrow updater shape doc
- an instance metadata spec
- an `Edict` package manifest spec
- local implementation README content for the updater CLI

If current canon still leaves a physical location unresolved, the agent should choose the smallest provisional implementation location and document that it is provisional rather than treating it as settled canon.

## 12. Key Guardrails

- Do not replace the current RAIDEN architecture.
- Do not collapse central toolkit form and downstream instance form into one undifferentiated structure.
- Do not turn overlay or live-state material into managed-core files just to simplify implementation.
- Do not add remote distribution, sidecar sync, or audit-report systems to the MVP.
- Do not silently resolve conflicts.
- Do not assume imported prototype repos are canonical.

## 13. Expected Outcome

At the end of the first build pass, RAIDEN should have:

- a runnable local updater CLI
- explicit version and compatibility checks
- delta-only update behavior
- anomaly warnings for unusually large or suspicious change sets
- explicit metadata models
- explicit conflict detection behavior
- tests proving the managed-versus-local contract
- enough implementation reality to support later canonical spec promotion and broader toolkit materialization
