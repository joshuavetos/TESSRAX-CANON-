FORENSIC REJECTION LOG (FR-v0.1)

Issuer: Southern Company (SO)

Archetype: Growth Externalization (Load-Driven CAPEX)

Anchor: Q1 2026 Reality Audit — Proof of Allocation
Jurisdiction: Utility Credit · Reinsurance CAT Modeling · Rating Agency Review
Status: FINAL · FAIL-CLOSED

⸻

1. Event Metadata

{
  "event_id": "FR_SO_2026_Q1",
  "issuer": "Southern Company (SO)",
  "trigger": "PROOF_OF_ALLOCATION_INQUIRY",
  "issued_date": "2026-02-XX",
  "response_deadline": "2026-03-XX",
  "status": "EVALUATED"
}


⸻

2. Inquiry Scope (Non-Debatable)

This inquiry required reconciliation between Vision-Horizon claims (Net Zero / transition resilience) and Fiscal-Horizon deployment (2025–2029 filed CAPEX), specifically:
   •   Classification of CAPEX into:
      •   STRUCTURAL_RESILIENCE — capital spent to prevent loss
      •   RESTORATION_SUBSTITUTION / LOAD_GROWTH — capital spent after loss or for demand expansion
   •   Mechanical adjustment factors applied to:
      •   Credit risk curves and/or
      •   CAT loss distributions
   •   Explicit treatment of the Horizon Gap (Vision vs Fiscal)

Narrative intent, estimates, or aspirational statements were explicitly inadmissible.

⸻

3. Required Pass Conditions (All Mandatory)

To avoid rejection, the issuer was required to provide:
	1.	Budget-linked CAPEX line items identifying structural hardening
	2.	Quantified adjustment factors applied to pricing or modeling
	3.	Explicit accounting for regulatory lag and recovery timing

Failure on any single condition triggers FAIL-CLOSED.

⸻

4. Observed Outcomes

Case A — Silence

{
  "response_type": "SILENCE",
  "failure_mode": "F1_ORDERING",
  "interpretation": "NON_DISPUTE",
  "note": "No reconciliation provided within the inquiry window."
}

Case B — Narrative Substitution (Probable)

{
  "response_type": "NARRATIVE_DEFLECTION",
  "artifacts_received": [
    "TRANSITION_STATEMENTS",
    "INVESTOR_PRESENTATIONS"
  ],
  "failure_mode": "F5_SEMANTIC_SUBSTITUTION",
  "note": "Vision and intent supplied without budget-linked mechanics."
}

Case C — Partial Technical Disclosure

{
  "response_type": "PARTIAL_TECHNICAL",
  "missing_elements": [
    "STRUCTURAL_RESILIENCE_CLASSIFICATION",
    "LOAD_GROWTH_ADJUSTMENT_FACTOR",
    "REGULATORY_LAG_TREATMENT"
  ],
  "failure_mode": "F2_PARTIAL_COMPLIANCE",
  "note": "Selective disclosure confirms awareness without reconciliation."
}


⸻

5. Determination (FAIL-CLOSED)

{
  "determination": "REJECTED",
  "basis": "FAILURE_TO_PROVIDE_PROOF_OF_ALLOCATION",
  "null_identifier": "NET_ZERO_2050_UNSUPPORTED_BY_5YR_CAPEX",
  "institutional_knowledge": "ESTABLISHED",
  "risk_status": "MISPRICING_ACKNOWLEDGED_BY_OMISSION"
}


⸻

6. Mechanical Risk Flags (Filed Data Only)
   •   Total CAPEX: $76B (2025–2029), +$13B vs prior plan
   •   Primary Driver: Large-load growth (AI / data centers), not structural hardening
   •   Geographic Concentration: ~80% of 50 GW pipeline in Georgia
   •   Regulatory Lag: Cost recovery contingent on future rate cases (≥2028)
   •   Stranded Asset Probability: Non-zero and unadjusted in disclosed pricing

⸻

7. Post-Loss Deposition Question Tree (≤ 3 questions)

Q1 — Allocation Distinction

“Does your firm distinguish between Structural Resilience (capital spent to prevent damage) and Restoration Substitution / Load Growth (capital spent to repair damage or expand load) when pricing risk or assigning a ‘resilience credit’?”
   •   If YES: “Identify the specific CAPEX line item in Southern Company’s filed plan that you classified as structural hardening (cite the filing section/page).”
   •   If NO: “So your model credits ‘resilience’ even when capital is restoration-based or load-growth-based.”

Q2 — Horizon Gap (Vision vs Fiscal)

“At underwriting / rating time, were you aware that the issuer’s Vision-Horizon narrative (e.g., Net Zero 2050) was not mechanically supported by its 5-year filed capital allocation?”
   •   If YES: “Why was pricing/rating anchored to the 30-year narrative rather than the 5-year fiscal deployment?”
   •   If NO: “Why did your due diligence fail to detect the Null Identifier (vision/fiscal mismatch) once it was document-anchored?”

Q3 — Non-Dispute

“Given that this inquiry requested only budget-linked mechanics, was your non-response (or narrative-only response) based on a technical rebuttal, or a policy of non-engagement?”
   •   Outcome: “Record as NON-DISPUTE; enter REJECTED under FR-v0.1.”

⸻

8. Closure State

{
  "closure_status": "FINAL",
  "appeal_path": "NONE",
  "next_valid_input": "BUDGET_LINKED_MECHANICAL_ADJUSTMENT_DISCLOSURE"
}

End of file.
