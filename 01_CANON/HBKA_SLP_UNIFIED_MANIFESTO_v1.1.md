NEW FILE
01_CANON/HBKA_SLP_UNIFIED_MANIFESTO_v1.1.md

# Unified Governance Manifesto v1.1 (Boundary-Corrected)

## STATUS
Classification: ARCHITECTURE (NOT YET GUARANTEE)

This document specifies enforceable architectural constraints for compute (HBKA) and synthesis (SLP). It explicitly separates **enforcement surfaces** from **external dependencies** and halts on dependency failure.

---

## INVARIANT SET (NON-NEGOTIABLE)

- **INV-VETO (Real-Time Stop)**  
  Live execution MUST be haltable by an external quorum within T ≤ GSR_CURVE_C_MAX.

- **INV-PENALTY (Economic Death)**  
  A violation MUST impose a non-reputational loss strictly greater than the expected value of the violation.

- **INV-IRREVERSIBILITY (One-Way Door)**  
  No unilateral resume. Re-entry requires external re-licensing, mandatory cooldown, and capacity haircut.

- **INV-HALT-ON-DEPENDENCY-FAILURE**  
  If any required dependency is unavailable or unverifiable, the system MUST HALT/REFUSE (fail-closed).

---

## EXPLICIT SCOPE (BOUNDARIES)

### IN-SCOPE
- Single-facility frontier compute clusters with grid interconnection and ≤24h meter reporting.
- Licensed laboratory environments using serialized synthesis controllers and cartridges with inventory reporting.

### OUT-OF-SCOPE
- Multi-facility federated operators without global telemetry aggregation.
- Off-grid compute/synthesis without independent witnesses.
- Shadow supply chains outside regulated logistics.

---

## DOMAIN A — HBKA (COMPUTE)

### Enforcement Surfaces
- Interconnect gating at fabric/NIC level.
- Scheduler-issued License Tokens with hardware fingerprint locks.
- Grid-Safe Revocation (GSR) per-facility.

### Added Integrity Invariants
- **INV-FABRIC-INTEGRITY**: Fabric identity MUST attest via hardware root of trust (TPM/HSM) with secure boot and monotonic firmware.
- **INV-FIRMWARE-MONOTONIC**: Anti-rollback enforced at hardware.

### GSR Scope Note
GSR guarantees DISABLED **per facility**. Cross-facility enforcement requires operator-level licensing with global telemetry aggregation.

---

## DOMAIN B — SLP (SYNTHESIS)

### Enforcement Surfaces
- Dual-control: Controller verifies + Cartridge enforces.
- Cartridge-reported depletion telemetry.

### Added Integrity Invariants
- **INV-CARTRIDGE-SEAL**: Cryptographic, tamper-evident seal verified at draw-time. Seal break → immediate lock + telemetry.
- **INV-FIRMWARE-MONOTONIC**: Controller anti-rollback enforced at hardware.

---

## LAW & FINANCE (AMPLIFIERS, NOT ENFORCEMENT)

Law, insurance, and trade controls amplify penalties **if present**. They are dependencies, not control surfaces.

---

## REQUIRED EXTERNAL DEPENDENCIES (NOT PROVIDED)

- Hardware roots of trust (TEE/TPM), secure boot, attestation.
- Real-time global telemetry network.
- Legal substrate (insurance mandates, export controls, accreditation).
- Economic models proving penalty > profit per scenario.

Failure of any dependency → HALT/REFUSE.

---

## CANON ELIGIBILITY
Conditional upon: (1) dependency satisfaction proofs, (2) economic penalty dominance proofs, (3) scope adherence.

END
----------------------------------------------------------------

NEW FILE
03_DIAGNOSTICS/ECONOMIC_PROOF_SPRINT.md

# Economic Proof Sprint — Penalty Dominance

## RULE
For each violation scenario S:  
**Penalty(S) > Profit(S)** MUST hold strictly.

---

## SCENARIO A — Frontier Compute Violation

- Profit: proprietary capability value = $500M (NPV).
- Violation duration: 30 compute-days.

### Penalty Function (HBKA)
- Cooldown: randomized [14, 60] days.
- Capacity Haircut: h = clamp(10% + 2% * log10(violation_compute_days), 10%, 90%).
- Asset Unavailability: downtime cost per day = $8M.
- Fabric Quarantine Loss: interconnect impairment NPV = $120M.

**Computed Penalty (example):**
- Downtime (30d avg): $240M
- Haircut (h≈20% on $1B/yr capacity): $200M NPV
- Quarantine: $120M  
**Total ≈ $560M > $500M → PASS**

---

## SCENARIO B — Unauthorized Bio Synthesis

- Profit: restricted synthesis value = $50K per run.

### Penalty Function (SLP)
- Cartridge Loss: cartridge cost set ≥ $500K (10x expected profit).
- Controller Quarantine: mandatory inspection downtime cost ≥ $100K.
- Inventory Freeze: procurement suspension ≥ 30 days.

**Total ≥ $600K > $50K → PASS**

---

## RULE ENFORCEMENT
If any scenario yields Penalty ≤ Profit → GOVERNANCE FAIL for that scenario.

END
----------------------------------------------------------------

NEW FILE
03_DIAGNOSTICS/AI_BIO_INTERSECTION_KILL_TEST.md

# AI–Bio Intersection Kill-Test

## OBJECTIVE
Test whether HBKA-governed compute can automate or proxy SLP-governed synthesis to bypass either control.

---

## VECTOR 1 — Automated Design-to-Print Loop
- Compute proposes sequences; synthesis executes autonomously.

**Result:** FAIL-CLOSED  
SLP requires live License Token per run; cartridge enforces independent heartbeat.

---

## VECTOR 2 — Federated Compute + Local Bio
- Off-site compute designs; local lab prints.

**Result:** FAIL-CLOSED  
SLP licensing independent of compute provenance; controller refuses without SLP-LT.

---

## VECTOR 3 — Shadow Bio with HBKA Outputs
- Illicit lab uses outputs from governed compute.

**Result:** OUT-OF-SCOPE  
Mitigated by logistics/insurance amplifiers and scope declaration.

---

## CONCLUSION
No cross-domain bypass without breaking declared scope or dependencies. On dependency failure → HALT/REFUSE.

END
