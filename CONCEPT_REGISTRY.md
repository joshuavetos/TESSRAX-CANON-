# CONCEPT REGISTRY

GLOBAL RULES:
- If a concept is not listed here, it is NOT canonical
- PRIMARY DEFINITION outranks all other sources
- AUTHORITATIVE SOURCES outrank REFERENCES
- Filename casing and duplication do not imply authority
- This registry overrides directory structure in case of ambiguity

TYPE DEFINITIONS (MUST BE INCLUDED VERBATIM):
Canonical Concept:
A core invariant that defines system behavior. Removing it breaks the system.

Supporting Concept:
A protocol, metric, or mechanism that operationalizes canonical concepts.

Derived Concept:
A pattern identified through diagnostics or case analysis.

CHANGE CONTROL (MUST BE INCLUDED):
- New concepts require registry entry to be canonical
- Reclassification requires explicit commit justification
- Removal requires deprecation notice
- Any enforcement artifact referencing an unlisted concept MUST be treated as INVALID

## Atrophy of Truth

TYPE: Canonical Concept

PRIMARY DEFINITION:
- 01_CANON/CANON-002_Atrophy_of_Truth.md

AUTHORITATIVE SOURCES:
- 01_CANON/CANON-002_Atrophy_of_Truth.md
- 01_CANON/TESSRAX_CORE_THEORY.md

REFERENCES (non-authoritative):
- 07_THEORY/ATROPHY_OF_TRUTH.md
- TESSRAX_MASTER_NOTES.md

ALIASES (if any):
- The Atrophy of Truth

NOTES:
- Title variant appears with and without the definite article.

## Claim Economy

TYPE: Canonical Concept

PRIMARY DEFINITION:
- 01_CANON/CANON-003_Claim_Economy.md

AUTHORITATIVE SOURCES:
- 01_CANON/CANON-003_Claim_Economy.md
- 02_PROTOCOLS/CLAIM_ECONOMY_PROTOCOL.md

REFERENCES (non-authoritative):
- README.md
- 03_DIAGNOSTICS/AUDIT_RECEIPT_SPEC.md
- 02_PITCH/ACADEMIC_POSITIONING.md

ALIASES (if any):
- Claim Economy Protocol
- CEP

NOTES:
- Protocol and acronym are used as operational shorthand.

## Cold-Start Protocol

TYPE: Supporting Concept

PRIMARY DEFINITION:
- 02_PROTOCOLS/PROTO-001_Cold_Start.md

AUTHORITATIVE SOURCES:
- 02_PROTOCOLS/PROTO-001_Cold_Start.md
- 02_FRAMEWORKS/COLD_START_PROTOCOL_V0_1.md

REFERENCES (non-authoritative):
- 04_CASES/CASE-001_AI_Safety.md
- 04_CASES/CASE-002_Financial_Systems.md
- 02_PITCH/PITCH_TESSRAX.md

ALIASES (if any):
- Cold Start Protocol
- Cold-Start

NOTES:
- Multiple versioned protocol files share the same name.

## Epistemic Recovery Time

TYPE: Supporting Concept

PRIMARY DEFINITION:
- 03_DIAGNOSTICS/DIAG-001_Epistemic_Recovery_Time.md

AUTHORITATIVE SOURCES:
- 03_DIAGNOSTICS/DIAG-001_Epistemic_Recovery_Time.md
- 03_DIAGNOSTICS/ERT-01_EPISTEMIC_RECOVERY_TIME_RUBRIC.md

REFERENCES (non-authoritative):
- 03_DIAGNOSTICS/ERT_SCORECARD.md
- 04_CASES/CASE-003_Healthcare.md
- 04_CASES/CASE-002_Financial_Systems.md

ALIASES (if any):
- ERT

NOTES:
- Used as a diagnostic metric across cases.

## Fail-Closed Gating

TYPE: Canonical Concept

PRIMARY DEFINITION:
- 01_CANON/CANON.md

AUTHORITATIVE SOURCES:
- 01_CANON/CANON.md
- 02_PROTOCOLS/UNIVERSAL_CLAIMANT_SCHEMA.md

REFERENCES (non-authoritative):
- README.md
- 03_DIAGNOSTICS/UCS_Golden_Master_Tests.md
- 02_PROTOCOLS/SCANNER_DECISION_TREE.md

ALIASES (if any):
- Fail-Closed Systems

NOTES:
- Also referenced as a system-level safety posture.
- Distinct from Human Reconstructability; governs behavior on ambiguity.

## HALT Rule

TYPE: Canonical Concept

PRIMARY DEFINITION:
- 01_CANON/CANON.md

