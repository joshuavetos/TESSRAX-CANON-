# AUDIT RECEIPT SPECIFICATION v1.0
Status: CANON-COMPATIBLE  
Authority: CANON-003_Claim_Economy  

An Audit Receipt is a deterministic, append-only artifact emitted for a single decision.

No decision is considered real without a receipt.

## Receipt Invariants
- Atomic
- Append-only
- Evidence-bound
- Dependency-closed
- Dual-readable

Failure of any invariant renders the receipt INVALID.

## Auditor Provenance Requirement
Every receipt MUST declare auditor identity, infrastructure, and independence attestation.

Failure to demonstrate independence constitutes SELF_AUDIT_FAILURE.

## Self-Audit Failure
All receipts issued under SELF_AUDIT_FAILURE are downgraded to UNVERIFIED regardless of outcome.

END OF FILE
