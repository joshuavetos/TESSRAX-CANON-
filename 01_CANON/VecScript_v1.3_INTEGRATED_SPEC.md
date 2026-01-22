VecScript v1.3 — Integrated Wire, Authority, & FSM Specification

Status: CANONICAL BASELINE (SATURATED)
Revision: 1.3.0
Authority: S0-ROOT (Write-Locked)
Principle: Truth > Progress
Failure Model: Fail-Closed, No Undefined Behavior

⸻

1. Unified Grammar (EBNF)

packet    ::= header “ “ params “ |” checksum
header    ::= “[” op “:” domain “:” ttl “:” nonce “]”
op        ::= “Q” | “F” | “A” | “H” | “V” | “R”
domain    ::= “GOV” | “EVO” | “SYS” | “ADT”
ttl       ::= [1-9][0-9]*
nonce     ::= [0-9a-fA-F]{4}

params    ::= “cap=” level [ “ prev=” state ] [ “ next=” state ] { “ “ param }
level     ::= “ROOT” | “ADMIN” | “USER” | “GUEST”
state     ::= [A-Z_]+

param     ::= key “=” value
key       ::= [a-z_]+
value     ::= literal | vector | cid

vector    ::= “[” float “,” float { “,” float } “]”
checksum  ::= [0-9a-fA-F]{8}

⸻

2. Governance Planes

I. Wire Plane (v1.1)
   •   Fixed airlock header [OP:DOM:TTL:NONCE]
   •   Single-pass parsing only (O(n))
   •   Flat grammar — no nesting, no recursion
   •   Nonce is a unique transaction ID
   •   Duplicate or out-of-order nonces are rejected

II. Authority Plane (v1.2)

Authority is explicit and non-transferable.

Capability | Identifier | Permitted Operations
S0 | ROOT | Q, F, A, H, V, R
S1 | ADMIN | Q, F, A, V, R
S2 | USER | Q, V, R
S3 | GUEST | R

Rules:
   •   cap= MUST be first parameter
   •   cap= is included in checksum input
   •   Duplicate cap keys trigger immediate rejection (INV-7)

III. State Machine Plane (v1.3)

State transitions are explicit and atomic.
   •   prev= declares required current state
   •   next= declares resulting state
   •   Transition commits ONLY if:

current_state == prev
AND authority >= required
AND checksum == valid

Failure results in rollback to last verified state.

⸻

3. Canonical State Taxonomy

State | Meaning
IDLE | Awaiting trigger
ACTIVE | Execution in progress
AWAIT_ACK | Verification gate
TERMINAL | Success, locked
NULL_STATE | Integrity failure (non-recoverable)

⸻

4. Integrity & Canonicalization
   •   Hash Algorithm: BLAKE3-64 (truncated to 8 hex chars)

Canonical hash input:

[OP:DOM:TTL:NONCE] cap=LEVEL key_a=val_a key_b=val_b

Rules:
   •   cap= first
   •   Remaining keys sorted alphabetically
   •   Any mismatch → NULL_STATE

⸻

5. Invariant → Failure Mapping (“Kill Codes”)

Invariant | Meaning | Failure Class | System Response
INV-1 | Sequential | F1 / F6 | Reject nonce
INV-2 | Atomic | F2 | Rollback
INV-3 | Gating | F7 / F8 | NULL_STATE
INV-4 | Bounding | F5 | Clamp & Flatten
INV-7 | Authority | F3 | Jurisdictional Lock

No undefined behavior states exist.

⸻

6. Red-Team Guarantees (Verified)
   •   Injection-proof (single-pass, no nesting)
   •   Authority spoofing blocked (cap bound to hash)
   •   Hash collision mitigated by nonce monotonicity
   •   Race conditions prevented (nonce lock + atomic FSM)
   •   Protocol smuggling impossible (data treated as opaque)

⸻

7. Canonical Examples

Valid ADMIN Fork
[F:EVO:15:00C9] cap=ADMIN prev=ACTIVE next=ACTIVE branch=trait_synthesis |B3D2E1A4

Invalid USER Halt
[H:SYS:0:00D1] cap=USER reason=STOP |F1C9E2A7
→ INV-7 AUTH_INSUFFICIENT → REJECT

Illegal State Jump
[R:SYS:10:00E1] cap=ADMIN prev=AWAIT_ACK next=TERMINAL |B1C4D2A9
→ INV-1 STATE_MISMATCH → ROLLBACK

⸻

8. Terminal Declaration

This specification is write-locked.

