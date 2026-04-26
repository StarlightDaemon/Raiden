# RAIDEN Agent Guide

## Project

RAIDEN is the canonical central toolkit/framework repository for reusable AI-agent governance, repository-structure, and execution-support artifacts.

Root-level canonical Markdown files define authority. `toolkit/` is the only explicitly designated canonical implementation subtree.

## Read First

- `README.md`
- `SOURCE_OF_TRUTH.md`
- `REPOSITORY_MAP.md`
- `CURRENT_STATE.md`
- `DECISIONS.md`
- `AGENT_BOUNDARIES.md`
- `MANAGED_VS_LOCAL.md`
- `RELEASE_READY_CHECKLIST.md`

## Important Paths

- `toolkit/` - canonical reusable toolkit/package and instance materials
- `reference-repos/` - imported prototype snapshots; read-only evidence by process
- `reference-reviews/` - comparative analysis and synthesis; not canon unless adopted
- `reference-extracts/` - compact extracted references; still non-canonical unless adopted
- `Source_info/` - preserved source history; not active canon
- `working/` - temporary planning/work bundles; not canon by default

## Conventions

- Prefer concise ASCII Markdown.
- Preserve canonical naming exactly: `RAIDEN`, `Edict`, `RAIDEN Instance`,
  `Writ`.
- Treat root canonical docs as the source of truth unless they explicitly delegate to `toolkit/`.
- Normalize prototype wording before adoption; do not promote imported phrasing by proximity.
- Keep provenance clear when canon is informed by `reference-reviews/` or `reference-extracts/`.
- When a canonical change affects status or structure, update the related continuity docs in the same pass.

## Validation

- No top-level automated test suite is currently present.
- For doc or canon changes, reread touched files against `SOURCE_OF_TRUTH.md`, `REPOSITORY_MAP.md`, `CURRENT_STATE.md`, and the relevant `toolkit/` docs.
- Use targeted search to verify names, paths, and canonical versus non-canonical status stay consistent.
- If a change affects boundaries or release readiness, confirm `AGENT_BOUNDARIES.md`, `MANAGED_VS_LOCAL.md`, and `RELEASE_READY_CHECKLIST.md` still agree.

## Guardrails

- Do not edit `reference-repos/` snapshots unless the operator explicitly asks.
- Do not treat `reference-reviews/`, `reference-extracts/`, or `Source_info/` as canon without explicit adoption.
- Do not rename core canonical terms or change authority order without explicit approval.
- Do not broaden updater-shape canon beyond the current local CLI surface without explicit operator direction and observed need.
- Do not make broad repo-wide rewrites when a bounded doc update is sufficient.

## Workflow

- Start with root canon, then read only the subtree relevant to the task.
- Keep edits narrow, review the exact diff, and validate immediately after each logical change.
- Prefer small targeted patches over sweeping rewrites.
- If Git is available, review `git diff --stat` plus targeted diffs before committing.
- For wider repo changes beyond setup files, ask the operator first.
