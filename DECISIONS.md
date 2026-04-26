# Decisions

## D-0001

- Date: 2026-04-18
- Status: Active
- Decision: `/mnt/e/RAIDEN` is the canonical central toolkit/framework repository.
- Rationale: this repo is the intended durable home for reusable agent governance, repository-structure, and execution-support artifacts.

## D-0002

- Date: 2026-04-18
- Status: Active
- Decision: `Source_info/` is preserved source history, not active canonical authority.
- Rationale: the current files are valuable prototype inputs but are transcript-heavy and require normalization before promotion.

## D-0003

- Date: 2026-04-18
- Status: Active
- Decision: imported working repos must be copied under `reference-repos/` as isolated reference snapshots.
- Rationale: this keeps prototype evidence separate from RAIDEN canon and avoids accidental authority confusion.

## D-0004

- Date: 2026-04-18
- Status: Active
- Decision: BIND and Starlight/Architect references are treated as prototype lineages, not active RAIDEN product scope.
- Rationale: RAIDEN is being normalized as a general reusable toolkit, not as a continuation of any one product ecosystem.

## D-0005

- Date: 2026-04-18
- Status: Active
- Decision: no reviewed prototype repo will be adopted wholesale as RAIDEN canon.
- Rationale: synthesis showed that the strongest RAIDEN shape is distributed across several lineages rather than contained in one repo.

## D-0006

- Date: 2026-04-18
- Status: Active
- Decision: RAIDEN canon is assembled by concept ownership rather than repo naming similarity.
- Rationale: multiple reviewed repos use different filenames for similar functions, while some similarly named artifacts serve different roles.

## D-0007

- Date: 2026-04-18
- Status: Active
- Decision: the current working canonical source map is:
  - `HardlinkOrganizer` for embedded local continuity and prompt-library structure
  - `Starlight Architect` for original governance architecture and formal boundary logic
  - `StarlightDaemonDev` for host/meta-workspace structure
  - `BIND` for sidecar governance, remote audit, and prompt interfaces
  - `CTRL` for artifact policy and current-state handoff discipline
  - `ARC` and `ARC-RC` for role memos, producer/consumer boundaries, and research-index patterns
- Rationale: this map best reflects completed cross-repo synthesis and should guide current canon drafting.

## D-0008

- Date: 2026-04-18
- Status: Active
- Decision: the first canonical RAIDEN draft order is:
  1. authority and structure
  2. live continuity
  3. support-layer canon
- Rationale: future agents need a stable authority spine before they can safely rely on continuity files, and continuity before they can use support artifacts.

## D-0009

- Date: 2026-04-18
- Status: Active
- Decision: RAIDEN will explicitly support both:
  - a central toolkit/package/sidecar-capable form
  - a downstream repo-local embedded-instance form
- Rationale: synthesis showed that the strongest reusable patterns split across these two forms rather than collapsing into one structure.
- Implementation note: both forms should be clearly typed and versioned so long-term maintenance, upgrades, and compatibility are easy to reason about.

## D-0010

- Date: 2026-04-18
- Status: Active
- Decision: canonical prompt rules, guidance, and shared prompt assets belong to the central RAIDEN toolkit layer, while repo-local operational prompts created for a deployed downstream instance belong in the downstream repo subtree.
- Rationale: root canon and toolkit materials should remain the source of truth for reusable prompt policy, while deployed repos need a local place for prompts tied to their own bounded work and continuity state.
- Implementation note: root-level RAIDEN docs should index and govern prompt structure, but not become a dumping ground for every repo-local prompt.

## D-0011

- Date: 2026-04-18
- Status: Active
- Decision: the downstream embedded-instance name must be finalized before `TOOLKIT_INDEX.md` and toolkit-subtree drafting, but not before all remaining continuity-layer work.
- Rationale: naming becomes structurally important once toolkit and downstream template artifacts depend on it, but forcing it before all continuity work would block useful progress.

## D-0012

- Date: 2026-04-18
- Status: Active
- Decision: RAIDEN will default to a simple exception record first, with richer drift-report workflows used only when escalation is warranted.
- Rationale: a lightweight baseline is easier to operate day to day, while heavier forensic drift reporting remains available for exceptional cases.

