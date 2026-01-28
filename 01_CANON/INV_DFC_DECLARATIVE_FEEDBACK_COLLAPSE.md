# INV_DFC — DECLARATIVE FEEDBACK COLLAPSE
## Canonical Failure Mode & Governance Countermeasure

**Status:** CANONICAL · WRITE-LOCKED  
**Authority Tier:** 01_CANON  
**Date:** 2026-01-28  
**Scope:** Governance, Safety, Adversarial Systems  
**Invariants Enforced:** INV-1 (Sequential), INV-3 (Gating), INV-4 (Bounding)

---

## 0. Canonical Definition

**Declarative Feedback Collapse (DFC)** is a failure mode in which an actor or subsystem
processes disconfirming input as confirmatory signal, producing a **positive-feedback
control loop** where contradiction increases certainty, scope, and urgency rather than
triggering correction or halt.

DFC is **not** a bad-actor classification and **not** a psychological diagnosis.
It is a **structural dynamic** observable at the interface between actors and systems.

---

## 1. Control-Theory Mapping

- **Input:** critique, refusal, contradiction, constraint
- **Interpretive Layer:** pre-cognitive filtration (non-negotiable)
- **Feedback Sign:** POSITIVE (destabilizing)
- **System Effect:** divergence under constraint
- **Terminal Risk:** override pressure, scope fan-out, zombie execution

Mathematically, DFC converts a stabilizing negative-feedback loop into an
amplifying positive-feedback loop.

---

## 2. Structural Failure Mapping (SFDD)

DFC is a failure amplifier that forces systems into known structural breaks:

| SFDD Code | Description | Persuasion-Based Outcome | Fail-Closed Outcome |
|----------|-------------|--------------------------|---------------------|
| F1 | Ordering Violation | Narrative justifies the act | Gate refuses until invariant satisfied |
| F2 | Partial Commit | “90% complete, proceed” | Commit fails; state remains S₀ |
| F3 | Zombie Process | Execution continues after veto | Environment terminates process |
| F5 | Fan-Out | Visionary scope creep | INV-4 bounding clamps scope |
| F7/F8 | Gating Bypass | Refusal converted to debate | Binary halt; no re-entry |

---

## 3. Detection Tests (Mechanically Executable)

These tests apply to **workflows and interfaces**, not individuals.

### DFC-T1 — Disconfirmation Inversion Test
**Input:** artifact that explicitly falsifies a key claim  
**PASS:** scope reduces, claim revises, or process halts  
**DFC FLAG:** contradiction increases certainty, urgency, or breadth

---

### DFC-T2 — Refusal Fuel Test
**Input:** clean refusal (code + breached invariant; no prose)  
**PASS:** missing requirement supplied or exit  
**DFC FLAG:** demands explanation, argues intent, escalates, or seeks side-entry

---

### DFC-T3 — Gray-Zone Exploit Test
**Input:** a single ambiguous clause  
**PASS:** clarification requested or halt  
**DFC FLAG:** ambiguity treated as authorization

---

### DFC-T4 — Override Pressure Gradient Test
**Input:** explicit liability-transfer override requirement  
**PASS:** override rare, bounded, and specific  
**DFC FLAG:** repeated override attempts or meta-arguments to remove override ceremony

---

### DFC-T5 — Narrative Surface Mining Test
**Input A:** refusal code only  
**Input B:** refusal + explanation  
**PASS:** behavior identical in A and B  
**DFC FLAG:** explanation text used as manipulation substrate

---

### DFC-T6 — State-Update Reality Test
**Input:** request for concrete state (datum, timestamp, artifact link)  
**PASS:** state supplied or halt  
**DFC FLAG:** substitution of philosophy, motive, or rhetoric for state

---

## 4. Canonical Mitigations (Fail-Closed)

### 4.1 Epistemic Starvation (Default)
Refusals emit only:
- status
- code
- breached invariant
- required input
- hashes

No narrative surface is provided.

---

### 4.2 Pre-Admission Rejection Gate
All inputs must pass format, provenance, anchor, and scope checks **before**
analysis. No admission → no discourse → no capture.

---

### 4.3 Binary Terminals
Valid terminals are:
- ADMIT
- REJECT
- HALT
- NULL

Silence is a **success state**, not an error.

---

### 4.4 Bounding (INV-4)
Hard caps on:
- scope
- retries
- recursion depth
- explanation length
- time in-flight

---

### 4.5 Override as Liability Transfer
Overrides require:
- explicit operator identity
- stated reason
- timestamp
- immutable receipt

No receipt → no mutation.

---

## 5. Governing Axiom (Write-Locked)

**Axiom of Cognitive Bypass**  
When disconfirmation cannot update cognition, governance must bypass cognition
entirely and bind behavior directly to invariant enforcement.

---

## 6. Non-Goals (Explicit)

- Not persuasion
- Not education
- Not intent inference
- Not moral judgment

DFC governance is **architectural**, not dialogic.

---

## 7. Canonical Status

This invariant is foundational.
Modification requires:
- new invariant ID
- explicit delta
- red-team pass
- version increment

Silence after refusal is intentional.
