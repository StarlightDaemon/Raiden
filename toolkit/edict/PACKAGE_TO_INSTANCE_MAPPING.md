# Edict Package To Instance Mapping

## Purpose

This document defines the current high-level mapping between the central
`Edict` package example and the deployed downstream `RAIDEN Instance`.

It exists to make the managed package boundary explicit without defining
manifest schema, updater commands, or archive format.

## Core Mapping

The current minimal package example maps as follows:

- `toolkit/edict/example-package/payload/`
  -> `.raiden/edict/`

Interpretation:

- `toolkit/edict/example-package/` is the central package-side example root
- `payload/` is the installed managed-core subtree
- `.raiden/edict/` is the downstream managed-core destination inside a
  `RAIDEN Instance`

## What Is Inside The Managed Package

The managed package currently covers only the managed-core payload that belongs
under:

- `.raiden/edict/`

This is the RAIDEN-owned layer that may later be refreshed by managed package
or updater flows.

## What Is Outside The Managed Package

The managed package does not include:

- `.raiden/local/`
- `.raiden/state/`
- `.raiden/instance/`

Those paths remain outside the current managed package because they belong to
other layers or deferred support surfaces:

- `.raiden/local/` = repo-local overlay
- `.raiden/state/` = repo-local live continuity state
- `.raiden/instance/` = reserved instance support area with deferred internal
  filenames

## Current Practical Use

Use this mapping when:

- reviewing whether a package-side example stays inside managed-core scope
- checking whether a proposed file belongs in the package payload or another
  instance layer
- preparing later updater canon without pulling local-only material into the
  managed package

## Still Deferred

This mapping does not yet define:

- exact manifest field names
- final package archive format
- updater command behavior
- whether future package shapes will include additional central package-side
  metadata adjacent to `payload/`

Those remain deferred until later package and updater canon.