## D-0013

- Date: 2026-04-18
- Status: Active
- Decision: imported prototype snapshots only become eligible for retirement after:
  1. support-layer canon exists
  2. a retirement rule is written
  3. the repo has completed review coverage, import candidates, synthesis coverage, and no unresolved reread questions
- Rationale: this preserves evidence until extraction is mature while still preventing long-term search noise and storage bloat.

## D-0014

- Date: 2026-04-18
- Status: Active
- Decision: downstream RAIDEN usage will follow a three-layer model:
  - managed core
  - local overlay
  - local live state
- Rationale: RAIDEN core law must remain updateable and authoritative, while downstream repos still need a safe place for local rules, prompts, context, and active continuity state.

## D-0015

- Date: 2026-04-18
- Status: Active
- Decision: downstream repo agents may extend RAIDEN through approved local overlay artifacts, but may not silently rewrite RAIDEN-managed source-of-truth or law files during normal repo work.
- Rationale: this preserves the integrity of managed RAIDEN core materials while still allowing target-specific adaptation where needed.

## D-0016

- Date: 2026-04-18
- Status: Active
- Decision: all future RAIDEN update mechanisms must obey the same contract:
  1. update managed core
  2. preserve local overlay
  3. preserve local live state
  4. stop and report conflict if a managed file was locally modified
- Rationale: update shape may vary, but the safety contract must remain stable across CLI, drag-and-drop, or bundle-based update flows.

## D-0017

- Date: 2026-04-18
- Status: Active
- Decision: the central governing agent remains `RAIDEN`.
- Rationale: `RAIDEN` is the canonical governing intelligence and central source-of-truth authority for the framework.

## D-0018

- Date: 2026-04-18
- Status: Active
- Decision: the downstream repo-local deployed form is named `RAIDEN Instance`.
- Rationale: this name is structurally clear, supports versioning and update logic, and distinguishes the downstream deployed form from central RAIDEN canon.

## D-0019

- Date: 2026-04-18
- Status: Superseded by D-0031
- Decision: the managed core artifact inside a `RAIDEN Instance` is named `Edict`.
- Rationale: `Edict` is concise, authoritative, subordinate to RAIDEN itself, and fits the managed-law/control-package role better than documentation-heavy alternatives.

## D-0020

- Date: 2026-04-18
- Status: Superseded by D-0031
- Decision: the naming stack for current canon is:
  - `RAIDEN` = central governing agent/framework authority
  - `RAIDEN Instance` = downstream deployed repo-local form
  - `Edict` = managed core artifact/law package within a `RAIDEN Instance`
- Rationale: separating these names prevents the central intelligence, deployed form, and managed artifact from being conflated.

## D-0021

- Date: 2026-04-18
- Status: Active
- Decision: RAIDEN will preserve a non-canonical extracted-reference layer under `reference-extracts/` for high-value patterns taken from reviewed prototype repos.
- Rationale: large prototype snapshots contain useful reusable patterns, but RAIDEN should not keep all raw product code as the preferred reread surface forever.

## D-0022

- Date: 2026-04-18
- Status: Active
- Decision: prototype snapshot retirement follows a three-state model:
  - full snapshot retained
  - extracted reference retained
  - full snapshot retired
- Rationale: review completion alone is too coarse a threshold for retirement; reusable value must be preserved in canon or extracted references before a raw snapshot is removed.

## D-0023

- Date: 2026-04-18
- Status: Active
- Decision: future external repo evidence enters RAIDEN through a controlled ingress path: import to `reference-repos/`, review in `reference-reviews/`, extract to `reference-extracts/` only when needed, and retire snapshots only under `SNAPSHOT_RETIREMENT_RULE.md`.
- Rationale: the early broad prototype intake was useful for initial normalization, but RAIDEN should use a narrower repeatable intake process going forward.

## D-0024

- Date: 2026-04-18
- Status: Active
- Decision: `toolkit/` is the first explicitly designated canonical RAIDEN toolkit subtree.
- Rationale: RAIDEN now needs a real non-root home for shared prompt assets and the first central `Edict` package surface without waiting for the full updater/package stack to be finished.
- Implementation note: root canonical docs remain the higher-order authority, and unresolved updater metadata or downstream folder details should not be treated as settled only because the subtree now exists.

