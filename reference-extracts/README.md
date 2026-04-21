# Reference Extracts

## Purpose

`reference-extracts/` is the compact extracted-reference layer for RAIDEN.

It exists to preserve the reusable value of large prototype repos without keeping all raw product code and repo noise in the active evidence surface forever.

This layer sits between:

- `reference-repos/` raw prototype snapshots
- root RAIDEN canon

## What Belongs Here

Keep:

- normalized pattern summaries
- small high-value examples
- artifact-role explanations
- provenance notes pointing back to the original reviewed repo
- caveats about what should and should not be reused

Do not keep:

- full product source trees
- build outputs
- large repo-local histories
- implementation detail that matters only to the original product

## Authority

Items here are not canonical by default.

They are RAIDEN-owned extracted references:

- narrower than raw snapshots
- more durable than temporary review notes
- still subordinate to root canonical docs

## Layout Rules

- use one lowercase folder per source repo
- prefer plain purpose-based filenames
- preserve provenance inside each extract
- keep each extract compact and high-signal

Example shape:

```text
reference-extracts/
├── ctrl/
│   ├── README.md
│   ├── artifact-policy-pattern.md
│   ├── current-state-handoff-pattern.md
│   └── project-structure-pattern.md
```

## Current Status

| Source Repo | Extract Status | Notes |
|---|---|---|
| `CTRL` | Pilot extraction created | first extracted-reference test case |
| `HardlinkOrganizer` | Extract set created | embedded-instance structure, continuity roles, prompts, and startup extracts now preserved |
| `BIND` | Extract set created | governance sidecar, maturity model, remote audit, prompt interface, and remediation extracts now preserved |
| `Starlight Architect` | Pending | likely later source for original governance-architecture extracts |

## Working Rule

Do not retire a raw snapshot from `reference-repos/` until the required reusable material is preserved in canon or in this layer and the retirement rule is satisfied.
