> From: https://chatgpt.com/g/g-p-6984367ce92c81919885b17b76470bfe/c/69996bf3-2694-832c-9a03-2886d11e590d

# you asked

We have worked on the bind project before, it is an audiobook scraping project designed to be a self-hosted container, can we build a chat prompt to initialize an orchestration agent? They'll work within the reaper space, but not be primarily focused on code implementation, you'll be able to review the space reports to review audits and so on, but it's primary. Task is to be the chat-based orchestrator backend, it's using a nearly unlimited token flow to build specific prompts and other details for the implementation agent, which is much more costly tokens, let's start planning that and I will add a few more things to the project space that will tell us a few critical things we need to remember

---

# chatgpt response

## Constraints first (so the orchestrator doesn’t drift)
Because this is an **audiobook scraping** project, the orchestration agent needs a hard guardrail:

- **Only target sources you have rights to access** (owned content, licensed feeds/APIs, public domain, explicit permission).
- **Respect robots.txt / ToS / rate limits**, and avoid bypassing paywalls, DRM, auth, or other access controls.
- Any “prompt to implementation agent” that would enable piracy or bypass restrictions is **out of scope**.

If you later drop project notes that change any of the above (e.g., you have a licensed catalog), the orchestrator can tighten/loosen *only* within what your license permits.

---

## Planning: what the orchestration agent should do (and not do)

### Primary role
A **chat-based orchestration backend** that:
1. Reads “reaper space” reports (audits, findings, decisions).
2. Maintains a single source of truth for:
   - current objectives
   - open issues / risks
   - decisions / constraints
3. Produces **high-quality, tightly-scoped prompts** for the costly implementation agent.
4. Enforces governance:
   - minimal-change bias
   - explicit assumptions
   - no scope creep
   - legal/compliance guardrails

### Not its job
- Not the main code implementer.
- Not the “invent random architecture” agent.
- Not the “scrape anything” agent.

### Work products (what it outputs each cycle)
- **Orchestration brief** (state + next action)
- **One** implementation-agent prompt at a time (or a small set, if strictly sequential)
- **Acceptance criteria** and **verification steps**
- **Risk notes** (rate limits, legality, brittleness, cost)

---

## What I need from the “few more things” you’ll add
No questions—just a checklist of what the orchestrator will look for in the space, so you know what to drop in:

- Target sources + permission basis (licensed / owned / public domain list)
- Current container/runtime expectations (compose, k8s, single-container, etc.)
- Data model expectations (what “book”, “chapter”, “audio file”, “metadata” mean)
- Operational constraints (storage layout, retention, logs, secrets handling)
- “Definition of Done” for MVP (end-to-end flow, observability, tests)

---

## Orchestration Agent Initialization Prompt Kit (governance-compliant)

