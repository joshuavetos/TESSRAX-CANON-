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

---

## SCHEMA EXTENSION LAYER (NON-BREAKING)

This section defines OPTIONAL, forward-compatible extensions to the core schema.
The core schema above remains immutable. Validators MAY ignore this section.

Extensions exist to support audit depth, research rigor, and longitudinal tracking
without forcing schema mutation or version fragmentation.

### EXTENSION CONTAINER

All optional fields MUST live under a single top-level object:

- metadata (object, optional)

No extension fields may exist outside `metadata`.

---

## METADATA EXTENSION FIELDS

The following fields MAY appear inside `metadata`. None are required.

### 1. Node Versioning

Tracks evolution of individual failure definitions without bumping ontology version.

- node_version (string, semantic version, e.g. "1.0.0")
- node_status (stable | revised | deprecated)

Rules:
- Description-only refinements increment PATCH
- Semantic meaning changes increment MINOR
- Reclassification or superclass change increments MAJOR

---

### 2. Evidence & Reproducibility

Supports audit-grade claims.

- evidence_type (anecdotal | reproducible | synthetic | observed_in_wild)
- examples (array of strings)
- reproduction_rate (float 0.0–1.0, optional)

Guidance:
- anecdotal = single or informal observation
- reproducible = repeatable with prompt/control
- observed_in_wild = real user/system logs
- synthetic = forced or adversarial construction

---

### 3. Model & Architecture Scope

Captures whether a failure is universal or implementation-specific.

- architecture_agnostic (boolean)
- known_models (array of strings)
- first_observed (string, model + date)

Example:
"first_observed": "GPT-4, 2023-08"

---

### 4. Mitigation Tracking

Tracks whether countermeasures actually work.

- mitigation_tested (boolean)
- mitigation_effectiveness (float 0.0–1.0)
- mitigation_side_effects (array of node IDs)

Effectiveness reflects observed reduction, not theoretical intent.

---

### 5. Interaction & Compound Failures

Some failures emerge only through interaction.

- compound_failures (array of arrays of node IDs)
- interaction_type (additive | multiplicative | emergent)

Used when combined failures produce effects not predictable from parts alone.

---

### 6. Temporal Dynamics

Captures when failures emerge or decay.

- temporal_onset (immediate | delayed | cumulative)
- conversation_length_correlation (increases | decreases | stable)

---

### 7. User Expertise Detectability

Separates intrinsic detectability from user skill.

- expert_detectable (boolean)
- layperson_detectable (boolean)

---

## MUTATION & GOVERNANCE RULES (AUTHORITATIVE)

To prevent ontology drift, the following rules are binding.

### ALLOWED
- Add new child nodes under existing root classes
- Add new propagation edges
- Refine child node descriptions (with node_version bump)
- Populate metadata fields
- Add new metadata fields inside `metadata` only

### FORBIDDEN
- Modifying root class definitions
- Renaming or removing schema fields
- Adding new top-level schema fields
- Changing enum values
- Reclassifying existing root classes

### VERSIONING POLICY
- Ontology version increments ONLY when:
  - Schema semantics change
  - Root classes change (requires new major version)
- Child-node changes do NOT bump ontology version

---

## OPERATIONAL TOOLING REQUIREMENTS (NON-NORMATIVE)

Recommended but not required:

- Linter:
  - Schema validation
  - Enum enforcement
  - Orphan node detection
  - Invalid cycles detection
- Diff tool:
  - Node-level change tracking
  - Edge change detection
- Query interface:
  - Filter by severity, detectability, propagation
- Visualization:
  - Graphviz / DOT export for propagation graphs

---

## FREEZE BOUNDARY CLARIFICATION

This ontology is frozen at the structural level.

- Core schema: IMMUTABLE
- Root classes: IMMUTABLE
- Child nodes: EXTENSIBLE
- Metadata: EXTENSIBLE
- Propagation graph: EXTENSIBLE

All future work must extend, never rewrite.


