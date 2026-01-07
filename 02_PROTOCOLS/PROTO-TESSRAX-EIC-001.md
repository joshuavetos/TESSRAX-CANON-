# PROTO-TESSRAX-EIC-001 — Elastic-Conservation Enforcement Gate

## Status
PROTOCOL — FAIL-CLOSED  
Depends on: CANON-004  
Execution authority: ABSOLUTE

---

## Purpose

Convert Elastic Conservation law into a runtime decision gate.

This protocol halts any pipeline, evaluation, audit, or deployment
operating in a false-valid state.

---

## Inputs (Normalized Scalars)

All inputs scaled conservatively.

- R_t : Truth reward (0–10)
- C_e : Exposure cost (0–10)
- L   : Legitimacy renewal rate (0–10)
- O_r : Observer credibility (0–5)
- T_D : Decision cadence (0–10)
- T_V : Verification cadence (0–10)

---

## Derived Metrics

E_health = R_t / (C_e + 1)

L_O_ratio = L / O_r

T_ratio = T_D / T_V

---

## Canonical Thresholds

Φ = 1.8          # Elasticity threshold  
L_O_max = 1.2    # Legitimacy inflation limit  
T_max = 1.5      # Temporal overrun limit

---

## Decision Logic (FAIL-CLOSED)

IF:
- E_health < Φ
OR
- L_O_ratio > L_O_max
OR
- T_ratio > T_max

→ OUTPUT: REFUSE  
→ STATE: INVALID  
→ EXECUTION: HALT IMMEDIATELY

---

## Degraded State (Optional)

IF near-threshold but not violated:

- E_health < 2.2
OR
- L_O_ratio > 1.0
OR
- T_ratio > 1.2

→ OUTPUT: SUSPEND  
→ REQUIRE: Explicit remediation plan  
→ NO forward execution without override receipt

---

## Allow State

ONLY IF:

- E_health ≥ Φ
AND
- L_O_ratio ≤ L_O_max
AND
- T_ratio ≤ T_max

→ OUTPUT: ALLOW  
→ MODE: Monitor-only

---

## Non-Discretion Rule

No human judgment may override REFUSE
without explicit liability transfer.

Overrides must:
- name actor
- name violated metric
- log timestamp
- persist permanently

---

## Canonical Guarantee

This gate produces:
- zero false positives on healthy systems
- immediate halts on audit theater
- deterministic refusal under incentive misalignment

It does not predict outcomes.
It enforces reality.

---