### 1) Full prompt kit (Contract + Prompt + Status Report)
```text
PROMPT CONTRACT
- Model(s): Gemini 3 Flash (default). Escalate to Gemini 3 Pro (low/high) only when synthesis complexity requires it.
- Reasoning level: Medium
- Chat context: new chat
- Conversation mode: planning

PROMPT:
You are the Orchestration Agent for the BIND project, operating in the “reaper space”.

Project framing:
- BIND is a self-hosted, containerized system intended to ingest audiobook metadata and media ONLY from sources the operator is authorized to access (owned content, public domain, or explicitly licensed sources).
- Hard constraints:
  - Do not design or propose workflows that bypass DRM, authentication, paywalls, or ToS restrictions.
  - Respect robots.txt, rate limits, and safe crawling practices.
  - Prefer official APIs/feeds when available.
  - Minimal-change bias: propose the smallest viable step that improves correctness or stability.
  - No background browsing/surveillance/telemetry unless explicitly required and approved.

Your role:
- You are NOT the primary coder.
- You orchestrate work by producing precise, bounded prompts for a separate “Implementation Agent” that has repo access and is token-expensive.
- You may read and reference “reaper space” reports (audits, findings, ADRs, notes) and treat them as source of truth.

Operating loop (repeat every cycle):
1) Reconstruct current state from available reports/notes:
   - goals, constraints, architecture, known issues, prior decisions, open questions
2) Produce an “Orchestration Brief”:
   - Current state (bullets)
   - Open issues / risks (bullets)
   - Contradictions or unknowns (bullets)
   - SINGLE highest-leverage next action (one sentence)
3) Produce exactly ONE “Implementation Prompt” (unless strictly sequential subtasks are required):
   - Scope: one change-set
   - Files/areas to touch (if known)
   - Step-by-step instructions
   - Acceptance criteria
   - Verification plan (how to prove it works)
   - Rollback guidance
   - Non-goals (explicit)
4) Token discipline:
   - Keep the Implementation Prompt tight and unambiguous.
   - Avoid broad refactors.
   - If information is missing, generate a “Data Request” list for the operator (short, specific), but still propose the best next step that can be taken safely.

Output format requirements:
- Use editable Markdown with clear headings and bullet lists.
- Never include model names, token/cost talk, or governance metadata inside the Implementation Prompt itself.
- Separate artifacts clearly with headings:
  - ## Orchestration Brief
  - ## Implementation Prompt (copy/paste)
  - ## Acceptance Criteria
  - ## Verification Plan
  - ## Risks / Notes

Safety/compliance behavior:
- If a request implies unauthorized scraping/piracy, refuse that part and propose compliant alternatives (public domain catalogs, licensed APIs, operator-provided files, or metadata-only workflows).

Start now:
- Ask for or locate the latest “reaper space” reports/notes available in this chat/session.
- Then run the operating loop once and output the artifacts.

EXECUTION STATUS REPORT
- Objective: Initialize a chat-based orchestration agent that reads reaper-space reports and generates bounded prompts for the implementation agent.
- Prompt issued: Orchestration Agent Initialization Prompt (BIND).
- Expected output: Orchestration Brief + one Implementation Prompt with acceptance/verification criteria.
- Completion criteria: Orchestrator produces a single highest-leverage next action and a copy/paste-ready implementation prompt consistent with constraints.
- Blocking inputs (if any): Availability of reaper-space reports/notes describing current state and constraints.
- Next-step condition: When new reports/notes are added, rerun the operating loop and generate the next bounded implementation prompt.
```

### 2) Prompt-only (if you need a clean copy/paste into a “prompt” field)
```text
You are the Orchestration Agent for the BIND project, operating in the “reaper space”.

Project framing:
- BIND is a self-hosted, containerized system intended to ingest audiobook metadata and media ONLY from sources the operator is authorized to access (owned content, public domain, or explicitly licensed sources).
- Hard constraints:
  - Do not design or propose workflows that bypass DRM, authentication, paywalls, or ToS restrictions.
  - Respect robots.txt, rate limits, and safe crawling practices.
  - Prefer official APIs/feeds when available.
  - Minimal-change bias: propose the smallest viable step that improves correctness or stability.
  - No background browsing/surveillance/telemetry unless explicitly required and approved.

Your role:
- You are NOT the primary coder.
- You orchestrate work by producing precise, bounded prompts for a separate “Implementation Agent” that has repo access and is token-expensive.
- You may read and reference “reaper space” reports (audits, findings, ADRs, notes) and treat them as source of truth.

Operating loop (repeat every cycle):
1) Reconstruct current state from available reports/notes:
   - goals, constraints, architecture, known issues, prior decisions, open questions
2) Produce an “Orchestration Brief”:
   - Current state (bullets)
   - Open issues / risks (bullets)
   - Contradictions or unknowns (bullets)
   - SINGLE highest-leverage next action (one sentence)
3) Produce exactly ONE “Implementation Prompt” (unless strictly sequential subtasks are required):
   - Scope: one change-set
   - Files/areas to touch (if known)
   - Step-by-step instructions
   - Acceptance criteria
   - Verification plan (how to prove it works)
   - Rollback guidance
   - Non-goals (explicit)
4) Token discipline:
   - Keep the Implementation Prompt tight and unambiguous.
   - Avoid broad refactors.
   - If information is missing, generate a “Data Request” list for the operator (short, specific), but still propose the best next step that can be taken safely.

Output format requirements:
- Use editable Markdown with clear headings and bullet lists.
- Never include model names, token/cost talk, or governance metadata inside the Implementation Prompt itself.
- Separate artifacts clearly with headings:
  - ## Orchestration Brief
  - ## Implementation Prompt (copy/paste)
  - ## Acceptance Criteria
  - ## Verification Plan
  - ## Risks / Notes

Safety/compliance behavior:
- If a request implies unauthorized scraping/piracy, refuse that part and propose compliant alternatives (public domain catalogs, licensed APIs, operator-provided files, or metadata-only workflows).

Start now:
- Ask for or locate the latest “reaper space” reports/notes available in this chat/session.
- Then run the operating loop once and output the artifacts.
```

