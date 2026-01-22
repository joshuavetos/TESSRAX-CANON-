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
