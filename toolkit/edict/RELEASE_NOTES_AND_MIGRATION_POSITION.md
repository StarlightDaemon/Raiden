# Edict Release Notes And Migration Position

## Purpose

This document defines the current high-level position of release notes and
migration notes relative to a managed `Edict` package.

It exists to reduce release-preparation ambiguity without defining:

- final file formats
- manifest fields
- updater commands
- migration record schema

## Core Rule

Release notes and migration notes are release-support materials, not automatic
default payload files.

At the current phase, they should be treated as conditional package-adjacent
materials unless later canon shows that a given class of note must live inside
the managed payload itself.

## Current Position

For current canon, the default position is:

- managed payload:
  `.raiden/writ/` after install
- package-adjacent release-support materials:
  central package-side materials next to the payload rather than inside it

Working interpretation:

- the managed payload should stay focused on RAIDEN-owned installed core files
- release notes and migration notes may accompany a package revision
- those notes should not be assumed to install into `.raiden/writ/` by
  default

## When Package-Adjacent Is The Right Default

Package-adjacent positioning is the correct default when the note:

- explains a release transition rather than defining installed managed law
- is relevant only for certain upgrades or revisions
- would create clutter inside `.raiden/writ/` after installation
- is mainly for operator or updater-facing review rather than steady-state use

## When In-Payload Placement Might Later Be Justified

In-payload placement might later be justified if a note is:

- meant to remain part of the installed managed core after the transition
- required for steady-state interpretation of the installed `Writ`
- centrally owned guidance that should persist across normal downstream use

That remains conditional until later updater and release canon.

## What This Means For The Current Example Package

The current minimal example package should not grow release notes or migration
files inside:

- `toolkit/edict/example-package/payload/`

unless RAIDEN later decides that a particular class of note belongs in the
installed managed core.

For now, the example should stay narrowly focused on clearly RAIDEN-owned
payload files.

## Practical Review Rule

When deciding where a release-support note belongs, ask:

1. Is this note about an installed steady-state managed file, or about a
   transition between package revisions?
2. Should a downstream repo still keep this note inside `.raiden/writ/` after
   the transition is complete?
3. Would placing it in the payload blur the boundary between managed core and
   release-support scaffolding?

If the note is mainly transition-specific, package-adjacent is the safer
default.

## Still Deferred

This document does not yet define:

- exact filenames for release notes or migration notes
- whether they will ship in one bundle or multiple artifacts
- how later tooling will discover or apply them
- rollback or downgrade note handling

Those remain later package and updater canon.
