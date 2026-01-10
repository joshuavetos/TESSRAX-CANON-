# DIAG-001: Epistemic Recovery Time (ERT)

## Definition
Epistemic Recovery Time (ERT) is the time required for humans to reconstruct the authoritative state of a system after total digital loss.

ERT measures **understanding**, not uptime.

## Why This Exists
Institutions routinely measure:
- RTO (Recovery Time Objective)
- RPO (Recovery Point Objective)

They do **not** measure:
- How long it takes a human to know what is true

ERT exposes that gap.

## Test Procedure
1. Export all raw events for the last 24 hours.  
2. Print them.  
3. Remove all digital tools.  
4. Ask humans to determine current state.  

If humans cannot do this, the system owns the truth.

## Scoring Rubric (0–10)

| Criteria        | 0                  | 1                    | 2                    |
|-----------------|--------------------|----------------------|----------------------|
| Tool Isolation  | Cloud/LLM used     | Local tools allowed  | Paper only           |
| Input Sufficiency | Incomplete        | Requires lookup      | Self-contained       |
| Causal Trace    | Guessing           | Partial trace        | Full audit trail     |
| Drift Tolerance | >5% error          | 1–5%                 | <1%                  |
| Time to Truth   | >24h               | 8–24h                | <8h                  |

**Total score = sum of all criteria (0–10).**

## Interpretation
- **8–10**: Sovereign State  
- **4–7**: Brittle Dependency  
- **0–3**: Pathological Entanglement  

## Red Flag
If leadership refuses or cannot tolerate this test, the institution is committing semantic fraud.

## Status
ACTIVE DIAGNOSTIC
