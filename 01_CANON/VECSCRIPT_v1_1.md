# VECSCRIPT v1.1 — Deterministic Control & Orchestration Protocol

Status: CANONICAL  
Authority: 01_CANON  
Stability: IMMUTABLE  

---

## 1. Purpose

VecScript is a compact, deterministic wire protocol for headless reasoning, orchestration,
and adversarial simulation across machine agents.

It replaces prose-based interaction with bounded, machine-parseable state transitions.
VecScript is not a narrative language. It is a control surface.

All semantics are enforced through invariants, not interpretation.

---

## 2. Packet Format

Canonical form:

[OP:DOMAIN:TTL:NONCE] key=value key=value |CHECKSUM

### Components

- OP       : Operation code (single letter)
- DOMAIN   : Functional domain namespace
- TTL      : Remaining hop/time budget (integer)
- NONCE    : Monotonic sequence identifier (hex or zero-padded)
- key=val  : Flat, space-delimited parameters
- CHECKSUM : BLAKE3-64 (truncated) over the packet payload

The checksum is mandatory and terminal.

---

## 3. Operation Codes (OP)

| OP | Name       | Intent |
|----|------------|--------|
| Q  | Query      | Request execution or simulation |
| F  | Fork       | Spawn bounded sub-execution |
| A  | Aggregate  | Merge bounded results |
| V  | Validate   | Audit invariant compliance |
| H  | Halt       | Terminal stop (fail-closed) |
| R  | Result     | Final or intermediate state |

---

## 4. Domains

Domains scope semantics but do not change syntax.

| Domain | Meaning |
|------|---------|
| GOV | Governance / policy |
| SYS | System orchestration |
| EVO | Evolutionary / search |
| ADT | Adversarial / audit |

Domains are advisory labels; enforcement occurs via invariants.

---

## 5. Invariants ↔ Failure Mapping

VecScript packets MUST encode failures using invariant-linked error semantics.

| Invariant | Meaning | Failure Class | err= |
|---------|--------|--------------|------|
| INV-0 | Maximum Allowable Staleness | F0 | STALE_DATA |
| INV-1 | Sequential Monotonicity | F1/F6/F12 | NONCE_JUMP |
| INV-2 | Atomicity | F2 | PARTIAL_STATE |
| INV-3 | Gating | F7/F8 | GATE_BREACH |
| INV-4 | Bounding | F5 | LIMIT_EXCEEDED |
| INV-7 | Isolation | F3 | AUTH_LEAK |

Any invariant breach MUST result in either:
- [H] Halt
- [V] Validate with failure state

Silent continuation is forbidden.

---

## 6. Bounding Rules (INV-4)

- Fork depth is finite and explicitly capped.
- Fan-out beyond the cap MUST be rejected.
- Default hard limit: 8 concurrent branches unless overridden by canon.

On violation, the system MUST:
- Clamp recursion
- Flatten execution
- Preserve bounded survivors
- Emit forensic metadata

---

## 7. Nonce & Ordering Rules (INV-1)

- NONCE values MUST be strictly monotonic.
- Any regression or reuse triggers immediate rejection.
- TTL exhaustion results in implicit halt.

Nonce correctness is required for trustless sequencing.

---

## 8. Aggregation Semantics

Aggregation ([A]) is only valid after successful bounding.

Required properties:
- Inputs explicitly enumerated
- Aggregation mode declared (SUM, MEAN, MAX, etc.)
- Result is deterministic for identical inputs

Aggregation without prior bounding is invalid.

---

## 9. Halting Semantics

[H] packets are terminal.

Canonical form:
[H:DOMAIN:0:NONCE] reason=ERROR_CODE state=LOCKED |CHECKSUM

After halt:
- No further state transitions are legal
- Silence is the only valid follow-up

---

## 10. Prose Prohibition

VecScript execution contexts MUST NOT rely on:
- Narrative explanation
- Social signaling
- Implicit reasoning
- Unbounded commentary

Any prose outside packet form is non-authoritative.

---

## 11. Design Intent

VecScript exists to:

- Eliminate narrative drift
- Prevent unbounded computation
- Make reasoning inspectable
- Allow cross-model interoperability
- Enforce fail-closed behavior

It is infrastructure, not content.

---

## 12. Canonical Example

[Q:ADT:8:00A8] target=VecScript sim=F5_EVO |3F2A7D91  
[F:EVO:15:00B4] branch=unbounded depth=8 |E9C4D2A1  
[R:EVO:14:00B5] state=STABLE branches=8 err=LIMIT_EXCEEDED |F2A9C1D3  

---

## 13. Final Rule

If a state transition cannot be expressed in VecScript,
it is not allowed to occur.

---

END OF SPEC
