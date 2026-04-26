# RAIDEN Guided Setup

## Purpose

This directory contains a small operator-facing guide and helper script for
trying the current RAIDEN local CLI flow end to end.

It is a step-by-step surface for:

- creating a downstream `RAIDEN Instance` skeleton in a target repo
- installing a package payload into `.raiden/writ/`
- running the updater plan/apply flow
- checking the resulting instance shape

This guide uses the current local CLI updater contract. It does not define
package distribution, remote publishing, or broader updater metadata.

## Quick Start

From the RAIDEN repo root:

```sh
python3 toolkit/guide/raiden_guide.py steps
```

Create an empty target repo for a trial:

```sh
mkdir -p /tmp/raiden-trial
printf '# Trial Repo\n' > /tmp/raiden-trial/README.md
```

Initialize the downstream instance skeleton:

```sh
python3 toolkit/guide/raiden_guide.py init --target /tmp/raiden-trial
```

Preview installation from the sample package:

```sh
python3 toolkit/guide/raiden_guide.py install \
  --target /tmp/raiden-trial \
  --package toolkit/updater/fixtures/sample_package
```

Apply the installation:

```sh
python3 toolkit/guide/raiden_guide.py install \
  --target /tmp/raiden-trial \
  --package toolkit/updater/fixtures/sample_package \
  --apply
```

Check the instance:

```sh
python3 toolkit/guide/raiden_guide.py doctor --target /tmp/raiden-trial
```

## What The Tool Creates

The `init` command creates only the current required downstream shape:

```text
<target-repo>/
├── AGENTS.md
└── .raiden/
    ├── README.md
    ├── writ/
    ├── local/
    │   ├── README.md
    │   ├── prompts/
    │   ├── rules/
    │   └── context/
    ├── state/
    │   ├── README.md
    │   ├── CURRENT_STATE.md
    │   ├── GOALS.md
    │   ├── OPEN_LOOPS.md
    │   ├── DECISIONS.md
    │   └── WORK_LOG.md
    └── instance/
        └── metadata.json
```

`baseline.json` is written by the updater after a successful install or update.

## Safety Rules

- Existing files are not overwritten unless `--force` is provided.
- `install` runs as a dry-run plan unless `--apply` is provided.
- Managed files are written only under `.raiden/writ/`.
- `.raiden/local/` and `.raiden/state/` are preserved by the updater.