## D-0025

- Date: 2026-04-18
- Status: Superseded by D-0032
- Decision: updater-shape canon remains intentionally deferred until RAIDEN is materially closer to a v1 release state.
- Rationale: RAIDEN still needs more toolkit/package and release-preparation work completed before an updater design would be stable enough to justify canonizing delivery and manifest behavior.
- Implementation note: updater work remains open, but it should not be treated as an active planning or build task while release-readiness preparation is still incomplete.

## D-0026

- Date: 2026-04-18
- Status: Active
- Decision: the default physical root of a downstream `RAIDEN Instance` is a compact `.raiden/` subtree, with a repo-root `AGENTS.md` acting as the startup bridge into that instance.
- Rationale: this keeps the repo-local control plane explicit without overtaking the whole target repository, preserves a clear agent entrypoint at the repo root, and fits the strongest embedded-instance evidence from `HardlinkOrganizer`.
- Implementation note: within `.raiden/`, the first-pass canonical structure distinguishes `writ/`, `local/`, `state/`, and `instance/`; the first updater later named `.raiden/instance/metadata.json` and `.raiden/instance/baseline.json`, and D-0034 promoted their current local CLI field contracts.

## D-0027

- Date: 2026-04-20
- Status: Active
- Decision: RAIDEN execution policy assumes opaque token limits and model-bound work cycles unless the active environment explicitly exposes safer capabilities.
- Rationale: agents often do not know real-time context usage or remaining token headroom, and many environments do not permit reliable mid-cycle model switching. RAIDEN must therefore control token pressure indirectly through bounded scope, explicit pause points, compact carried-forward state, and continuation artifacts rather than through assumed live token awareness.
- Implementation note: do not require mid-cycle model switching for task success; prefer one model set per cycle, require a pause-point handoff before model changes when they are allowed, and preserve continuity in durable artifacts rather than raw chat accumulation.

## D-0028

- Date: 2026-04-20
- Status: Active
- Decision: RAIDEN will use a two-tier language standard across execution surfaces: durable human-facing artifacts stay readable, while agent-facing internal execution layers may use compressed machine-oriented language when operationally lossless.
- Rationale: RAIDEN must preserve operator readability and maintainability in canon, while also reducing token drag in internal prompts, pause-point packages, validation checks, and transient orchestration layers.
- Implementation note: classify surfaces rather than whole files; mixed-surface files may keep readable wrappers around compressed template bodies. Compression must not weaken scope clarity, validation quality, or pause-point reliability.

## D-0029

- Date: 2026-04-20
- Status: Active
- Decision: RAIDEN artifacts will be classified by canonicality, primary audience, intended role, and non-use boundary when confusion risk is material.
- Rationale: authority order alone does not prevent audience bleed. RAIDEN needs an explicit distinction between files meant to define RAIDEN itself, files meant for review/synthesis, and files meant for downstream execution or deployment.
- Implementation note: layer defaults are defined in `ARTIFACT_AUDIENCE.md`; files outside root canon, especially under `Source_info/`, should add local status blocks when they contain prescriptive language or could be mistaken for downstream instruction.

## D-0030

- Date: 2026-04-20
- Status: Active
- Decision: when an execution environment exposes explicit model and reasoning controls, RAIDEN should default to one bounded moderate-reasoning pass first and escalate reasoning only after observed failure or repeated rerun pressure.
- Rationale: repeated low-signal retries can burn more tokens than one stronger follow-up pass, but always starting at the highest reasoning level is also wasteful. RAIDEN should therefore prefer a stable moderate baseline, then escalate only when the first pass shows incompleteness, contradiction, premature stopping, or repeated steering needs.
- Implementation note: keep the durable rule vendor-neutral in root canon. Prompt-layer guidance may define host-specific baseline profiles and escalation paths, but RAIDEN should not hard-code one provider's model family as a global default in root law.

## D-0031

