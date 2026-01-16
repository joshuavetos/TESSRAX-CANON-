TESSRAX ENGINE — EXECUTION CONTRACT
Version: v0.1.0
Status: ENFORCEMENT-BOUND

This document defines the authoritative execution contract for the Tessrax
validation engine. Any behavior not explicitly permitted here is disallowed.

----------------------------------------------------------------

1. PURPOSE

The Tessrax engine exists to make binary enforcement decisions over
claim-related artifacts using deterministic, fail-closed rules.

It does NOT:
- Discover data
- Modify artifacts
- Persist state
- Perform recovery
- Interpret law
- Explain outcomes

It only evaluates inputs and emits a verdict.

----------------------------------------------------------------

2. INPUT CONTRACT

The engine accepts exactly two inputs per execution:

A) Claim Data (claim_data)
   - Must be a structured object
   - Must include "custodian_class"
   - No implicit defaults are allowed

B) Artifact (artifact)
   - Must be a structured object
   - Must include:
     • retrieval_timestamp (ISO-8601 UTC)
     • metadata (object)

Inputs that do not conform SHALL cause immediate failure.

----------------------------------------------------------------

3. EXECUTION SURFACE

The only supported execution surface is:

    python -m engine.main <claim_data.json> <artifact.json>

Any other invocation path is unsupported.

----------------------------------------------------------------

4. VERDICT SEMANTICS

The engine emits exactly one of the following verdicts:

PASS
- All required fields present
- No exclusion indicators triggered
- Artifact freshness within bounds

PARTIAL
- Artifact structurally valid
- Temporal drift exceeds freshness threshold
- No exclusion or MVE failure present

NERF
- Exclusion indicator triggered
- Required field missing
- Timestamp invalid
- Any ambiguous or unsafe condition

Verdict meaning is absolute. No soft interpretation is permitted.

----------------------------------------------------------------

5. FAIL-CLOSED RULE

Any of the following conditions SHALL result in NERF:

- Missing required fields
- Exclusion indicator triggered
- Timestamp parsing failure
- Unknown custodian_class
- Unexpected input shape

The engine must prefer refusal over continuation.

----------------------------------------------------------------

6. OUTPUT CONTRACT

The engine outputs a single JSON receipt to stdout containing:

- engine_version
- timestamp_utc
- verdict
- violations (list)

No other output is permitted.

----------------------------------------------------------------

7. VERSIONING

All outputs MUST include engine_version.

Behavior changes require:
- Version increment
- Updated contract
- Updated diagnostics

Silent semantic drift is forbidden.

----------------------------------------------------------------

8. EXTENSION BOUNDARY

Additional logic may ONLY be added by:
- Introducing a new validator
- Publishing a new contract version
- Adding diagnostics proving non-regression

Inline mutation of enforcement logic without versioning is prohibited.

----------------------------------------------------------------

9. AUTHORITY

This contract is authoritative.

If code and this contract disagree:
- The contract governs
- Code MUST be updated or considered invalid

----------------------------------------------------------------

END CONTRACT
