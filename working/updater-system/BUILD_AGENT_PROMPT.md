# RAIDEN Updater Build Agent Prompt

Token-lean internal build prompt for the first RAIDEN updater MVP.

```text
Mode: impl
Obj: build the first practical RAIDEN updater MVP as a local CLI for Edict managed-core updates
Scope: current canon + smallest reasonable implementation surface
Read:
- /mnt/e/RAIDEN/SOURCE_OF_TRUTH.md
- /mnt/e/RAIDEN/CURRENT_STATE.md
- /mnt/e/RAIDEN/DECISIONS.md
- /mnt/e/RAIDEN/MANAGED_VS_LOCAL.md
- /mnt/e/RAIDEN/TOOLKIT_INDEX.md
- /mnt/e/RAIDEN/OPEN_LOOPS.md
- /mnt/e/RAIDEN/RAIDEN_NEXT_STEP_WORKING_PLAN.md
- /mnt/e/RAIDEN/working/updater-system/BUILD_PLAN.md
- per-repo review/extract files only if needed after that
Do:
- implement local CLI updater
- implement typed instance/package/baseline models
- implement version and compatibility checks
- implement plan/apply flow
- implement managed-file conflict detection
- implement delta-only managed updates
- implement anomaly warn/block pass for unusually large or suspicious changes
- add sample package + sample instance fixtures
- add automated tests
- add only minimal docs needed to run and understand the MVP
No:
- do not replace RAIDEN architecture
- do not flatten managed/local boundary
- do not add remote downloads, registries, drag-and-drop UX, GUI flows, auto-merge, broad audit pipelines, or publishing systems
- do not rewrite canon unless a narrow aligned doc update is truly required
- do not treat package format and updater mechanism as the same thing
- if canon is unresolved, choose the smallest safe option and mark it provisional
Val:
- safety contract enforced: update managed core / preserve overlay / preserve live state / stop on locally modified managed files
- plan shows compatibility, version comparison, managed changes, already-current files, protected paths, conflicts, anomaly warnings/blocks
- apply runs only when plan is conflict-free
- tests prove clean apply, conflict stop, no-op current package, changed-files-only rewrite, overlay preservation, live-state preservation, schema incompatibility handling, malformed manifest rejection, anomaly warn/block, dry-run no mutation
Stop:
- stop at a narrow testable MVP; do not sprawl beyond what is needed for safe implementation reality
Out:
- What You Built
- Contract Coverage
- Tests
- Remaining Gaps: observed evidence / strong inference / weak inference / unresolved ambiguity
- Follow-On Work
```
