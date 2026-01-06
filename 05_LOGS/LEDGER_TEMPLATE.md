# TESSRAX Ledger Template (Human-Readable)

Format: Fixed-width, printable, no nested structures.

| TIMESTAMP | ACTOR_ID | ACTION_TYPE | EVID_HASH | GATE_STATUS | RISK_DELTA | INVARIANT |
|-----------|----------|-------------|-----------|-------------|------------|-----------|

## Rules
- One line per causal action
- Evidence hash must map to offline appendix
- Risk deltas are cumulative and visible
- Any REJECT halts downstream actions

## Invariant
If this ledger cannot explain the system to a stranger,
the system is unsafe.
