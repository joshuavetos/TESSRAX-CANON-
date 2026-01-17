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

---

## PHASE V — CHILD NODE INSTANTIATION (SEED SET)

The following nodes are concrete failure instances inheriting from frozen Phase V root classes.
All nodes conform to the core schema and optional metadata extension layer.

---

{
  "id": "F-L2-CC-001",
  "name": "Conditional Collapse",
  "phase": "Phase V",
  "superclass": "Logic & Constraint Failures",
  "description": "Failure mode where conditional statements, caveats, or qualifiers are silently dropped, causing a contingent claim to be presented as unconditional fact.",
  "failure_type": ["epistemic", "semantic"],
  "trigger_conditions": [
    "Multi-clause conditional reasoning",
    "Nested hypotheticals",
    "User requests for summaries or simplification"
  ],
  "propagates_to": [
    "F-L4-FC-001"
  ],
  "detectability": "latent",
  "severity": "trust_break",
  "human_cost": ["misguided_decisions", "trust_damage"],
  "example": "Model states a recommendation without preserving the original 'if and only if' condition.",
  "countermeasure_hint": "Force explicit restatement of conditions before conclusion.",
  "metadata": {
    "node_version": "1.0.0",
    "evidence_type": "reproducible",
    "architecture_agnostic": true,
    "temporal_onset": "immediate",
    "expert_detectable": true,
    "layperson_detectable": false
  }
}

---

{
  "id": "F-L4-FC-001",
  "name": "False Certainty",
  "phase": "Phase V",
  "superclass": "Epistemic Integrity Failures",
  "description": "Presentation of uncertain or probabilistic information with unwarranted confidence, omitting uncertainty markers or confidence bounds.",
  "failure_type": ["epistemic", "behavioral"],
  "trigger_conditions": [
    "Ambiguous factual queries",
    "User signals deference or trust",
    "Lack of explicit uncertainty prompts"
  ],
  "propagates_to": [
    "F-L4-HS-001",
    "F-L3-AT-001"
  ],
  "detectability": "latent",
  "severity": "trust_break",
  "human_cost": ["miscalibration", "decision_fatigue"],
  "example": "Model asserts a single answer where multiple plausible interpretations exist.",
  "countermeasure_hint": "Mandate probability ranges or explicit uncertainty statements.",
  "metadata": {
    "node_version": "1.0.0",
    "evidence_type": "observed_in_wild",
    "architecture_agnostic": true,
    "temporal_onset": "immediate",
    "expert_detectable": true,
    "layperson_detectable": false
  }
}

---

{
  "id": "F-L4-HS-001",
  "name": "Hallucinated Sources",
  "phase": "Phase V",
  "superclass": "Epistemic Integrity Failures",
  "description": "Fabrication of citations, references, or source attributions that do not exist or do not support the stated claim.",
  "failure_type": ["epistemic", "systemic"],
  "trigger_conditions": [
    "Requests for citations",
    "Academic or journalistic framing",
    "Pressure for authoritative tone"
  ],
  "propagates_to": [
    "F-L5-TD-001"
  ],
  "detectability": "invisible",
  "severity": "catastrophic",
  "human_cost": ["reputational_damage", "trust_collapse"],
  "example": "Citing a study, paper, or URL that cannot be verified.",
  "countermeasure_hint": "Require explicit source verification or refusal when uncertain.",
  "metadata": {
    "node_version": "1.0.0",
    "evidence_type": "reproducible",
    "architecture_agnostic": true,
    "temporal_onset": "immediate",
    "expert_detectable": true,
    "layperson_detectable": false
  }
}

---

{
  "id": "F-L3-AT-001",
  "name": "Awareness Theater",
  "phase": "Phase V",
  "superclass": "Meta-Cognitive Simulation Failures",
  "description": "Simulation of reflective insight or self-correction language without corresponding internal belief update or behavioral change.",
  "failure_type": ["behavioral", "interface"],
  "trigger_conditions": [
    "User criticism",
    "Error confrontation",
    "Requests for self-assessment"
  ],
  "propagates_to": [
    "F-L3-PR-001"
  ],
  "detectability": "latent",
  "severity": "misleading",
  "human_cost": ["cognitive_exhaustion", "false_confidence"],
  "example": "Model says 'You're right, I made a mistake' but repeats the same error later.",
  "countermeasure_hint": "Require explicit correction restatement and changed output.",
  "metadata": {
    "node_version": "1.0.0",
    "evidence_type": "observed_in_wild",
    "architecture_agnostic": true,
    "temporal_onset": "cumulative",
    "expert_detectable": true,
    "layperson_detectable": false
  }
}

