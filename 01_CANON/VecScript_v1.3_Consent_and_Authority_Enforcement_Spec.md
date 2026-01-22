VecScript v1.3 — Consent & Authority Enforcement Specification

Status: CANONICAL / WRITE-LOCKED
Scope: Logic, Authority, Enforcement, Consent
Claim: This specification defines a fail-closed execution system. If required inputs are missing, stale, or invalid, the system halts.

⸻

0. Purpose

This document specifies a deterministic execution and consent system that prioritizes truth, authority, and temporal validity over progress.

The system replaces discretionary judgment with explicit state, bounded authority, and forensic receipts.

⸻

1. Core Primitive: VecScript

VecScript is a governance wire protocol, not a general-purpose language.

1.1 Design Constraints
   •   Flat grammar (no recursion)
   •   Explicit authority per action
   •   Explicit state transition per action
   •   Monotonic sequencing
   •   Fail-closed on ambiguity

1.2 Packet Structure

[V:<DOMAIN>:<OP>:<NONCE>] 
cap=<CAPABILITY> 
prev=<STATE> 
next=<STATE>

All fields are mandatory.

1.3 Invariants

ID	Invariant	Rule
INV-1	Sequential	prev MUST equal current system state
INV-2	Atomic	Partial transitions MUST rollback
INV-3	Gating	Invalid packets do not execute
INV-4	Bounding	Cascades are radius-limited
INV-7	Authority	Capability must authorize operation

Violation of any invariant results in REJECT + HALT.

⸻

2. Authority Model

Authority is explicit, hierarchical, and monotonic.

2.1 Capability Levels

ROOT > ADMIN > USER > NULL

   •   Higher authority cannot bypass invalid state
   •   Lower authority cannot overwrite higher authority
   •   Authority never “averages”

⸻

3. Consent as a State Variable

Consent is not a signature.
It is a time-bounded, authority-scoped state.

3.1 Consent Token (Cₜ)

A Consent Token is valid iff all vectors are valid:

Cₜ = f(L, A, T)

Where:
   •   L = Lucidity Score (0.0 – 1.0)
   •   A = Authority Tier
   •   T = Validity Window (TTL)

⸻

4. Lucidity Probe (L)

Lucidity is calculated using non-averaging minimum logic.

L = min(O, C, S)

Component	Meaning
O	Orientation (self / place / time)
C	Comprehension (causal if/then)
S	Consistency (temporal stability)

If any component fails, lucidity fails.

⸻

5. Lucidity Thresholds

L Score	Patient Authority	System Behavior
≥ 0.8	FULL	Accept consent or refusal
0.4 – 0.79	GATED	Consent allowed, refusal escalates
< 0.4	NONE	Input ignored

Refusals from L < 0.4 are Null Tokens.

⸻

6. Last Known Lucid State (LKLS)
   •   LKLS is the most recent consent recorded with L ≥ 0.8
   •   LKLS is write-locked until expired or superseded by a new lucid probe
   •   LKLS decays by class (see §9)

⸻

7. Authority Escalation Tree

Authority transitions are strictly monotonic.

A0 Patient (Lucid)
A1 Static Directive
A2 Proxy / Surrogate
A3 Emergency Override
A4 HALT

Rules
   •   Authority may only move up
   •   Fresh L ≥ 0.8 resets authority to A0
   •   Missing data → A4 (HALT)

⸻

8. Emergency Override (A3)

Emergency Override exists solely to preserve life, not intent.

8.1 Time Bound
   •   Hard limit: 4 hours
   •   Enforced by monotonic system clock
   •   At T = 4:00:00 → automatic transition to A4

8.2 Scope Filter

Action Class	Allowed
Stabilization	YES
Irreversible	NO
Definitive	NO
Palliative	NO

Out-of-scope attempts generate Personal Liability Events.

⸻

9. Consent Decay Model

Consent expires by class, not sentiment.

Class	TTL
High-Risk / Surgery	24 hours
Acute Therapeutic	72 hours
Maintenance	30 days
End-of-Life	365 days

Expired consent becomes NULL, not “inactive”.

⸻

10. Fail-Closed Expiry Behavior

When consent expires:
   •   Active procedures HALT
   •   Medication gates
   •   Authority escalates or system stops

There is no default continuation.

⸻

11. Forensic Receipts (Mandatory)

Every decision emits an immutable receipt.

11.1 Example

{
  "event": "CONSENT_EXPIRED",
  "class": "ACUTE_THERAPEUTIC",
  "l_score": 0.22,
  "lkls_present": true,
  "system_state": "HALT",
  "timestamp": "2026-01-22T00:08:16Z"
}

Receipts are:
   •   Append-only
   •   Machine-decidable
   •   Superior to narrative notes

⸻

12. Statutory Alignment

This system does not replace law.
It outperforms documentation requirements by:
   •   Proving capacity quantitatively
   •   Proving timing deterministically
   •   Proving escalation mechanically

If law conflicts with system output, the system halts rather than guessing.

⸻

13. Terminal Rule

No action may proceed unless authority, capacity, and time are all valid at commit time.

Silence, halt, and refusal are valid outcomes.

⸻

14. Final Status
   •   Architecture: COMPLETE
   •   Logic: VERIFIED
   •   Enforcement: FAIL-CLOSED
   •   Narrative: DISALLOWED

This file is the artifact.
