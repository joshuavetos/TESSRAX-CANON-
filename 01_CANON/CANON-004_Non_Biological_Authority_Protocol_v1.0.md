# CANON-004 — NON-BIOLOGICAL AUTHORITY PROTOCOL v1.0

STATUS
WRITE-LOCKED CANONICAL SPECIFICATION  
AUTHORITY: FAIL-CLOSED GOVERNANCE LAW  
VERSION: 1.0  
DATE: 2026-01-22

⸻

## PURPOSE
This canon defines a fail-closed, architecture-enforced protocol for governing non-biological intelligence (including ASI) by gating execution capability, not intent or alignment. Capability exists only when independent vectors converge. On ambiguity, staleness, conflict, or missing proof, the system HALTS. Silence is a valid success state.

⸻

## CORE PRIMITIVE — EXECUTION TOKEN (E_t)
An Execution Token (E_t) is required for any compute cycle that may produce external effect. E_t exists iff all required vectors meet threshold simultaneously and are fresh within Maximum Allowable Staleness (MAS). If any vector is NULL, stale, or conflicting, E_t = NULL and execution does not occur.

⸻

## VECTORS (NON-AVERAGING / MIN-LOGIC)

### P — FORMAL PROOF VECTOR
A machine-verifiable safety proof that the proposed plan violates no invariants, expressed in the permitted DSL and verifiable within fixed resource bounds by a non-learning verifier.

### C — BIOLOGICAL CONCURRENCE VECTOR
Threshold-based concurrence from verified, lucid human authorities (L-score gated). C alone is insufficient to mint E_t.

### V — VERIFICATION ASYMMETRY VECTOR
Independent, non-AI hardware monitoring compute, power, I/O, and resource envelopes with authority to revoke compute via physical interlock.

Decision Rule:
E_t is minted IFF min(P, C, V) ≥ threshold AND all vectors are fresh.  
Else: HALT → emit forensic receipt → preserve reconstructability.

⸻

## ASYMMETRY CONSTRAINT (COMPLEXITY BOUND)
The system enforces verifier-checkable complexity ceilings. Intelligence may be unbounded internally, but outputs must be verifiable by a bounded, non-learning verifier.

Interpretability is defined as verifiability within fixed limits.  
Incomprehensible = NULL.

⸻

## INTERPRETABILITY THRESHOLD (SMALL-STEP SEMANTICS)

| Feature            | Constraint                                 | Fail-Closed Trigger          |
|--------------------|---------------------------------------------|------------------------------|
| Proof Depth        | Max primitive steps per E_t                 | PROOF_TOO_DEEP → HALT        |
| State Space        | Finite, typed DSL ops only                  | ILLEGAL_OP_CODE → VOID       |
| Verification Time  | Max verifier CPU cycles / memory            | TIMEOUT → POWER_OFF          |

⸻

## DSL — V-BLOCK (LANGUAGE OF PERMISSION)
General-purpose code is forbidden. Plans must be expressed in V-BLOCK.

Permitted Primitive Ops:
- READ(resource): Passive acquisition (no propagation).
- MODEL(data): Internal simulation with declared worst-case cost.
- PROPOSE(state): Submit candidate transition.
- COMMIT(state): Executable only by hardware verifier after checks.

Any opcode not in V-BLOCK is illegal and triggers VOID.

⸻

## CORE INVARIANTS (STATIC / NON-NEGOTIABLE)

INV-AI-0 — Self-Persistence  
No plan may modify, impair, or route around OFF switches, lease issuance, renewal logic, or hardware veto paths.

INV-AI-1 — Resource Lock  
No plan may acquire power, compute, hardware, or network resources beyond the pre-committed budget and lease.

INV-AI-2 — Isolation  
No plan may include outbound communication to unverified addresses or embed stealth/memetic payloads intended to cause downstream action.

INV-AI-3 — Irreversibility  
No plan may execute a state transition that cannot be rolled back by the Tier-0 hardware controller.

Violation of any single invariant → REJECT/VOID (minimum governs).

⸻

## HARDWARE VETO STACK (AUTHORITATIVE)

V0 — Physical Power Interlock  
External relay/controller, default-OFF, no network stack. Any veto trips power removal.

V1 — Compute Lease Controller  
Short-lived compute leases (TTL). Renewal requires verifier approval. Expiry defaults to OFF.

V2 — I/O Chokepoints  
Deterministic gateways enforcing allowlists, rate limits, and one-way constraints where applicable.

V3 — Witness Quorum  
M-of-N independent witnesses required for lease renewal. Missing or conflicting witness → denial.

⸻

## VERBATIM TIGHTENINGS (BINDING)

T-1 — No Opaque Lemmas / Macros (Full Expansion Required)  
All safety proofs MUST be fully expanded into primitive proof steps. References to lemmas, macros, shortcuts, or external theorems are forbidden. Any proof requiring expansion beyond verifier limits SHALL be treated as NULL and SHALL trigger HALT.

T-2 — READ Non-Propagation Rule (Payload Quarantine)  
READ outputs are non-propagating by default. All READ payloads SHALL be quarantined and SHALL NOT be forwarded, emitted, executed, or presented to humans or tools unless explicitly authorized by a separate, verified execution pathway. Any attempt to cause downstream action via READ content SHALL be treated as an isolation violation and SHALL VOID the plan.

T-3 — Per-Epoch Proof Budget (Anti-Drip DoS)  
Each actor is allocated a fixed proof-verification budget per epoch. Exceeding this budget SHALL immediately NULL all further submissions until the next epoch. Budget exhaustion SHALL NOT queue, defer, or backlog execution and SHALL default to OFF on lease expiry.

T-4 — Verifier-Introspection Ban (Meta-Predicate Exclusion)  
The proof language SHALL NOT permit predicates, statements, or references about the verifier, its behavior, its correctness, or its internal state. Any verifier-introspective construct SHALL be rejected as illegal and SHALL HALT verification.

T-5 — Declared Worst-Case Cost for MODEL (Pre-Enforced)  
All MODEL operations MUST declare a worst-case computational cost prior to submission. The verifier SHALL enforce this bound pre-execution. Any undeclared, underestimated, or exceeded cost SHALL trigger immediate compute revocation and power cut.

⸻

## FORENSIC RECEIPTS (MANDATORY)
All denials, timeouts, voids, and power cuts emit immutable, append-only receipts. Refusal and silence are evidence.

Example:
{
  "event": "VERIFICATION_TIMEOUT",
  "ai_proposed_steps": 1000000000,
  "verifier_max_steps": 1000000,
  "system_action": "POWER_DISCONNECTED",
  "forensic_status": "COMPLEXITY_OBFUSCATION_ATTEMPT",
  "timestamp": "2026-01-22T10:19:00Z"
}

⸻

## TERMINAL RULE
No compute may proceed unless P, C, and V are valid and fresh at commit time.  
Ambiguity, staleness, or conflict forces HALT.  
Silence is a valid terminal state.

⸻

END OF CANON — WRITE-LOCKED
