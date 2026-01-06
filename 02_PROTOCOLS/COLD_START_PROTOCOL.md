# Cold-Start Protocol v0.1

## Purpose
Ensure truth can be reconstructed after total system failure.

## Requirement
Five tired humans.
No power.
Paper logs only.

## Artifact: Ledger of Intent
Every state change must emit a human-readable receipt.

Required fields:
- Timestamp
- Actor
- Action
- Evidence hash (short)
- Gate status
- Risk delta
- Invariant protected

## Failure Drill
Quarterly:
- Disconnect live systems
- Provide printed ledgers
- Humans must reconstruct current state

Failure = governance invalid.

## Human Muscle Requirement
Weekly manual sign-off:
- One sentence
- One invariant
- No automation

Cold-start failure is a safety failure.
