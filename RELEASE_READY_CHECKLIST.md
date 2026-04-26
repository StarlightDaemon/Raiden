# Release-Ready Checklist

## Purpose

This document turns "release-ready preparation" into a concrete canonical
checklist for RAIDEN.

Use it to record the release-preparation threshold that allowed the current
local CLI updater work to proceed, and to judge future updater broadening.

This file does not define updater behavior.
It defines the preparation threshold that should be reached before updater
scope expands.

## Core Rule

Updater-shape canon should remain narrow until RAIDEN is materially closer to a
v1 release state and observed usage justifies broadening.

For current canon, "materially closer to a v1 release state" means:

- the checklist's required items are complete or explicitly waived by operator
- only updater-specific delivery, metadata, or distribution questions remain as the main
  unresolved work

## Status Meanings

- `Done` = materially complete in current canon
- `Partial` = started, but still missing important release-prep clarity
- `Open` = not yet sufficiently defined for release-readiness
- `Deferred` = intentionally postponed and not required before updater scope
  broadens

## Required Checklist

### 1. Canon Coherence

| Item | Status | Notes |
|---|---|---|
| Authority order and promotion rules are stable | `Done` | `SOURCE_OF_TRUTH.md` exists and the toolkit subtree is explicitly designated |
| Root continuity files agree on current priorities | `Done` | current continuity docs agree on phase, release-prep focus, and current updater scope |
| Naming stack is fixed and consistently used | `Done` | `RAIDEN`, `Edict`, `RAIDEN Instance`, and `Writ` are settled |
| Managed-vs-local boundary remains explicit | `Done` | boundary and update contract are defined in canon |

### 2. Central Toolkit Surface

| Item | Status | Notes |
|---|---|---|
| Canonical `toolkit/` subtree exists | `Done` | first explicit subtree now exists |
| Shared prompt assets have a real central home | `Done` | `toolkit/prompts/` exists |
| Shared prompt governance and catalog exist | `Done` | prompt governance and catalog docs now exist |
| Central `Edict` package boundary is documented | `Done` | boundary and lifecycle docs now exist |
| Package-side release vocabulary exists | `Done` | lifecycle language is defined without updater specifics |
| Further central package docs are added only where they reduce ambiguity | `Done` | current canon keeps the central `Edict`, installable `payload`, and downstream `Writ` mapping explicit; add further package docs only if a new release-prep ambiguity appears |

### 3. Downstream Instance Preparation

| Item | Status | Notes |
|---|---|---|
| Central versus downstream forms are clearly distinguished | `Done` | supported forms are documented |
| Three-layer downstream model is stable | `Done` | managed core, local overlay, local live state are fixed |
| Concrete downstream instance folder structure is documented | `Done` | default `.raiden/` structure and root `AGENTS.md` startup bridge are now defined |
| Central prompt assets are mapped to downstream operational prompt usage | `Done` | downstream local prompt home and derivation model are now documented |
| Minimum downstream artifact set is documented clearly enough for release prep | `Done` | first-pass required instance files and subtrees are now defined |

### 4. Package And Release Preparation

| Item | Status | Notes |
|---|---|---|
| Managed-core ownership test is documented | `Done` | the `Edict` boundary doc defines what belongs in the downstream `Writ` |
| Release-prep work no longer depends on raw naming ambiguity | `Done` | naming stack is fixed |
| Release-prep work no longer depends on prompt-home ambiguity | `Done` | shared prompts now live under `toolkit/prompts/` |
| Package examples or package-ready skeleton materials exist | `Done` | `toolkit/edict/example-package/` now provides a minimal real managed-core package skeleton with a deployable `payload/` mapping to `.raiden/writ/` |
| Compatibility/release documentation is far enough along to support updater design later | `Done` | lifecycle, mapping, compatibility, release-support positioning, compact review-checklist guidance, and the minimum installed `Writ` payload are explicit enough that later updater work has a stable current package target |

### 5. Evidence And Retirement Readiness

| Item | Status | Notes |
|---|---|---|
| High-value prototype reviews are complete | `Done` | main source repos have review coverage |
| High-value extracted references exist where needed | `Done` | `CTRL`, `HardlinkOrganizer`, and `BIND` now have extracts |
| Source-history index matches actual extract state | `Done` | updated to reflect current extract coverage |
| Retirement readiness has been explicitly assessed for current candidate repos | `Done` | assessment exists for `CTRL`, `HardlinkOrganizer`, and `BIND` |
| At least one raw snapshot is clearly safe to retire | `Done` | `CTRL` was retired from `reference-repos/` on 2026-04-23 after review, synthesis, extraction, and operator approval satisfied the retirement rule |
| Future evidence intake is staying narrow and policy-driven | `Done` | pre-intake gate (§0 of `INGRESS_POLICY.md`) requires a bounded design reason and five yes/no checks before any import; intake is now auditable by process, not only by policy wording |

### 6. Resume Gate For Updater Canon

| Item | Status | Notes |
|---|---|---|
| Remaining active work is mostly release-prep rather than broad architecture discovery | `Done` | current work is narrower than earlier synthesis phases |
| Remaining ambiguity is concentrated enough that updater design would not freeze weak assumptions | `Done` | the `Edict`-to-`Writ` package-side distinction is explicit, and the toolkit surface is now sufficiently prepared; updater design would no longer freeze weak assumptions |
| Operator agrees RAIDEN is close enough to a v1 release state to resume updater canon | `Done` | operator approved updater MVP build on 2026-04-24; first updater implemented and tested under `toolkit/updater/` (D-0032) |

## Current Priority Gaps

The highest-value incomplete work is now:

1. keep broader updater metadata extensions, downgrade policy, and
   package/distribution design deferred unless real downstream usage shows a
   concrete need to promote them
2. keep future evidence intake narrow and policy-driven unless a new bounded
   design reason appears

## What This Checklist Does Not Require Yet

The following are not required before broader updater canon resumes:

- final updater command surface
- exact package archive format
- remote distribution mechanics
- native OS GUI or drag-and-drop update flow

Current operator-surface direction instead favors a local web UI, which is now
tracked separately from native GUI scope by D-0035.

Those belong to later updater-shape or package/distribution canon.

## Use Rule

When a future agent asks whether updater work should broaden:

1. review this checklist
2. identify which required items remain `Open` or materially `Partial`
3. finish or explicitly waive those items first
4. broaden updater-shape canon only when the remaining unresolved work is mostly
   updater-specific and backed by observed need
