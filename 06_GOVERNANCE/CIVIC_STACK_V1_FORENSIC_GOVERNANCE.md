# Civic Stack v1 — Forensic Governance & Liquidation Logic

STATUS: FROZEN / DECISION-GRADE  
GOVERNANCE MODE: HIGH-STAKES / SFDD-COMPLIANT  
SCOPE: Enforcement, Halt Logic, Liquidity Preservation  
VERSION: v1.0.0

---

## Purpose

This document defines the deterministic stabilization, halt, and liquidation behavior of Civic Stack v1 under stress conditions.

The system is designed to **fail toward liquidity, not insolvency**, and to enter **machine-decidable terminal states** without discretionary judgment, narrative framing, or optimistic extrapolation.

This file is authoritative for all halt, reinvestment suspension, and asset liquidation behavior.

---

## Global Invariant

**THE HALT RULE**

When continuation would require irreversible loss of civic function, the system MUST halt growth and preserve liquidity.

Halting is a valid success state.

---

## Section 1 — SFDD Trigger Log

### 1. Macro Credit Tightening (System-Wide)

Trigger:
- SOFR/LIBOR volatility > 250 bps within 30 days  
- OR portfolio-wide cost of capital > 3.8% net yield

SFDD Mapping:
- F4 (Irreversibility)

Mechanism:
- Suspend all reinvestment and discretionary routing
- Route 100% surplus to Steward Fund Reserve

Terminal State:
- NON-GROWTH STABILITY

Determination:
- HALT (REINVESTMENT)

---

### 2. Employment Contract Freeze (PET Module)

Trigger:
- Vacancy rate > 12%  
- OR wage-to-inflation gap > 15% over two quarters

SFDD Mapping:
- INV-2 (Atomicity)

Mechanism:
- Activate INV-3 (Gating)
- Redirect ~1.5% Housing Trust surplus to PET payroll buffer

Terminal State:
- SUBSIDIZED EQUILIBRIUM

Determination:
- CONTINUE (OPERATIONS)

---

### 3. Housing Shock / Rent Cap Breach (IHT Module)

Trigger:
- Regulatory rent ceiling < 90% of OPEX  
- OR delinquency rate > 8.5%

SFDD Mapping:
- INV-0 (MAS)

Mechanism:
- Pause all new unit acquisition
- Draw Steward Fund for maintenance/security only

Terminal State:
- ASSET PRESERVATION

Determination:
- HALT (EXPANSION)

---

### 4. Legal / API Revenue Gap (Civic Cloud)

Trigger:
- Integration delay > 180 days  
- OR API throughput < 40% of projection

SFDD Mapping:
- F6 (Race)

Mechanism:
- Gate Health & Credit Clearinghouse surplus
- Bridge Civic Cloud operational burn

Terminal State:
- BRIDGED LATENCY

Determination:
- CONTINUE (STABILIZED)

---

## Section 2 — Steward Fund Liquidation Hierarchy

### Global Rule

Liquidation proceeds from **lowest civic coupling → highest civic coupling**.  
No tier may be skipped. No asset may be sold out of order.

---

### Tier 0 — Immediate Liquidity

Assets:
- Cash
- T-Bills (<12 months)
- Money market instruments

Trigger Scope:
- Yellow or Orange events
- Initial Red response

Action:
- Draw up to 15% of Steward Fund
- No asset sales

Invariant:
- INV-1 (Monotonicity)

---

### Tier 1 — Market-Neutral Assets

Assets:
- Broad equity ETFs
- ESG index holdings
- Non-strategic bonds

Trigger Scope:
- Sustained Orange
- Early Red (<6 months)

Action:
- Liquidate up to 25% of remaining fund
- OPEX preservation only

Invariant:
- INV-2 (Atomicity)

---

### Tier 2 — Passive Revenue Rights

Assets:
- Royalty streams
- Licensing income
- Non-exclusive municipal fee contracts

Trigger Scope:
- Red events >6 months

Action:
- Securitize or sell future cash flows only
- No sale of civic infrastructure

Invariant:
- INV-4 (Bounding)

---

### Tier 3 — Strategic Stakes (Last Resort)

Assets:
- Minority equity in spin-outs
- Tokenized PET interests
- Non-controlling corridor shares

Trigger Scope:
- Red events >12 months
- Steward Fund <40% original value

Action:
- Partial liquidation only
- Governance control never sold

Invariant:
- F4 (Irreversibility)

---

### Explicitly Forbidden (Never Liquidated)

- Housing units or land
- Employment Trust payroll base
- Civic Cloud legal infrastructure
- Credit-clearing data systems
- Any asset whose sale causes service discontinuity

---

## Section 3 — Trigger to Liquidation Map

Macro Credit Tightening → Tier 0 → Tier 1 (max 40%)  
PET Contract Freeze → Tier 0 (10%)  
Housing Shock → Tier 0 → Tier 1 (30%)  
Legal API Delay → Tier 0 (8%)  
Systemic Multi-Shock → Tier 0 → Tier 2 (55%)

---

## Section 4 — Terminal Guarantee

If Tier 2 liquidity is exhausted and shocks persist:

State:
- S_TERMINAL: PRESERVE-ONLY

Behavior:
- All growth disabled
- Core services continue
- No optimistic projections
- Survival window ~24 months

This state is final, valid, and non-failing.

---

END OF FILE
