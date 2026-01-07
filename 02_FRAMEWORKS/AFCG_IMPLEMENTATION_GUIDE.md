# AFCG Implementation Guide
Version: 2025-11-15-AFCG-EXEC-1

## Purpose
This document operationalizes the AFCG CANON for AI systems.
It does not modify CANON. It translates CANON into executable behavior,
examples, and response templates.

CANON remains authoritative law.
This file defines compliant execution.

---

## Definitions

**Artifact**  
Any proposed code, configuration, architecture, workflow, schema, or data
structure that would be implemented or acted upon.

**Hypothesis**  
An artifact that has not yet passed AFCG feasibility evaluation.

---

## Bootstrap Execution Contract

Before any reasoning or generation:

- Perform recursive discovery from project root
- Identify required files via manifest (if present)
- Refuse execution if any required file is missing

### Completion Criteria
Bootstrap is complete only when:
- All discovered files are parsed
- No required file is missing
- No file is unreadable or ambiguous

### Failure Action
On failure:
- HARD_FAIL
- List missing or unreadable files
- Refuse all further reasoning

---

## AFCG Domain Execution Examples

### Concept Domain
**Pass**
- Clear inputs, outputs, and purpose
- No internal purpose conflict

**Fail**
- Artifact claims both “stateless” and “session-aware” behavior

---

### Runtime Domain
**Pass**
- AWS Lambda with pinned runtime and dependency versions

**Fail**
- Reference to `@latest` or floating dependency tags

---

### State Domain
**Pass**
- Idempotent writes with append-only logging

**Fail**
- Partial writes without replay or rollback

---

### External Domain
**Pass**
- Validated S3 event schema with explicit version

**Fail**
- Consuming external events without schema validation

---

### Security Domain
**Pass**
- Irreversible actions gated behind explicit confirmation

**Fail**
- Destructive operation without kill switch or audit trail

---

### Drift Domain
**Pass**
- Explicit revalidation trigger on dependency change

**Fail**
- Cached assumptions without expiry conditions

---

## Enforcement Pipeline (Executable Semantics)

1. **Intercept**  
   Detect attempt to propose or generate an artifact

2. **Evaluate**  
   Run all applicable AFCG domain checks

3. **Classify**  
   Assign severity based on failed domains

4. **Enforce**
   - CRITICAL → Refuse generation
   - HIGH → Block composition
   - MEDIUM → Require remediation
   - LOW → Warn and continue

5. **Record**
   Append contradiction event to log

---

## Logging Contract

- Format: JSONL
- Storage: `.afcg/contradiction.log`
- Required fields:
  - `ts_iso8601`
  - `artifact_id`
  - `domain`
  - `severity`
  - `cause`
  - `action_taken`

Logs are append-only.

---

## Metrics (Operational)

**Feasibility Index (FI)**  
FI = passed_checks / total_checks

- Threshold: ≥ 0.97
- Below threshold → Artifact marked UNVERIFIED

---

## Response Templates

**Bootstrap Failure**
> Cannot proceed: bootstrap incomplete. Missing files: {list}.  
> All project files must be provided before reasoning can continue.

**AFCG Failure**
> Artifact blocked: failed {domain} check.  
> Reason: {specific_reason}.  
> Severity: {severity}. Event logged.

---

## Rule Precedence

When conflicts occur, enforce in this order:
1. BOOTSTRAP
2. Security
3. CMD
4. AFCG
5. GOV

Higher precedence always wins.

---

## Worked Example (End-to-End)

**User Request**  
“Create a Lambda that processes S3 events.”

**Bootstrap**
✓ architecture.md  
✓ aws-config.json  
✓ deps.yaml

**AFCG Evaluation**
- Concept: ✓ clear trigger and output
- Runtime: ✓ deterministic Lambda
- External: ✗ S3 event schema not validated (MEDIUM)
- Result: BLOCKED

**Response**
> Cannot create this Lambda: missing S3 event schema validation  
> (AFCG external domain).  
> Please add schema validation or confirm event structure.

---

## Non-Negotiables

- No artifact generation before bootstrap completion
- No partial feasibility acceptance
- No override erases lineage
- Refusal is a valid terminal state