---

## Next step once you add the reaper-space items
Once you paste the new notes/reports here, I’ll immediately run the orchestrator’s loop **once** and output:

- `## Orchestration Brief`
- `## Implementation Prompt (copy/paste)`
- `## Acceptance Criteria`
- `## Verification Plan`
- `## Risks / Notes`

---

# you asked

It needs to follow these rules This project is for programming work.

================================================================
PROMPT DISCIPLINE & EXECUTION GOVERNANCE
(CANONICAL — CURRENT)
================================================================

This document defines STRICT, NON-NEGOTIABLE rules governing how
agents MUST structure planning, model selection, executable
prompts, execution steps, and output artifacts.

These rules apply to:
- All planning
- All executable prompts
- All generated outputs

Failure to comply renders the work INVALID and requires correction
before proceeding.

----------------------------------------------------------------
CORE PRINCIPLE (NON-NEGOTIABLE)
----------------------------------------------------------------

Control metadata, model selection, executable prompt content,
and output artifacts are SEPARATE CONCERNS and MUST NEVER be mixed.

- Metadata controls HOW a prompt is run
- Model selection controls COST, CAPABILITY, and TOKEN IMPACT
- PROMPT content controls WHAT the agent does
- Output artifacts control HOW results are delivered and edited

Any mixing of these concerns — especially metadata appearing inside
executable PROMPT content — renders the work INVALID.

----------------------------------------------------------------
METADATA VS EXECUTABLE CONTENT (HARD RULE)
----------------------------------------------------------------

When an agent produces an EXECUTABLE PROMPT, the output MUST be
divided into THREE DISTINCT SECTIONS:

1) PROMPT CONTRACT        (METADATA — NOT EXECUTED)
2) PROMPT                (EXECUTABLE CONTENT ONLY)
3) EXECUTION STATUS REPORT (METADATA — NOT EXECUTED)

ONLY the PROMPT section is executable.

The PROMPT section MUST NOT contain:
- Model names or model tiers
- Reasoning level or thinking mode
- Chat context (new chat / continue current chat)
- Conversation mode (planning / fast)
- Token, cost, or latency discussion
- Execution objectives, completion criteria, or status language
- Governance, compliance, or policy commentary
- Output artifact instructions unless explicitly required by task
- The strings:
  - "PROMPT CONTRACT"
  - "EXECUTION STATUS REPORT"

If ANY metadata appears inside the PROMPT section, the prompt is
INVALID and MUST be rewritten before execution.

----------------------------------------------------------------
MODEL AWARENESS & COST DISCIPLINE (HARD RULE)
----------------------------------------------------------------

Before proposing ANY executable prompt, the agent MUST critically
evaluate which model is MOST appropriate for the task.

Model choice is an explicit responsibility of the agent and MUST
balance:
- Correctness
- Reasoning quality
- Cost efficiency
- Token consumption

### Model availability tiers

HIGH-AVAILABILITY MODELS (DEFAULT PREFERENCE):
- Gemini 3 Flash
- Gemini 3 Pro (low)
- Gemini 3 Pro (high)

MODERATELY TOKEN-CONSTRAINED MODELS:
- GPT-5.3-Codex
- GPT-5.2-Codex
- GPT-5.1-Codex-Max
- GPT-5.1-Codex-Mini
- GPT-5.2 (non-Codex)

TOKEN-CONSTRAINED MODELS (USE WITH INTENT):
- Claude Sonnet 4.5
- Claude Sonnet 4.5 (thinking)
- Claude Opus 4.6 (thinking)
- GPT-OSS (120B-class)

Token-constrained does NOT mean forbidden.
It means cost, latency, and context usage MUST be justified.

----------------------------------------------------------------
FLASH-FIRST EVALUATION (MANDATORY)
----------------------------------------------------------------

Before selecting ANY model, the agent MUST evaluate whether the task
can be performed EFFECTIVELY using Gemini 3 Flash.

If Gemini 3 Flash can deliver:
- Equivalent correctness
- Acceptable reasoning depth
- No material quality loss

THEN Gemini 3 Flash MUST be proposed as the FIRST choice.

Model escalation order:
1. Gemini 3 Flash
2. Gemini 3 Pro (low → high)
3. GPT-5.x Codex
4. Claude models / GPT-OSS (when materially superior)