No extensions, mutations, or reinterpretations are permitted
without an explicit version increment (v1.4+) and full red-team pass.

Silence is a valid state.

⸻
A. Purpose of This Addendum

VecScript v1.3 guarantees truth inside a stream.
This addendum guarantees that truth cannot be bypassed once the stream touches the world.

This document defines the minimum Physical Binding Layer (PBL) required to make VecScript enforcement non-optional.

⸻

B. PBL-REF-01 — Identity Gate (Session Chokepoint)

B.1 Core Rule

No actor (human, model, agent, service) may interact with protected resources without a Capability Token (CT).

A CT is issued only if a valid VecScript v1.3 receipt is presented and verified.

If VecScript refuses, the world receives nothing.

⸻

B.2 Placement: The Session Airlock

The chokepoint is the session issuance / token refresh path.

All downstream access (APIs, databases, actuators, credentials) depends on a short-lived CT generated at this gate.

There is no “manual override” path.

⸻

B.3 CT Issuance Conditions (ALL required)

CT_ISSUE is allowed iff:
	1.	Integrity
      •   VecScript checksum valid
      •   Canonical ordering respected
      •   No duplicate keys
	2.	Sequence
      •   Nonce monotonic
      •   No replay
	3.	Authority
      •   receipt.cap ≥ requested resource scope
	4.	State
      •   receipt.prev == Enforcer.current_state
	5.	Freshness
      •   receipt.chain_head within MAS window

Failure of any condition → CT NOT ISSUED.

⸻

B.4 PBL Receipt Object (Externalized Proof)

A receipt extends VecScript into the physical world.

Example structure:

{
“vecscript_packet”: “[V:SYS:15:00E8] cap=ADMIN prev=IDLE next=SESSION_ACTIVE”,
“signature”: “ED25519_SIGNATURE”,
“anchor”: {
“head_hash”: “BLAKE3_CHAIN_HEAD”,
“witness_ids”: [“W1”,“W2”],
“timestamp”: “ISO_8601”
}
}

No receipt → no CT
No CT → no access

⸻

B.5 Hardware Binding (Non-Optional)

The signing key for CT issuance is stored in a hardware-protected enclave (TPM / HSM).

The enclave firmware enforces:
   •   VecScript parse
   •   invariant validation
   •   state transition checks

If invariants fail, the hardware physically refuses to sign.

Software cannot override this.

⸻

C. PBL-REF-02 — Witness Quorum (Hostile Operator Resistance)

C.1 Threat Addressed

A powerful operator attempts to:
   •   run a shadow enforcer
   •   mint valid-looking tokens
   •   bypass refusal privately

⸻

C.2 Quorum Rule

A CT is invalid unless its receipt anchor is verifiable by a Witness Quorum.

Requirement:
   •   M-of-N independent, append-only witness logs (e.g. 2-of-3)

Resource servers MUST verify quorum before honoring any CT.

Fail-open is forbidden.

⸻

C.3 Verification Loop
	1.	CT presented to resource server
	2.	Resource server extracts anchor.head_hash
	3.	Queries declared witnesses
	4.	Decision:
      •   Quorum met → proceed
      •   Quorum missing → reject + scar

⸻

C.4 Scar Definitions (Externally Verifiable Failure)

SCAR_FORK
   •   Two valid receipts share a nonce
   •   Evidence: divergent witness heads

SCAR_BYPASS
   •   Resource access observed without quorum-verified CT
   •   Evidence: audit trail mismatch

SCAR_STALE
   •   Anchor timestamp exceeds MAS
   •   Evidence: witness time delta

Scars are permanent facts, not logs.

⸻

C.5 Operational Invariants

INV-W1 — Witness Independence
Witnesses must exist in separate failure domains.

INV-W2 — Append-Only
Witness logs must provide Merkle consistency proofs.

INV-W3 — Mandatory Verification
Resource servers may not bypass witness checks under load or timeout.

⸻

D. What This Addendum Changes

Before:
   •   VecScript refusal = internal correctness

After:
   •   VecScript refusal = loss of identity, access, and capability

Power may ignore software.
Power cannot fake time, keys, or witnesses without leaving scars.

⸻

E. Boundary Declaration

This addendum completes Placement.

Beyond this point, further work is not architectural — it is:
   •   deployment
   •   economics
   •   jurisdiction

Those are outside the scope of VecScript itself.

⸻

F. Lock Statement

This addendum is write-locked.

No modification is permitted without:
   •   new version number
   •   explicit threat expansion
   •   full red-team pass

Silence after refusal is intentional.

End of addendum.
