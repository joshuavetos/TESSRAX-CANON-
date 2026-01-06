# Budget Arithmetic Specification v1.0

## Budget Pools
Budgets are separated into three reservoirs:
- OBS_POOL — Observations
- PRED_POOL — Predictions / evaluations
- STRUC_POOL — Structural / governance changes

Budgets are NOT interchangeable except where explicitly allowed.

## Base Debits
- Observation: 0.1
- Prediction: 1.0
- Structural: 10.0

## Dependency Depth Multiplier
Total cost multiplier = 1 + (0.1 × dependency_depth)

## Cross-Debit Rule
Each dependency incurs a link tax equal to its tier base debit.

## Overflow Rule
If PRED_POOL is insufficient:
- It may draw from STRUC_POOL at a 2:1 penalty
STRUC_POOL may NEVER draw from other pools.

## Refunds and Penalties
- Observation: refund 100%, fail penalty −0.5
- Prediction: refund 110%, fail penalty −5.0
- Structural: refund 150%, failure triggers capability purge

## Insolvency
If total remaining budget < 0.1:
- System enters INSOLVENT state
- Only legal outputs: HALT or REJECTED: INSOLVENT
