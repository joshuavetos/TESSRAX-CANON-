# CANON-ZZZ — Status-Change Stranding Model

This canon defines the final, closed-world architecture of claimant-addressable liabilities.
Discovery is complete. Definition is locked.

---

## The Stranding Topology

All included custodian classes operate on a single mechanical failure loop:

**Prepayment / Debt → Status Change → Transaction Failure → Public Disclosure**

| Class | Source of Liability | Mechanical Trigger | Public Artifact |
|------|-------------------|-------------------|-----------------|
| Courts | Litigation / Registry | Case closure + staleness | Registry PDFs / UCFL |
| Treasurers | Commercial / Government activity | Statutory dormancy | UCP portals / PDF lists |
| FDIC / NCUA | Bank / Credit Union failure | Receivership liquidation | Unclaimed deposit search |

---

## Invariants for Ingestion

- **INV-STRAND-0**  
  The liability must arise from a *status-change*, not an ongoing dispute.

- **INV-STRAND-1**  
  The public surface must expose the *claimant name* without authentication.

- **INV-STRAND-2**  
  The failure must be *clerical*: resolution requires only notice + claim, not negotiation.

---

## Applied Schema Deltas

The `NCUA_Normalization_Schema` is the baseline.
All other surfaces extend it with bounded deltas.

### COURT-DELTA
Additional fields:
- `case_number`
- `court_jurisdiction`
- `asset_type`  
  (e.g., Bail, Excess Proceeds, Registry Funds)

### TREASURER-DELTA
Additional fields:
- `last_known_address`
- `reporting_entity`  
  (e.g., Bank of America, State Payroll, County Treasurer)

### FDIC-DELTA
Additional fields:
- `failed_institution_name`
- `receivership_id`

---

## Canonical Status

- Topology: **CLOSED**
- Mechanism: **LOCKED**
- Expansion: **Schema-only via deltas**

No additional custodian classes qualify unless they expose unauthenticated,
claimant-addressable public artifacts.

This file supersedes exploratory surface maps.
