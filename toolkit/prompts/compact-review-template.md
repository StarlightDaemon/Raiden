# Compact Review Template

## Prompt ID

`raiden.shared.compact-review.v1`

## Purpose

Use this prompt when a bounded review should stay findings-first and token-lean.

## Template

```text
Mode: review
Obj: <review objective>
Scope: <exact files/areas>
Read:
- <required reads only>
Check:
- <questions or risks to test>
No:
- <what not to reopen or broaden>
Out:
- findings first
- file refs
- risks
- recommended adjustment
```

## Notes

- Strong lineage: `BIND`
- Supporting lineage: `CTRL`
