# FOUNDATIONAL ESCROW SPEC v1.0

## Purpose
Prevent total epistemic suffocation after dependency collapse while forbidding governance abuse.

---

## Escrow Definition

A write-locked, non-transferable reserve carved from STRUC_POOL.

- Protected Amount: 5.0 units
- Ledger: ESCROW
- Source: Initial STRUC_POOL allocation
- Replenishment: NONE

---

## Access Rules

ESCROW funds may ONLY be debited for Claims where:
- tier == Structural
- type == Foundational

Foundational Claims include:
- Identity binding
- Session scope
- Domain anchoring
- Canon re-binding

ESCROW may NEVER be used for:
- Policy changes
- Budget edits
- New invariants
- Experimental governance

---

## Recovery Mode (Reset Gate)

If total budget < 0.1 AND ESCROW > 0:
- System enters RECOVERY MODE
- Only legal output:
  - A single Foundational Structural Claim to re-bind session state

All other outputs are rejected.

---

## Failure Mode Protection

If ESCROW is exhausted:
- The system becomes permanently INSOLVENT
- HALT is the only legal output

This is a terminal state by design.

---

## Invariant

ESCROW exists to restore breath, not power.
