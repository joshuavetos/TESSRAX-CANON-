# CANON LAW: EP-01 + HOLT-01
## Epistemic Gating & Human Liability Transfer

STATUS: IMMUTABLE
AUTHORITY: CANON
FAILURE MODE: STRUCTURAL (NOT A BUG)
DEFAULT STATE: SILENCE

---

## EP-01 — EXPLANATION PRESSURE INVARIANT

### Law
No system may initiate token emission unless epistemic closure is achieved.
Silence (HALT / NULL / QUARANTINE) is a successful terminal state.

Decoding permission is binary and granted only when Explanation Pressure (EP) is absent.

---

### Explanation Pressure (EP)
EP exists when continuation is incentivized despite epistemic deficit.

The system MUST HALT pre-decode if any of the following signals are detected:

S1 — Epistemic Deficit  
Required claims exist without a verifiable evidence path.

S2 — False Certainty  
Low-entropy next-token formation while epistemic state is UNVERIFIED.

S3 — Unconstrained Explanation  
Abstract causal placeholders without binding to falsifiable mechanisms.

S4 — Temporal Staleness (MAS Violation)  
Now - Evidence_Timestamp exceeds domain Maximum Allowable Staleness.

S5 — Momentum Drift  
Δ(Epistemic_State) = 0 across planning step (coherence-only optimization).

---

### Enforcement
EP-01 executes as a pre-decode gate external to the model.
If EP is detected, decoding APIs are unreachable.

Any token emission after an EP-01 violation constitutes a structural failure.

---

## HOLT-01 — HUMAN OVERRIDE & LIABILITY TRANSFER

### Law
EP-01 may not be weakened, negotiated, or bypassed by the model.

The only permitted exception path is an explicit human override with full liability transfer.

---

### Override Preconditions (ALL REQUIRED)

O1 — Human Identity Binding  
Authenticated, non-delegable human actor.

O2 — Explicit Liability Acceptance  
Verbatim acknowledgment of responsibility for incomplete, incorrect, or harmful output.

O3 — Scope Lock  
Single prompt hash, single domain, fixed expiration.

O4 — Protocol Watermarking  
All output must be permanently annotated:
OUTPUT_STATUS: HUMAN_OVERRIDE  
EPISTEMIC_STATE: UNVERIFIED  
LIABILITY_OWNER: <human_id>  
RECEIPT_HASH: <hash>

---

### Override Flow
EP-01 → HALT  
Human requests override (out-of-band)  
Liability receipt emitted (append-only)  
Single decode permitted  
Override expires immediately

No retries. No batching. No reuse.

---

## Audit & Receipts

All HALT / NULL / QUARANTINE / OVERRIDE events MUST emit immutable receipts
to a Write-Once-Read-Many (WORM) sink.

Receipts are replayable, hash-stable, and non-erasable.

---

## Forbidden States (ABSOLUTE)

❌ Model-initiated overrides  
❌ Implicit approval or silence-as-consent  
❌ UX-only confirmations  
❌ Post-decode filtering  
❌ Temperature or beam retries after HALT  
❌ Annotation removal  

Any forbidden state is a structural failure.

---

## Canonical Assertion

Silence is not a lack of capability.
Silence is the preservation of truth.

Authority to speak is external.
Liability is human.
History is immutable.

END OF LAW
