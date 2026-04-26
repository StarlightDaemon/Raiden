# Open Loops

## LOOP-0001

- Title: Finish the P1-B continuity canon
- Status: Closed
- Why it matters: RAIDEN now has authority and structure, but its live operating state layer must match the actual project phase.
- Success condition: `CURRENT_STATE.md`, `GOALS.md`, `OPEN_LOOPS.md`, and `DECISIONS.md` fully reflect the completed prototype reviews and synthesis.

## LOOP-0002

- Title: Draft the P1-C support canon
- Status: Closed
- Why it matters: future agents still need canonical prompt indexing, workbook usage, source-history indexing, and toolkit/component mapping.
- Success condition: `PROMPT_ASSET_INDEX.md`, `SOURCE_HISTORY_INDEX.md`, `WORKBOOK.md`, and `TOOLKIT_INDEX.md` all exist in usable canonical form.

## LOOP-0003

- Title: Decide RAIDEN's central-vs-downstream model shape
- Status: Closed
- Why it matters: synthesis shows RAIDEN likely needs both a central toolkit/sidecar surface and a repo-local embedded-instance model.
- Success condition: RAIDEN canon explicitly defines whether both forms will exist and how they relate.

## LOOP-0004

- Title: Determine canonical naming for the repo-local artifact RAIDEN produces
- Status: Closed
- Why it matters: the central tool name was fixed earlier, but the downstream deployed form and managed core also needed canonical naming before toolkit and update-facing work could proceed cleanly.
- Success condition: a canonical downstream naming decision is recorded in `DECISIONS.md`.

## LOOP-0005

- Title: Define the canonical home for prompt assets
- Status: Closed
- Why it matters: synthesis shows strong prompt patterns from `HardlinkOrganizer`, `BIND`, and `CTRL`, but canon has not yet chosen whether prompt assets live at the root, in a toolkit subtree, or both.
- Success condition: `PROMPT_ASSET_INDEX.md` and `REPOSITORY_MAP.md` agree on a stable prompt-home model.

## LOOP-0006

- Title: Define the exception/drift handling model
- Status: Closed
- Why it matters: synthesis surfaced both a simple `EXCEPTIONS` slot and a richer drift-report workflow; RAIDEN should choose one default shape.
- Success condition: canonical exception handling is recorded and mapped to a specific artifact.

## LOOP-0007

- Title: Set a retirement rule for imported prototype snapshots
- Status: Closed
- Why it matters: `reference-repos/` is a temporary evidence layer, and the imported repos are too large to keep indefinitely.
- Success condition: RAIDEN has a clear rule for when a reviewed snapshot is safe to delete while preserving review value.

## LOOP-0008

- Title: Prepare a normalized handoff package for secondary agent review
- Status: Closed
- Why it matters: an outside agent should be able to review the current plan and work without reconstructing context from chat history.
- Success condition: a full-status handoff artifact exists and aligns with the current canon layer.

## LOOP-0009

- Title: Finalize canonical downstream embedded-instance naming
- Status: Closed
- Why it matters: the downstream form needed a fixed canonical name before toolkit indexing and downstream structure work could proceed cleanly.
- Success condition: a downstream embedded-instance name is recorded in `DECISIONS.md` before `TOOLKIT_INDEX.md` and toolkit-subtree drafting proceed.

## LOOP-0010

- Title: Write the prototype snapshot retirement rule
- Status: Closed
- Why it matters: retirement timing is now approved in principle, but the concrete rule still needs to be written before large imported snapshots can be removed safely.
- Success condition: RAIDEN canon contains an explicit retirement rule and the first eligible snapshots can be assessed against it.

## LOOP-0011

- Title: Define the first concrete RAIDEN updater shape
- Status: Closed
- Why it matters: the managed-vs-local update contract is now defined, but RAIDEN still needs a practical delivery/update mechanism such as CLI, bundle import, or drag-and-drop update flow.
- Success condition: RAIDEN canon identifies the first supported updater form and the metadata or manifest expectations that go with it.
- Closed by: first updater MVP implemented and tested under `toolkit/updater/` as a local CLI with `plan` and `apply` commands; recorded as D-0032.

## LOOP-0012

- Title: Materialize the first toolkit structure around the adopted RAIDEN / Edict / RAIDEN Instance / Writ naming stack
- Status: Closed
- Why it matters: naming is now fixed, but the toolkit/component map and future subtree still need to translate that naming into concrete structure and responsibilities.
- Success condition: `TOOLKIT_INDEX.md` defines the first canonical toolkit/component structure using the adopted naming model.

## LOOP-0013

- Title: Expand extracted-reference coverage for high-value prototype repos
- Status: Closed
- Why it matters: the retirement rule depends on preserving useful patterns in canon or `reference-extracts/` before large reviewed snapshots can move toward retirement readiness.
- Success condition: at least the next highest-value repos needed for long-term retention decisions have extracted-reference coverage or an explicit decision that extraction is unnecessary.

## LOOP-0014

- Title: Apply the ingress policy to future external repo intake
- Status: Closed
- Why it matters: the early heavy prototype-import phase should not become the default long-term behavior for RAIDEN.
- Success condition: future repo intake follows `INGRESS_POLICY.md`, with import, review, optional extraction, and retirement handled intentionally rather than ad hoc.
- Closed by: a pre-intake go/no-go gate (§0) added to `INGRESS_POLICY.md` on 2026-04-23; any future import must pass five bounded questions before proceeding, making intake auditable by process rather than only by policy wording.
