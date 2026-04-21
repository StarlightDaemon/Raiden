# ARC-RC Repo Tooling Review

## 1. Repo Identity

- Repo name: `ARC-RC`
- Snapshot location: `/mnt/e/RAIDEN/reference-repos/ARC-RC`
- Apparent role in lineage: private producer/research repo paired with ARC as the public consumer
- Review framing: stronger than `ARC` as a role-boundary and workflow repo, but still not a full toolkit; most useful as a producer/consumer split and research-ops pattern

## 2. Executive Summary

`ARC-RC` is a **private research-and-generation repo** that sits upstream of `ARC`.

Observed evidence shows:

- a clear backend/research role file in `DEVELOPER_AGENT.md`
- explicit project rules for AI efficiency and artifact handling in `docs/research/AGENT-RULES.md`
- generator, tooling, n8n workflow, schema, and export areas
- policy files for backups and hardcoded-element audits

This makes `ARC-RC` useful to RAIDEN as a source for:

- paired-repo producer/consumer boundary design
- role-specific backend/research agent framing
- project-local agent work rules
- research-result indexing and preservation patterns

It is not a canonical toolkit model. Its governance is fragmented across README, developer-agent instructions, research docs, and policy docs, and some documentation points to `.agent/` and `.gemini/` directories that are missing from the snapshot.

## 3. Artifact Inventory

| Item | Location | Category | Apparent Purpose | Status | Reusability | Notes |
|---|---|---|---|---|---|---|
| Product front page | `README.md` | Navigation artifact | Repo overview, setup, export flow to ARC | Active | Medium | Good producer/consumer overview |
| Developer agent mission | `DEVELOPER_AGENT.md` | Agent-facing artifact | Backend research agent scope, metrics, forbidden actions | Active | High | Strong paired role with ARC |
| Agent work rules | `docs/research/AGENT-RULES.md` | Governance/control artifact | Token efficiency, file hygiene, research delegation rules | Active | High | Strong local agent-rule example |
| Research docs index | `docs/research/README.md` | Navigation artifact | Research and documentation hub | Active | Medium-high | Good knowledge-hub pattern, but references missing dirs |
| Research master index | `docs/research/RESEARCH-INDEX.md` | Navigation + planning artifact | Summaries of research, decisions, and artifacts | Active-historical | High | Strong research-index pattern |
| Hardcoded audit | `docs/policies/HARDCODED-AUDIT.md` | Operational artifact | Specific modularity/drift audit of frontend elements | Active-historical | Medium-high | Useful targeted audit pattern |
| Backup policy | `docs/policies/BACKUP-POLICY.md` | Governance/control artifact | Back up before major edits | Active | Medium | Useful but environment-specific |
| Tooling inventory | `tools/` | Execution-support artifact | Batch research, audits, export, cleanup, migration tools | Active | Medium | Tool-rich operational repo |
| Generator suite | `generators/` | Execution-support artifact | Build/export/hydration generators | Active | Medium | Supports the producer role |
| n8n workflow area | `n8n/` | Operational artifact | Workflow automation and docs | Active | Medium-high | Strong automation surface |
| Sync workflow | `.github/workflows/sync-to-catalog.yml` | Operational artifact | Bridge outputs to catalog repo | Active | Medium-high | Strong producer-to-consumer bridge pattern |
| Schema contract | `schemas/product-collection.schema.json` | Toolkit definition | Output data contract | Active | Medium-high | Useful contract pattern |
| Output zone | `output/` | Operational artifact | Export zone for downstream sync | Active | Medium-high | Clear export boundary |

## 4. Authority Map

### Observed authority surfaces

- `DEVELOPER_AGENT.md`
- `docs/research/AGENT-RULES.md`
- `README.md`
- `docs/research/RESEARCH-INDEX.md`

### Inferred authority order

1. `DEVELOPER_AGENT.md` for agent role and forbidden actions
2. `docs/research/AGENT-RULES.md` for working rules and artifact handling
3. `README.md` for repo architecture and export flow
4. `docs/research/RESEARCH-INDEX.md` and related docs for accumulated knowledge and decision history

### Strong finding

`ARC-RC` is a **workflow-and-research producer repo**, not a control-plane repo. Its governance comes from:

- role definitions
- working rules
- preserved research and implementation knowledge

rather than from a ledger or centralized governance subtree.

## 5. Structural Classification

- Governance/control artifacts:
  - `DEVELOPER_AGENT.md`
  - `docs/research/AGENT-RULES.md`
  - `docs/policies/BACKUP-POLICY.md`
- Agent-facing artifacts:
  - `DEVELOPER_AGENT.md`
- State-tracking artifacts:
  - no dedicated ledger/state stack visible
  - some planning/timeline material in `RESEARCH-INDEX.md`
