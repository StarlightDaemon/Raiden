# Validation Template

## Prompt ID

`raiden.shared.validation.v1`

## Purpose

Use this prompt when the active task needs a compact validation pass rather than
a broad review narrative.

## Template

```text
Mode: validate
Obj: <what must be validated>
Scope: <exact files, commands, or behaviors>
Check:
- <validation checks>
Pass:
- <what counts as valid>
Fail:
- <what must be reported as failure>
Out:
- pass/fail summary
- evidence checked
- residual risk
```

## Notes

- Strong lineage: `CTRL`
