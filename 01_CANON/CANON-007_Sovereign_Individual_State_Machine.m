PATH: 01_CANON/CANON-007_Sovereign_Individual_State_Machine.md
AUTHORITY: CANON-007 (Unified Individual Financial Shield)
STATUS: WRITE-LOCKED
VERSION: v1.0
DATE: 2026-01-22

---

# SOVEREIGN INDIVIDUAL STATE MACHINE v1.0  
## Fail-Closed Governance Visualization Specification

## 0. PURPOSE

This artifact defines the authoritative state machine governing an individual’s financial liability under the Unified Individual Financial Shield (CANON-007).

It is not illustrative.  
It is a **deterministic execution model** describing how all incoming claims interact with the Individual Shield, the Public Truth Ledger (PTL), and Agency Authority Scores (AAS).

Silence, refusal, and null states are first-class terminal outcomes.

---

## 1. CORE ENTITY

**Biological Individual**  
A finite, non-fungible actor protected by a cryptographic Individual Financial Shield.

The individual does not negotiate.  
They either present a valid State Claim (S_c), or the system halts.

---

## 2. INPUT PLANES (R / A / C)

### 2.1 Reality Plane (R — Ground Truth)

Authoritative only if physics-bound and within MAS.

- Income Telemetry (Payroll / Tax API)
- Employment State
- Residency Proof
- Clinical Encounter Tokens
- Enrollment / Credential Tokens

Failure Modes:
- Missing telemetry → R = NULL
- Stale telemetry → SAFE PAUSE
- Conflicting signals → HALT

---

### 2.2 Authority Plane (A — Permission)

Defines who may assert a claim.

- Proof of Note (Housing)
- Ruleset Hash (Benefits / Education)
- Judicial Order (Justice)
- Servicer Authority (Interest DSL)
- Agency Authority Score (AAS)

Failure Modes:
- Broken custody chain → A = NULL
- AAS below threshold → WRITE-LOCKED
- Unauthorized opcode → REJECT

---

### 2.3 Concurrence Plane (C — Consensus)

Non-averaging agreement at time T.

- Patient Handshake
- Student Attestation
- Tenant Acknowledgment
- Employer / University / Court Confirmation

Failure Modes:
- Missing concurrence → NULL
- Retroactive concurrence → INVALID
- Proxy outside scope → REJECT

---

## 3. GATES (ENFORCEMENT ORDER)

Claims traverse gates **in order**.  
Failure at any gate halts execution.

### Gate 1 — Proof Gate
Rule: No Receipt → NULL  
Effect: Claim evaporates. No liability attaches.

### Gate 2 — Freshness Gate
Rule: MAS exceeded → SAFE PAUSE  
Effect: Interest frozen. Payments escrowed if applicable.

### Gate 3 — Authority Gate
Rule: AAS < Threshold → WRITE-LOCKED  
Effect: Claim unenforceable. Agency blocked.

### Gate 4 — Invariant Gate
Rule: Invariant violation → REJECT + PENALIZE  
Effect: Claim voided. Agency score degraded.

---

## 4. GLOBAL LIABILITY STATES

### ACTIVE_CLAIM
- Bounded
- Receipted
- Enforceable

### SAFE_PAUSE
- Reality degraded
- Interest frozen
- No compounding
- No penalties

### WRITE_LOCKED
- Authority failure
- Claim unenforceable
- Asset protected

### NULL
- Proof failure
- Claim non-existent
- No debt possible

### A3_SURVIVAL
- Time-boxed fail-open
- Life preservation only
- Mandatory forensic flag

### TERMINAL_CLEAR
- Zero liability
- No active claims
- Shield idle

---

## 5. PUBLIC TRUTH LEDGER (PTL) INTERFACE

The Shield continuously ingests Agency Authority Scores.

### AAS States
- ≥ 0.90 → Full Authority
- 0.89 – 0.70 → Degraded (GATED)
- < 0.70 → NULLIFIED (GLOBAL HALT)

Effects:
- AAS degradation propagates to all individual shields.
- Institutional failure scales instantly.

---

## 6. CROSS-DOMAIN TERMINAL INVARIANTS

INV-U-0 — No Debt Without Proof  
INV-U-1 — No Interest Without Reality  
INV-U-2 — No Surprise Liability  
INV-U-3 — Staleness Nullifies Authority  
INV-U-4 — Agency Error Is Socialized  

Violation of any invariant is unrecoverable for that claim.

---

## 7. TERMINAL RULE

The individual never argues.  
The institution never pleads.

If proof converges → execute.  
If proof fails → halt.  

**Silence is stability.**  
**Fail-Closed is safety.**

END OF CANON-007 STATE MACHINE  
WRITE-LOCKED — NO MUTATION
