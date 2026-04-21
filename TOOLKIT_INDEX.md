# Toolkit Index

## Purpose

This file defines the first canonical component map for RAIDEN as a toolkit/framework.

It also governs the first materialized toolkit subtree under `toolkit/`.
It defines:

- the major supported forms
- the major component layers
- the naming model
- what is central versus downstream

## Canonical Naming Model

Current naming stack:

- `RAIDEN` = central governing agent/framework authority
- `RAIDEN Instance` = downstream deployed repo-local form
- `Edict` = managed core artifact/law package within a `RAIDEN Instance`

This naming is canonical and should be used consistently in future toolkit drafting.

## Supported Forms

RAIDEN currently recognizes two supported forms.

### 1. Central RAIDEN Toolkit Form

This is the central reusable framework/package/sidecar-capable form maintained in this repository.

Its responsibilities include:

- source-of-truth governance
- shared boundary definitions
- shared prompt policy and shared prompt assets
- update rules
- versioning rules
- reusable templates and structures

### 2. Downstream RAIDEN Instance Form

This is the deployed repo-local form used inside a target repository.

Its responsibilities include:

- carrying the managed `Edict`
- hosting local overlay materials
- hosting live repo-local continuity state
- supporting repo-specific operational prompts and local adaptation

## Core Component Model

### A. Central Components

These belong to the central RAIDEN toolkit form.

| Component | Role | Current Status |
|---|---|---|
| Root canonical docs | source-of-truth governance and navigation | active |
| Shared prompt policy/indexing | central prompt model and prompt governance | active |
| Managed-vs-local update contract | update safety model | active |
| Review/synthesis layer | prototype extraction and comparison | active |
| `toolkit/` subtree | reusable deployable toolkit materials | initial |

### B. Downstream RAIDEN Instance Components

These belong to a deployed repo-local `RAIDEN Instance`.

| Component | Role | Current Status |
|---|---|---|
| `Edict` | managed core artifact/law package | initial skeleton exists |
| Local overlay | repo-specific rules, prompts, and context | concept approved |
| Local live state | current state, goals, loops, decisions, work log | concept approved |
| Instance update metadata | version/update tracking for the instance | planned |

## `RAIDEN Instance` Layer Model

A `RAIDEN Instance` follows the three-layer structure already adopted in canon:

1. managed core
2. local overlay
3. local live state

Within that model:

- the managed core is expressed through the `Edict`
- the local overlay belongs to the target repo
- the local live state records the target repo's operational continuity

## First Materialized Toolkit Surface

The first explicit toolkit surface now exists under `toolkit/`.

Its current scope is intentionally narrow:

- `toolkit/README.md`
  - subtree identity and boundary
- `toolkit/prompts/`
  - canonical shared prompt asset home plus governance and catalog docs
- `toolkit/edict/`
  - first managed `Edict` package surface plus boundary, lifecycle, and minimal
    example package docs
- `toolkit/instance/`
  - downstream `RAIDEN Instance` structure and prompt-mapping docs

This first surface is meant to:

- give prompt assets a real canonical home outside the root
- create a concrete package boundary for the managed `Edict`
- define the first concrete downstream `RAIDEN Instance` folder structure
- avoid freezing unresolved updater metadata or downstream folder details too early

## Source Lineage

Primary lineage sources for this toolkit model:

- `HardlinkOrganizer`
  - embedded local control plane
  - prompt-library structure
  - continuity-file role separation

- `BIND`
  - sidecar governance and remote audit
  - prompt-interface and maturity-model patterns

- `Starlight Architect`
  - original governance architecture
  - formal boundary logic

- `StarlightDaemonDev`
  - host/meta-workspace structure

- `CTRL`
  - artifact policy and handoff discipline

## What This File Does Not Yet Define

This file does not yet define:

- version manifest field names
- first updater implementation shape
- packaging/publish mechanics

Those remain dependent on:

- updater-shape decisions
- deeper downstream-instance documentation beyond the first-pass physical layout
- further toolkit-surface materialization

## Immediate Use

Use this file when:

- drafting future toolkit subtree structure
- deciding where shared versus local assets belong
- explaining the difference between `RAIDEN`, `RAIDEN Instance`, and `Edict`
- evaluating update and versioning plans

## Current Status

- naming model: defined
- supported forms: defined
- high-level component model: defined
- physical toolkit subtree: initially materialized
- first-pass downstream instance folder structure: defined
