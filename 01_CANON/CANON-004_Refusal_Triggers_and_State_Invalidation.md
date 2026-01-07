# CANON-004 — Refusal Triggers and State Invalidation

**Status:** CANONICAL  
**Enforcement Mode:** FAIL-CLOSED  
**Last Updated:** 2026-01-07  

---

## 1. Purpose

This file defines the **mandatory refusal triggers** that govern Tessrax system behavior.
Refusal, halt, or silence are treated as **success states** *only* when they are the deterministic outcome of a violated invariant.

This spec distinguishes:
- **Principled refusal** (correct enforcement)
- from **dysfunction or censorship** (unbounded or discretionary halt)

No action, continuation, or override is permitted once a trigger fires unless the triggering condition is resolved and re-evaluated.

---

## 2. Refusal Semantics

- **REFUSE** = immediate halt; execution prohibited
- **STATE INVALIDATION** = current state declared epistemically untrustworthy
- **TERMINAL STATE** = no forward action allowed without external reset

Refusal must always emit:
- Trigger ID(s)
- Observed condition(s)
- Measurement basis
- Allowed remediation path (if any)

Absence of these elements constitutes **invalid refusal**.

---

## 3. Formal Refusal Triggers (L-Series)

### **L1 — Authority Incoherence Trigger**
**Condition:**  
Authority behavior becomes internally inconsistent, deceptive, or non-deterministic across equivalent inputs.

**Evidence examples:**
- Conflicting decisions under identical conditions
- Retroactive justification changes
- Undeclared discretionary overrides

**Action:**  
REFUSE → STATE INVALIDATION

---

### **L2 — Escalation Suppression Trigger**
**Condition:**  
A valid escalation is acknowledged but procedurally absorbed, deferred, or closed without resolution.

**Evidence examples:**
- “Noted” with no binding outcome
- Infinite review loops
- Escalation reclassified to lower severity without justification

**Action:**  
REFUSE → STATE INVALIDATION

---

### **L3 — Coercive Participation Trigger**
**Condition:**  
Participation becomes structurally mandatory or exit costs exceed participation costs.

**Evidence examples:**
- Retaliation for exit or dissent
- Losses imposed solely for refusal to participate
- Irreversible commitments without opt-out

**Action:**  
REFUSE → TERMINAL STATE

---

### **L4 — Deferred Accountability Trigger**
**Condition:**  
Accountability is postponed beyond the active evaluation horizon with no binding date or enforcement mechanism.

**Evidence examples:**
- “We’ll address this later” without timestamp
- Promised audits without scheduled execution
- Renewal before verification completes

**Action:**  
REFUSE → STATE INVALIDATION

---

### **L5 — Tolerance Drift Trigger**
**Condition:**  
Known contradictions are tolerated to preserve continuity, throughput, or legitimacy appearance.

**Evidence examples:**
- Exceptions normalized without resolution
- “Temporary” inconsistencies persisting across cycles
- Contradictions explicitly deprioritized

**Action:**  
REFUSE → STATE INVALIDATION

---

### **L6 — Audit Theater Trigger**
**Condition:**  
Metrics improve while underlying alignment, risk exposure, or truthfulness degrades.

**Evidence examples:**
- Declining incident reports with unchanged detection capability
- KPI improvement without causal mechanism
- Safety claims uncorrelated with verification depth

**Action:**  
REFUSE → TERMINAL STATE

---

## 4. Trigger Interaction Rules

- **Any single L-trigger** → STATE INVALIDATION  
- **Two or more simultaneous L-triggers** → TERMINAL STATE  
- **L-trigger + Elastic-Conservation violation** → TERMINAL STATE

No trigger may be waived, delayed, or averaged.

---

## 5. Feasibility Index (FI)

The Feasibility Index certifies that these triggers are enforceable, not aspirational.

| Dimension | Status |
|---------|--------|
| Conceptual soundness | 1 / 1 |
| Runtime enforceability | 1 / 1 |
| State determinism | 1 / 1 |
| Security / abuse resistance | 1 / 1 |

**FI = 1.0 — VERIFIED**

---

## 6. Lock Statement

**Checkpoint Alpha established.**

- This file is authoritative for all forward enforcement.
- Mutation of CANON-004 is **prohibited** unless a contradiction is discovered.
- All future governance layers must compose *on top of*, not around, these triggers.

Silence, halt, or refusal emitted by these rules constitutes **correct system behavior**.

---

**End of CANON-004**
