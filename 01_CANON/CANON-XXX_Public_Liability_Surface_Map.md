# CANON-XXX — Public Liability Surface Map

## Definition
A *claimant-addressable liability surface* is a public liability artifact that:
- Exposes name-level claimant records
- Requires no authentication or identity credential
- Is machine-discoverable at scale
- Provides deterministic join keys (name ± locality OR name + case ID)

This canon defines which custodians qualify.

---

## INCLUDED (Company-Grade Surfaces)

### 1. State & Local Treasurers
- Unclaimed Property (UCP)
- Uncashed / stale checks
- County treasurer unclaimed-funds lists

Characteristics:
- Name-level artifacts
- No authentication
- Public portals, PDFs, or bulk files

### 2. Courts
- Federal bankruptcy unclaimed funds (UCFL + court sites)
- County / municipal court registry and unclaimed-funds PDFs

Characteristics:
- Name + case ID
- No authentication
- Deterministic clerical recovery

### 3. NCUA (Liquidated Credit Unions)
- Unclaimed member deposits for involuntarily liquidated credit unions

Characteristics:
- Public HTML tables / bulk lists
- Name + city/state
- No authentication

---

## CONDITIONAL (Non-Foundational)

### FDIC (Failed Banks)
- Unclaimed dividends and deposits

Status:
- Public search exists
- Bulk / name-dump availability inconsistent
- Included only when unauthenticated claimant lists are verifiable

---

## EXCLUDED (By Hard Gate)

- IRS / State Tax Authorities — identity-gated (SSN/TIN)
- PBGC / Retirement Locators — identity-gated
- SEC / CFTC / Financial Regulators — case-level notices only
- Treasury Hunt / Savings Bonds — identity-gated
- Class Action Administrators — sealed or credential-gated claimant lists

---

## Invariants

- **INV-SURF-0**: Any authentication requirement disqualifies the surface.
- **INV-SURF-1**: Case metadata alone is insufficient; claimant records must be exposed.
- **INV-SURF-2**: Surfaces must be reusable at scale, not scoped to an inquirer.

This map is closed-world until a new unauthenticated claimant surface is proven.
