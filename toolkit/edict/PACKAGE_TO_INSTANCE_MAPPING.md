# Edict Package To Writ Mapping

## Purpose

This document defines the current high-level mapping between the central
`Edict` package example and the deployed downstream `Writ` carried by a
`RAIDEN Instance`.

It exists to make the managed package boundary explicit without defining
package manifest extensions, updater behavior beyond the current local CLI, or
archive format.

## Core Mapping

The current minimal package example maps as follows:

- `toolkit/edict/example-package/payload/`
  -> `.raiden/writ/`

Interpretation:

- `toolkit/edict/example-package/` is the central package-side example root
- `payload/` is the technical installable subset of an `Edict`
- `.raiden/writ/` is the downstream issued managed-core destination inside a
  `RAIDEN Instance`

## What Is Inside The Managed Package

The managed package currently covers only the managed-core payload that belongs
under:

- `.raiden/writ/`

This is the RAIDEN-owned layer that may later be refreshed by managed package
or updater flows.

## What Is Outside The Managed Package

The managed package does not include:

- `.raiden/local/`
- `.raiden/state/`
- `.raiden/instance/`

Those paths remain outside the current managed package because they belong to
other layers or support surfaces:

- `.raiden/local/` = repo-local overlay
- `.raiden/state/` = repo-local live continuity state
- `.raiden/instance/` = reserved instance support area for metadata and
  installed baseline records

## Current Practical Use

Use this mapping when:

- reviewing whether a package-side example stays inside managed-core scope
- checking whether a proposed file belongs in the package payload or another
  instance layer
- preparing later package or updater canon without pulling local-only material
  into the managed package

## Still Deferred

This mapping does not yet define:

- package manifest extensions beyond the current updater contract
- final package archive format
- updater command behavior
- whether future package shapes will include additional central package-side
  metadata adjacent to `payload/`

Those remain deferred until later package and updater canon.
