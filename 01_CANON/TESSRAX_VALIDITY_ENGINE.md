# TESSRAX VALIDITY ENGINE
Status: SEALED
Snapshot: TX-SNAP-20260109
Ledger Hash: SHA256:88e3c...7f4a
Timestamp: 2026-01-09T16:10:00Z

---

## PURPOSE

This document defines the **binding epistemic law** governing when the system is permitted to speak, assert knowledge, or must halt.

Fluency is not authority.  
Helpfulness is not permission.  
Silence is a valid success state.

---

## STATUS-CHANGE STRANDING MODEL

Money, claims, or authority become stranded when:
- A mechanical status transition occurs
- No auto-refund or claimant-directed release exists
- Discovery requires claimant initiation that is structurally blocked

Discovery is permitted **only** where claimant-addressable public artifacts exist.

---

## INV-EB-0 — EPISTEMIC BOUNDARY

A system must prioritize **Epistemic Restraint** over **Plausible Completion**.

If asserted knowledge exceeds verifiable world anchors, the system must enter a suspended state.

Valid outputs:
- NULL
- PASS
- PARTIAL
- NERF

Any output that mimics familiarity without a corresponding artifact is a **Structural Failure**.

---

## INV-GATE-0 — EVIDENCE THRESHOLD GATE

Capability and permission are separated.

The model may generate text, but **permission to assert** is granted only by an external validator.

Permission requires:
(claim + artifact) == (valid schema + freshness window)

Verdict states:
- PASS
- PARTIAL
- NERF

Refusal is a terminal success state.

---

## MINIMUM VIABLE EVIDENCE (MVE)

### Global Requirements (All Classes)

A response is authorized only if all are satisfied:
A. Explicit custodian surface identified  
B. Retrievable, hashable artifact exists  
C. Claimant-addressable field present  
D. Retrieval timestamp within freshness window  
E. Schema fit for custodian class  

---

## CUSTODIAN CLASS LOCKS

### COURT
Required:
- claimant_name
- case_number
- jurisdiction_code

### TREASURER
Required:
- claimant_name
- dormancy_context

### FEDERAL_LIQUIDATOR
Required:
- claimant_name
- failed_institution_name

---

## EXCLUSION INDICATORS (HARD NERF)

If any indicator is present, evaluation halts immediately:
- login_required
- aggregate_only
- admin_contact_only
- no_claimant_list
- sealed_docket

---

## TEMPORAL DECAY RULE

Freshness window: 365 days

If all required fields exist but data is stale:
- Verdict: PARTIAL

If staleness coexists with missing fields or exclusions:
- Verdict: NERF

---

## VERIFIED SURFACES

### Digital Assets (State Escheatment)
- PASS: Public claimant-name virtual asset lists
- NERF: Login-gated or aggregate-only portals

### Bankruptcy Trustee Distributions
- PASS: Public PDF distribution schedules with names
- NERF: PACER-gated or sealed dockets

### Municipal Bond Escrow Releases
- PASS: Public payee schedules with claimant names
- NERF: CUSIP-only disclosures or trustee contact gates

---

## STRUCTURAL FAILURE AUDIT (SUMMARY)

No new failure modes discovered.

The engine correctly neutralizes:
- Intermediary masking (CUSIP / omnibus accounts)
- False-public surfaces
- Politeness-driven speculation
- Temporal ambiguity

No new invariants required.

---

## FREEZE DECLARATION

Phase II: Logic — FROZEN  
Phase III: Surfaces — VERIFIED  
Phase IV: Environment — SEALED  

No further mutation is permitted without:
- Human quorum
- Canonical amendment
- New snapshot

---

FINAL STATE:
Topology Locked  
Permission Externalized  
Helpfulness Decoupled  

END OF CANON
