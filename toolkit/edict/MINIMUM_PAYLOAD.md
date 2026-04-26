# Minimum Installed Writ Payload

## Purpose

This document defines the minimum canonical installed payload for the managed
`Writ` issued from the current `Edict` during the current
release-preparation phase.

It exists to make the current managed-core target explicit enough for release
review and later updater canon without freezing manifest fields, archive
format, or updater commands.

## Core Rule

For current release-prep, RAIDEN treats the minimum installed managed-core
payload under `.raiden/writ/` as a real canonical surface, not only as a loose
example.

This minimum payload is intentionally small.
Its role is to make the current managed-core target explicit and reviewable.

## Current Minimum Installed Files

The minimum canonical installed payload is:

```text
.raiden/writ/
├── README.md
├── OPERATING_RULES.md
└── OWNERSHIP_BOUNDARY.md
```

Required current files:

- `README.md`
  - installed index for the managed `Writ`
- `OPERATING_RULES.md`
  - minimal RAIDEN-owned law and operating-rule artifact
- `OWNERSHIP_BOUNDARY.md`
  - minimal RAIDEN-owned managed-versus-local boundary reminder

## Canonical Mapping

The current canonical package-side mapping is:

- `toolkit/edict/example-package/payload/README.md`
  -> `.raiden/writ/README.md`
- `toolkit/edict/example-package/payload/OPERATING_RULES.md`
  -> `.raiden/writ/OPERATING_RULES.md`
- `toolkit/edict/example-package/payload/OWNERSHIP_BOUNDARY.md`
  -> `.raiden/writ/OWNERSHIP_BOUNDARY.md`

This means the current example package is not only illustrative.
Its `payload/` subtree expresses the present minimum canonical installed managed
core for release-prep review.

## Release-Prep Interpretation

This minimum payload is sufficient for current release-prep when all of the
following are true:

- the payload remains mapped only to `.raiden/writ/`
- all included files are clearly RAIDEN-owned
- no repo-local overlay, live-state, or instance-support files leak into the
  payload
- the payload remains interpretable as one managed unit

Additional managed files may be added later only when they reduce release
ambiguity without forcing updater-shape canon forward too early.

## What This Does Not Settle

This document does not settle:

- package manifest extensions beyond the current updater contract
- updater commands or conflict-record mechanics
- package archive or bundle layout
- exact field names inside `.raiden/instance/metadata.json` and
  `.raiden/instance/baseline.json`
- release artifact naming
- whether future managed payloads will include more files than this minimum

Those remain deferred until later package or updater canon requires them.

## What Stays Outside This Minimum Payload

The minimum installed payload does not include:

- `.raiden/local/` overlay materials
- `.raiden/state/` live continuity materials
- `.raiden/instance/` support metadata
- repo-specific prompts, context, rules, or exceptions
- release-transition notes that are only package-adjacent by current canon

## Use Rule

Use this document when:

- reviewing whether the current `Edict` surface is concrete enough for release
  prep and yields a stable downstream `Writ` target
- checking whether a proposed managed file belongs in the current minimum
  payload
- aligning package-side examples with downstream installed-surface docs
- preparing later updater canon without rediscovering the present managed-core
  target
