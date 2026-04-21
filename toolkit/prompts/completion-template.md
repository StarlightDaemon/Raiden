# Completion Template

## Prompt ID

`raiden.shared.completion.v1`

## Purpose

Use this prompt when a bounded task needs a concise completion report that
records outcome, verification, and residual risk without turning into a large
narrative.

## Template

```text
Complete the task and report back in this shape:

Outcome:
- <what was completed>

Verification:
- <what was checked or tested>

Not done:
- <any intentionally deferred work>

Risks:
- <only real residual risk or ambiguity>
```

## Notes

- Strong lineage: `BIND`
- Supporting lineage: `CTRL`