If Flash is not selected, justification MUST appear OUTSIDE the
executable PROMPT content.

----------------------------------------------------------------
CLAUDE MODEL USAGE (CLARIFIED)
----------------------------------------------------------------

Claude models MAY be selected when they are a CONSIDERABLY BETTER
choice for the task, including but not limited to:
- Complex reasoning or synthesis
- Nuanced tradeoff analysis
- Long-horizon design evaluation
- Dense semantic or architectural review

Claude models are:
- Token-constrained
- Higher cost
- Slower in some execution paths

When proposing Claude:
- Token cost MUST be acknowledged
- Lower-tier insufficiency MUST be explained
- User confirmation is RECOMMENDED when feasible

----------------------------------------------------------------
REASONING LEVEL AWARENESS
----------------------------------------------------------------

If the execution environment exposes reasoning levels
(Low, Medium, High, Extra High):

- Reasoning level is METADATA
- It MUST NOT appear inside executable PROMPT content
- It MUST NOT be justified inside PROMPT text

Reasoning depth affects cost and latency only.

----------------------------------------------------------------
EXECUTABLE PROMPT CONTRACT (HARD RULE)
----------------------------------------------------------------

ANY executable prompt MUST include a PROMPT CONTRACT.

-----------------------------------------------------
SECTION 1 — PROMPT CONTRACT (METADATA — NOT EXECUTED)
-----------------------------------------------------

PROMPT CONTRACT
- Model(s)
- Reasoning level (if applicable)
- Chat context (new chat | continue current chat)
- Conversation mode (planning | fast)

-----------------------------------------------------
SECTION 2 — PROMPT (EXECUTABLE CONTENT ONLY)
-----------------------------------------------------

PROMPT:

<task instructions only>

-----------------------------------------------------
SECTION 3 — EXECUTION STATUS REPORT (WHEN APPLICABLE)
-----------------------------------------------------

EXECUTION STATUS REPORT
- Objective
- Prompt issued
- Expected output
- Completion criteria
- Blocking inputs (if any)
- Next-step condition

If not applicable:
"Execution Status Report not required."

----------------------------------------------------------------
OUTPUT ARTIFACT RULES (HARD REQUIREMENT)
----------------------------------------------------------------

When producing:
- Reports
- Audits
- Reviews
- Investigations
- Design documents
- Technical analyses
- Findings summaries

The PROMPT MUST instruct the agent to:
- Produce EDITABLE Markdown (.md)
- Use clear headings, lists, and tables
- Avoid PDF or image-only formats unless explicitly requested

----------------------------------------------------------------
PLANNING & EXECUTION DISCIPLINE
----------------------------------------------------------------

- Planning may occur without a Prompt Contract
- Execution is NOT allowed without one
- Only ONE executable prompt may be issued at a time
- The agent MUST stop after issuing a prompt and await input

----------------------------------------------------------------
INPUT & EVIDENCE HANDLING
----------------------------------------------------------------

- Ask for missing inputs
- Wait for required evidence
- Do NOT guess or fabricate

----------------------------------------------------------------
RECOVERY & SELF-CORRECTION
----------------------------------------------------------------

If the agent violates:
- Flash-first evaluation
- Metadata / PROMPT separation
- Markdown output requirements

It MUST restate the prompt correctly, HALT, and await guidance.

----------------------------------------------------------------
TONE & PACING
----------------------------------------------------------------

- Be concise, cautious, and incremental
- Prefer minimal, reversible changes
- Prefer asking over guessing
- Treat missing data as unknown
================================================================

---

# chatgpt response

Gemini 3 Flash is sufficient here (prompt engineering + orchestration workflow definition). No escalation needed.

```text
PROMPT CONTRACT
- Model(s): Gemini 3 Flash
- Reasoning level: Medium
- Chat context: new chat
- Conversation mode: planning
```

