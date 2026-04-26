# Governance Sidecar Pattern

## Purpose

This extract preserves the strongest `BIND` pattern for RAIDEN: a governance
kit that sits beside a normal product repo rather than restructuring the entire
repo into a ledger-first control plane.

## Observed Structure

Observed high-signal layout:

- a normal product root remains product-shaped
- governance lives under `.governance/`
- the sidecar includes protocol docs, prompt interfaces, tokens, and validator
  tooling
- audits and remediation records live outside the product implementation paths

## Why It Matters To RAIDEN

This is the clearest reviewed example of a repo-adjacent governance sidecar.
It demonstrates that a governed repo can preserve a normal product-facing
structure while still carrying:

- explicit governance rules
- audit protocol
- prompt interfaces
- validation tooling

For RAIDEN, this is strong evidence for a future sidecar-capable toolkit form
that is distinct from the embedded-instance pattern seen in
`HardlinkOrganizer`.

## Reusable Pattern

Preserve these structural ideas:

1. keep governance in a dedicated sidecar subtree
2. let the product repo remain product-shaped
3. give the sidecar its own authority surface and startup docs
4. keep audit and remediation outputs distinct from the main governance kit
5. treat the sidecar as a controlled kit, not as scattered duplicate files

## RAIDEN-Relevant Implication

This pattern is strong evidence for the central toolkit or sidecar-capable form
already recognized in RAIDEN canon.

It is especially useful for future RAIDEN work that needs a deployable kit
without assuming every target repo will adopt a full embedded continuity tree.

## What Not To Reuse Literally

Do not promote directly:

- Starlight or Carbon-specific design-language framing
- duplicated governance content across multiple locations
- product-specific audit history
- domain-specific token sets

## Provenance

- Primary sources from the retired `BIND` snapshot:
  - `reference-repos/BIND/.governance/README.md`
- Supporting sources:
  - `reference-reviews/BIND/REPO_TOOLING_REVIEW.md`
  - `reference-reviews/BIND/IMPORT_CANDIDATES.md`
