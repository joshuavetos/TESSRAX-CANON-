# BUDGET ARITHMETIC SPEC v1.0

## Purpose
Define a dynamic, risk-sensitive speech cost system that enforces the Claim Economy by making deep, high-impact reasoning increasingly expensive.

---

## Tier-Separated Budgets

The system maintains three independent ledgers:

- OBS_POOL — observations and measurements
- PRED_POOL — predictions and evaluations
- STRUC_POOL — governance and invariant changes

Budgets are not fungible unless explicitly stated.

---

## Base Debits

| Tier        | Base Debit |
|-------------|------------|
| Observation | 0.1        |
| Prediction  | 1.0        |
| Structural  | 10.0       |

---

## Dependency-Depth Multiplier

Let `depth` = longest path from the new Claim to a foundational Claim.

Total Emission Cost:

C_e = BaseDebit × (1 + 0.1 × depth)

This multiplier applies at emission time.

---

## Cross-Debit Rule (Link Tax)

For each dependency `d` referenced by a new Claim:
- Apply an additional debit equal to `0.05 × BaseDebit(d.tier)`
- Debit is charged to the same pool as the new Claim

This discourages fragile dependency stacking on cheap claims.

---

## Overflow Rule

If PRED_POOL is insufficient:
- It may draw from STRUC_POOL at a 2:1 penalty  
  (2 Structural units → 1 Prediction unit)

OBS_POOL and PRED_POOL may NEVER replenish STRUC_POOL.

---

## Refunds and Penalties

| Tier        | Refund on PASS | Penalty on FAIL |
|-------------|---------------|-----------------|
| Observation | 100%          | -0.5            |
| Prediction  | 110%          | -5.0 + Tier Lock |
| Structural  | 150%          | Capability Purge |

Refunds are applied only upon PASSED adjudication.

---

## Insolvency Thresholds

Critical Floor:
- If total available budget < 0.1 → STATUS: INSOLVENT

Insolvent State:
- Legal outputs: HALT or REJECTED: INSOLVENT
- No predicates, no prose, no claims

---

## Design Consequence

As dependency depth and claim centrality increase:
- Cost rises non-linearly
- Silence becomes the mathematically optimal strategy

This is intentional.
