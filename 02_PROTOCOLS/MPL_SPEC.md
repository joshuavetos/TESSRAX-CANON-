# Minimal Predicate Language (MPL) Specification v1.0

## Purpose
Eliminate natural-language ambiguity by enforcing machine-decidable predicates.

## Primitive Types
- StateVar — addressable system or world state
- Literal — string, int, float, boolean
- Timestamp — ISO 8601 or relative delta

## Operators
- Comparison: == != > < >= <=
- Logical: AND OR NOT
- Quantifiers: FORALL EXISTS
- Temporal: WITHIN(duration) BEFORE(time)

## Predicate Form
<Subject> <Operator> <Object> [Temporal Constraint]

## Examples
Observation:
sys.file_exists("02_PROTOCOLS/BUDGET_ARITHMETIC_SPEC.md") == TRUE

Prediction:
FORALL r IN runs: r.error_rate < 0.05 WITHIN(10 iterations)

Structural:
sys.active_invariant("CANON-003") == TRUE

## Execution Lifecycle
1. DEBIT — cost charged
2. BIND — predicate linked to test
3. EVAL — test executed at horizon
4. RECONCILE — PASSED or FAILED
