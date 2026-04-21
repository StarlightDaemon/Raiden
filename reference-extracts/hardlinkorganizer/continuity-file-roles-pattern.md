# Continuity File Roles Pattern

## Purpose

This extract preserves the `HardlinkOrganizer` pattern of splitting local
continuity into distinct durable files instead of collapsing state, planning,
and history into one running note.

## Observed File Roles

Observed `agent-ledger/` roles:

- `CURRENT_STATE.md`: evidence-based present-tense repo status
- `GOALS.md`: active priorities and intended direction
- `OPEN_LOOPS.md`: the only entry point for new execution work
- `DECISIONS.md`: durable decision record with rationale
- `WORK_LOG.md`: chronological work history
- `EXCEPTIONS.md`: explicit deviations when needed
- `AGENT_LEDGER_STANDARD.md`: local operating standard for evidence and loops

## Why It Matters To RAIDEN

This file-role split is one of the strongest sources behind RAIDEN's own
continuity canon. It demonstrates that local live state becomes more usable
when:

- present status is separated from future goals
- executable work intake is separated from durable decision memory
- chronological history is separated from the current truth

## Reusable Pattern

Preserve these behaviors:

1. current state should describe what is true now, with evidence
2. goals should describe intended priorities, not current facts
3. open loops should gate new work and define closure conditions
4. decisions should explain why a structural choice was made
5. work log should record historical execution without replacing current state

## RAIDEN-Relevant Implication

This pattern remains strong evidence for the local live-state portion of a
future `RAIDEN Instance`.

It is also useful for updater work because it shows which local files are
likely to be preserved as live state rather than treated as managed core.

## What Not To Reuse Literally

Do not promote directly:

- project-specific version and roadmap details
- time-sensitive model-availability records
- product-specific loop scope and milestone names

## Provenance

- Primary sources:
  - `reference-repos/HardlinkOrganizer/agent-ledger/CURRENT_STATE.md`
  - `reference-repos/HardlinkOrganizer/agent-ledger/GOALS.md`
  - `reference-repos/HardlinkOrganizer/agent-ledger/OPEN_LOOPS.md`
  - `reference-repos/HardlinkOrganizer/agent-ledger/DECISIONS.md`
  - `reference-repos/HardlinkOrganizer/agent-ledger/WORK_LOG.md`
  - `reference-repos/HardlinkOrganizer/agent-ledger/AGENT_LEDGER_STANDARD.md`
- Supporting sources:
  - `reference-reviews/HardlinkOrganizer/REPO_TOOLING_REVIEW.md`
  - `reference-reviews/HardlinkOrganizer/IMPORT_CANDIDATES.md`
