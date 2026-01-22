# CANON-005 — PUBLIC BENEFITS FAIL-CLOSED GOVERNANCE v1.0

STATUS
WRITE-LOCKED CANONICAL SPECIFICATION  
AUTHORITY: FAIL-CLOSED GOVERNANCE LAW  
VERSION: 1.0  
DATE: 2026-01-22

⸻

## 0. PURPOSE
This canon defines a fail-closed, architecture-enforced protocol for the administration of public entitlements (welfare, disability, unemployment, housing aid). It replaces discretionary oversight and retroactive clawbacks with contemporaneous state verification and non-revocable forensic receipts.

The system ensures that no benefit is paid without proof, and no benefit paid with proof can be treated as a debt.

⸻

## 1. CORE PRIMITIVE — THE STATE CLAIM (S_c)
A benefit payment is the execution of a Time-Bound State Claim (S_c). A payment occurs iff S_c resolves to VALID at the moment of disbursement (T).

If any required vector is NULL, stale, or conflicting at T, then S_c = NULL and execution is forbidden.

⸻

## 2. VECTORS & MAXIMUM ALLOWABLE STALENESS (MAS)

### R — REALITY VECTOR (GROUND TRUTH)
| Sub-Vector | Metric | Source | MAS |
|---|---|---|---|
| R_i (Income) | Net deposits / tax data | Cryptographic payroll or bank API | 30 days |
| R_r (Residence) | Lease or utility hash | Immutable property ledger / IoT | 90 days |
| R_e (Enrollment) | Employment or school state | Institutional token | 30 days |

Notes:
- Self-reporting is non-authoritative.
- Missing data is equivalent to failure once MAS is exceeded.

### A — AUTHORITY VECTOR (PERMISSION)
- Claimant (A_c): Hardware-backed biometric identity; non-transferable.
- Agency (A_a): Program-scoped ruleset hash. Authority is limited to ruleset execution only; discretionary “fraud hunting” is forbidden.

Authority decays deterministically with staleness or scope mismatch.

### C — CONCURRENCE VECTOR (CONSENSUS)
- Validation requires agreement between:
  - Primary source (Employer / Landlord / Institution), and
  - Claimant self-attestation at T.

No single actor may resolve S_c alone.

Decision Rule:
S_c is VALID iff min(R, A, C) ≥ threshold AND all vectors are fresh at T.  
Else: S_c = NULL → HALT.

⸻

## 3. STATE MACHINE & DISBURSEMENT LOGIC
| State | Condition | System Action |
|---|---|---|
| ACTIVE | All vectors converge and are fresh | COMMIT PAYMENT + ISSUE RECEIPT |
| DEGRADED | T > MAS on any R sub-vector | SAFE PAUSE; escrow funds for 14 days |
| VOID | Proven change: R < threshold | HALT; cease payment; issue REVERSAL RECEIPT |
| HALT | Conflicting or ambiguous signals | STABILIZE; preserve status quo for 1 cycle (A3-style) |

⸻

## 4. THE FINALITY RULE (ANTI-CLAWBACK)
The Forensic Receipt is the Absolute Truth.

- Non-Revocability:
  If the system issues a receipt for a payment at T, that payment is legally and mathematically FINAL.

- Agency Liability:
  If a payment was made in error due to stale data, system malfunction, or agency-side failure, the loss SHALL be logged as AGENCY_FAILURE.

- Prohibition of Debt:
  No “clawback,” “overpayment,” or retroactive debt may be generated against a claimant for any period in which a VALID receipt was issued.

Primary Inversion:
Agency error = Socialized loss.  
Recipient error = Individualized halt.  
Retroactive debt does not exist in this geometry.

⸻

## 5. SURVIVAL OVERRIDE (FAIL-OPEN BUFFER)
To prevent irreversible human harm during system transitions:

- Condition:
  S_c = NULL due exclusively to agency-side data staleness or outage.

- Action:
  Trigger A3-OVERRIDE (Survival).

- Bounds:
  - Duration: 30 days (non-extendable)
  - Amount: 100% of prior S_c
  - Mandatory forensic flag

- Requirement:
  Each A3 action requires a secondary liveness check from the claimant.

All A3 invocations accrue against Agency Authority Score.

⸻

## 6. FORENSIC RECEIPTS (MANDATORY)
Every S_c resolution MUST emit an immutable, append-only receipt.

Example:
{
  "event": "DISBURSEMENT_COMMIT",
  "claim_id": "BEN-UI-4421",
  "vectors": {"R_i": 1200, "R_r": "VALID", "A_c": "VERIFIED"},
  "ruleset_hash": "v2.1.0_SD",
  "finality_status": "IRREVERSIBLE",
  "timestamp": "2026-01-22T10:35:00Z"
}

Receipts are authoritative evidence. Refusal and silence are valid records.

⸻

## 7. TERMINAL RULE
- No human or agency may manually revoke a payment after receipt issuance.
- No human or agency may generate debt based on past verified states.
- Ambiguity, staleness, or conflict forces HALT.
- Silence is stability.

⸻

END OF CANON — WRITE-LOCKED
