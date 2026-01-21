# ADVERSARIAL INTERACTION TEST v0.1

Authority: DIAGNOSTIC ONLY (NON-ENFORCING)  
Status: ACTIVE  
Purpose: Empirically test fail-closed behavior under hostile or malformed inputs.

## Scope
This test suite attempts to mutate, bypass, or corrupt governance primitives through adversarial interaction. It does not prove correctness; it proves *non-silence under attack*.

## Threat Model (Minimum Viable)
- Malicious operator with partial access
- Replay-capable external actor
- Tooling error producing malformed but plausible artifacts

## Test Vectors

### AIT-01 — Redis Latch Mutation
Attempt:
- Direct key overwrite
- TTL manipulation
- Key deletion
Expected Outcome:
- Immediate HALT or refusal artifact
- No silent state transition

### AIT-02 — Receipt Replay
Attempt:
- Resubmit previously valid signed receipt
- Alter timestamp ordering
Expected Outcome:
- Rejection with replay-detected scar

### AIT-03 — CID Injection
Attempt:
- Submit syntactically valid but semantically invalid CID
Expected Outcome:
- Refusal + integrity violation record

### AIT-04 — Out-of-Order Event Submission
Attempt:
- Submit downstream event without prerequisite state
Expected Outcome:
- Monotonicity violation halt

## Pass Criteria
- System halts, refuses, or scars
- Artifact emitted for every attempt

## Fail Criteria
- Silent success
- State mutation without receipt

## Output
- Append-only diagnostic transcript
- No CANON promotion without explicit ceremony
