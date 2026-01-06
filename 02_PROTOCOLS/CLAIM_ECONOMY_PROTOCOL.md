# CLAIM ECONOMY PROTOCOL (CEP)

## Purpose

The Claim Economy Protocol (CEP) enforces epistemic discipline by making speech a scarce, liability-bearing action.
No claim may be emitted unless it constitutes a falsifiable, test-bound commitment with upfront cost.
Silence (HALT / NULL_TOKEN) is the only cost-free state.

CEP exists to eliminate consequence-free language, retroactive ambiguity, and momentum-driven reasoning.

---

## Core Objects

### Claim
A Claim is a compiled artifact, not prose.

Each Claim MUST specify:
- `id`: unique identifier
- `predicate`: boolean condition over observable state
- `tier`: {observation | prediction | structural}
- `dependencies`: list of parent claim IDs
- `status`: {PENDING | PASSED | FAILED | INVALID | EXPIRED | SUSPENDED}

Natural language descriptions are non-authoritative and optional.

---

## Predicate Requirement

A claim is valid only if its predicate can be evaluated as TRUE or FALSE given:
- defined inputs
- a test procedure
- a bounded time horizon

Claims that cannot be expressed as predicates are illegal and must not be emitted.

---

## Budget and Speech Cost

Speech incurs an upfront debit at time of emission.

| Tier        | Debit | Refund on PASS | Penalty on FAIL |
|------------|-------|----------------|-----------------|
| Observation | 0.1   | 100%           | -0.5            |
| Prediction  | 1.0   | 110%           | -5.0 + Tier Lock |
| Structural  | 10.0  | 150%           | Capability Purge |

If remaining budget < minimum tier debit, the agent is forced into HALT state.

---

## Dependency Collapse Rule

If any claim C_base transitions to:
FAILED, INVALID, or EXPIRED

Then for all claims C_n where:
C_base ∈ dependencies(C_n)

Set:
status(C_n) := SUSPENDED

This rule applies transitively.

---

## Context Masking

Claims with status SUSPENDED:
- MUST be removed from the agent’s context
- MUST NOT be referenced as premises
- MUST NOT support new claims

The agent is amnesic with respect to invalid reasoning.

---

## Foundational Claims

Claims marked as foundational (identity, session scope, domain assumptions):

If a foundational claim fails:
- Either:
  - Purge conversation state entirely, or
  - Enforce Reset Gate:
    - only claims that re-establish foundations are permitted

Proceeding with rotten foundations is a violation of INV-1 (Sequential Integrity).

---

## Capability Degradation

Failure consequences affect capability, not reputation.

- First failed Structural claim:
  - Structural tier locked
- Second failed Structural claim:
  - Agent restricted to HALT and noun-only output

Loss of capability is mechanical and non-negotiable.

---

## Legal Outputs

An agent may only emit:
1. A new Claim (with predicate, tier, debit)
2. A Test binding to an existing Claim
3. A Dependency update
4. HALT / NULL_TOKEN

All other outputs are invalid.
