# PROTO-001: Cold-Start Protocol (v0.1)

## Purpose
Ensure that “Truth” remains reconstructable by humans if all digital systems fail.

This protocol defines the minimum conditions under which a system can be
considered epistemically sovereign.

## Definition
A system passes Cold-Start if:

> Five tired humans, with no power and no screens, can reconstruct
> the authoritative state of the system using only printed logs.

If this is not possible, the system is unsafe regardless of uptime.

## Core Artifact: The Human-Readable Ledger

Every critical action must emit a **Canonical Receipt** with the following properties:

- Fixed-width text
- Printable on A4
- No nested structures
- One line = one causal claim

### Required Fields
| Field | Description |
|------|-------------|
| Timestamp | When the action occurred |
| Actor_ID | Human or system responsible |
| Action_Type | What changed |
| Evidence_Ref | Short hash or pointer |
| Gate_Status | OPEN / SEALED / REJECTED |
| Risk_Delta | Change in systemic risk |
| Invariant | Which invariant was protected |

## Weekly Re-Enactment (The Muscle)

Once per week:

1. Print the last 7 days of ledger entries
2. Disconnect all live systems
3. A human must verbally summarize:
   - What changed
   - Why it was allowed
   - What risk increased or decreased

Failure to do this indicates epistemic atrophy.

## Success Criteria
- Humans can explain system state without querying it
- Disagreements can be resolved by pointing to ledger lines
- No appeal to “the system says so”

## Failure Mode
If Cold-Start fails, the system must be treated as:
- Operationally live
- Epistemically dead

## Status
ACTIVE PROTOCOL
