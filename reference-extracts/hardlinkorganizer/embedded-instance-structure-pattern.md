# Embedded Instance Structure Pattern

## Purpose

This extract preserves the strongest `HardlinkOrganizer` pattern for RAIDEN:
an embedded repo-local control plane that lives inside a normal project repo
without taking over the whole repository shape.

## Observed Structure

Observed high-signal layout:

- product-facing root `README.md`
- agent startup file at `AGENTS.md`
- project-local control plane under `agent-ledger/`
- bounded prompt library under `agent-prompts/`
- support and planning notes under `notes/`
- product-specific operational material under `packaging/`

## Why It Matters To RAIDEN

This is the clearest reviewed example of a downstream `RAIDEN Instance` style
layout where:

- product files remain product files
- agent continuity has a dedicated local home
- prompts are separated from durable state
- planning/support notes do not become the source of truth by accident

For RAIDEN, this is strong evidence that a downstream instance does not need to
restructure an entire target repo into a pure governance tree. A compact local
control plane is enough if its boundaries are explicit.

## Reusable Pattern

Preserve these structural ideas:

1. keep a clear product front door
2. provide a distinct agent startup/read-order file
3. keep the continuity layer in one dedicated local subtree
4. keep bounded prompt assets in a separate prompt subtree
5. keep planning/support notes outside the continuity control plane

## RAIDEN-Relevant Implication

This pattern supports the current canon that a downstream `RAIDEN Instance`
should distinguish:

- managed core
- local overlay
- local live state

The `HardlinkOrganizer` structure is especially useful for drafting where local
live state and repo-local prompts belong in a deployed instance.

## What Not To Reuse Literally

Do not promote directly:

- absolute root paths such as `/mnt/e/HardlinkOrganizer` or `E:\\HardlinkOrganizer`
- project-specific packaging layout
- project-specific roadmap or release content
- migration history tied to extraction from another repo

## Provenance

- Primary sources:
  - `reference-repos/HardlinkOrganizer/AGENTS.md`
  - `reference-repos/HardlinkOrganizer/agent-ledger/README.md`
  - `reference-repos/HardlinkOrganizer/agent-prompts/README.md`
- Supporting sources:
  - `reference-reviews/HardlinkOrganizer/REPO_TOOLING_REVIEW.md`
  - `reference-reviews/HardlinkOrganizer/IMPORT_CANDIDATES.md`
