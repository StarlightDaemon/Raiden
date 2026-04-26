# RAIDEN Updater MVP

## Status

This is the first practical RAIDEN updater implementation.

The package-manifest surface, core `MAJOR.MINOR.PATCH` version comparison
rules, refined anomaly thresholds, and safe managed-file removal policy are
now part of current updater canon. Instance-side metadata and installed
baseline fields are also current local CLI canon after validation hardening.

## Purpose

A local CLI installer/update tool that installs or refreshes the managed core
(`.raiden/writ/`) of a downstream `RAIDEN Instance` from an `Edict` package,
while preserving local overlay and live state.

The same package now also contains the first shared installer service layer for
future local web UI work:

- `raiden_updater/installer.py`
  - shared repo scan, init preview, init apply, and doctor services
- `raiden_updater/server.py`
  - dependency-free local JSON API wrapper for web UI development
- `raiden_updater/cli.py`
  - local CLI surface for direct operator use and engine verification
- `web/`
  - local browser UI scaffold for install/update operator flow

## Canon-Backed Contract

This updater enforces the four-point update contract from `D-0016` and
`MANAGED_VS_LOCAL.md`:

1. **Update managed core** — writes only to `.raiden/writ/`
2. **Preserve local overlay** — never touches `.raiden/local/`
3. **Preserve local live state** — never touches `.raiden/state/`
4. **Stop on locally modified managed files** — detects and blocks on
   conflicts

## Commands

### plan

Produce a dry-run install/update report without mutating the filesystem.

```
py -m raiden_updater.cli plan --instance <path> --package <path>
```

Output includes:
- compatibility status
- version comparison (upgrade / same / downgrade)
- file actions (update / add / unchanged / remove)
- conflicts (local modifications)
- anomalies (warn / block)
- protected paths (overlay and live-state roots)
- whether apply can proceed

### apply

Execute the install or update only if the plan is conflict-free.

```
py -m raiden_updater.cli apply --instance <path> --package <path>
```

After a successful apply:
- changed managed files are updated from the package payload
- baseline-tracked managed files absent from the new package are removed when
  they are still unchanged from the last installed baseline
- a new installed baseline is written to `.raiden/instance/baseline.json`
- instance metadata version is updated

Missing `baseline.json` is allowed only for an initial install into a fresh
managed root with no existing files. If `.raiden/writ/` already contains files,
the updater blocks because it cannot prove whether those files were locally
modified.

## Local Web Backend

The current local web backend is intentionally narrow and wraps existing
installer/update logic rather than reimplementing it.

Current endpoints:

- `POST /api/scan`
- `POST /api/init-preview`
- `POST /api/init-apply`
- `POST /api/plan`
- `POST /api/apply`
- `POST /api/doctor`
- `POST /api/select-folder`

This server is a backend foundation for a browser-first local operator surface,
not a separate updater engine.

## Data Models

### Instance Metadata (`.raiden/instance/metadata.json`, current local CLI canon)

| Field | Type | Example |
|---|---|---|
| `instance_schema_version` | string | `"1"` |
| `instance_form_type` | string | `"raiden-instance"` |
| `installed_edict_version` | string | `"0.1.0"` |
| `managed_roots` | list[string] | `[".raiden/writ"]` |
| `overlay_roots` | list[string] | `[".raiden/local"]` |
| `live_state_roots` | list[string] | `[".raiden/state"]` |

Current semantics:

- all six fields are required
- unknown extra fields are rejected
- `instance_form_type` is fixed to `"raiden-instance"`
- the current local CLI supports exactly one managed root,
  `[".raiden/writ"]`
- overlay and live-state roots are fixed to `[".raiden/local"]` and
  `[".raiden/state"]`

### Package Manifest (`manifest.json`, current canon)

| Field | Type | Example |
|---|---|---|
| `package_type` | string | `"edict"` |
| `edict_version` | string | `"0.2.0"` |
| `compatible_instance_schemas` | list[string] | `["1"]` |
| `managed_files` | list[{path, hash}] | file entries with SHA-256 hashes |
| `created_at` | string | ISO-8601 |

Current semantics:

- `package_type` is currently fixed to `"edict"`
- `edict_version` uses strict core `MAJOR.MINOR.PATCH` comparison
- `compatible_instance_schemas` is checked as simple membership against
  `instance_schema_version`
- `managed_files` enumerates the managed payload relative to `payload/`
- `created_at` records package creation time as an ISO-8601 timestamp

### Installed Baseline (`.raiden/instance/baseline.json`, current local CLI canon)

| Field | Type | Example |
|---|---|---|
| `installed_edict_version` | string | `"0.2.0"` |
| `installed_at` | string | ISO-8601 |
| `managed_files` | list[{path, hash}] | file entries at install time |

Current semantics:

- all three fields are required
- unknown extra fields are rejected
- each `managed_files` entry contains exactly `path` and SHA-256 `hash`
- paths are unique relative managed-file paths inside the installed `Writ`
- the baseline is the conflict-detection authority for existing managed files

## Running Tests

```
cd E:\RAIDEN\toolkit\updater
py -m pytest tests/ -v
```

## Anomaly Detection

The updater classifies unusual conditions during planning:

| Anomaly | Severity | Trigger |
|---|---|---|
| `high_change_ratio` | warn | >50% of managed files changing when the managed set has at least 8 files |
| `high_change_count` | warn | >10 files changing |
| `protected_path_write` | block | package writes to overlay or state root |
| `managed_file_removal` | warn | baseline-tracked file absent from new package |

## What Is Not Included

- Remote download or registry resolution
- Drag-and-drop UX or GUI
- Auto-merge for conflicts
- Publishing/distribution systems
- Downgrade blocking (reported but not blocked)
- Rollback support

## Provisional Choices

The following are MVP implementation decisions, not canon:

1. **Language**: Python 3.10+
2. **Location**: `toolkit/updater/`
3. **Downgrade policy**
4. **Prerelease/build version metadata support**
5. **Packaging/distribution mechanics beyond the local CLI**

These may change when updater-shape canon is formalized.
