# Pause-Point Template

## Prompt ID

`raiden.shared.pause-point.v1`

## Purpose

Use this prompt when a work cycle must stop cleanly and export a compact
handoff before continuation or model change.

## Template

```text
Obj: <task objective>
Success: <success condition>
Stop: <why cycle is stopping now>
Phase: <current phase>
Scope:
- repo: <repo or subproject boundary>
- paths: <exact files/dirs in scope>
Done:
- <completed facts only>
Open:
- <remaining work only>
Dec:
- <active decisions/constraints>
Val:
- <validation state>
Blk:
- <current blockers or none>
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
- Supporting lineage: `BIND`
