# Snapshot Retirement Readiness Assessment

## Purpose

This document assesses whether the current imported snapshots for `CTRL`,
`HardlinkOrganizer`, and `BIND` are ready to move from:

- State 2: extracted reference retained

to:

- State 3: full snapshot retired

The assessment uses `SNAPSHOT_RETIREMENT_RULE.md` as the governing rule.

## Executive Judgment

All three repos are now in the extracted-reference stage, but none should be
retired from `reference-repos/` yet.

Current judgment:

- `CTRL`: closest candidate, but still not ready today
- `HardlinkOrganizer`: not ready
- `BIND`: not ready

The main blocker is not review or extraction coverage. The main blocker is that
active toolkit-surface work and the still-open updater question make raw reread
of these source snapshots still plausible, especially for `HardlinkOrganizer`
and `BIND`.

## Retirement Criteria

Per `SNAPSHOT_RETIREMENT_RULE.md`, a repo is eligible for retirement only when:

1. `REPO_TOOLING_REVIEW.md` exists
2. `IMPORT_CANDIDATES.md` exists
3. the repo is represented in `CROSS_REPO_MATRIX.md`
4. the repo is represented in `CANONICAL_SOURCE_MAP.md`
5. still-needed reusable material is preserved in root canon or
   `reference-extracts/`
6. no open loop still depends on rereading the raw snapshot
7. the operator approves retirement

## Assessment Matrix

| Repo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Current State | Judgment |
|---|---|---|---|---|---|---|---|---|---|
| `CTRL` | Yes | Yes | Yes | Yes | Yes | No | No | State 2 | retain for now |
| `HardlinkOrganizer` | Yes | Yes | Yes | Yes | Partial | No | No | State 2 | retain |
| `BIND` | Yes | Yes | Yes | Yes | Partial | No | No | State 2 | retain |

## Repo Assessments

### `CTRL`

Status:

- review coverage exists
- synthesis coverage exists
- extracted references exist
- raw snapshot still retained

What is preserved well:

- artifact policy
- current-state handoff discipline
- project-structure guidance

Why it is not ready yet:

- `CTRL` is still the first pilot extraction case named directly by the
  retirement rule, so retiring it before the current toolkit/updater phase
  stabilizes would be premature.
- The updater question is still open, and `CTRL` remains one of the strongest
  sources for local artifact-split discipline around durable versus
  session-shaped materials.
- Operator approval has not been given.

Assessment:

- `CTRL` is the closest candidate of the three.
- It should stay in State 2 until updater-shape canon is clearer and RAIDEN has
  higher confidence that the existing extracts fully replace the remaining raw
  reread value.

### `HardlinkOrganizer`

Status:

- review coverage exists
- synthesis coverage exists
- extracted references exist
- raw snapshot still retained

What is preserved well:

- embedded-instance structure
- continuity-file role separation
- prompt-library pattern
- startup/read-order pattern

What still argues for retention:

- `HardlinkOrganizer` remains the strongest practical source for the downstream
  embedded-instance model and continuity-file structure.
- Current toolkit and downstream-shape work still plausibly benefits from raw
  reread of items that were intentionally held for comparison rather than fully
  extracted, such as governance wording, terms control, exception handling, and
  ledger-standard phrasing.
- Open work around updater shape and further toolkit/downstream materialization
  still intersects directly with `HardlinkOrganizer`'s raw repo-local layout.

Assessment:

- `HardlinkOrganizer` clearly belongs in State 2, not State 3.
- Reassess only after more downstream-instance and updater-facing structure is
  stable, or after any remaining still-needed comparison items are either
  extracted or explicitly judged unnecessary.

### `BIND`

Status:

- review coverage exists
- synthesis coverage exists
- extracted references exist
- raw snapshot still retained

What is preserved well:

- governance sidecar pattern
- integration maturity model
- remote audit pattern
- prompt interface
- bounded remediation ledger pattern

What still argues for retention:

- `BIND` remains the strongest source for sidecar governance, maturity-model,
  and remote-audit patterns that still touch open updater/package questions.
- Some useful comparison material was intentionally held rather than fully
  extracted, especially drift-report structure, validator-tooling shape, and
  narrower release-decision artifacts.
- Toolkit and package-surface work may still need raw reread of `.governance/`
  layout decisions before retirement would be prudent.

Assessment:

- `BIND` is not ready for retirement.
- Keep it in State 2 until updater/package canon settles enough that the raw
  snapshot is no longer a likely reread surface.

## Recommended Next Handling

1. Keep all three repos retained in `reference-repos/` for now.
2. Treat `CTRL` as the first re-check candidate after updater-shape canon
   resumes or after one explicit no-reread-needed pass.
3. Retain `HardlinkOrganizer` and `BIND` through the next round of
   updater/package and downstream-instance clarification.
4. Only extract additional material if a current task actually needs it.

## Result

No retirement action is recommended today for:

- `CTRL`
- `HardlinkOrganizer`
- `BIND`

## Addendum: 2026-04-23 Reassessment

### Context Change Since Original Assessment

Since this assessment was written on 2026-04-18:

- `CTRL` was retired from `reference-repos/` on 2026-04-23 after operator
  approval, satisfying all 7 retirement criteria
- updater-shape canon was explicitly deferred by operator direction
- extract sets were completed for both `HardlinkOrganizer` and `BIND`
- no open loop currently depends on rereading either raw snapshot
- the canonical toolkit surface advanced past the active comparison stage

### Updated Assessment Matrix

| Repo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Current State | Judgment |
|---|---|---|---|---|---|---|---|---|---|
| `CTRL` | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Retired | retired 2026-04-23 |
| `HardlinkOrganizer` | Yes | Yes | Yes | Yes | Yes | Yes | No | State 2 | retirement-eligible |
| `BIND` | Yes | Yes | Yes | Yes | Yes | Yes | No | State 2 | retirement-eligible |

### Reassessment Rationale

The original assessment held that raw reread was still plausible because
active toolkit-surface and updater work intersected with these repos'
raw layouts. That blocker has weakened because:

1. updater work is explicitly deferred
2. extract coverage is now complete for the primary patterns
3. canon has advanced to the point where the remaining comparison
   value is marginal rather than active

The remaining marginal reread value (governance wording comparison, terms
control, drift-report structure, sidecar layout details) does not justify
indefinite retention given that extracts and canon now preserve the primary
patterns.

### Updated Recommendation

- `CTRL`: already retired
- `HardlinkOrganizer`: retirement-eligible; recommend operator approval
- `BIND`: retirement-eligible; recommend operator approval

See `REFERENCE_REPO_DISPOSITION_REGISTER.md` for the unified register
covering all repos including those outside this assessment's original scope.

## Addendum: 2026-04-23 Operator Approval And Retirement

Operator approval was later granted on 2026-04-23 for both remaining
retirement-eligible repos in this assessment.

### Final Status Matrix

| Repo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Current State | Judgment |
|---|---|---|---|---|---|---|---|---|---|
| `CTRL` | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Retired | retired 2026-04-23 |
| `HardlinkOrganizer` | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Retired | retired 2026-04-23 |
| `BIND` | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Retired | retired 2026-04-23 |

### Final Note

This assessment's repo set is now fully retired from `reference-repos/`.
