# Prompt Governance

## Purpose

This document defines the working rules for central shared prompt assets under
`toolkit/prompts/`.

It governs:

- what may enter the shared prompt layer
- how prompt surfaces are classified
- how prompts should be written
- how prompt changes should be introduced
- what must remain outside the central prompt surface

It does not define package manifests, updater metadata, or downstream prompt
folder names.

## Core Rule

A prompt belongs in the central shared layer only when it is reusable across
more than one repo, task family, or operator workflow.

If a prompt depends on a specific repo's:

- filesystem layout
- live continuity state
- local tools
- local exceptions
- project identity

it belongs in a downstream local layer instead.

## Execution Assumptions

Central shared prompts should assume:

- token limits may be opaque
- agents may not know current context usage or remaining headroom
- work is often model-bound for the duration of a cycle
- mid-cycle model switching must not be required for success
- continuation should rely on compact artifacts, not raw chat replay

Therefore:

- bound scope before broad reads or edits
- prefer one model set per cycle
- choose the model and reasoning level at the start of the cycle when the
  environment requires that choice up front
- do not assume the active agent can switch model or reasoning level mid-run
- define stop conditions for non-trivial work
- require pause-point export before model handoff when handoff is allowed
- keep continuation payloads compact and stable

## Reasoning Escalation Rule

When the active environment exposes selectable model or reasoning levels,
central shared prompts should prefer:

- one bounded first pass at a moderate reasoning level
- explicit escalation only after observed failure, contradiction, premature
  stopping, or repeated rerun pressure
- changing the next pass rather than repeating the same weak pass several times

This rule exists because several partial reruns can cost more than one stronger
follow-up pass.

This is a progression rule, not a single-provider default.

When prompts rely on selectable models or reasoning levels, they should prefer:

- one named baseline profile for the active host environment
- a clear next-step escalation path after material failure
- host-local model choices rather than pretending one vendor default fits every
  environment
- optional cheaper first-pass checkers only when the task is high-frequency,
  low-risk, or explicitly designed for staged escalation

Host-specific execution profiles may be added in prompt surfaces or companion
docs when they are stable enough to matter operationally.

Example OpenAI-hosted baseline today:

- start with `gpt-5.4` at `medium` reasoning for important text, continuity,
  and mixed reasoning/coding work
- escalate the next pass to a higher reasoning level only when the prior pass
  fails materially

Prompts that rely on this pattern should name:

- the active host profile when known
- the starting model and reasoning level when known
- whether model/reasoning selection is fixed for the whole run
- what counts as failure
- when the next pass should escalate instead of rerunning unchanged

If the host environment binds the agent to one model and reasoning level for
the duration of a run, prompts should say so explicitly and require selection
at the start rather than implying later switching is available.

## Target-Agent Selection Rule

When a task may be delegated to more than one available agent model, `RAIDEN`
should first choose the best target agent for that specific task before
building the execution prompt.

Do not default to a model-agnostic prompt when the real operating decision is
which concrete agent should run the work.

Selection should consider at least:

- task type: review, planning, implementation, audit, or mixed work
- required context depth
- expected ambiguity level
- required caution level
- whether the pass is fast triage or deeper planning/build work
- whether the target agent is stronger at long-context review, bounded
  implementation, or concise synthesis in the active host environment

After selection:

- name the chosen target agent model in the wrapper metadata
- name the chosen reasoning level in the wrapper metadata
- explain briefly why that target is preferred over the obvious alternatives
- build the copyable prompt body for that specific target pass, not for a vague
  generic agent

This does not require provider-specific wording in the executable prompt body.
It means the wrapper artifact should be intentionally tuned for a defined
target agent rather than pretending all agents are equally appropriate.

Use model-agnostic prompt files only when:

- the prompt is a reusable base template, or
- the task truly does not benefit from target-specific tuning

For task-specific working prompts, prefer:

1. target-agent review by `RAIDEN`
2. explicit target-model selection
3. tuned prompt for that chosen agent

## Surface Standard

RAIDEN uses a two-tier language standard for prompt work.

### Tier 1: Durable Readable Language

Use readable language for:

- long-lived repo artifacts
- human review surfaces
- policy and governance
- adoption notes
- final summaries

### Tier 2: Compressed Machine-Oriented Language

Use compressed language for:

- internal prompts
- scoped execution instructions
- pause-point exports
- continuation packages
- validation checks
- transient orchestration directives

### Mixed-Surface Rule

Some files are durable readable Markdown wrappers around compressed internal
prompt bodies.

In mixed-surface files:

- keep headings, purpose, and notes readable
- keep the executable template body compact when safe
- do not classify the whole file by the loudest style inside it

## Shared Prompt Categories

The current central categories are:

- bounded task templates
- compact task templates
- handoff templates
- pause-point templates
- continuation-state templates
- completion templates
- validation templates
- compact review templates
- audit/review templates

Future central categories may include:

- operator-facing kickoff prompts

Only add a new category when it represents a stable reusable task shape rather
than one session's wording.

## Authoring Rules

Shared prompts should be:

- short enough to scan quickly
- explicit about outcome and boundaries
- robust against scope drift
- neutral about one repo's naming or toolchain
- explicit about whether the active surface is readable, compressed, or mixed
- explicit about the recommended starting model/reasoning profile when the host
  environment makes that operationally important

Shared prompts should not:

- assume one project's file paths
- mix execution instructions with large status reports
- encode local exceptions as if they were global defaults
- carry product-specific branding or ecosystem assumptions

## Compressed Internal Standard

Compressed internal prompts should prefer:

- short imperative statements
- explicit scope markers
- dense constraint packing
- stable field labels
- short validation statements
- direct stop conditions

Compressed internal prompts should avoid:

- conversational padding
- motivational language
- repeated framing
- long transitions
- redundant restatement of known constraints

Approved stable labels:

- `Mode`
- `Obj`
- `Scope`
- `Read`
- `Do`
- `No`
- `Val`
- `Stop`
- `Out`
- `Phase`
- `Done`
- `Open`
- `Dec`
- `Blk`
- `Next`
- `Alt`
- `Trim`

Guardrails:

- compression must remain operationally lossless enough for reliable execution
- if one field becomes ambiguous, expand that field rather than the whole prompt
- exact file scope and exact validation checks outrank prose smoothness

## Prompt Shape

A central shared prompt should usually include:

1. a prompt ID
2. a short purpose statement
3. the prompt body or template
4. concise notes on source lineage or intended usage

When prompts are intended for reuse across tooling agents, they should usually
also include:

- a short runtime-selection section that tells the operator to choose the model
  and reasoning level before launch when those settings are run-fixed
- one copyable prompt body in a fenced code block

When `RAIDEN` delivers a prompt to the operator during active work, the prompt
should exist in both places:

- as a durable file artifact in the repo
- as a copyable fenced code block in the active chat response

Reason:

- the repo file preserves continuity, reuse, and auditability
- the active operator may only be able to use the chat-visible code block at
  launch time

The surrounding file may explain usage in readable prose, but the executable
prompt text should be easy to copy without reconstruction.

This is a documentation shape, not yet a package manifest requirement.

## Prompt Output Rule

When `RAIDEN` builds a prompt that asks another agent to report findings,
assessment, plans, or implementation outcomes, the requested output should
usually contain two surfaces:

- a readable operator-facing response
- a fenced code block with the compact structured information needed for a
  follow-on agent to review or continue the work

Reason:

- the readable surface helps the operator understand the judgment quickly
- the code-block surface reduces ambiguity for agent-to-agent review, handoff,
  or continuation

The readable surface should:

- explain the judgment in normal prose
- highlight the main findings, decisions, risks, and next actions
- stay concise enough for operator use

The code-block surface should:

- be compact and structured
- contain only the information needed for agent review or continuation
- avoid decorative prose
- be easy to copy as a durable handoff or verification block

Preferred compact fields when relevant:

- `Obj`
- `Scope`
- `Done`
- `Open`
- `Dec`
- `Val`
- `Blk`
- `Next`
- `Confidence`

This is an output rule, not a requirement that the executable prompt body
itself must contain those labels.

## Metadata Boundary

Prompt files may contain both:

- wrapper metadata for the operator
- executable prompt text for the agent

Treat them as different layers.

Wrapper metadata includes:

- chosen target agent model
- recommended model
- reasoning level
- host/tool selection
- fast versus planning selection
- runtime notes about whether the run is model-bound
- usage notes and escalation guidance

Executable prompt text includes:

- the task objective
- scope boundaries
- required reads
- required actions
- prohibitions
- validation checks
- expected output

Rule:

- operator/runtime metadata should stay outside the copyable prompt body
- the fenced prompt body should contain instructions to the agent, not launch
  configuration for the host
- if a prompt is being handed to the operator for immediate use, provide the
  same executable body in chat as a fenced code block even when the repo file
  also exists

Therefore:

- do not leave target-agent selection implicit when the task depends on model
  strengths
- do not put model names inside the main prompt body unless the task itself is
  about choosing or auditing models
- do not put reasoning-level selection inside the main prompt body
- do not put fast/planning profile selection inside the main prompt body
- do not use labels such as `Mode` in the copyable prompt body when they only
  restate wrapper metadata rather than instruct the agent's work

If a wrapper file offers multiple runtime profiles, select one in the wrapper
section first, then paste a prompt body that already stands on its own.

## Change Discipline

When updating an existing shared prompt:

- preserve the prompt ID unless the task shape changes materially
- tighten wording before adding sections
- remove repo-specific leakage rather than documenting around it
- update `CATALOG.md` if the prompt role or status changes

When adding a new shared prompt:

- confirm it is reusable
- give it a distinct prompt ID
- place it in the narrowest suitable category
- record it in `CATALOG.md`

## Promotion Rule

Candidate prompt material may come from:

- reviewed prototype patterns
- repeated RAIDEN operator workflows
- repeated central-agent handoff needs

It does not become a shared prompt asset only because it was useful once.

Promotion still requires:

1. review or demonstrated repeat use
2. normalization into RAIDEN wording
3. placement in this subtree

## Anti-Drift Rules

- Do not use this directory as a session prompt dump.
- Do not copy raw prototype prompts without normalization.
- Do not store downstream local prompts here.
- Do not let prompt inventory drift out of sync with `CATALOG.md`.
- Do not compress human-facing governance just because the execution layer is compact.

## Current Deferred Questions

The following are still intentionally open:

- exact version metadata shape for prompt bundles
- whether prompt compatibility markers are needed beyond plain notes
- how shared prompts will be packaged within `Edict` releases and whether any
  should install into downstream `Writ`s by default
