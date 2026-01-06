# Cold-Start Protocol v0.1
Status: ACTIVE
Purpose: Epistemic Reconstruction Under Total System Failure

## Goal
Enable five tired humans, no power, no network, no machines, to reconstruct truth.

Truth is defined as:
- Who has authority
- What actions occurred
- Why those actions were permitted

## Principle
If it cannot be reconstructed by hand, it is not safe.

## Components

### 1. Ledger of Intent
All meaningful actions must emit a human-readable receipt.

Required fields:
- Timestamp
- Actor
- Action Type
- Evidence Reference
- Gate State
- Risk Delta
- Invariant Protected

No nested structures.
No opaque hashes without context.
Printable on paper.

### 2. Offline Replay Drill
At least once per quarter:
- Disconnect live systems
- Provide printed ledgers only
- Require humans to explain current state

Failure to explain = epistemic failure.

### 3. Manual Sign-Off
All sealed decisions require a human to state, in one sentence:
“What invariant is being protected?”

No UI shortcuts.
No batch approval.

## Failure Condition
If humans defer understanding to a machine, the protocol has failed.
