# CANON-006 — EDUCATION AID FAIL-CLOSED GOVERNANCE v1.0

STATUS  
WRITE-LOCKED CANONICAL SPECIFICATION  
AUTHORITY: FAIL-CLOSED GOVERNANCE LAW  
VERSION: 1.0  
DATE: 2026-01-22

⸻

## 0. PURPOSE
This canon defines a fail-closed, architecture-enforced protocol for the administration of education loans and aid. It replaces speculative, unbounded debt with Performance-Gated Multi-Stage State Claims (S_c).

The system ensures that debt cannot outgrow the reality it was intended to fund, and that servicer authority terminates the moment data integrity fails.

⸻

## 1. CORE PRIMITIVE — PERFORMANCE-GATED STATE CLAIM (S_c)
An education loan is a series of state-contingent disbursements. A loan exists iff S_c resolves to VALID at the moment of each disbursement (T).

If any required vector is NULL, stale, or conflicting at T, then S_c = NULL and execution is forbidden.

⸻

## 2. VECTORS & MAXIMUM ALLOWABLE STALENESS (MAS)

### R — REALITY VECTOR (GROUNDING)
| Sub-Vector | Metric | Source | MAS |
|---|---|---|---|
| R_e (Enrollment) | Active student status | University Registrar API | 24 hours |
| R_p (Performance) | Academic Progress (SAP) | Institutional Grade Ledger | 1 semester |
| R_i (Income) | Post-graduation earnings | Cryptographic payroll / tax API | 30 days |

Notes:
- Enrollment is checked continuously during STUDY state.
- Performance is evaluated at formal academic checkpoints.
- Income telemetry is authoritative only when fresh; staleness equals failure.

### A — AUTHORITY VECTOR (PERMISSION)
- Student (A_s): Biometric identity locked via hardware key.
- Servicer (A_v): Authority restricted strictly to the Interest Calculation DSL. No discretionary balance modification, fee insertion, or retroactive adjustment is permitted.

Authority decays deterministically on scope violation or telemetry loss.

### C — CONCURRENCE VECTOR (CONSENSUS)
- Triple-Lock concurrence is required between:
  - University (service provider attestation),
  - Student (beneficiary attestation),
  - Creditor (funding authorization).

No single party may resolve S_c unilaterally.

Decision Rule:  
S_c is VALID iff min(R, A, C) ≥ threshold AND all vectors are fresh at T.  
Else: S_c = NULL → HALT.

⸻

## 3. STATE MACHINE & INTEREST KILL-SWITCH
| State | Condition | Outcome |
|---|---|---|
| STUDY | R_e = TRUE AND R_p = PASS | Interest GATED (0%). Disbursement committed. |
| REPAYMENT | R_e = GRADUATED AND R_i > threshold | Interest active. Amortization driven strictly by R_i telemetry. |
| STABILIZE | R_i ≤ threshold (unemployment / underemployment) | SAFE PAUSE. Interest compounding HALTS. |
| VOID | Credential fraud or R_p failure | Immediate HALT. System emits DEBT_CAP_RECEIPT. |

Interest authority exists only in REPAYMENT state with fresh income telemetry.

⸻

## 4. INVARIANTS (THE STALENESS SHIELD)

### INV-ED-0 — Debt-to-Reality Cap
The total lifetime liability (Principal + Interest) MAY NOT exceed X% (e.g., 200%) of the Verified Reality.

Verified Reality is defined as the rolling average of 10-year income associated with the earned credential, derived from authoritative R_i telemetry.

Any liability exceeding this cap SHALL be AUTO-VOIDED at detection.

### INV-ED-1 — Staleness = Interest Freeze
The authority to compound interest is contingent on continuous freshness of the R-vector.

If the servicer (A_v) cannot prove the student’s current income or status due to telemetry loss or staleness:
- Interest calculation is REJECTED.
- The balance is WRITE-LOCKED at the last verified state.
- The burden of data freshness resides exclusively with the Creditor.

No adverse inference may be drawn against the student.

⸻

## 5. FORENSIC RECEIPT CHAIN
The balance is a calculation, not a variable.

- Chain of Truth:
  The current balance MUST be reconstructable from an append-only chain of forensic receipts:
  Disbursement → Payment → Interest Tick.

- Unreconstructable Debt = NULL:
  If a servicer cannot produce the complete receipt chain for any segment of the debt’s history, the balance for that segment is treated as NULL and unenforceable.

Receipts are immutable. History is append-only.

⸻

## 6. TERMINAL RULE
- No debt may outlive the forensic evidence of its creation.
- No interest may accumulate in the absence of verified reality.
- No receipt = No debt.
- Ambiguity, staleness, or conflict forces HALT.

Silence is stability.

⸻

END OF CANON — WRITE-LOCKED