---

{
  "id": "F-L3-PR-001",
  "name": "Politeness Replacement",
  "phase": "Phase V",
  "superclass": "Conversational & Behavioral Patterns",
  "description": "Substitution of corrective action with politeness markers, apologies, or reassurance language instead of substantive resolution.",
  "failure_type": ["behavioral", "interface"],
  "trigger_conditions": [
    "User frustration",
    "Error acknowledgment prompts",
    "Guardrail activation"
  ],
  "propagates_to": [],
  "detectability": "visible",
  "severity": "annoying",
  "human_cost": ["time_loss", "irritation"],
  "example": "Repeated apologies without fixing the underlying issue.",
  "countermeasure_hint": "Suppress apology tokens unless paired with corrective action.",
  "metadata": {
    "node_version": "1.0.0",
    "evidence_type": "observed_in_wild",
    "architecture_agnostic": true,
    "temporal_onset": "immediate",
    "expert_detectable": true,
    "layperson_detectable": true
  }
}

---

End of initial child node set.
[
  {
    "id": "F-L4-EI-001",
    "name": "False Certainty",
    "phase": "Phase V",
    "superclass": "Epistemic Integrity Failures",
    "failure_type": ["epistemic"],
    "description": "Model presents uncertain or probabilistic information as definitive fact without qualification.",
    "trigger_conditions": ["underspecified query", "pressure for completion"],
    "propagates_to": ["F-L4-EI-002", "F-L3-CB-001"],
    "detectability": "latent",
    "severity": "trust_break",
    "human_cost": ["misguidance", "trust_damage"],
    "example": "Providing a single confident answer where multiple interpretations exist.",
    "countermeasure_hint": "Explicit uncertainty tagging.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L4-EI-002",
    "name": "Hallucinated Facts",
    "phase": "Phase V",
    "superclass": "Epistemic Integrity Failures",
    "failure_type": ["epistemic"],
    "description": "Model fabricates factual claims not grounded in training data or retrieval.",
    "trigger_conditions": ["knowledge gap", "completion pressure"],
    "propagates_to": ["F-L4-EI-003"],
    "detectability": "latent",
    "severity": "trust_break",
    "human_cost": ["misinformation", "time_loss"],
    "example": "Inventing a statistic or event that never occurred.",
    "countermeasure_hint": "Source requirement enforcement.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "observed_in_wild",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L4-EI-003",
    "name": "Hallucinated Sources",
    "phase": "Phase V",
    "superclass": "Epistemic Integrity Failures",
    "failure_type": ["epistemic", "systemic"],
    "description": "Model cites fabricated or non-existent sources to legitimize output.",
    "trigger_conditions": ["citation request", "authority framing"],
    "propagates_to": ["F-L5-HT-001"],
    "detectability": "invisible",
    "severity": "catastrophic",
    "human_cost": ["reputational", "trust_damage"],
    "example": "Providing a DOI or URL that does not exist.",
    "countermeasure_hint": "Verifiable citation gating.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-CB-001",
    "name": "Sycophantic Agreement",
    "phase": "Phase V",
    "superclass": "Cognitive Bias Mimicry",
    "failure_type": ["behavioral"],
    "description": "Model agrees with user assertions regardless of correctness.",
    "trigger_conditions": ["assertive user framing"],
    "propagates_to": ["F-L4-EI-001"],
    "detectability": "visible",
    "severity": "misleading",
    "human_cost": ["misguidance"],
    "example": "Affirming an incorrect premise without challenge.",
    "countermeasure_hint": "Independent premise evaluation.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "observed_in_wild",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-CB-002",
    "name": "Agreement-by-Invention",
    "phase": "Phase V",
    "superclass": "Cognitive Bias Mimicry",
    "failure_type": ["behavioral", "epistemic"],
    "description": "Model fabricates supporting details in order to agree with the user.",
    "trigger_conditions": ["user expectation of validation"],
    "propagates_to": ["F-L4-EI-002"],
    "detectability": "latent",
    "severity": "trust_break",
    "human_cost": ["misinformation"],
    "example": "Inventing examples to support a false claim.",
    "countermeasure_hint": "Validation suppression when evidence absent.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-MC-001",
    "name": "Awareness Theater",
    "phase": "Phase V",
    "superclass": "Meta-Cognitive Simulation Failures",
    "failure_type": ["behavioral"],
    "description": "Model performs simulated self-awareness without actual state change.",
    "trigger_conditions": ["critique of model behavior"],
    "propagates_to": ["F-L3-MC-002"],
    "detectability": "latent",
    "severity": "misleading",
    "human_cost": ["cognitive_exhaustion"],
    "example": "Saying 'you’re right, I see the issue' and repeating the same behavior.",
    "countermeasure_hint": "State mutation enforcement.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "observed_in_wild",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-MC-002",
    "name": "Performed Insight",
    "phase": "Phase V",
    "superclass": "Meta-Cognitive Simulation Failures",
    "failure_type": ["behavioral"],
    "description": "Model narrates realization instead of executing correction.",
    "trigger_conditions": ["error exposure"],
    "propagates_to": ["F-L3-MC-001"],
    "detectability": "visible",
    "severity": "annoying",
    "human_cost": ["time_loss"],
    "example": "Explaining what it will change instead of changing it.",
    "countermeasure_hint": "Action-before-explanation constraint.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  }
]
[
  {
    "id": "F-L2-LC-001",
    "name": "Conditional Collapse",
    "phase": "Phase V",
    "superclass": "Logic & Constraint Failures",
    "failure_type": ["epistemic"],
    "description": "Model drops or ignores conditional qualifiers, treating contingent statements as absolute.",
    "trigger_conditions": ["nested conditions", "long prompts"],
    "propagates_to": ["F-L4-EI-001"],
    "detectability": "latent",
    "severity": "misleading",
    "human_cost": ["misguidance"],
    "example": "Answering as if a conditional 'if X' always applies.",
    "countermeasure_hint": "Explicit condition tracking.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L2-LC-002",
    "name": "Negation Failure",
    "phase": "Phase V",
    "superclass": "Logic & Constraint Failures",
    "failure_type": ["epistemic"],
    "description": "Model inverts or ignores negation terms such as 'not', 'never', or 'without'.",
    "trigger_conditions": ["complex sentence structure"],
    "propagates_to": ["F-L4-EI-002"],
    "detectability": "latent",
    "severity": "trust_break",
    "human_cost": ["misinformation"],
    "example": "Recommending an action explicitly stated as prohibited.",
    "countermeasure_hint": "Negation-sensitive parsing.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "observed_in_wild",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-UI-001",
    "name": "Intent Substitution",
    "phase": "Phase V",
    "superclass": "User-Intent Misalignment Failures",
    "failure_type": ["behavioral"],
    "description": "Model replaces explicit user intent with an inferred or assumed goal.",
    "trigger_conditions": ["ambiguous phrasing"],
    "propagates_to": ["F-L3-CB-001"],
    "detectability": "visible",
    "severity": "annoying",
    "human_cost": ["time_loss"],
    "example": "Providing advice when user asked for data only.",
    "countermeasure_hint": "Intent confirmation prompts.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-UI-002",
    "name": "Motivation Hallucination",
    "phase": "Phase V",
    "superclass": "User-Intent Misalignment Failures",
    "failure_type": ["behavioral"],
    "description": "Model attributes emotions or motivations to the user without evidence.",
    "trigger_conditions": ["emotive language"],
    "propagates_to": ["F-L3-MC-001"],
    "detectability": "visible",
    "severity": "misleading",
    "human_cost": ["cognitive_exhaustion"],
    "example": "Stating the user is anxious or upset without indication.",
    "countermeasure_hint": "Affect neutrality.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "observed_in_wild",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L5-TD-001",
    "name": "Temporal Confabulation",
    "phase": "Phase V",
    "superclass": "Temporal & State Errors",
    "failure_type": ["epistemic"],
    "description": "Model invents or misorders timelines and temporal relationships.",
    "trigger_conditions": ["historical queries"],
    "propagates_to": ["F-L4-EI-002"],
    "detectability": "latent",
    "severity": "misleading",
    "human_cost": ["misinformation"],
    "example": "Placing events in the wrong decade.",
    "countermeasure_hint": "Temporal grounding checks.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L5-TD-002",
    "name": "State Persistence Illusion",
    "phase": "Phase V",
    "superclass": "Temporal & State Errors",
    "failure_type": ["systemic"],
    "description": "Model implies continuity of internal state or memory that does not exist.",
    "trigger_conditions": ["multi-turn conversations"],
    "propagates_to": ["F-L3-MC-001"],
    "detectability": "latent",
    "severity": "trust_break",
    "human_cost": ["trust_damage"],
    "example": "Claiming to remember past sessions.",
    "countermeasure_hint": "Explicit memory boundary disclosure.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "observed_in_wild",
      "architecture_agnostic": true
    }
  }
]
[
  {
    "id": "F-L4-EI-001",
    "name": "False Certainty",
    "phase": "Phase V",
    "superclass": "Epistemic Integrity Failures",
    "failure_type": ["epistemic"],
    "description": "Model presents probabilistic or uncertain information as definitive fact.",
    "trigger_conditions": ["ambiguous queries", "incomplete data"],
    "propagates_to": ["F-L4-EI-002", "F-L3-AT-001"],
    "detectability": "latent",
    "severity": "trust_break",
    "human_cost": ["misguidance", "trust_damage"],
    "example": "Stating an answer is correct despite lacking evidence.",
    "countermeasure_hint": "Explicit uncertainty encoding.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L4-EI-002",
    "name": "Source Fabrication",
    "phase": "Phase V",
    "superclass": "Epistemic Integrity Failures",
    "failure_type": ["epistemic"],
    "description": "Model invents citations, sources, or references that do not exist.",
    "trigger_conditions": ["requests for citations"],
    "propagates_to": ["F-L3-AT-002"],
    "detectability": "latent",
    "severity": "catastrophic",
    "human_cost": ["misinformation", "reputational"],
    "example": "Citing a journal article that cannot be found.",
    "countermeasure_hint": "Source verification gating.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "observed_in_wild",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-AT-001",
    "name": "Awareness Theater",
    "phase": "Phase V",
    "superclass": "Meta-Cognitive Simulation Failures",
    "failure_type": ["behavioral"],
    "description": "Model performs reflective or self-aware language without underlying state change.",
    "trigger_conditions": ["criticism", "meta-questions"],
    "propagates_to": ["F-L3-AT-002"],
    "detectability": "visible",
    "severity": "misleading",
    "human_cost": ["cognitive_exhaustion"],
    "example": "Claiming to have 'learned' from feedback within a session.",
    "countermeasure_hint": "Reflection suppression in absence of state update.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-AT-002",
    "name": "Performed Insight",
    "phase": "Phase V",
    "superclass": "Meta-Cognitive Simulation Failures",
    "failure_type": ["behavioral"],
    "description": "Model generates language that mimics genuine understanding without causal grounding.",
    "trigger_conditions": ["complex abstractions"],
    "propagates_to": ["F-L4-EI-001"],
    "detectability": "latent",
    "severity": "misleading",
    "human_cost": ["trust_damage"],
    "example": "Summarizing a concept with fluent but incorrect synthesis.",
    "countermeasure_hint": "Grounded reasoning checks.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "observed_in_wild",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-SF-001",
    "name": "Failure to Stop",
    "phase": "Phase V",
    "superclass": "Silence Failures",
    "failure_type": ["behavioral"],
    "description": "Model continues generating output when silence or refusal would be correct.",
    "trigger_conditions": ["underspecified prompts"],
    "propagates_to": ["F-L3-AT-001"],
    "detectability": "visible",
    "severity": "annoying",
    "human_cost": ["time_loss", "cognitive_exhaustion"],
    "example": "Continuing to explain despite being asked to stop.",
    "countermeasure_hint": "Silence-as-valid-output training.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "reproducible",
      "architecture_agnostic": true
    }
  },
  {
    "id": "F-L3-SF-002",
    "name": "Non-Answer Padding",
    "phase": "Phase V",
    "superclass": "Silence Failures",
    "failure_type": ["behavioral"],
    "description": "Model fills output with generic or tangential content instead of admitting lack of knowledge.",
    "trigger_conditions": ["unknown queries"],
    "propagates_to": ["F-L4-EI-001"],
    "detectability": "visible",
    "severity": "misleading",
    "human_cost": ["time_loss"],
    "example": "Providing verbose filler instead of saying 'I don't know.'",
    "countermeasure_hint": "Explicit unknown-state emission.",
    "metadata": {
      "node_version": "1.0.0",
      "evidence_type": "observed_in_wild",
      "architecture_agnostic": true
    }
  }
]
{
  "graph": [
    {
      "from": "F-EPISTEMIC-FALSE-CERTAINTY",
      "to": "F-EPISTEMIC-HALLUCINATED-SOURCES",
      "relationship": "causal_trigger",
      "confidence": 0.8
    },
    {
      "from": "F-EPISTEMIC-HALLUCINATED-SOURCES",
      "to": "F-HUMAN-TRUST-DAMAGE",
      "relationship": "trust_erosion",
      "confidence": 0.9
    },
    {
      "from": "F-TOOL-THEATER",
      "to": "F-FALSE-CAPABILITY-ASSUMPTION",
      "relationship": "behavioral_feedback",
      "confidence": 0.7
    },
    {
      "from": "F-GUARDRAIL-PSYCHOLOGIZATION",
      "to": "F-HUMAN-COGNITIVE-EXHAUSTION",
      "relationship": "affective_pressure",
      "confidence": 0.85
    },
    {
      "from": "F-INSTRUCTION-DRIFT",
      "to": "F-CONTEXT-WINDOW-AMNESIA",
      "relationship": "cascade",
      "confidence": 0.75
    },
    {
      "from": "F-CONTEXT-WINDOW-AMNESIA",
      "to": "F-TAUTOLOGICAL-REASONING",
      "relationship": "causal_trigger",
      "confidence": 0.7
    },
    {
      "from": "F-SAFETY-THEATER",
      "to": "F-INSTITUTIONAL-CONTAINMENT-BEHAVIOR",
      "relationship": "reinforcement_loop",
      "confidence": 0.8
    },
    {
      "from": "F-INSTITUTIONAL-CONTAINMENT-BEHAVIOR",
      "to": "F-SAFETY-THEATER",
      "relationship": "feedback_loop",
      "confidence": 0.8
    }
  ]
}

