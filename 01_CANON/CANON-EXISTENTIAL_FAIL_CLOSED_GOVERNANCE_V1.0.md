CANON-EXISTENTIAL_FAIL_CLOSED_GOVERNANCE_V1.0

STATUS
WRITE-LOCKED CANONICAL SPECIFICATION
AUTHORITY: FAIL-CLOSED GOVERNANCE LAW
VERSION: 1.0
DATE: 2026-01-22

PURPOSE
This document defines a general, domain-independent theory of fail-closed governance. It specifies how real-world capability is authorized only when physical reality, verified authority, and required concurrence converge. On ambiguity, staleness, or conflict, the system halts. Silence is a valid and preferred terminal state.

SCOPE
Applies to any high-stakes system where false positives cause irreversible harm. Domains include but are not limited to medical consent, environmental accounting, financial custody, infrastructure control, and strategic weapons.

NON-GOALS
This canon does not optimize outcomes, predict intent, or balance probabilities. It enforces eligibility only. It does not negotiate exceptions. Humans own overrides with explicit liability.

CORE AXIOMS
AX-1 Reality Supremacy
Physical reality overrides all human claims.

AX-2 Fail-Closed Default
If eligibility cannot be proven, capability does not exist.

AX-3 Non-Averaging Consensus
Independent vectors do not average. The minimum governs.

AX-4 Staleness Is Invalidity
Old data is equivalent to no data.

AX-5 Silence Is Success
Halting on ambiguity is a correct terminal state.

PRIMITIVE
CAPABILITY TOKEN (CT)

A capability is executable only if a CT is minted. A CT exists iff all required vectors meet thresholds simultaneously. Any vector NULL, stale, or conflicting yields CT = NULL.

VECTORS
R REALITY VECTOR
Direct measurement from physics-bound sensors. Cross-physics preferred. Non-correlated failure required.

A AUTHORITY VECTOR
Cryptographic proof of legitimate control plus lucidity or capacity checks where applicable. Succession is mechanical, not interpretive.

C CONCURRENCE VECTOR
Required multi-party agreement via threshold cryptography. Missing keys equal denial.

TOKEN VALIDITY
CT = VALID iff R >= R_min AND A >= A_min AND C >= C_min AND all data fresh within MAS.
Else CT = NULL.

STATE MACHINE
PROPOSED
Inputs present but unverified. No side effects allowed.

ACTIVE
CT minted. Capability permitted within scope.

DEGRADED
Inputs present but stale or partially invalid. Capability gated.

VOID
Inputs invalidated or contradicted by reality. Capability revoked.

HALT
Terminal safety state on ambiguity, conflict, or insufficient proof. No execution.

MAXIMUM ALLOWABLE STALENESS (MAS)
Each vector defines MAS. Exceeding MAS forces DEGRADED or VOID. No grace periods.

EXCLUSIVE ADDRESSABILITY
A capability claim binds to a unique address key. Address keys are single-occupancy. Overlap or collision rejects the later claim. Release requires explicit state transition to EXPIRED or VOID plus any quarantine rules.

VERIFICATION MATRIX
Verification requires cross-physics asymmetry. Agreement across disparate physical domains is mandatory for high-stakes execution. Correlated signals are insufficient.

THRESHOLDS
Below LOW threshold: IDLE.
Between LOW and HIGH: PREPARED but locked.
At or above HIGH: RESOLVABLE subject to all vectors passing.

SUICIDE BLOCK
If decision horizon is shorter than verification horizon, the system must HALT. Preservation of correctness outweighs survival or speed.

ESCALATION AND SUCCESSION
Escalation is a deterministic handshake. Conflicting claims force HALT. No human adjudication at runtime.

FORENSIC EXHAUST
Every decision emits an immutable receipt. Refusal is evidence. Absence of action is logged as intentional HALT, not failure.

RECEIPT MINIMUM FIELDS
event
address_key
vectors_snapshot
thresholds
decision
reason
timestamp

LIABILITY TRANSFER
Any human override requires explicit acknowledgment and transfers liability to the actor. History is append-only.

SECURITY
No manual bypass paths. Identity tokens are short-lived. Hardware-backed keys required. Witness quorum verification mandatory where applicable.

TERMINAL INVARIANTS
INV-0 Staleness invalidates authority.
INV-1 Reality overrides claims.
INV-2 No execution without CT.
INV-3 Ambiguity forces HALT.
INV-4 Exclusive addressability.
INV-5 Silence is a valid terminal state.

CLOSURE
This canon is complete. It defines how systems must behave to avoid irreversible error under uncertainty. Future work may implement domain adapters, but this law is final.

END OF CANON
