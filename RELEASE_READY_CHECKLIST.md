# Release-Ready Checklist

## Purpose

This document turns "release-ready preparation" into a concrete canonical
checklist for RAIDEN.

Use it to judge whether RAIDEN is sufficiently prepared at the
toolkit/package/downstream-structure level before updater-shape canon resumes.

This file does not define updater behavior.
It defines the preparation threshold that should be reached first.

## Core Rule

Updater-shape canon should remain deferred until RAIDEN is substantially closer
to release-ready toolkit/package state.

For current canon, "substantially closer to release-ready" means:

- the checklist's required items are complete or explicitly waived by operator
- only updater-specific delivery and manifest questions remain as the main
  unresolved work

## Status Meanings

- `Done` = materially complete in current canon
- `Partial` = started, but still missing important release-prep clarity
- `Open` = not yet sufficiently defined for release-readiness
- `Deferred` = intentionally postponed and not required before updater canon

## Required Checklist

### 1. Canon Coherence

| Item | Status | Notes |
|---|---|---|
| Authority order and promotion rules are stable | `Done` | `SOURCE_OF_TRUTH.md` exists and the toolkit subtree is explicitly designated |
| Root continuity files agree on current priorities | `Partial` | continuity is mostly aligned, but must keep tracking checklist progress as work continues |
| Naming stack is fixed and consistently used | `Done` | `RAIDEN`, `RAIDEN Instance`, and `Edict` are settled |
| Managed-vs-local boundary remains explicit | `Done` | boundary and update contract are defined in canon |

### 2. Central Toolkit Surface

| Item | Status | Notes |
|---|---|---|
| Canonical `toolkit/` subtree exists | `Done` | first explicit subtree now exists |
| Shared prompt assets have a real central home | `Done` | `toolkit/prompts/` exists |
| Shared prompt governance and catalog exist | `Done` | prompt governance and catalog docs now exist |
| Managed `Edict` package boundary is documented | `Done` | boundary and lifecycle docs now exist |
| Package-side release vocabulary exists | `Done` | lifecycle language is defined without updater specifics |
| Further central package docs are added only where they reduce ambiguity | `Partial` | subtree is real, but still intentionally thin |

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
| Managed-core ownership test is documented | `Done` | `Edict` boundary doc defines what belongs in managed core |
| Release-prep work no longer depends on raw naming ambiguity | `Done` | naming stack is fixed |
| Release-prep work no longer depends on prompt-home ambiguity | `Done` | shared prompts now live under `toolkit/prompts/` |
| Package examples or package-ready skeleton materials exist | `Done` | `toolkit/edict/example-package/` now provides a minimal real managed-core package skeleton with a deployable `payload/` mapping to `.raiden/edict/` |
| Compatibility/release documentation is far enough along to support updater design later | `Partial` | lifecycle, mapping, compatibility, release-support positioning, and compact review-checklist docs now exist, but exact release/compatibility mechanics remain intentionally deferred |

### 5. Evidence And Retirement Readiness

| Item | Status | Notes |
|---|---|---|
| High-value prototype reviews are complete | `Done` | main source repos have review coverage |
| High-value extracted references exist where needed | `Done` | `CTRL`, `HardlinkOrganizer`, and `BIND` now have extracts |
| Source-history index matches actual extract state | `Done` | updated to reflect current extract coverage |
| Retirement readiness has been explicitly assessed for current candidate repos | `Done` | assessment exists for `CTRL`, `HardlinkOrganizer`, and `BIND` |
| At least one raw snapshot is clearly safe to retire | `Open` | current assessment says none should be retired yet |
| Future evidence intake is staying narrow and policy-driven | `Partial` | policy exists, but this remains a live discipline task |

### 6. Resume Gate For Updater Canon

| Item | Status | Notes |
|---|---|---|
| Remaining active work is mostly release-prep rather than broad architecture discovery | `Done` | current work is narrower than earlier synthesis phases |
| Remaining ambiguity is concentrated enough that updater design would not freeze weak assumptions | `Partial` | still blocked by downstream/package readiness gaps |
| Operator agrees RAIDEN is close enough to release-ready state to resume updater canon | `Open` | current operator direction is to continue release-prep first |

## Current Priority Gaps

The highest-value incomplete checklist items are:

1. continue narrow release-prep work until updater-specific questions are the
   main unresolved surface
2. improve package/release documentation where it reduces ambiguity
3. keep future evidence intake narrow and policy-driven while the release-prep
   pass continues

## What This Checklist Does Not Require Yet

The following are not required before updater canon resumes:

- final updater command surface
- exact manifest field names
- exact package archive format
- remote distribution mechanics
- GUI or drag-and-drop update flow

Those belong to updater-shape canon later.

## Use Rule

When a future agent asks whether updater work should resume:

1. review this checklist
2. identify which required items remain `Open` or materially `Partial`
3. finish or explicitly waive those items first
4. resume updater-shape canon only when the remaining unresolved work is mostly
   updater-specific
