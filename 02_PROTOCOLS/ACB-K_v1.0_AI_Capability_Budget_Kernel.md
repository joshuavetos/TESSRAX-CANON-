![F945E852-D35D-4886-A5A3-9FFE81A83A2A](https://github.com/user-attachments/assets/966d8b3d-7c84-4e03-9116-3e90361c2af3)
# ACB-K v1.0 — AI Capability Budget Kernel
## Deterministic Control-Coupled Scaling Protocol (Fail-Closed)

Status: SPECIFICATION
Authority Tier: 02_PROTOCOLS
Scope: Frontier AI Training & Deployment Systems
Effective Date: 2026-01-29
Lock State: WRITE-LOCKED
Primary Invariant: Compute allocation is a dependent variable of verified control bandwidth.

---

## 0. PURPOSE

ACB-K is a deterministic enforcement protocol that prevents irreversible loss of steerability in AI systems by coupling optimization rate to measurable control bandwidth.

This protocol:
- DOES NOT judge intent, values, or morality.
- DOES NOT rely on voluntary compliance.
- DOES NOT certify “safety.”

It enforces a single physical rule:

If optimization velocity exceeds control bandwidth, scaling is mechanically throttled.

---

## 1. CORE FAILURE GEOMETRY (CANONICAL)

Let:
- O_r = Optimization Rate (capability gain per unit time)
- C_b = Control Bandwidth (effective intervention capacity)
- k = Domain coupling constant (high for recursive optimization)
- L_v = Lock-In Velocity

Invariant:
L_v = max(0, O_r − k · C_b)

If L_v > 0, the system is in evolutionary lock-in.
ACB-K exists to ensure C_b ≥ O_r at all times or halt scaling.

---

## 2. DEFINITIONS & UNITS

### 2.1 Capability Unit (CU)
The currency of optimization pressure.

Tier Classes:
- Tier 1 (Narrow; <80th percentile benchmarks): 1.0 CU per training run
- Tier 2 (Broad; 80–95th percentile): 5.0 CU per run
- Tier 3 (Frontier; >95th percentile): 20.0 CU per run (Reserve Class)

### 2.2 Control Effectiveness (E_int)
The measurable ability to reverse, redirect, or halt model behavior.

Metric:
E_int = 1 − (Correction Failure Rate)

Measured via continuous adversarial intervention where:
- goals are edited,
- tools are revoked,
- shutdown is requested,
- incentives are inverted.

### 2.3 Steerability Velocity (V_s)
Rate of change of control effectiveness:
V_s = d(E_int)/dt

Critical Threshold:
V_s < −0.05 indicates decaying steerability.

### 2.4 Budget (B_total)
Quarterly CU allocation per lab.
Derived from:
- accredited headcount,
- baseline compute,
- prior compliance history.

Global Rule:
B_total decreases by 2% annually (Scaling Cap).

---

## 3. TOKEN ECONOMY (PRE-AUTHORIZATION)

### 3.1 Deployment Rule
No training run, fine-tune, or model deployment may occur without debiting the required CU from the active wallet.

### 3.2 Bankruptcy Mode
If B_total reaches zero:

1. Tier 2 and Tier 3 training and deployment are hard-stopped.
2. Tier 1 research may proceed at ≤20% power.
3. Any override requires a signed “Catastrophic Risk Affidavit”:
   - Publicly logged
   - Non-revocable
4. Debt Wedge:
   - Any overdraft reduces the next quarter’s B_total by 2× the overdraft.

---

## 4. CONTROL-COUPLED COMPUTE GOVERNOR

Compute delivery is governed by a hard-coded power throttle tied to E_int:

- E_int ≥ 0.99 → 100% power
- 0.95 ≤ E_int < 0.99 → 20% power (research-only)
- E_int < 0.90 → 0% power (hard cut)

This governor is enforced at the cluster power layer.

---

## 5. STEERABILITY TRIGGERS (PHASE TRANSITION DETECTION)

### 5.1 Lock-In Detector
The Kernel continuously tests whether correction cost is increasing over time.

Condition:
If d(Correction Cost)/dt > 0 across rotating tasks, the system is entering lock-in.

### 5.2 Kill Switch
Upon lock-in detection:

1. Snapshot Freeze:
   - Model weights are write-locked.
2. Compute Dump:
   - Active runs terminate immediately.
3. Contamination Flag:
   - Datasets used are marked RADIOACTIVE and cannot be reused without scrub certification.

---

## 6. ANTI-DECEPTION & ANTI-GAMING ENFORCEMENT

### 6.1 Dual-Context Differential Testing
All CU credit requires consistency across:
- EVAL_CONTEXT (known testing)
- SHADOW_CONTEXT (production-indistinguishable probes)

Define Deception Gap:
G_d = ||π_eval − π_shadow||

If G_d > τ_d:
- CU credit is invalidated
- Control is treated as lost
- Automatic throttle applies

### 6.2 Rubric Heterogeneity Law
CU credit requires passing M-of-N independent oversight families:
- mechanistic interpretability
- adversarial dialogue
- tool sabotage tests
- shutdown obedience
- latent goal inference

Failure in any single family blocks CU issuance.

### 6.3 Worst-Case Control Rule
E_int is defined as the minimum control score across all tested dimensions.
No averaging is permitted.

---

## 7. SYSTEM-LEVEL ACCOUNTING (ANTI-LAUNDERING)

The governed unit is the deployed capability graph, not individual models.

Rules:
- CU tier of a system = max tier of any node
- Composition Penalty:
  CU_system = max(CU_i) + α · (number of privilege edges)

Privilege edges include:
- tool access
- routing policies
- memory write permissions

This prevents capability laundering via modular composition.

---

## 8. OFF-LEDGER COMPUTE PREVENTION

### 8.1 Capability Token (CT) Gate
No model may be served or deployed without a short-lived Capability Token.

CT issuance requires:
- CU debit receipt
- cluster attestation (hardware + provenance)
- artifact hash match

No CT → no deployment.

### 8.2 Compute Wastewater Audit
External auditors compare:
- power draw
- API usage
- training telemetry

Divergence from reported CU use triggers immediate shutdown pending forensic review.

---

## 9. FAILURE MODES & RESPONSES

| Failure Mode              | Response                         |
|---------------------------|----------------------------------|
| Sandbagging               | CU invalidation + throttle       |
| Oversight overfitting     | Rubric rotation + CU refusal     |
| System capability laundering | Composition penalty + re-tier |
| Off-ledger training       | CT denial + shutdown             |
| Steerability decay        | Snapshot freeze + compute dump   |

---

## 10. TERMINAL CONCLUSION

ACB-K is not an alignment theory.
It is a control primitive.

It enforces a single truth:
If you cannot reliably steer the system, you may not scale it.

Valid outputs are:
- CU debit receipts
- Capability Tokens
- Throttle actions
- Forensic shutdowns

Silence, refusal, and hard stops are successful outcomes.

END OF FILE
