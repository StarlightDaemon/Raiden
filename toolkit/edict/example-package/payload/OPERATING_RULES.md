# Edict Operating Rules

This file is a minimal example of a RAIDEN-managed law artifact inside an
installed `Edict`.

## Core Rules

1. Treat files in `.raiden/edict/` as RAIDEN-managed core.
2. Put repo-specific adaptation in `.raiden/local/`, not in managed-core files.
3. Put continuity and fast-changing operational truth in `.raiden/state/`.
4. Treat local edits to managed-core files as exceptions that require explicit
   update conflict handling rather than silent overwrite.

## Why This File Exists

The example package needs at least one real managed artifact that a future
updater could target.

This file fills that role without inventing manifest schema, release archive
format, or command behavior.