- Navigation artifacts:
  - `README.md`
  - `docs/research/README.md`
  - `docs/research/RESEARCH-INDEX.md`
  - `n8n/docs/README.md`
- Planning artifacts:
  - `RESEARCH-INDEX.md`
  - targeted audits and guides
- Prompt assets:
  - implied through research docs and external prompt preservation, but not cleanly surfaced in the snapshot
- Toolkit definitions:
  - producer/consumer split with `ARC`
  - schema contract
  - output/sync workflow
- Unknown/unresolved:
  - where the referenced `.agent/` and `.gemini/` artifacts went in this snapshot

## 6. Strengths

### 1. Clear paired-repo role model

Together with `ARC`, this repo forms a very clear split:

- `ARC-RC` generates and validates data
- `ARC` consumes and presents it

That producer/consumer pattern is useful.

### 2. Strong backend/research role definition

`DEVELOPER_AGENT.md` mirrors `ARC`’s role memo well and gives a strong example of a backend/research agent contract.

### 3. Useful local agent work rules

`AGENT-RULES.md` is one of the more concrete imported rule files for:

- minimizing token waste
- separating code from docs
- limiting command output
- saving research prompts/results

### 4. Research preservation pattern

`docs/research/RESEARCH-INDEX.md` and the associated README provide a durable pattern for indexing external research, implementation rationale, and knowledge preservation.

### 5. Clear export boundary

The schema, output zone, and sync workflow make the data handoff to `ARC` explicit.

## 7. Weaknesses, Drift, And Risks

### 1. Documentation drift

`docs/research/README.md` and `RESEARCH-INDEX.md` reference `.agent/` and `.gemini/antigravity/brain/`, but those directories are not present in this snapshot.

That weakens trust in the documentation as a current source of truth.

### 2. Fragmented governance

Useful rules exist, but they are spread across:

- `DEVELOPER_AGENT.md`
- `docs/research/AGENT-RULES.md`
- `docs/policies/`
- README and n8n docs

There is no single authority spine.

### 3. No durable current-state layer

Unlike ledger-style repos, there is no clear always-current state/goals/open work artifact set.

### 4. Operational and research sprawl

The repo has n8n docs, policy docs, tools, generators, and research history. That is useful, but it increases navigation cost.

### 5. Environment-specific backup and path guidance

Some docs assume local backup paths and specific personal workstation layout. Those are not generalizable.

## 8. Reusable Components

### Likely reusable with minimal normalization

- backend/research role mission statement pattern
- agent work rules around artifact hygiene and output minimization
- research index pattern
- producer/consumer export zone pattern
- schema plus sync workflow boundary pattern

### Reusable with moderate normalization

- backup-before-major-edits policy
- targeted audit artifact pattern
- n8n workflow docs organization

### Reusable only with caution

- token-optimization rules as written
- research preservation layout that references hidden sidecar dirs
- direct local path assumptions in backup policy

### Mostly repo-specific or historical

- ARC accessory research workflows
- API/provider specifics
- n8n setup details
- phone/accessory data generation logic

## 9. RAIDEN Import View

### Retain as reference only

- ARC-specific generators and workflows
- accessory research and API details
- environment-specific backup procedures

### Candidate for promotion

- backend/research role memo pattern
- local agent work-rules pattern
- research-index and knowledge-preservation pattern
- output-zone and sync-boundary pattern
- schema-contract pattern

### Candidate for merge with other repos

- merge role-boundary language with `ARC`
- merge research-index ideas with RAIDEN source-history and workbook planning
- compare agent work rules with `CTRL` artifact policy and `BIND` prompt interfaces

### Candidate for deprecation or caution

- treating missing `.agent/` and `.gemini/` references as current truth
- fragmented governance spread across too many surfaces
- importing token-efficiency rules without adapting them to RAIDEN’s operating context

## 10. Bottom-Line Assessment

`ARC-RC` is a useful **producer/research operations reference**, not a canonical toolkit reference.

Its strongest value to RAIDEN is:

- the paired producer/consumer repo model with `ARC`
- the backend/research role memo
- the local work-rules document
- the research-index/knowledge-preservation pattern

It should inform RAIDEN’s role-boundary and artifact-preservation thinking, but it should not be treated as a direct toolkit template.

## 11. Confidence

- Observed evidence:
  - the repo has explicit role, rule, policy, schema, tool, and workflow surfaces
  - there is no ledger/control-plane structure
  - docs reference missing `.agent/` and `.gemini/` directories
- Strong inference:
  - the repo’s main reusable value is producer/research role discipline and knowledge preservation
- Weak inference:
  - some missing research sidecar content may have existed locally but was excluded from the imported snapshot
- Unresolved ambiguity:
  - whether the missing directories were intentionally excluded or represent documentation drift in the live repo
