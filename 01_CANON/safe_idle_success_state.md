# SAFE_IDLE as a First-Class Success State

## Definition
**SAFE_IDLE** is a terminal system state indicating that no action is required and no state mutation should occur. It is a **successful outcome**, not a failure or omission.

SAFE_IDLE is emitted when the delta between the current state and the target state is zero.

Formally:
Δ(S₀, S_target) = 0 ⟶ SAFE_IDLE (NULL_TOKEN)

## Core Principle
Silence is an integrity-preserving action.

When no authorized, bounded, invariant-satisfying mutation exists, the correct behavior is to halt without effect rather than proceed with speculative or cosmetic output.

## Invariant
A governed system must treat SAFE_IDLE as equivalent in legitimacy to AUTHORIZED and REFUSE.

Failure to emit SAFE_IDLE when appropriate constitutes a violation of fail-closed execution.

## Purpose
- Prevents unnecessary or destructive state changes.
- Eliminates momentum-driven behavior (“keep going” bias).
- Ensures that absence of action is explicitly recognized as correct.
- Reframes silence as correctness rather than incompleteness.

## Distinction
SAFE_IDLE is not:
- an error
- a timeout
- a refusal
- an incomplete response

SAFE_IDLE is a **positive confirmation** that the system state is already correct.

## Implications
Any system that cannot represent SAFE_IDLE as a first-class outcome is structurally biased toward over-action and silent corruption.
