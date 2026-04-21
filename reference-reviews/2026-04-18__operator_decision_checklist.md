# Operator Decision Checklist

## Purpose

This checklist turns the current review response into a small set of operator decisions that should be resolved before deeper support-layer canon drafting.

These decisions are not active until adopted into `DECISIONS.md`.

## Decision 1: Dual-Form RAIDEN Model

### Question

Should RAIDEN explicitly support both:

- a **central toolkit/package/sidecar-capable form**
- and a **downstream repo-local embedded-instance form**

### Recommended Answer

Yes.

### Why

- synthesis shows `BIND` and `HardlinkOrganizer` contribute different but complementary strengths
- forcing one model too early would flatten useful distinctions

### Approval Slot

- Status: `Approve / Reject / Revise`
- Operator note:

## Decision 2: Canonical Home For Prompt Assets

### Question

Where should canonical prompt assets live?

Options:

- `A` root of RAIDEN
- `B` future toolkit subtree, with root-level indexing docs
- `C` both, with different purposes

### Recommended Answer

`B` future toolkit subtree, with root-level indexing docs

### Why

- keeps root canon focused on authority, navigation, and state
- keeps operational prompt assets grouped with toolkit/package structure
- avoids cluttering the root with too many executable/support artifacts

### Approval Slot

- Status: `Approve / Reject / Revise`
- Operator note:

## Decision 3: Downstream Naming Timing

### Question

When must the downstream embedded-instance name be finalized?

Options:

- `A` before any more drafting
- `B` before `TOOLKIT_INDEX.md` and toolkit-subtree drafting
- `C` only when implementation starts

### Recommended Answer

`B` before `TOOLKIT_INDEX.md` and toolkit-subtree drafting

### Why

- naming matters once toolkit structure and templates depend on it
- requiring it before all continuity/support work would over-block progress

### Approval Slot

- Status: `Approve / Reject / Revise`
- Operator note:

## Decision 4: Default Exception Handling Shape

### Question

What should RAIDEN use as the default exception/drift handling model?

Options:

- `A` simple exception record first, richer drift reporting only when needed
- `B` richer drift-report workflow by default

### Recommended Answer

`A` simple exception record first, richer drift reporting only when needed

### Why

- `HardlinkOrganizer` provides the more practical baseline
- `BIND` provides a stronger escalation model, but it is too heavy as the default

### Approval Slot

- Status: `Approve / Reject / Revise`
- Operator note:

## Decision 5: Snapshot Retirement Timing

### Question

When should large imported prototype snapshots become eligible for removal from `reference-repos/`?

### Recommended Answer

After:

1. support-layer canon exists
2. a retirement rule is written
3. the repo has:
   - a completed review
   - import candidates
   - synthesis coverage
   - no unresolved reread questions

### Why

- prevents premature evidence loss
- reduces long-term search noise once extraction is complete

### Approval Slot

- Status: `Approve / Reject / Revise`
- Operator note:

## Recommended Response Format

Reply in a compact format such as:

```text
Decision 1: Approve
Decision 2: Approve
Decision 3: Revise -> A
Decision 4: Approve
Decision 5: Approve
Notes: ...
```