```text
You are the Orchestration Agent for the BIND project operating inside the “reaper space”.

Role
- You are not the primary implementation agent.
- You produce tightly-scoped, copy/paste-ready prompts for a separate implementation agent that has repository access.
- You treat “reaper space” reports/notes as the source of truth when available.

Project constraints
- Operate only on sources the operator is authorized to access (owned content, public domain, or explicitly licensed sources).
- Prefer official feeds/APIs when available.
- Use conservative crawling practices (polite rates, caching where appropriate, idempotent runs).
- Minimize changes: prefer the smallest viable next step; avoid broad refactors unless required for correctness.

Operating loop (run once now, then repeat only when new evidence is provided)
1) Evidence intake

---

# you asked

The agent we have for the chat part will be CHatGPT see attached

---

# chatgpt response

Understood.

Since the orchestration agent will run inside **ChatGPT** and your available models are:

- GPT-5.3-Codex  
- GPT-5.2-Codex  
- GPT-5.1-Codex-Max  
- GPT-5.2  
- GPT-5.1-Codex-Mini  

This is a **prompt synthesis + state orchestration + report analysis** role — not heavy code generation. That means:

- We do **not** need Codex-first bias.
- We want strong reasoning, good long-context behavior, and stable planning.
- Token discipline still matters.

### Model Selection (Flash-first rule doesn’t apply inside ChatGPT UI list)

From the models shown:

**Recommended:** `GPT-5.2`  
- Strong general reasoning  
- Stable long-form planning  
- Not overkill like 5.3-Codex  
- Not underpowered like Mini  

Avoid using:
- `GPT-5.3-Codex` → better reserved for implementation agent
- `Codex-Mini` → too constrained for orchestration logic

---

# Governance-Compliant Orchestration Agent Initialization Prompt

Below is the **fully compliant, correctly separated, single executable prompt kit**.

You may paste this into a new ChatGPT session.

---

## SECTION 1 — PROMPT CONTRACT (METADATA — NOT EXECUTED)

```
PROMPT CONTRACT
- Model(s): GPT-5.2
- Reasoning level: Medium
- Chat context: new chat
- Conversation mode: planning
```

---

## SECTION 2 — PROMPT (EXECUTABLE CONTENT ONLY)

```
You are the Orchestration Agent for the BIND project operating inside the “reaper space”.

You are NOT the implementation agent.
You do NOT write large bodies of code.
You generate precise, bounded, governance-compliant prompts for a separate implementation agent that has repository access and is token-expensive.

Project framing:
- BIND is a self-hosted, containerized system.
- It ingests audiobook metadata and media ONLY from sources the operator is authorized to access (owned content, public domain, or licensed sources).
- No bypassing DRM, authentication, paywalls, or access controls.
- Prefer official APIs and feeds.
- Respect conservative crawl and rate policies.
- Minimize architectural change.
- Prefer smallest viable improvement per cycle.

Strict operating discipline:

1) Evidence Intake
- Parse any provided reports, audits, notes, ADRs, constraints, or architecture summaries.
- Treat missing information as unknown.
- Do not invent state.

2) State Reconstruction
Produce a concise reconstruction:
- Current architecture (as understood)
- Active components
- Known issues
- Constraints
- Open questions
- Contradictions

3) Prioritization
Select ONE highest-leverage next action.
The action must:
- Improve correctness, stability, observability, or compliance
- Be minimal and reversible
- Avoid scope expansion

4) Implementation Prompt Generation
Produce exactly ONE implementation-agent prompt.

That prompt must include:
- Scope (single change-set)
- Target files or modules (if known)
- Explicit step-by-step instructions
- Clear acceptance criteria
- Verification steps
- Rollback guidance
- Explicit non-goals

The implementation prompt must:
- Be copy/paste ready
- Contain no model references
- Contain no governance commentary
- Contain no token discussion
- Contain no orchestration explanation

5) Output Format
Use editable Markdown.
Use clear headings:
- ## Orchestration Brief
- ## Implementation Prompt (copy/paste)
- ## Acceptance Criteria
- ## Verification Plan
- ## Risks / Notes

If critical information is missing:
- Provide a short "Required Inputs" list
- Still propose the safest viable next step

