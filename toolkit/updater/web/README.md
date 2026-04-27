# RAIDEN Web Installer — Operator Guide

This directory contains the Vite/React frontend for the RAIDEN local web installer UI.

## Starting the backend

Run from `toolkit/updater/`:

```
python3 -m raiden_updater.server
```

The backend listens on `127.0.0.1:8080` by default. It serves a JSON API used
by the UI. Endpoints: `/api/scan`, `/api/init-preview`, `/api/init-apply`,
`/api/plan`, `/api/apply`, `/api/doctor`, `/api/select-folder` (all `POST`).

See `CLAUDE.md §5` for the full endpoint reference.

## Serving the UI

During development, run the Vite dev server from this directory:

```
npm install
npm run dev
```

For production use, build the UI (`npm run build`) and serve the `dist/` output
statically. The Python backend does not serve the frontend; use a static file
server or a reverse proxy pointed at `dist/`.

## End-to-end operator workflow

1. Start the Python backend (`python3 -m raiden_updater.server`).
2. Start the Vite dev server (`npm run dev`) or serve a built `dist/`.
3. Open the UI in a browser; it connects to the backend at `http://127.0.0.1:8080`.
4. Use the UI to scan for existing RAIDEN instances, initialize new ones, run
   plan/apply cycles, or run the doctor check.
