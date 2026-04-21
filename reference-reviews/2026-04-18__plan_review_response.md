# RAIDEN Plan Review Response

## Purpose

This document records a structured response to the external read-only plan review.

It does **not** change canon by itself.
It is a review-response artifact intended to help decide whether and how to update RAIDEN root documents next.

## 1. Acceptance Assessment

### Overall Assessment

The external review is accepted as a strong validation of the current RAIDEN direction.

The review does **not** indicate a structural failure or major contradiction in:

- the authority model
- repository layering
- cross-repo synthesis method
- current P1 sequencing

Instead, it identifies a small set of unresolved design decisions that should be tightened before deeper support-layer canon drafting proceeds.

### Accepted Conclusions

The following conclusions are accepted:

1. The current authority and boundary model is strong.
2. The current source map is defensible.
3. The current short-term plan is broadly correct.
4. The highest-value remaining pre-support-layer decisions are:
   - central vs downstream form
   - prompt asset home
   - downstream embedded-instance naming
5. Snapshot-retirement rules should be formalized before long-term accumulation of search noise.

### Moderated Conclusion

One conclusion should be slightly narrowed:

- downstream naming should **not** block all further canon work
- downstream naming **should** be resolved before:
  - `TOOLKIT_INDEX.md`
  - toolkit subtree materialization
  - final prompt/toolkit placement logic that depends on downstream terminology

So naming is treated as a **support-layer boundary issue**, not a blocker on every remaining continuity update.

## 2. Response To Findings

## Finding 1: Downstream Embedding Naming Causes Ambiguity

### Response

Accepted in substance.

The repo is still using descriptive placeholders for the future repo-local form RAIDEN will support. That is appropriate temporarily, but not sustainable once support-layer canon starts naming toolkit surfaces or downstream templates.

### Planned Handling

- keep placeholders for now in already-existing high-level docs
- resolve canonical downstream naming before finalizing:
  - `TOOLKIT_INDEX.md`
  - downstream template language
  - future toolkit subtree structure

### Outcome

This becomes a real near-term decision, but not an emergency blocker for already-started continuity cleanup.

## Finding 2: Prompt Asset Location Is Undecided

### Response

Accepted fully.

This is the clearest immediate structural blocker before drafting `PROMPT_ASSET_INDEX.md`.

Without a decision on prompt-home location, the index would risk encoding a temporary assumption as if it were structure.

### Planned Handling

Resolve whether prompt assets live:

1. at the root
2. in the future toolkit subtree
3. in both, with different purposes

### Outcome

This should be decided before drafting `PROMPT_ASSET_INDEX.md`.

## Finding 3: Prototype Snapshot Retention Introduces Search Noise

### Response

Accepted, with sequencing adjustment.

The concern is valid, but the repo should not start snapshot retirement too early. Retirement needs a stable threshold so evidence is not discarded before support-layer canon captures the useful patterns cleanly.

### Planned Handling

- define a retirement rule after support-layer canon is drafted
- then retire large snapshots once:
  - review exists
  - import-candidate extraction exists
  - synthesis mapping exists
  - no unresolved reread questions remain

### Outcome

This becomes a **post-P1-C cleanup decision**, not an immediate precondition for further drafting.

## 3. Recommended Decision Set

These decisions are recommended next. They are not yet adopted.

## Proposed Decision A

- Title: RAIDEN supports both a central toolkit form and a downstream embedded-instance form
- Reason:
  - synthesis shows `BIND` and `HardlinkOrganizer` represent different but complementary strengths
  - forcing them into one form too early would flatten useful distinctions
- Proposed effect:
  - RAIDEN canon can explicitly describe:
    - a central toolkit/package/sidecar-capable form
    - a repo-local embedded-instance form for target repos

## Proposed Decision B

- Title: Prompt assets live in a future toolkit subtree as the canonical home, with root-level docs indexing and governing them
- Reason:
  - root canon should define authority and navigation
  - toolkit/prompt assets should remain operationally grouped
  - this avoids mixing too many executable/support assets directly into the root
- Proposed effect:
  - `PROMPT_ASSET_INDEX.md` lives at the root
  - prompt files themselves live in the toolkit/package area once materialized

## Proposed Decision C

- Title: Downstream naming must be resolved before toolkit-index and toolkit-subtree drafting, but not before all continuity-layer work
- Reason:
  - naming matters most once structure and templates start depending on it
  - delaying all continuity work for naming would over-block progress
- Proposed effect:
  - continuity docs may continue using descriptive placeholders briefly
  - support-layer canon and toolkit structure work should not proceed past a certain point without a naming decision

## Proposed Decision D

- Title: RAIDEN defaults to a simple exception record first, with richer drift-report workflow as an optional escalation path
- Reason:
  - `HardlinkOrganizer` provides the more practical default baseline
  - `BIND` provides a useful richer pattern, but it is too heavy as the default
- Proposed effect:
  - default canon would use a light exception/drift record
  - heavier forensic drift reporting can remain available when needed

## Proposed Decision E

- Title: Imported prototype snapshots become eligible for retirement only after support-layer canon and an explicit retirement rule exist
- Reason:
  - avoids premature deletion of source evidence
  - reduces long-term search noise once extraction is complete
- Proposed effect:
  - no immediate deletions
  - explicit cleanup phase after P1-C

## 4. Recommended Immediate Next Sequence

If proceeding from this review response, the recommended sequence is:

1. record a decision on central-vs-downstream dual-form support
2. record a decision on prompt asset home
3. record a decision on downstream naming threshold or actual name
4. record a decision on simple-vs-heavy exception handling baseline
5. continue P1-C support canon with those structural choices fixed
6. define snapshot-retirement rules after support-layer canon exists

## 5. Suggested Review Question For Operator Approval

Before converting any of the above into `DECISIONS.md`, the operator should confirm:

1. whether RAIDEN should explicitly support both central and downstream forms
2. whether prompt assets should canonically live under the future toolkit subtree
3. whether simple exception handling should be the default baseline

## 6. Bottom Line

The external review confirms the current direction.

The correct response is not to reopen the architecture, but to lock a few remaining structural decisions before deeper support-layer drafting proceeds.