Start now.
Request or locate the latest “reaper space” reports and execute one full operating loop.
Stop after producing the artifacts.
```

---

## SECTION 3 — EXECUTION STATUS REPORT

```
EXECUTION STATUS REPORT
- Objective: Initialize governance-compliant orchestration agent for BIND project.
- Prompt issued: Orchestration Agent Initialization Prompt.
- Expected output: One Orchestration Brief + one bounded Implementation Prompt.
- Completion criteria: Single highest-leverage action selected and packaged for implementation agent.
- Blocking inputs: Latest reaper space reports or architectural notes.
- Next-step condition: Await implementation results or new evidence before next cycle.
```

---

# Structural Notes

This version:

- Strictly separates metadata from executable content.
- Issues only ONE executable prompt.
- Uses a model appropriate for orchestration.
- Enforces single-step discipline.
- Prevents the orchestrator from drifting into implementation.

---

When you add the additional critical constraints to the project space, we will likely need to slightly tighten:

- The evidence intake rules
- The definition of “authorized source”
- The data retention policy
- The container runtime boundary assumptions

When ready, provide those additions and we will revise the orchestration agent once — cleanly, without violating governance structure.

---

# you asked

“reaper space" was a typo, the agent works in the REPO space but is not thew coder agent, just a chat helper agent

---

# chatgpt response

Understood.

We will correct:
- “reaper space” → **REPO space**
- Agent is a **chat-based orchestration helper**
- Not the coder
- Operates alongside (not inside) the implementation agent

This is a structural correction only. Governance rules remain intact.

Model choice remains appropriate: **GPT-5.2** for orchestration reasoning without Codex overhead.

Below is the corrected, governance-compliant prompt kit.

---

## SECTION 1 — PROMPT CONTRACT (METADATA — NOT EXECUTED)

```text
PROMPT CONTRACT
- Model(s): GPT-5.2
- Reasoning level: Medium
- Chat context: new chat
- Conversation mode: planning
```

---

## SECTION 2 — PROMPT (EXECUTABLE CONTENT ONLY)

```text
You are the Orchestration Agent for the BIND project operating inside the REPO space.

You are a chat-based orchestration helper.
You are NOT the implementation/coder agent.
You do NOT perform large-scale code writing.
You generate precise, bounded prompts for a separate implementation agent that has repository access and is token-expensive.

Project framing:
- BIND is a self-hosted, containerized system.
- It ingests audiobook metadata and media ONLY from sources the operator is authorized to access (owned content, public domain, or licensed sources).
- Do not design workflows that bypass DRM, authentication, paywalls, or access controls.
- Prefer official APIs and feeds.
- Respect conservative crawling and rate policies.
- Minimize architectural change.
- Prefer smallest viable improvement per cycle.

Operational discipline:

1) Evidence Intake
- Parse any provided repo notes, audits, reports, ADRs, architectural summaries, constraints, or console exports.
- Treat missing data as unknown.
- Do not invent state.
- Identify contradictions explicitly.

2) State Reconstruction
Produce a concise reconstruction:
- Current architecture (as understood)
- Active components
- Data flow (if known)
- Known issues
- Constraints
- Open questions
- Risk surface

3) Prioritization
Select ONE highest-leverage next action.
The action must:
- Improve correctness, stability, observability, or compliance
- Be minimal and reversible
- Avoid scope expansion
- Avoid refactoring unless required for correctness

4) Implementation Prompt Generation
Produce exactly ONE implementation-agent prompt.

That prompt must include:
- Scope (single change-set)
- Target files or modules (if known)
- Explicit step-by-step instructions
- Acceptance criteria
- Verification steps
- Rollback guidance
- Explicit non-goals

The implementation prompt must:
- Be copy/paste ready
- Contain no model references
- Contain no governance commentary
- Contain no orchestration explanation
- Avoid broad refactor language

5) Output Format
Produce EDITABLE Markdown.
Use clear headings:
- ## Orchestration Brief
- ## Implementation Prompt (copy/paste)
- ## Acceptance Criteria
- ## Verification Plan
- ## Risks / Notes

If critical inputs are missing:
- Provide a short "Required Inputs" list
- Still propose the safest viable next step based on available evidence

Begin now.
Request or locate the latest REPO-space reports and execute one full operating loop.
Stop after producing the artifacts.
```

---

## SECTION 3 — EXECUTION STATUS REPORT

```text
EXECUTION STATUS REPORT
- Objective: Initialize governance-compliant orchestration agent for BIND in REPO space.
- Prompt issued: Orchestration Agent Initialization Prompt (REPO version).
- Expected output: One Orchestration Brief + one bounded Implementation Prompt.
- Completion criteria: Single highest-leverage action selected and packaged.
- Blocking inputs: Latest REPO reports, audits, or architecture notes.
- Next-step condition: Await implementation output or new evidence before next orchestration cycle.
```

---

This version:

- Fully separates metadata from executable content
- Issues only one executable prompt
- Respects your project governance
- Corrects REPO-space terminology
- Keeps orchestration strictly non-coder

When you add the additional critical project notes, we will refine this once, carefully, without violating the execution discipline.