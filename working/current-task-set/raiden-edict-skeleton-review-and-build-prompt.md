# RAIDEN Edict Skeleton Review And Build Prompt

Use this as the working prompt for a bounded agent pass on the current
`toolkit/edict/` surface.

Recommended runtime:

- choose the model and reasoning level before launch
- assume the run is model-bound and reasoning-bound unless the host explicitly
  proves otherwise
- prefer a moderate-to-high reasoning implementation pass for canon-sensitive
  doc/build work
- if the first pass fails materially, start a new pass with stronger settings
  rather than planning around mid-run switching

Use the fenced block below as the exact copyable prompt body.

```text
Mode: impl
Obj: make toolkit/edict materially real with the smallest useful package skeleton/example
Scope: /mnt/e/RAIDEN/toolkit/edict plus directly affected canon
Read:
- /mnt/e/RAIDEN/SOURCE_OF_TRUTH.md
- /mnt/e/RAIDEN/CURRENT_STATE.md
- /mnt/e/RAIDEN/DECISIONS.md
- /mnt/e/RAIDEN/RELEASE_READY_CHECKLIST.md
- /mnt/e/RAIDEN/TOOLKIT_INDEX.md
- /mnt/e/RAIDEN/MANAGED_VS_LOCAL.md
- /mnt/e/RAIDEN/toolkit/README.md
- /mnt/e/RAIDEN/toolkit/edict/README.md
- /mnt/e/RAIDEN/toolkit/edict/PACKAGE_BOUNDARY.md
- /mnt/e/RAIDEN/toolkit/edict/LIFECYCLE.md
- /mnt/e/RAIDEN/toolkit/instance/STRUCTURE.md
- /mnt/e/RAIDEN/toolkit/instance/PROMPT_MAPPING.md
- if needed: /mnt/e/RAIDEN/toolkit/prompts/README.md
- if needed: /mnt/e/RAIDEN/PROMPT_ASSET_INDEX.md
- if needed: /mnt/e/RAIDEN/reference-extracts/hardlinkorganizer/embedded-instance-structure-pattern.md
- if needed: /mnt/e/RAIDEN/reference-extracts/hardlinkorganizer/continuity-file-roles-pattern.md
- if needed: /mnt/e/RAIDEN/reference-extracts/bind/integration-maturity-model-pattern.md
Do:
- review current toolkit/edict package surface
- choose the smallest useful Edict package skeleton/example
- implement it under toolkit/edict
- update only directly affected docs
No:
- do not reopen updater-shape canon
- do not define exact manifest fields
- do not define updater command behavior
- do not define final archive/bundle format
- do not move local overlay or live-state materials into the managed package
- do not reopen naming or managed-vs-local contract
- do not turn this into a deployment system
- do not create fake complexity
Val:
- new skeleton is consistent with PACKAGE_BOUNDARY.md
- new skeleton is consistent with LIFECYCLE.md
- new skeleton is consistent with MANAGED_VS_LOCAL.md
- new skeleton is consistent with toolkit/instance/STRUCTURE.md
- no new file silently hardens deferred updater/manifest decisions
- any RELEASE_READY_CHECKLIST change is justified by the new artifact
Stop:
- stop when toolkit/edict has a real minimal package skeleton/example and related docs are aligned
Out:
- Outcome: skeleton/example added
- Verification: docs/rules checked
- Not done: intentionally deferred updater/package details
- Risks: remaining ambiguity that still blocks later updater canon
```
