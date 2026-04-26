# Registry and Stewardship Pattern

## Provenance
Extracted from `Stargate` legacy holding (`FINAL_STEWARDSHIP_REPORT.md` and `stargate-registry.json`).

## Concept
The `Stargate` snapshot demonstrated a lightweight approach to prototype-sprawl control and handoff/archive separation through two mechanisms:
1. A structured JSON registry for tracking prototypes.
2. A maturity category scoring system.

## 1. Maturity Category Scoring
Prototypes were evaluated on UI fidelity and Backend rigor, then assigned to a maturity category. This is a reusable pattern for separating system-grade work from disposable experiments.

### Categories:
1. **Category 1 (System-Grade)**: Rigorous state machines, detached logic, testable.
2. **Category 2 (Balanced)**: Functional UI with store-based logic.
3. **Category 3 (UI-Heavy)**: Visual demonstrations with mock backends.
4. **Category 4 (Abandoned)**: Remnants or static assets.

## 2. Lightweight JSON Registry
The registry format tracks the lineage, confidence, and tier of various experiments to avoid sprawl.

### Schema Example:
```json
{
  "schemaVersion": "1.0",
  "primaryId": "stargate-main",
  "lastUpdated": "2026-01-31T05:00:00Z",
  "prototypes": {
    "stargate-main": {
      "id": "stargate-main",
      "folderPath": "Stargate_main",
      "tier": "A",
      "identity": {
        "name": "GateNetwork Core",
        "lineage": "PRIMARY",
        "confidence": 1.0,
        "description": "Reference implementation."
      },
      "tech": {
        "framework": "vite",
        "language": "ts",
        "stack": ["xstate", "react", "typescript"]
      },
      "status": {
        "launchable": true,
        "launchCommand": "npm run dev"
      }
    }
  }
}
```

## RAIDEN Value
While `RAIDEN` has its own `REPOSITORY_MAP.md` and `TOOLKIT_INDEX.md`, this lightweight approach to scoring and tracking scattered prototypes remains a useful pattern for future bounded registry or toolkit-surface design.
