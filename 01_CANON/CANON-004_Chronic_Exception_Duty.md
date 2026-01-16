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
