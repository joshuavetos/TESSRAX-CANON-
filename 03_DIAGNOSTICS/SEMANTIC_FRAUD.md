# Diagnostic: Semantic Fraud

## Definition
Semantic Fraud occurs when an institution represents certainty it cannot manually verify.

## Indicators
- Emphasis on uptime over understanding
- Disaster recovery plans without epistemic recovery
- Compliance defined by tool presence, not capability

## Key Absence
No logged failure for:
“Human unable to re-derive state from raw inputs.”

## Consequence
Truth is leased, not owned.
Governance becomes narrative maintenance.

## Classification
ERT < 6 automatically constitutes Semantic Fraud.
## INCENTIVE GAP — EPISTEMIC UX AUDIT

### Definition
An Incentive Gap exists when an organization:
1) Discloses epistemic risk (hallucination, uncertainty, misuse) in compliance artifacts
2) While optimizing user-facing interfaces to suppress or mask that uncertainty
3) Because confidence-forward presentation outperforms truth-signaling on engagement KPIs

This is not a bug. It is a selection effect.

---

### Falsifiable Hypothesis
If an Incentive Gap exists, then the organization has run (or avoided running) A/B tests where:
- Variant A: Uncertainty-forward UX (hedging, confidence indicators, verification prompts)
- Variant B: Declarative confidence-forward UX

And Variant B won on retention/session metrics and shipped.

---

### Audit Demand (Forcing Function)
Produce results of any experiments comparing uncertainty-forward vs declarative UX variants, including:
- Variant descriptions
- Primary KPI (retention, session length, DAU)
- Safety or correctness KPI (user correction rate, complaints, reversals)
- Decision outcome (which variant shipped)

Refusal, “proprietary” claims, or absence of such experiments is itself a positive signal of Incentive Gap risk.

---

### Pass / Fail Criteria
PASS:
- Quantitative deltas disclosed OR
- Explicit admission that no such experiments exist

FAIL:
- Risk disclosed in footnotes while UX optimization data is withheld

---

### Failure Mode Classification
SFDD:
- F6 (Metric Proxy / Goodhart)
- F9 (Epistemic Laundering)
