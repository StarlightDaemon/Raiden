# Writ Ownership Boundary

This file is a minimal example of a managed ownership note that would install
with the `Writ`.

## Managed Core Includes

- RAIDEN-owned law and operating-rule artifacts
- managed boundary guidance
- centrally owned files that should update as one governed unit

## Managed Core Excludes

- `.raiden/local/` overlay materials
- `.raiden/state/` live continuity files
- `.raiden/instance/` deferred install/update metadata files
- repo-specific prompts, context, or exceptions

## Use Rule

If a target repo would normally need to edit a file for local reasons, that
file is a poor candidate for the managed `Writ` payload and should stay
outside this package example.