- Date: 2026-04-23
- Status: Active
- Decision: current canon distinguishes the central `Edict` from the downstream `Writ`:
  - `RAIDEN` = central governing agent/framework authority
  - `Edict` = central RAIDEN-authored managed instruction/package surface
  - `RAIDEN Instance` = downstream deployed repo-local form
  - `Writ` = installed managed core artifact within a `RAIDEN Instance`
- Rationale: this separates central authored authority from the downstream issued managed form while preserving the intended medieval/legal naming model.
- Implementation note: `payload` remains a technical package-side term for the installable subset of an `Edict`; by default that payload installs into `.raiden/writ/`.

## D-0032

- Date: 2026-04-24
- Status: Active
- Decision: the first concrete RAIDEN updater is a local CLI with `plan` and `apply` commands, implemented under `toolkit/updater/`.
- Rationale: a local CLI is the narrowest updater form that satisfies the four-point managed-core update contract (D-0016) with tested evidence. The MVP proves update safety, conflict detection, delta-only behavior, and anomaly classification without requiring remote distribution, packaging polish, or GUI flows.
- Implementation note: the updater uses `.raiden/instance/metadata.json` and `.raiden/instance/baseline.json` within the reserved instance support area (D-0026). Package-manifest fields, core version comparison semantics, anomaly thresholds, and managed-file removal behavior were later refined and promoted in D-0033; instance-side metadata and installed-baseline fields were later refined and promoted for the current local CLI updater in D-0034.

## D-0033

- Date: 2026-04-24
- Status: Active
- Decision: updater Tier 2 canon now promotes the current package-manifest surface, core version comparison semantics, anomaly threshold refinement, and safe managed-file auto-removal rules for the local CLI updater.
- Rationale: the current updater implementation and test suite now provide enough evidence to stabilize the package-side contract without broadening into a full package ecosystem design. This closes the remaining Tier 2 gaps while keeping broader updater metadata extensions and distribution questions provisional.
- Implementation note:
  - package manifests live at `manifest.json` beside `payload/` and require `package_type`, `edict_version`, `compatible_instance_schemas`, `managed_files`, and `created_at`; each `managed_files` entry contains `path` and SHA-256 `hash`
  - version comparison uses strict core `MAJOR.MINOR.PATCH` numeric comparison; prerelease/build metadata and downgrade policy remain outside the current canon surface
  - `high_change_ratio` warns only when more than 50 percent of the managed set changes and the managed set contains at least 8 files; `high_change_count` warns when more than 10 managed files change
  - managed-file removals may auto-apply only when the file is recorded in the installed baseline and has not been locally modified since install; removals remain operator-visible in plan output and anomaly reporting
  - instance-side metadata and installed-baseline field names were intentionally left provisional by this decision and later addressed in D-0034

## D-0034

- Date: 2026-04-25
- Status: Active
- Decision: the current local CLI updater canon now promotes the instance-side metadata and installed-baseline field contracts for `.raiden/instance/metadata.json` and `.raiden/instance/baseline.json`.
- Rationale: the updater implementation now validates the field sets strictly enough to support canon promotion without weakening the managed/local safety rule. Missing installed baselines are no longer broadly allowed; they are allowed only for initial install into a fresh managed root with no existing files.
- Implementation note:
  - `metadata.json` requires exactly `instance_schema_version`, `instance_form_type`, `installed_edict_version`, `managed_roots`, `overlay_roots`, and `live_state_roots`
  - `instance_form_type` is fixed to `raiden-instance`; the current local CLI supports `managed_roots` of `[".raiden/writ"]`, `overlay_roots` of `[".raiden/local"]`, and `live_state_roots` of `[".raiden/state"]`
  - `baseline.json` requires exactly `installed_edict_version`, `installed_at`, and `managed_files`; each `managed_files` entry contains exactly `path` and SHA-256 `hash`, and managed-file paths must be unique
  - unknown extra fields in these current local CLI metadata files are rejected rather than ignored
  - if `baseline.json` is missing while `.raiden/writ/` already contains files, planning blocks with `missing_baseline`; a missing baseline is accepted only when the managed root is empty or absent
  - broader metadata extensions, multiple managed roots, downgrade policy, prerelease/build metadata, and package/distribution mechanics remain outside this promoted surface
