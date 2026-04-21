# Prompt Governance

## Purpose

This document defines the working rules for central shared prompt assets under
`toolkit/prompts/`.

It governs:

- what may enter the shared prompt layer
- how prompt surfaces are classified
- how prompts should be written
- how prompt changes should be introduced
- what must remain outside the central prompt surface

It does not define package manifests, updater metadata, or downstream prompt
folder names.

## Core Rule

A prompt belongs in the central shared layer only when it is reusable across
more than one repo, task family, or operator workflow.

If a prompt depends on a specific repo's:

- filesystem layout
- live continuity state
- local tools
- local exceptions
- project identity

it belongs in a downstream local layer instead.

## Execution Assumptions

Central shared prompts should assume:

- token limits may be opaque
- agents may not know current context usage or remaining headroom
- work is often model-bound for the duration of a cycle
- mid-cycle model switching must not be required for success
- continuation should rely on compact artifacts, not raw chat replay

Therefore:

- bound scope before broad reads or edits
- prefer one model set per cycle
- define stop conditions for non-trivial work
- require pause-point export before model handoff when handoff is allowed
- keep continuation payloads compact and stable

## Surface Standard

RAIDEN uses a two-tier language standard for prompt work.

### Tier 1: Durable Readable Language

Use readable language for:

- long-lived repo artifacts
- human review surfaces
- policy and governance
- adoption notes
- final summaries

### Tier 2: Compressed Machine-Oriented Language

Use compressed language for:

- internal prompts
- scoped execution instructions
- pause-point exports
- continuation packages
- validation checks
- transient orchestration directives

### Mixed-Surface Rule

Some files are durable readable Markdown wrappers around compressed internal
prompt bodies.

In mixed-surface files:

- keep headings, purpose, and notes readable
- keep the executable template body compact when safe
- do not classify the whole file by the loudest style inside it

## Shared Prompt Categories

The current central categories are:

- bounded task templates
- compact task templates
- handoff templates
- pause-point templates
- continuation-state templates
- completion templates
- validation templates
- compact review templates
- audit/review templates

Future central categories may include:

- operator-facing kickoff prompts

Only add a new category when it represents a stable reusable task shape rather
than one session's wording.

## Authoring Rules

Shared prompts should be:

- short enough to scan quickly
- explicit about outcome and boundaries
- robust against scope drift
- neutral about one repo's naming or toolchain
- explicit about whether the active surface is readable, compressed, or mixed

Shared prompts should not:

- assume one project's file paths
- mix execution instructions with large status reports
- encode local exceptions as if they were global defaults
- carry product-specific branding or ecosystem assumptions

## Compressed Internal Standard

Compressed internal prompts should prefer:

- short imperative statements
- explicit scope markers
- dense constraint packing
- stable field labels
- short validation statements
- direct stop conditions

Compressed internal prompts should avoid:

- conversational padding
- motivational language
- repeated framing
- long transitions
- redundant restatement of known constraints

Approved stable labels:

- `Mode`
- `Obj`
- `Scope`
- `Read`
- `Do`
- `No`
- `Val`
- `Stop`
- `Out`
- `Phase`
- `Done`
- `Open`
- `Dec`
- `Blk`
- `Next`
- `Alt`
- `Trim`

Guardrails:

- compression must remain operationally lossless enough for reliable execution
- if one field becomes ambiguous, expand that field rather than the whole prompt
- exact file scope and exact validation checks outrank prose smoothness

## Prompt Shape

A central shared prompt should usually include:

1. a prompt ID
2. a short purpose statement
3. the prompt body or template
4. concise notes on source lineage or intended usage

This is a documentation shape, not yet a package manifest requirement.

## Change Discipline

When updating an existing shared prompt:

- preserve the prompt ID unless the task shape changes materially
- tighten wording before adding sections
- remove repo-specific leakage rather than documenting around it
- update `CATALOG.md` if the prompt role or status changes

When adding a new shared prompt:

- confirm it is reusable
- give it a distinct prompt ID
- place it in the narrowest suitable category
- record it in `CATALOG.md`

## Promotion Rule

Candidate prompt material may come from:

- reviewed prototype patterns
- repeated RAIDEN operator workflows
- repeated central-agent handoff needs

It does not become a shared prompt asset only because it was useful once.

Promotion still requires:

1. review or demonstrated repeat use
2. normalization into RAIDEN wording
3. placement in this subtree

## Anti-Drift Rules

- Do not use this directory as a session prompt dump.
- Do not copy raw prototype prompts without normalization.
- Do not store downstream local prompts here.
- Do not let prompt inventory drift out of sync with `CATALOG.md`.
- Do not compress human-facing governance just because the execution layer is compact.

## Current Deferred Questions

The following are still intentionally open:

- exact version metadata shape for prompt bundles
- whether prompt compatibility markers are needed beyond plain notes
- how shared prompts will be packaged alongside managed `Edict` releases
