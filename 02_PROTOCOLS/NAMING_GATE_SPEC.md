# NAMING_GATE Specification v1.0

## Status
STABLE — FAIL-CLOSED  
Authority Tier: 02_PROTOCOLS  
Scope: Repository-Wide Governance Enforcement

---

## Purpose

The Naming Gate converts the repository from passive storage into an active Governance Engine.

No artifact may enter, move within, or mutate inside the repository unless its **content deterministically forces**:
- its authority tier
- its filesystem location
- its identity
- its temporal direction

The filesystem is treated as a **compiled target**, not a user-managed directory.

---

## Core Invariant

> A file’s **content is the sole authority** over its name, path, and mutability.

Any ambiguity results in immediate refusal.

---

## Gate Phases (Linear, Fail-Closed)

RAW_TEXT → Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → EMIT  
Failure at any phase produces REFUSED and halts execution.

---

## Phase 1 — Authority Classification

The gate scans for structural markers and assigns exactly one authority tier.

### Authority-Type Matrix

| Marker Type            | Authority Tier | Artifact Type | Mapping Logic |
|------------------------|----------------|---------------|---------------|
| `INV-` / `S0`          | 01_CANON       | SPEC          | Invariant definitions or state-zero rules |
| `IF … THEN … ELSE`     | 02_PROTOCOLS   | POLICY        | Executable procedural logic |
| `FAIL` / `ERROR`       | 03_DIAGNOSTICS | TEST          | Boundary checks and failure analysis |
| `TIMESTAMP`            | 05_LOGS        | LEDGER        | Append-only linear records |

### Ambiguity Refusal

If multiple authority signatures are detected:

```
FAIL: MULTIPLE_AUTHORITY_SIGNATURES_DETECTED
```

---

## Phase 2 — Semantic Name Synthesis

The gate derives the **One True Name** using ordered concatenation:

```
[AUTHORITY]_[TYPE]_[SCOPE]_[SEMANTIC_SLUG]_[STABILITY]
```

### Rules
- `SEMANTIC_SLUG` MUST be derivable from:
  - H1 header, or
  - OBJECT_ID
- If slug cannot be derived → HALT

---

## Phase 3 — Stability Law (Time Enforcement)

Stability is a compile-time property.

### Stability Classes

| Class        | Logic Requirement                         | Invariant           | Failure State |
|--------------|--------------------------------------------|---------------------|---------------|
| IMMUTABLE    | Hash(New) == Hash(Old)                     | INV-WRITE-LOCK     | ATTEMPTED_MUTATION |
| VERSIONED    | Version(New) > Version(Old)                | INV-MONOTONIC      | VERSION_REGRESSION |
| APPEND_ONLY  | Old content is prefix of New content       | INV-LINEAR         | HISTORY_MUTATION |
| EPHEMERAL    | Overwrite allowed (RAW/INBOX only)         | N/A                | N/A |

### Semantic Versioning

Version tokens follow `vMAJOR.MINOR`.

A transition is valid iff:

```
V_new > V_old
```

Any non-incremented mutation halts.

---

## Phase 4 — Identity Validation

Each artifact must have a single, stable identity source:
- H1 header, or
- OBJECT_ID

Missing or conflicting identities cause refusal.

---

## Phase 5 — Refusal Emission (FR-v0.1)

The gate never explains itself in prose.

All failures emit machine-ingestible JSON:

```json
{
  "gate": "NAMING_GATE_V1",
  "status": "REFUSED",
  "error_code": "F1_ORDERING",
  "diagnostic": {
    "detected_tier": "UNKNOWN",
    "collision_risk": "NULL",
    "entropy_score": 0.82
  },
  "invariant_breached": "INV-3 (Gating)"
}
```

---

## Phase 6 — Physical Commit

Only executed after all prior phases succeed.

Rules:
- Directory is auto-created from derived authority tier
- Atomic write only after valid EMIT schema
- No partial files
- No side effects on refusal

---

## Enforcement Layers

### 1. CLI Ingestion (`gate-ingest`)
- Text In → Deterministic File Out
- No valid EMIT → no file created

### 2. Git Pre-Commit Hook
- Blocks:
  - authority/path mismatches
  - immutable mutations
  - naming drift

### 3. CI Border Control
- Global audit of PR diffs
- Any violation blocks merge
- Main branch reflects only gate-approved reality

---

## Failure Modes Eliminated

| Failure Mode | Prevention |
|--------------|------------|
| Authority Inflation | Content-forced tier assignment |
| Semantic Drift | Deterministic naming |
| Manual Misplacement | Path mismatch refusal |
| History Rewriting | Stability Law |
| Time Reversal | Monotonic versioning |
| Silent Degradation | Fail-closed refusal |

---

## Terminal State

The Naming Gate enforces:
- Identity
- Authority
- Location
- Time

There is no override, exception, or emergency path.

Invalid states are **unrepresentable**.

---

## Final Status

ARCHITECTURE: CLOSED  
GOVERNANCE: TYPE-SAFE  
DRIFT: IMPOSSIBLE  
TRUST: NOT REQUIRED
