# Edict Package Boundary

## Purpose

This document defines the current high-level boundary of the central `Edict`
package surface.

It answers:

- what kinds of material belong in the managed core
- what kinds of material must stay outside it
- what remains intentionally undecided beyond the current updater contract

It does not define package manifest extensions beyond the current local CLI
contract or archive formats.

## Core Rule

The `Edict` is the central RAIDEN-authored managed instruction/package surface.
Its installable `payload/` issues a downstream `Writ` inside a
`RAIDEN Instance`.

It should contain the material that RAIDEN owns centrally and expects to issue
and later update as a governed unit.

It should not absorb local overlay or live-state material just to simplify
distribution.

## Material That Belongs In The Managed Core

The managed core may include:

- source-of-truth and law artifacts adopted for downstream use
- boundary and operating-rule artifacts that RAIDEN owns centrally
- shared prompt assets intended for managed deployment
- package-side compatibility guidance
- central templates that are meant to remain RAIDEN-owned after installation

These are categories, not a finalized file list.

## Material That Does Not Belong In The Managed Core

The managed core must not include:

- downstream local overlay rules
- downstream live continuity state
- repo-specific operational prompts
- imported prototype evidence
- extracted-reference material
- session-only or temporary planning artifacts

If a file changes mainly because one target repo is different from another, it
is a strong candidate for the local overlay rather than the managed core.

## Conditional Material

Some materials may end up inside or adjacent to the managed package depending on
later package or updater decisions:

- instance metadata templates
- release notes or migration notes
- compatibility reference docs
- baseline or install-state records

These remain conditional beyond the current local CLI updater surface.

Current positioning guidance for release notes and migration notes is documented
in `RELEASE_NOTES_AND_MIGRATION_POSITION.md`.

## Ownership Test

When deciding whether something belongs in the `Edict`, ask:

1. Is this centrally owned by RAIDEN?
2. Should it be updated as part of the managed core?
3. Would local repo adaptation be a mistake rather than a normal use case?

If the answer to all three is yes, it is a good `Edict` candidate.

If the material needs routine local adaptation, it likely belongs outside the
`Edict` and outside the downstream `Writ`.

## Current Practical Implication

At the current phase, the `Edict` package surface is a boundary marker plus a
minimal example package skeleton.

It gives RAIDEN a place to:

- document managed-core ownership
- separate package-side concerns from root canon
- materialize a small example payload under `toolkit/edict/example-package/`
- prepare for later manifest extensions and compatibility specs

without broadening beyond the update mechanism already promoted for the current
local CLI surface.

## Current Example Boundary

The current minimal example package:

- keeps the central example root under `toolkit/edict/example-package/`
- treats `toolkit/edict/example-package/payload/` as the installed
  `.raiden/writ/` mapping
- includes only clearly RAIDEN-owned managed-core files
- leaves local overlay, live state, and instance-support materials out of the
  package example