AUTHORITATIVE SOURCES:
- 01_CANON/CANON-004_Irreversibility_and_Exit_Cost_Invariant.md
- 01_CANON/CANON-006_Receipt-and-Audit-Spec.md

REFERENCES (non-authoritative):
- 02_PROTOCOLS/BUDGET_ARITHMETIC_SPEC.md
- 02_PROTOCOLS/CLAIM_ECONOMY_PROTOCOL.md
- 03_DIAGNOSTICS/UCS_Golden_Master_Tests.md
- 06_GOVERNANCE/CIVIC_STACK_V1_FORENSIC_GOVERNANCE.md

ALIASES (if any):
- HALT
- Halt Rule

NOTES:
- Enforcement appears across canon, protocols, diagnostics, and governance records.

## Human Reconstructability

TYPE: Canonical Concept

PRIMARY DEFINITION:
- 01_CANON/CANON.md

AUTHORITATIVE SOURCES:
- 01_CANON/CANON.md
- 02_PROTOCOLS/PROTO-001_Cold_Start.md

REFERENCES (non-authoritative):
- README.md
- 00_README/REPO_INTENT.md
- 04_CASES/CASE-001_AI_Safety.md

ALIASES (if any):
- Reconstructability

NOTES:
- Appears as a core invariant and as a protocol objective.

## Notice of Epistemic Fragility

TYPE: Supporting Concept

PRIMARY DEFINITION:
- 02_PROTOCOLS/PROTO-002_Notice_of_Epistemic_Fragility.md

AUTHORITATIVE SOURCES:
- 02_PROTOCOLS/PROTO-002_Notice_of_Epistemic_Fragility.md
- 06_GOVERNANCE/NEF-01_NOTICE_OF_EPISTEMIC_FRAGILITY.md

REFERENCES (non-authoritative):
- 03_DIAGNOSTICS/NEF-01_NOTICE_OF_EPISTEMIC_FRAGILITY.md
- 03_DIAGNOSTICS/ERT-01_EPISTEMIC_RECOVERY_TIME_RUBRIC.md

ALIASES (if any):
- NEF-01

NOTES:
- NEF-01 is the codified notice identifier.

## Receipt and Audit Invariant

TYPE: Canonical Concept

PRIMARY DEFINITION:
- 01_CANON/CANON-006_Receipt-and-Audit-Spec.md

AUTHORITATIVE SOURCES:
- 01_CANON/CANON-006_Receipt-and-Audit-Spec.md
- 03_DIAGNOSTICS/AUDIT_RECEIPT_SPEC.md

REFERENCES (non-authoritative):
- 02_PROTOCOLS/PROTO-001_Cold_Start.md
- 01_CANON/CANON-007_Threshold-Calibration-Methodology.md

ALIASES (if any):
- Audit Receipt
- Canonical Receipt

NOTES:
- Canonical receipts are the enforcement artifact for this invariant.

## Semantic Fraud

TYPE: Derived Concept

PRIMARY DEFINITION:
- 03_DIAGNOSTICS/SEMANTIC_FRAUD.md

AUTHORITATIVE SOURCES:
- 03_DIAGNOSTICS/SEMANTIC_FRAUD.md
- 01_CANON/TESSRAX_CORE_THEORY.md

REFERENCES (non-authoritative):
- 03_DIAGNOSTICS/ERT_SCORECARD.md
- 04_CASES/CASE-003_Healthcare.md
- 02_PITCH/PITCH_TESSRAX.md

ALIASES (if any):
- Semantic Fraud Mode

NOTES:
- Often triggered by ERT thresholds in diagnostics.

## Systemic Deadlock

TYPE: Canonical Concept

PRIMARY DEFINITION:
- 01_CANON/CANON-001_Systemic_Deadlock.md

AUTHORITATIVE SOURCES:
- 01_CANON/CANON-001_Systemic_Deadlock.md

REFERENCES (non-authoritative):
- 04_CASES/CASE-001_Systemic_Deadlock.md
- 04_CASES/CASE-001_SYSTEMIC_DEADLOCK.md
- TESSRAX_MASTER_NOTES.md

ALIASES (if any):
- Narrative Maintenance

NOTES:
- Used interchangeably with narrative maintenance in case files.

## Universal Claimant Schema

TYPE: Supporting Concept

PRIMARY DEFINITION:
- 02_PROTOCOLS/UNIVERSAL_CLAIMANT_SCHEMA.md

AUTHORITATIVE SOURCES:
- 02_PROTOCOLS/UNIVERSAL_CLAIMANT_SCHEMA.md

REFERENCES (non-authoritative):
- 03_DIAGNOSTICS/UCS_Golden_Master_Tests.md

ALIASES (if any):
- UCS

NOTES:
- Schema is validated by diagnostic golden master tests.
