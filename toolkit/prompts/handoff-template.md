# Handoff Template

## Prompt ID

`raiden.shared.handoff.v1`

## Purpose

Use this prompt when one agent needs to transfer a bounded work package to
another agent without requiring a full repo reread.

## Template

```text
You are continuing a bounded work package inside the current repo.

Read first:
- <list canonical files first>
- <list directly relevant implementation files second>

Current objective:
- <state the objective in one sentence>

Known constraints:
- <state non-negotiable rules>

Already true:
- <list completed or fixed facts only>

Still open:
- <list the remaining work only>

Do not:
- reopen settled naming or architecture
- treat review artifacts as canon unless adopted
- broaden the task beyond the stated objective

Close out with:
- result
- evidence checked
- remaining risks
```

## Notes

- Strong lineage: `BIND`
- Supporting lineage: `CTRL`
