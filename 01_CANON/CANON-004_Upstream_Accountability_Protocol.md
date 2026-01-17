TITLE: CANON-004 — Upstream Accountability Protocol (UAP)
STATUS: LOCKED / READ-ONLY / FORK-DETECTABLE
VERSION: 1.0.0-GENESIS
HASH-ANCHOR: sha256_jvetos_genesis_8829
AUTHORITY: 01_CANON
DATE: 2026-01-17

---

## PURPOSE

This document is the canonical constitutional specification for the
Upstream Accountability Protocol (UAP).

UAP is a non-negotiable, fail-closed governance layer designed to enforce
upstream liability in high-stakes systems where human discretion,
committee process, or narrative justification would otherwise allow
systemic harm.

This file is LAW.
Deviation from this document constitutes a governance breach.

---

## SECTION I — NON-NEGOTIABLE INVARIANTS (INVARIANT CORE)

These invariants are enforced at the logic-gate level.
They cannot be overridden, paused, scoped, or administratively bypassed.

### INV-0 — Identity–Budget Symmetry
No DecisionLog is valid unless the Owner_ID cryptographically possesses:
- Active budgetary authority
- Veto power over execution
- A verifiable succession chain

Accountability without power is invalid.

---

### INV-1 — Monotonic State Progression
State transitions toward liability are one-way.

Once a RISK_DETECTED signal is verified:
- The clock is immutable
- No human actor may pause, reset, or defer the transition
- Narrative delay is structurally impossible

---

### INV-2 — Atomic Proof Asymmetry
The system defaults to UNRESOLVED.

- Proof is scarce
- Silence is failure
- “Risk retired” has zero weight without verifier quorum attestation

---

### INV-3 — HARD_HALT GATING
Any architectural violation triggers HARD_HALT by default, including:
- Succession gaps
- 10-day reporting failure
- Verifier quorum dissent
- Root Covenant breach
- Aggregate Drift

HARD_HALT is not advisory. It is an execution interlock.

---

## SECTION II — CONTRADICTION METABOLISM (V2.0 HARDENED)

Contradiction Metabolism is the semantic enforcement engine of UAP.
It evaluates truth as a mechanical comparison between:

- Attestation (what was signed)
- Telemetry (what occurred)
- Audit (what is verifiable)

### Rule 1 — Vectorized Predicate–Outcome Mismatch
Intent is expressed as a predicate vector P.
Observed behavior is O.

If any axis satisfies |P - O| > threshold:
A Metabolic Conflict is generated.

Owners cannot override conflicts.
Only reconciliation artifacts may resolve them.

---

### Rule 2 — Evidence Scarcity
To prevent truth flooding:
- Maximum of three reconciliation artifacts per risk event
- Submissions beyond this are classified as EVIDENCE_ABUSE
- EVIDENCE_ABUSE escalates directly to STRICT_LIABILITY

---

### Rule 3 — Reaction Curve Hardening
Contradictions harden over time.

T+0 to T+10: Discovery (Safe Harbor eligible)
T+11 to T+30: Metabolism (mitigation required)
T+31 onward: Calcification

Unresolved contradictions at T+31 are treated as Intent Fraud.

---

### Rule 4 — A² Aggregate Drift Invariant
Local compliance is void under global harm.

If Global Telemetry Divergence exceeds survival thresholds:
- A JOINT_RISK_EVENT is triggered
- All contributing Owner_IDs are transitioned to RISK_DETECTED
- Co-signed reconciliation is required to exit

Systemic health supersedes local virtue.

---

## SECTION III — STATE MACHINE (HARDENED CORE)

The UAP engine is a deterministic, side-effect-free state machine.

S_next = f(S_current, Input)

The engine:
- Has no wall-clock access
- Uses fixed-point arithmetic only
- Accepts only signed, Merkle-validated inputs
- Defaults to HARD_HALT on ambiguity

### Terminal States
- NORMAL
- RISK_DETECTED
- SAFE_HARBOR
- STRICT_LIABILITY
- HARD_HALT

No state transition exists that reduces liability.

---

## SECTION IV — REFUSAL DOCTRINE

The power of UAP is refusal.

The system explicitly refuses:
- Committee-based ownership
- Retroactive intent modification
- Narrative justification
- Risk deferral
- Local virtue during global failure

A refusal is a valid terminal output.

---

## SECTION V — EVIDENCE PRIMITIVES (JURISDICTION-AGNOSTIC)

UAP evidence is admissible across civil and common law systems.

Required primitives:
- Attestation Header (intent + covenant + identity)
- Oracle Consensus Root (Merkle, >=3 heterogeneous sources)
- Verifier Quorum Receipt (VRF-selected, multi-signature)
- Causal Fingerprint (SHA-256 failure signature)

All artifacts are append-only and fork-detectable.

---

## SECTION VI — VERIFIER & ORACLE ANTI-CAPTURE

Witnesses are treated as adversarial components.

- Verifiers are VRF-selected
- Metadata is stripped (blind falsification)
- Co-occurrence is tracked
- Post-hoc recurrence triggers correlated slashing
- Quorum failure escalates to STRICT_LIABILITY

False-negative halts are acceptable.
False-positive passes are not.

---

## SECTION VII — AUDIT & REGULATORY STANDING

This protocol satisfies:
- ISO 42001 (Clauses 6.1, A.5.2)
- NIST AI RMF (GV.RM-01, ME-01)
- NIST CSF 2.0 accountability requirements

Compliance is continuous, not periodic.

“I followed the process” is not a valid defense under this system.

---

## SECTION VIII — TERMINAL LOCK

This document is LOCKED.

Any modification:
- Creates a fork
- Invalidates prior receipts
- Transfers liability to the modifier

Silence, refusal, and halt are valid success states.

END OF CANON.
