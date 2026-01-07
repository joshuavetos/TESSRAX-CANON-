CANON-007 — THRESHOLD CALIBRATION METHODOLOGY

Status
ACTIVE — Canonical Calibration Law

Purpose
Define how enforcement thresholds are derived, validated, updated, and frozen without circular logic, narrative justification, or emitter discretion.

Thresholds are not opinions.
Thresholds are empirically derived discriminators between survival and failure.

Any threshold lacking a calibration proof is INVALID.

Core Principle
No threshold may be introduced, modified, or applied unless it demonstrably separates historical success from historical failure under blind conditions.

Calibration is a governance action and therefore subject to receipt emission.

Universal Baseline

The Tessrax system defines a universal baseline set:

Φ_universal = 1.8
L_max_universal = 1.2
T_max_universal = 1.5

These values are not arbitrary.
They are the lowest thresholds that survive cross-domain falsification without false positives.

All domains inherit these baselines unless empirically proven unsafe.

Calibration Phases

Calibration MUST proceed through all four phases in order.

Phase 1 — Baseline Extraction

Collect historical data from the target domain BEFORE Tessrax enforcement.

Data MUST include both:

• Known successful systems (survived without cascading failure)
• Known failed systems (collapse, breach, litigation, recall, shutdown)

Minimum sample size: 50 independent cases.

Required metrics per case:

R_t — reward for truth revelation
C_e — cost of exposure
L — legitimacy renewal rate
O_r — observer credibility / signal propagation
T_D — decision cadence
T_V — verification cadence

If any metric cannot be estimated, calibration HALTS.

Phase 2 — Blind Mapping

Compute for each historical case:

E_health = R_t / (C_e + 1)
L_O_balance = L / O_r
T_ratio = T_D / T_V

Label outcomes ONLY as:

SUCCESS — survived ≥ 12 months without systemic failure
FAILURE — cascaded, collapsed, or required emergency intervention

Calibration MUST be blind:
No knowledge of outcome is permitted during threshold search.

Phase 3 — Threshold Derivation

Thresholds are chosen to maximize discrimination power.

Φ_domain MUST satisfy:

P(FAILURE | E_health < Φ_domain)
minus
P(FAILURE | E_health ≥ Φ_domain)

is maximized.

Equivalent ROC or Youden-index methods are acceptable if reproducible.

Constraints:

Φ_domain MUST be ≥ Φ_universal
Deviation from Φ_universal MUST be ≤ +20% unless regulator-approved

L_max_domain is derived as:

median(L / O_r | SUCCESS) × 1.2

T_max_domain is derived as:

argmin_t [ P(FAILURE | T_ratio > t) ]

If no discriminative threshold exists, Tessrax enforcement is NOT DEPLOYABLE in that domain.

Phase 4 — Falsification and Freeze

Candidate thresholds MUST be tested against a held-out blind set.

Required performance:

Sensitivity ≥ 85%
Specificity ≥ 90%

Failure to meet BOTH metrics INVALIDATES the calibration.

If successful:

• Thresholds are frozen
• Spec version increments
• Calibration receipt is emitted

Frozen thresholds may not be modified without a new calibration cycle.

Non-Circularity Rule

Thresholds may NOT be validated using systems already governed by those thresholds.

Only pre-enforcement or externally governed data is admissible.

Any circular validation attempt INVALIDATES the entire calibration.

Update Conditions

Threshold updates are permitted ONLY if:

• ≥ 10 new verified failure cases exist OR
• Outcome prediction improves by ≥ 20%

Updates MUST follow full recalibration, not patch adjustment.

Partial tuning is prohibited.

Calibration Receipt Requirement

Every calibration MUST emit a receipt containing:

calibration_id
domain
historical_sample_size
sensitivity
specificity
thresholds
baseline_reference
frozen = true

Calibration receipts are subject to the Receipt and Audit Invariant.

Failure to emit a calibration receipt renders thresholds INVALID.

Scope Restriction

This canon defines methodology only.

It does not define data sources, tooling, statistical packages, or visualization.

Those are implementation details and non-canonical.

Terminal Clause

Any enforcement threshold lacking a valid calibration receipt MUST cause the gate to FAIL CLOSED.

There is no discretionary fallback.

End of CANON-007
