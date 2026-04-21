# Prompt Interface Pattern

## Purpose

This extract preserves the `BIND` pattern of giving a governance sidecar a
clear handoff prompt and a clear completion prompt instead of relying on loose
unstructured agent interaction.

## Observed Pattern

Observed prompt interface behavior:

- a handoff prompt tells an implementation agent what to read first and what
  rules apply
- a completion prompt defines the expected closeout structure and evidence
- prompt interfaces are part of the governance kit, not scattered across the
  product tree
- drift or exception reporting is routed through a dedicated template

## Why It Matters To RAIDEN

This is strong evidence for prompt interfaces as part of governance packaging.
It shows how a governance kit can define both:

- how work starts
- how governed work closes

That is especially useful for any future RAIDEN sidecar or reusable prompt
asset set.

## Reusable Pattern

Preserve these ideas:

1. pair kickoff prompts with closeout prompts
2. define expected evidence in the closeout interface
3. keep governance prompts in a dedicated controlled home
4. route deviations through a specific drift or exception template

## RAIDEN-Relevant Implication

This pattern should be merged with `CTRL` handoff discipline and
`HardlinkOrganizer` prompt-library structure rather than copied alone. BIND is
strongest as evidence for the interface contract, not for the full surrounding
workflow volume.

## What Not To Reuse Literally

Do not promote directly:

- Starlight-specific role labels
- Carbon-specific component guidance
- report-heavy certification expectations as the default closeout model

## Provenance

- Primary sources:
  - `reference-repos/BIND/.governance/HANDOFF_PROMPT.md`
  - `reference-repos/BIND/.governance/COMPLETION_REPORT_PROMPT.md`
  - `reference-repos/BIND/.governance/drift-report-template.md`
- Supporting sources:
  - `reference-reviews/BIND/REPO_TOOLING_REVIEW.md`
  - `reference-reviews/BIND/IMPORT_CANDIDATES.md`
