# CTRL Import Candidates

## Candidate Summary

| Candidate | Source Path | Apparent Function | Proposed RAIDEN Target | Confidence | Notes |
|---|---|---|---|---|---|
| Local artifact split rule | `agent-ledger/2026-04-13__local_artifact_policy.md` | Separate durable local state from session-shaped reports | future RAIDEN artifact policy / `SOURCE_OF_TRUTH.md` support | High | strongest CTRL contribution |
| Current-state handoff artifact | `reports/2026-03-08__current_state_repo_agent_handoff.md` | Reset new agent to actual current baseline | handoff template / `CURRENT_STATE.md` companion patterns | High | strong practical template |
| Project-space audit pattern | `reports/2026-03-08__project_space_audit.md` | Full workspace baseline and cleanup audit | review template / maintenance audit pattern | Medium-high | useful for repo prep and cleanup |
| Project organization SOP | `docs/PROJECT_SOP.md` | High-quality repo structure and dependency rules | RAIDEN repo standards / future workspace conventions | High | strong structure source |
| Human + agent structure guide | `docs/reference/project_structure_guide.md` | LLM-readable workspace organization standard | historical input for `REPOSITORY_MAP.md` and support docs | Medium-high | early AI-readable framing |
| Handoff artifact style | `reports/2026-04-10__next_main_rebuild_handoff.md` | Bounded follow-on agent handoff | prompt/handoff asset patterns | Medium-high | useful but report-heavy |
| Local closeout note pattern | `agent-ledger/2026-04-10__next_main_rebuild_post_pr_closeout.md` | Durable post-merge closeout checklist | optional local closeout note pattern | Medium | useful for post-merge state tracking |

## Promotion Rules

- Promote the **artifact policy and template logic**, not CTRL’s product or release history.
- Prefer a clearer canonical home for prompts and handoffs than CTRL’s broad `reports/` accumulation.
- Reuse the `agent-ledger/` versus `reports/` distinction, but normalize names for RAIDEN’s artifact hierarchy.
- Do not copy product-specific report cadence or archive volume.

## Promote Soon

- local artifact split rule
- current-state handoff template
- project organization SOP ideas

## Hold For Comparison

- project-space audit pattern
- local closeout note pattern
- prompt-in-reports conventions

## Merge With Existing RAIDEN Material

- merge artifact policy with RAIDEN root authority model
- merge handoff style with `BIND` prompt interfaces
- merge structure guidance with RAIDEN root scaffold and review templates

## Keep As Historical Reference Only

- CTRL release/audit/report history
- browser-extension architecture specifics
- product rebuild and VPN-removal execution artifacts
