# Integration Maturity Model Pattern

## Purpose

This extract preserves the `BIND` maturity model for evolving a local
governance kit into a more maintainable managed package.

## Observed Model

Observed three-stage path:

1. vendored local governance kit inside the repo
2. CI or gatekeeper enforcement during active maintenance
3. managed package for long-term reuse and centralized updates

## Why It Matters To RAIDEN

This is one of the strongest reviewed concepts for how RAIDEN should think
about rollout and packaging maturity.

It avoids two weak extremes:

- embedding a governance kit forever until it drifts
- deleting governance scaffolding before a durable replacement exists

## Reusable Pattern

Preserve these ideas:

1. start with a local or vendored form when a project needs immediate access
2. add automated enforcement before scaling usage broadly
3. move to a managed package only after the kit is stable enough to version and
   update centrally
4. treat the package form as the long-term maintenance target, not the first
   requirement

## RAIDEN-Relevant Implication

This pattern is strong evidence for sequencing future RAIDEN toolkit
materialization. It supports current canon that RAIDEN should eventually have a
central toolkit/package form while not forcing premature package publishing
before the deployment contract is ready.

## What Not To Reuse Literally

Do not promote directly:

- npm-specific package names
- Carbon-specific compliance framing
- assumptions that every target repo uses the same frontend stack

## Provenance

- Primary sources:
  - `reference-repos/BIND/.governance/INTEGRATION_STRATEGY.md`
- Supporting sources:
  - `reference-reviews/BIND/REPO_TOOLING_REVIEW.md`
  - `reference-reviews/BIND/IMPORT_CANDIDATES.md`
