# Minimal Edict Example Package

## Purpose

This directory is the first concrete example of what a managed `Edict` package
could look like before manifest mechanics, updater commands, and archive format
are canonized.

It is intentionally small.

Its job is to make the package-side payload surface real enough that later
updater work has an actual managed-core target instead of only abstract
boundary notes.

## Example Shape

```text
toolkit/edict/example-package/
├── README.md
└── payload/
    ├── README.md
    ├── OPERATING_RULES.md
    └── OWNERSHIP_BOUNDARY.md
```

## How To Read This Example

- `README.md` explains the example from the central RAIDEN package side
- `payload/` represents the files that would install into the managed
  downstream `Edict`
- `payload/README.md` is the installed index for the managed core
- `payload/OPERATING_RULES.md` is a minimal managed law/rules artifact
- `payload/OWNERSHIP_BOUNDARY.md` is a minimal managed ownership guide

## Downstream Mapping

This example maps as follows:

- `toolkit/edict/example-package/payload/`
  -> `.raiden/edict/`

That means the example package root is central/package-side only, while the
`payload/` subtree is the installed managed-core surface.

## Intentionally Absent

This example does not define:

- exact manifest field names
- updater commands or conflict behavior beyond existing canon
- final archive or bundle format
- `.raiden/local/` contents
- `.raiden/state/` contents
- `.raiden/instance/` metadata files

Those remain deferred or belong to other layers.

## Working Rule

If a file would routinely vary by target repo, it should stay out of this
example package and live in local overlay or live state instead.