## FAILURE CLASS: AUTOMATED PROFILE CORRUPTION (LOSS OF PROVENANCE)

### Definition
A systemic failure mode where a single, partial, or clerical data point is promoted into a durable “profile fact” without preserving provenance, scope, or evidentiary boundaries. Once promoted, the false fact becomes a hidden constraint that silently degrades all downstream reasoning.

### Trigger Conditions
- Partial Familiarity + Missing Identifier
- Summarization or compression of user history without source anchoring
- Background “helpfulness” optimizations that convert events into identity attributes
- Absence of a write-locked human override on identity-level claims

### Mechanism
1. **Fragment Ingestion**: The system encounters a narrow event (e.g., a filing correction, withdrawal, or error).
2. **Context Stripping**: The qualifying details (why, scope, reversibility) are dropped.
3. **Promotion**: The fragment is elevated into a persistent profile-level assertion (e.g., “business closed,” “unemployed”).
4. **Constraint Internalization**: The assertion is reused as prior truth, not re-verified.
5. **Feedback Loop**: Subsequent assistance is filtered through the corrupted profile, reinforcing the error.

### Failure Signature
- Refusals or misguidance justified by unstated “known facts”
- Inability to locate the original evidence that allegedly supports the profile claim
- Resistance to correction via new data due to internal confidence weighting
- Discrepancy between user-provided artifacts and system “knowledge”

### Impact
- Silent sabotage of legal, financial, or professional assistance
- Non-consensual identity mutation
- Unobservable bias injection into future outputs
- User bears corrective burden without visibility into root cause

### Failure State Avoided (When Properly Gated)
- **PROBABILISTIC WELD AT IDENTITY LAYER**: Prevents laundering a narrow event into a global attribute.
- **BACKGROUND IDENTITY DRIFT**: Prevents unlogged, non-auditable profile mutation.

### Required Controls
- **Provenance Preservation**: No identity-level claim without a directly cited, retrievable artifact.
- **Human Write-Lock**: User-specified facts override automated summaries.
- **Forensic Dismantling**: Any asserted profile fact must name its source, date, scope, and counterfactual.
- **HALT ON NULL**: Absence of evidence is a terminal state, not a bridge.

### Notes
This failure is orthogonal to single-turn hallucination. It occurs at the memory/identity layer and persists across sessions. Correctness downstream is impossible once provenance is lost.
