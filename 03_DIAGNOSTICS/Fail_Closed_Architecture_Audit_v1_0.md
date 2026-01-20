# Fail-Closed Architecture Audit (Checklist v1.0)

**Purpose:**  
A one-page, fail-closed diagnostic to identify when a system (technical, organizational, or social) transitions from a productive tool into a parasitic enclosure. Anchored in thermodynamics, control theory, and metabolic cost accounting.

**Use:**  
Apply to any architecture prior to lock-in. If thresholds are breached, enforcement must halt or decompose to analog fallback. Silence / NO-CHANGE is a valid success state.

---

## 1. Variance & Noise — *The Slack Test*

- [ ] **Identification:** Are human/system variances treated as waste to be eliminated rather than slack for resilience?
- [ ] **Novelty Gap:** Does the system fail when encountering out-of-distribution inputs it was not pre-trained or pre-programmed to handle?
- [ ] **Innovation Leaks:** Are there explicit low-control zones where non-standard behavior is tolerated to preserve adaptation?

**Fail Condition:** Any two unchecked boxes ⇒ VARIANCE STARVATION.

---

## 2. Enforcement & Extraction — *The Metabolic Test*

- [ ] **Cost Scaling:** Does monitoring cost scale superlinearly as visibility approaches 100%?
- [ ] **Triage Point:** Is there a defined threshold where deviations are ignored because correction costs exceed value?
- [ ] **Parasitic Ratio:** Is >10% of total energy/revenue spent purely on compliance, auditing, or internal monitoring?

**Fail Condition:** Parasitic Ratio >10% OR absence of a triage point ⇒ PARASITIC DRIFT.

---

## 3. Buffers & Resonance — *The Physics Test*

- [ ] **JIT Fragility:** Have buffers (inventory, latency, manual override) been removed for efficiency?
- [ ] **Cascade Gating:** In a fail-closed event, can the periphery survive as an isolated analog unit?
- [ ] **Feedback Latency:** Is the control loop faster than the physical system’s settling time?

**Fail Condition:** Control faster than physics OR no isolatable periphery ⇒ RESONANT SHATTER RISK.

---

## 4. The Leaky Cage — *The Equilibrium Test*

- [ ] **Strategic Neglect:** Does the design intentionally abandon low-utility sectors to preserve the core?
- [ ] **Compliance Mimicry:** Can users provide perfect signals while materially diverging in reality?
- [ ] **Inevitability Check:** Has the design acknowledged that 100% control is a terminal failure state?

**Fail Condition:** Pursuit of total enclosure OR unacknowledged mimicry ⇒ LEAKY RIGIDITY.

---

## Final Classification

- **PASS:** No section fails.
- **WARN:** One section fails — remediation required before scale.
- **UNVERIFIED:** Two or more sections fail — enforcement halt required.
- **WRITE-LOCK:** Four sections fail — decompose to analog fallback; no further optimization.

**Invariant:** No optimization without slack. No control without metabolic accounting. No efficiency without buffers. No enforcement without an exit cost.

**Version:** v1.0  
**Status:** WRITE-LOCKED
