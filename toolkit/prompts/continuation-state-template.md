# Continuation State Template

## Prompt ID

`raiden.shared.continuation-state.v1`

## Purpose

Use this template to carry forward the smallest reliable state package after a
pause point.

## Template

```text
Obj: <goal>
Phase: <current phase>
Scope: <exact paths>
Done:
- <completed work>
Open:
- <remaining work>
Dec:
- <active decisions>
Val:
- <validation state>
Blk:
- <blockers or none>
Next:
- <recommended next action>
Alt:
- <fallback next action or none>
Trim:
- stale exploration removed
- verbose logs removed
- unrelated context removed
- superseded reasoning removed
```

## Notes

- Strong lineage: `CTRL`
- Supporting lineage: `HardlinkOrganizer`
