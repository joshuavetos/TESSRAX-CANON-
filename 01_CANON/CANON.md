# CANON — TESSRAX GOVERNANCE LAW

Status: BINDING  
Scope: All systems, tools, cases, and products in this repository  
Rule: Anything that contradicts this file is invalid by default

---

## CORE POSITION

Tessrax is not an AI assistant framework.  
It is a **governance system for bounded reasoning under liability**.

Explanation is a side effect.  
Provenance, refusal, and reconstructability are the product.

---

## DEFINITIONS (NON-DERIVABLE)

**Governance**  
Executable constraints that determine what actions are allowed, refused, or halted.

**Invariant**  
A rule that must always hold. If violated, the system must fail closed.

**Fail-Closed**  
On ambiguity, missing data, or rule violation: STOP, REFUSE, or HALT.

**Receipt**  
A durable artifact proving what was evaluated, under which rules, and why an action occurred or was refused.

**Refusal**  
A first-class, successful outcome when constraints are not met.

**Silence / NULL_TOKEN**  
A valid terminal state indicating no authorized output.

---

## GLOBAL INVARIANTS

### INV-0 — Temporal Reality Enforcement
All claims must bind to current, verifiable reality or be explicitly marked UNKNOWN.  
Stale or assumed truth invalidates output.

### INV-1 — Sequential Integrity
State transitions must be monotonic and reconstructable.  
No retroactive justification. No hidden jumps.

### INV-2 — Atomicity
Actions either complete fully with a receipt or do not occur at all.  
Partial execution is a failure state.

### INV-3 — Gating
No action without passing required gates.  
Gate failure produces refusal, not improvisation.

### INV-4 — Bounding
All systems must have a defined halt condition.  
Unbounded operation is a structural defect.

---

## FAILURE TAXONOMY (SFDD)

Structural failures are architectural, not semantic.

Closed set includes:
- Ordering violations
- Partial commits
- Zombie mutations
- Premature irreversibility
- Unbounded fan-out
- Race conditions

Structural failures cannot be patched with prompts, policy, or intent.

---

## EPISTEMIC RULES

- Unknown is a valid answer.
- Silence is a valid answer.
- Confidence without provenance is invalid.
- Plausibility is not permission.

If Unknowns > Knowns → HALT.

---

## LIABILITY & AUTHORITY

The system never absorbs liability.
Human override is allowed only with:
- Explicit acknowledgment
- Reason
- Timestamp
- Permanent receipt

Overrides transfer liability to the human actor.

History is append-only.
We do not fix bugs in history.
We ship new law forward.

---

## CANONICAL STOP CONDITION

If a system cannot:
- Refuse safely
- Halt cleanly
- Reconstruct its state from artifacts

Then it is **invalid**, regardless of usefulness.

---

END CANON
