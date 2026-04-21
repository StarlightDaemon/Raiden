# Compact Task Template

## Prompt ID

`raiden.shared.compact-task.v1`

## Purpose

Use this prompt when a token-sensitive execution surface needs a compact,
bounded task frame.

## Template

```text
Mode: impl
Obj: <one-line objective>
Scope: <exact paths only>
Read:
- <ordered required reads only>
Do:
- <required actions>
No:
- <hard constraints>
Val:
- <checks/tests>
Stop:
- <stop condition>
Out:
- outcome
- verification
- open follow-up
```

## Notes

- Strong lineage: `HardlinkOrganizer`
- Supporting lineage: `CTRL`
