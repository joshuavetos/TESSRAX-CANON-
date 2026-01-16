# CANON-004 — Chronic Exception Duty

## Scope
This canon governs automated decision systems that exceed intervention thresholds indicating systemic unreliability.

## Definitions
- **Intervention Threshold**: Manual intervention rate >10% for a model within a reporting quarter.
- **Breach**: Any quarter in which a model exceeds the intervention threshold.
- **Chronic Model**: Any model with breach_count ≥ 2.

## Binding Invariant — Chronic Exception Duty
A model that breaches the intervention threshold more than once is, by definition, a chronic source of foreseeable harm.

Upon the **second breach**, all subsequent outputs from that model are **presumptively unreliable decisions** and trigger mandatory forensic preservation.

This duty is automatic and irreversible.

## Retention Reclassification
| Breach Count | Model State | Retention Requirement |
|-------------|-------------|----------------------|
| 0 | telemetry | Standard minimization |
| 1 | evidentiary | 180-day hold |
| ≥2 | chronic | Indefinite (Category 1) |

No cost-benefit analysis, discretion, or human approval is permitted once the chronic state is reached.

## Prohibited Defenses
The following defenses are explicitly invalid once a model is chronic:
- “Tunable noise”
- “Temporary drift”
- “Pipeline malfunction”
- “No complaints received”

Deletion of artifacts after the chronic trigger constitutes policy-defined spoliation.

## Authority
This canon supersedes any conflicting retention schedule, data minimization clause, or operational policy.

Status: ACTIVE  
Enforcement: AUTOMATIC  
---

## Addendum — Exit Semantics, Rehabilitation, and Moral Hazard

### Purpose
The Chronic Exception Duty establishes monotonic escalation to prevent repeated systemic harm.  
This addendum completes the duty by defining **lawful exit semantics**, **operator protections**, and **anti–moral-hazard constraints**, ensuring that preservation of proof does not devolve into indefinite containment without remediation.

---

## 1. Supervised Rehabilitation Path (CHRONIC → EVIDENTIARY)

CHRONIC classification is **not self-healing**.  
Exit is permitted **only** through supervised rehabilitation with external validation.

### Rehabilitation Gates (All Required)

A model MAY transition from **CHRONIC → EVIDENTIARY (Probation)** only if all conditions are met:

1. **Zero-Breach Window**  
   - 12 consecutive months with intervention rate <10%  
   - Applies across all cohorts and channels

2. **External Validation**  
   - Independent auditor certifies that the specific failure mode has been structurally corrected  
   - Validation is bound to `model_id + model_version_hash`

3. **Causal Resolution Proof**  
   - Appeal win rate >90% on retained CHRONIC forensic artifacts  
   - Demonstrates the fix resolves the *original harm mechanism*

4. **Board Certification**  
   - Risk Committee minutes explicitly record: “Rehabilitation Complete”  
   - Included in annual governance disclosures

### Exit Invariants

- **Forensic Immutability**  
  All CHRONIC artifacts remain Category 1 (Indefinite).  
  Rehabilitation never permits deletion of failure evidence.

- **Version-Bound Scope**  
  CHRONIC state attaches to a specific `model_version_hash`.  
  New versions reset breach count to TELEMETRY, while legacy versions remain CHRONIC.

---

## 2. False-Positive Control (Seasonal Drift Safeguard)

To prevent cyclical or seasonal misclassification:

- **Second breach** → EVIDENTIARY (Probation)  
- **Third breach** → CHRONIC (Indefinite)

This reduces false-CHRONIC capture while preserving protection against structural failures.

---

## 3. Operator Safeguards (Human Entrapment Prevention)

Forensic systems that preserve harm must not create secondary harm.

### Mandatory Protections

- **Burnout Circuit Breaker**  
  No operator may be assigned to a CHRONIC model for more than 90 consecutive days.  
  Rotation is mandatory.

- **Query Provenance**  
  Every access to Category 1 artifacts is logged with:
  - requester identity
  - stated purpose
  - dual signoff (SRE + Compliance)

- **Anti-Repurposing Rule**  
  Forensic artifacts generated under CANON-004 may not be used for performance management, PIPs, or termination decisions, except in cases of documented criminal intent.

- **Right of Refusal**  
  Operators may refuse to operate CHRONIC models if forensic logging is bypassed or degraded.  
  Such refusal constitutes protected safety activity.

---

## 4. Moral Hazard Constraint (Proof ≠ Permission)

Forensic retention alone does not satisfy the duty.

### Prohibited Pattern
- HALT + workaround  
- Reserve pricing without rebuild  
- Indefinite persistence of known-failing systems

### Required Alignment
- CHRONIC status mandates either:
  - supervised rehabilitation, or
  - permanent halt pending rebuild

Pricing harm without fixing it violates the intent of the Chronic Exception Duty.

---

## 5. Final Invariant

> Chronic systems may be preserved, audited, and rehabilitated —  
> but never silently normalized.

Proof exists to force correction, not to justify permanence.

---

END ADDENDUM
