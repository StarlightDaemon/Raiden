# Writ Managed Core

## Purpose

This directory represents the installed managed-core payload of the example
`Edict` package.

In a downstream `RAIDEN Instance`, this directory maps to:

- `.raiden/writ/`

Everything here is RAIDEN-managed core, not local overlay and not local live
state.

## Included Files

| File | Role |
|---|---|
| `README.md` | installed index for the managed `Writ` |
| `OPERATING_RULES.md` | minimal centrally owned operating-law example |
| `OWNERSHIP_BOUNDARY.md` | minimal centrally owned managed-vs-local reminder |

## Intentionally Not Here

These do not belong in this payload example:

- repo-specific prompts
- repo-specific rules
- repo-specific context
- local continuity state
- updater metadata files with canonized field names

Those belong under `.raiden/local/`, `.raiden/state/`, or instance-support
material under `.raiden/instance/`.
