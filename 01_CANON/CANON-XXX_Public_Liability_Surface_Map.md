# CANON-XXX Public Liability Surface Map

## Definition
A *claimant-addressable liability surface* is a public liability artifact that:
- Exposes name-level artifacts unauthenticated
- Is machine-discoverable without credential gates
- Has deterministic join keys (name +/- locality / case ID)

## Included Custodian Classes
1. State & Local Treasurers — Unclaimed Property
2. Courts — Unclaimed Funds (Bankruptcy + Local Registry PDFs)
3. NCUA — Unclaimed Deposits for liquidated credit unions

## Excluded Custodian Classes
- IRS / tax refunds (identity-gated)
- PBGC / retirement locators (identity-gated)
- SEC & other regulators (case-level only, no claimant list)
- Treasury Hunt / bonds (identity-gated)
- Class Action Administrators (sealed or gated claimant lists)

## Invariants
- A surface must have *no authentication requirement* for name-level artifacts.
- Name + locality or name + case ID are necessary keys.
