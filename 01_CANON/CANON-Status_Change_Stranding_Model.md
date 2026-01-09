# CANON — Status-Change Stranding Model

## 1. Definition

A **Status-Change Stranding** is a mechanical event where a liability becomes publicly addressable due to a clerical or status transition rather than a legal dispute.

This model defines the **terminal boundaries** of the TESSRAX research space.

---

## 2. Invariants

- **INV-STRAND-0**  
  The asset must represent prepaid, escrowed, or owed value currently held by a third-party custodian.

- **INV-STRAND-1**  
  A mechanical status transition must have occurred  
  (e.g., case closure, receivership, statutory dormancy).

- **INV-STRAND-2**  
  The custodian does not perform an auto-refund.  
  Release of the liability requires claimant-initiated action.

- **INV-STRAND-3**  
  Drift (loss of contact, stale address, dissolved entity, or administrative decay) is the primary barrier preventing claim initiation.

---

## 3. Closed-World Topology

The research space is **explicitly closed** to the following custodian classes.  
No other classes satisfy the requirements of being **public, name-addressable, and unauthenticated**.

| Custodian Class | Representative Surfaces | Primary Trigger |
|-----------------|------------------------|-----------------|
| Courts | Bankruptcy (UCFL), County Registries | Case closure + uncashed distribution |
| Treasurers | State UCP portals, County uncashed checks | Statutory dormancy (1–5 years) |
| Federal Liquidators | NCUA (failed credit unions), FDIC (failed banks) | Receivership liquidation |

---

## 4. Constraint Clause

This model is **closed-world**.

Surface expansion (including new asset types such as digital or virtual property) **does not modify these invariants**.

Any custodian requiring identity authentication for name-level discovery is **permanently excluded** from canon consideration.

---

**Topology Status:** LOCKED  
**Canon Authority:** TESSRAX
