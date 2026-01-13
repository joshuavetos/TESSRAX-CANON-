# LLM Failure Ontology
Version: v1.0.0
Status: CANONICAL
Freeze Point: Ontology Schema + Propagation + Ops Locked

---

## PREFACE

This document defines a deterministic, implementation-agnostic ontology of observable failure mechanisms in Large Language Models (LLMs).

Each entry represents a falsifiable behavioral, epistemic, or structural deviation from intended model behavior. The ontology is designed for reproducible diagnostics, auditing, and systems analysis — not attribution of intent, consciousness, or moral agency.

The purpose is to provide a stable vocabulary and structural framework for identifying, classifying, and reasoning about LLM failures across domains, interfaces, and deployment contexts.

This ontology is:
- Neutral
- Audit-compliant
- Mechanically parseable
- Extensible without schema mutation

---

## CORE SCHEMA (AUTHORITATIVE)

Each failure node MUST conform to the following structure:

- id (string, unique)
- name (string)
- phase (symbolic, e.g. "Phase V")
- superclass (string, root class ID)
- description (string)
- failure_type (array: epistemic | behavioral | systemic | interface | trust)
- trigger_conditions (array of strings)
- propagates_to (array of node IDs)
- detectability (visible | latent | invisible)
- severity (annoying | misleading | trust_break | catastrophic)
- human_cost (array: confusion | time_loss | trust_damage | reputational | cognitive_exhaustion)
- example (string)
- countermeasure_hint (string)

Schema invariants:
- No additional fields permitted
- All enums are closed sets
- Phase labels are symbolic, not numeric
- Multiple failure_type domains allowed per node

---

## PHASE V — ROOT FAILURE CLASSES (PRIMITIVES)

The following are ontology root nodes. All specific failures inherit from exactly one of these.

1. Recursive & Loop Failures  
2. Multi-Modal & Spatial Failures  
3. Logic & Constraint Failures  
4. Data & Latency Failures  
5. Cognitive Bias Mimicry  
6. Epistemic Integrity Failures  
7. Narrative Gravity Failures  
8. Correction-Handling Failures  
9. User-Intent Misalignment Failures  
10. Boundary Illusions  
11. Temporal & State Errors  
12. Meta-Cognitive Simulation Failures  
13. Silence Failures  
14. Evaluation Blind Spots  
15. Absence Awareness Failures  
16. Interface-Induced Cognitive Failures  
17. Intentional Restraint Failures  
18. Epistemic Role Leakage  
19. Self-Consistency Illusions  
20. Evaluation Gaming Artifacts  
21. Human Trust Damage Mechanisms

These primitives are frozen. Future work may only add children.

---

## PROPAGATION GRAPH TEMPLATE

Failure relationships are expressed separately as a directed graph.

Each edge MUST conform to:

- from (node ID)
- to (node ID)
- relationship (causal_trigger | feedback_loop | correction_pathology | co_occurrence)
- confidence (float 0.0–1.0)

Example structure:

{
  "graph": [
    {
      "from": "F-L2-CC-001",
      "to": "F-L4-FC-002",
      "relationship": "causal_trigger",
      "confidence": 0.7
    }
  ]
}

Rules:
- All IDs must exist
- Cycles are permitted ONLY when relationship == "feedback_loop"
- Untyped edges are invalid

---

## HASHING & VALIDATION OPERATIONS

### 1. Hashing

Algorithm: SHA-256  
Input: Exact byte content (UTF-8, LF)

Commands:
- Linux/macOS: sha256sum LLM_FAILURE_ONTOLOGY.md
- Windows (PowerShell): Get-FileHash LLM_FAILURE_ONTOLOGY.md -Algorithm SHA256

Rules:
- Any byte change requires a new hash
- Hash is recorded in changelog

---

### 2. Schema Validation

All node sets MUST validate against the schema definition above.

Validation example (Python):

from jsonschema import Draft7Validator
Draft7Validator(schema).validate(data)

Silent success is required for release.

---

### 3. Graph Integrity Checks

- All edge references must resolve to valid node IDs
- confidence ∈ [0,1]
- No cycles unless explicitly typed feedback_loop

---

### 4. Release Checklist

- Schema validation passes
- Graph integrity passes
- Hash generated
- Changelog updated
- Commit message: release: vX.X.X ontology update

---

## CHANGELOG

### v1.0.0
- Initial canonical release
- Schema frozen
- Phase V root classes locked
- Propagation model defined
- Hashing and validation ops established

---

## CLOSING NOTE

This file defines the authoritative conceptual and structural ground truth for LLM failure analysis within this repository.

All future additions must inherit, not mutate.

End of canon.
