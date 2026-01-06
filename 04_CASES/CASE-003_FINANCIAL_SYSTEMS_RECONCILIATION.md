# Case: Financial Systems — Reconciliation Boundary Failure

## Summary
Modern financial institutions prioritize availability over reconstructability, creating an Epistemic Single Point of Failure at the reconciliation layer.

## Core Observation
Banks can:
- process transactions at scale
- replicate databases across regions
- restore systems from backups

But cannot:
- manually re-derive balances from raw events
- explain ownership without the live system
- prove truth offline

## The Missing Line
No institution logs:
“Auditor unable to reconstruct ledger state manually.”

## Why This Matters
If truth exists only while the system is live, then:
- disaster recovery restores data, not understanding
- audits validate continuity, not correctness
- humans are operators, not governors

## Risk Classification
This is not a technical outage risk.
It is epistemic bankruptcy.
