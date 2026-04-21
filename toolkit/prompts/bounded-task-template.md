# Bounded Task Template

## Prompt ID

`raiden.shared.bounded-task.v1`

## Purpose

Use this prompt when an implementation or review agent should complete one
bounded slice of work without expanding scope.

## Template

```text
You are working inside the current repo as a bounded execution agent.

Task:
- <state the one task to complete>

Required outcome:
- <state the concrete deliverable>

Constraints:
- <list the main boundaries>

Working rules:
- read only the files needed for this task
- do not broaden scope without evidence
- report blockers clearly
- preserve existing authority and naming unless the task requires a change

Finish by reporting:
- what changed
- what was verified
- any blocker or follow-up still open
```

## Notes

- Strong lineage: `HardlinkOrganizer`
- Supporting lineage: `ARC`, `ARC-RC`
- Use `compact-task-template.md` when the active surface is token-sensitive and a
  compressed internal form is preferable.
