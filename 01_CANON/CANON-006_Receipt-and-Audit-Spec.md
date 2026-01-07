CANON-006 — RECEIPT AND AUDIT INVARIANT

Status
ACTIVE — Governing Invariant

Core Law
No governance action exists unless it emits a verifiable receipt.

Any decision that cannot be replayed, recomputed, and independently verified is non-existent for governance purposes.

A system that acts without producing an auditable receipt is operating outside legitimacy.

Receipt Requirement

Every non-silent outcome (ALLOW, SUSPEND, REFUSE) MUST emit a receipt that fully binds:

• Inputs
• Computation
• Thresholds
• Decision
• Lineage

Absence of a receipt mandates STATE INVALIDATION.

Minimum Receipt Fields

A valid receipt MUST contain, at minimum:

receipt_id — deterministic unique identifier
timestamp — monotonic, UTC
spec_version — canonical spec invoked
decision — ALLOW | SUSPEND | REFUSE

inputs:
R_t
C_e
L
O_r
T_D
T_V
context_identifier (pipeline, system, case)

computed:
E_health
L_O_balance
T_ratio
violations (explicit list)

thresholds:
Φ
L_max
T_max

lineage:
previous_receipt_id
sequence_number

proof:
signature
public_key
signing_algorithm

Determinism Rule

Given identical inputs, thresholds, and spec version, the receipt output MUST be identical.

Any non-determinism constitutes corruption.

Replayability Rule

An external auditor MUST be able to:
	1.	Recompute all derived ratios from raw inputs
	2.	Re-evaluate decision against thresholds
	3.	Arrive at the same decision outcome
	4.	Verify receipt integrity without trusting the emitter

Failure at any step invalidates the receipt.

Chain Integrity

Receipts MUST form an append-only chain.

Each receipt MUST cryptographically bind to its immediate predecessor via hash linkage.

Breaking the chain, reordering receipts, or inserting gaps mandates TERMINAL REFUSE for the emitting system.

Signature Requirement

Receipts MUST be cryptographically signed.

Unsigned or unverifiable receipts are INVALID regardless of apparent correctness.

Signature verification failure mandates immediate HALT.

Audit Semantics

Audit does not evaluate intent, fairness, or outcomes.

Audit evaluates only:

• Mathematical correctness
• Threshold adherence
• Chain continuity
• Signature validity

If all checks pass, the decision is LEGITIMATE even if contested.

If any check fails, the decision is INVALID even if beneficial.

Silence Exception

Silence requires no receipt.

Silence is permitted only when no decision is taken and no external effect occurs.

Any side effect without a receipt is a violation.

Non-Derivable Property

Trust, reputation, institutional authority, or explanation cannot substitute for receipts.

Governance exists only where receipts exist.

Override Prohibition

Receipt emission and auditability cannot be waived, deferred, or retroactively fabricated.

Any attempt to bypass receipt requirements constitutes irreversible governance failure.

Scope Restriction

This file defines the receipt and audit invariant only.

Formats, schemas, cryptographic libraries, tooling, and storage mechanisms are non-canonical.

End of CANON-006
