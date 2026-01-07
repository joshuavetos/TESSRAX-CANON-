# CANON-004 — Structural Risk Transfer & Control Surfaces
Status: CANON  
Scope: Descriptive, non-intent-asserting analysis  
Invariant: Documents observed mechanisms only; no allegation of intent, coordination, or misconduct

---

## Canonical Invariant

This document **does not allege intent, coordination, or misconduct**.  
It documents **structural dependency, selective enforcement, and risk-transfer mechanisms** as *observed outcomes* of existing architectures, contracts, policies, and technical designs.

All entities operate independently unless explicitly stated otherwise.

---

## Purpose

To provide a **mechanically normalized registry** of:
1. Control surfaces used by dominant entities
2. The enforcement vectors those surfaces enable
3. The downstream parties that absorb financial or operational risk
4. The reversibility horizon of each mechanism

This canon exists to make **risk legible before regulation, litigation, or systemic failure**, without moral framing.

---

## Normalization Schema (Binding)

Every entry MUST conform to the following fields:

- **Entity**
- **Layer** (0–7, per Sovereignty Stack)
- **Control Surface Type**  
  *(technical / legal / contractual / architectural / algorithmic)*
- **Policy Mechanism**  
  *(neutral, verbatim where possible)*
- **Enforcement Vector**  
  *(how the policy is applied in practice)*
- **Primary Effect**  
  *(first-order operational or financial impact)*
- **Absorbing Party**  
  *(who bears downside risk or cost)*
- **Reversibility Horizon**  
  *(Immediate / Time-bounded / Cost-bounded / Practically irreversible)*

---

## I. Selective Enforcement & Rule Asymmetry

### Apple
- **Layer:** 5 — Interface  
- **Control Surface:** Technical + Policy  
- **Policy Mechanism:** Prohibition on third-party interactive overlays over other apps  
- **Enforcement Vector:** App Store review + API restrictions  
- **Primary Effect:** Third-party apps cannot replicate system-level interaction features  
- **Absorbing Party:** Developers  
- **Reversibility Horizon:** Low (requires platform policy change)

### Amazon Web Services (AWS)
- **Layer:** 2 — Infrastructure  
- **Control Surface:** Architectural  
- **Policy Mechanism:** Waiver of data egress fees for migrating customers  
- **Enforcement Vector:** Pricing policy change  
- **Primary Effect:** Data mobility without application logic portability  
- **Absorbing Party:** Customers with deeply AWS-native architectures  
- **Reversibility Horizon:** Cost-bounded (full re-architecture required)

### Broadcom (VMware)
- **Layer:** 2 / X — Cross-Layer Infrastructure  
- **Control Surface:** Contractual  
- **Policy Mechanism:** Refusal to renew support absent subscription bundle migration  
- **Enforcement Vector:** License termination  
- **Primary Effect:** 300–500% cost increases or forced re-platforming  
- **Absorbing Party:** Enterprise IT operators  
- **Reversibility Horizon:** Practically irreversible (short-term)

---

## II. Risk Transfer & Downside Absorption

### Hyperscale Data Centers
- **Layer:** 7 — Kinetic  
- **Control Surface:** Regulatory + Financial  
- **Policy Mechanism:** Inclusion of customer-specific infrastructure in general rate base  
- **Enforcement Vector:** Utility tariff design  
- **Primary Effect:** Socialization of stranded capital costs  
- **Absorbing Party:** Residential and municipal ratepayers  
- **Reversibility Horizon:** Long-term (20–30 year depreciation)

### Gig Economy Platforms
- **Layer:** 7 — Kinetic  
- **Control Surface:** Legal classification  
- **Policy Mechanism:** Independent contractor designation  
- **Enforcement Vector:** Labor law structuring (e.g., Prop 22)  
- **Primary Effect:** Externalization of asset depreciation and insurance risk  
- **Absorbing Party:** Workers  
- **Reversibility Horizon:** Legislative

### Payment Processors (Stripe / PayPal)
- **Layer:** 2.5 — Financial Utility  
- **Control Surface:** Contractual  
- **Policy Mechanism:** Reserve holds and account freezes upon risk flags  
- **Enforcement Vector:** Automated compliance systems  
- **Primary Effect:** Immediate liquidity seizure  
- **Absorbing Party:** Merchants  
- **Reversibility Horizon:** Time-bounded (90–180 days)

---

## III. Single-Node Dependency & Failure Horizons

### ASML
- **Layer:** 0 — Physics  
- **Control Surface:** Technical monopoly  
- **Policy Mechanism:** Denial of service, parts, or updates  
- **Enforcement Vector:** Export controls and vendor policy  
- **Primary Effect:** Long-term cap on advanced semiconductor manufacturing  
- **Absorbing Party:** Downstream national and industrial ecosystems  
- **Reversibility Horizon:** Multi-decade

### Microsoft Entra ID
- **Layer:** 2.5 — Identity  
- **Control Surface:** Architectural  
- **Policy Mechanism:** Centralized enterprise authentication  
- **Enforcement Vector:** Cloud identity dependency  
- **Primary Effect:** Recursive access lockout during failure  
- **Absorbing Party:** Enterprises and governments  
- **Reversibility Horizon:** Immediate upon outage

### CrowdStrike
- **Layer:** 2.5 — Endpoint Trust  
- **Control Surface:** Kernel-level technical control  
- **Policy Mechanism:** Real-time device trust scoring  
- **Enforcement Vector:** Mandatory agent enforcement  
- **Primary Effect:** Device de-platforming or instability  
- **Absorbing Party:** Operators and end users  
- **Reversibility Horizon:** Immediate to time-bounded

---

## Canonical Conclusions

1. **Risk flows downward; control flows upward.**
2. **Most modern systems are resilient to component failure but fragile to control-node constraint.**
3. **Downside is routinely absorbed by actors without decision authority.**
4. **Selective enforcement is structurally enabled even without coordinated intent.**

This canon defines the **mechanical reality** of modern corporate sovereignty, independent of motive.

---

## Canon Boundary

Prescriptive action, regulation, advocacy, or enforcement strategies are **explicitly out of scope** and must live in non-canonical analysis or case files.
