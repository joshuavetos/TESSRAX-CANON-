# Universal Claimant Schema (UCS) — v1.0

This file defines the single master schema for all claimant-addressable liability surfaces in this repo.
Baseline: `NCUA_Normalization_Schema`
Extension model: bounded deltas (COURT-DELTA, TREASURER-DELTA, FDIC-DELTA)

---

## 1) Scope

UCS applies to these included surfaces:
- Courts (bankruptcy unclaimed funds, court registry/unclaimed lists)
- Treasurers (state/local unclaimed property, uncashed check lists)
- NCUA (unclaimed deposits for liquidated credit unions)
- FDIC (conditional; only when name-level artifacts are exposed unauthenticated)

UCS does not define claim filing workflows. UCS defines normalization + storage schema only.

---

## 2) Field Set

### 2.1 Core Baseline Fields (NCUA baseline)
These fields exist on every UCS record.

- `claimant_full_name` (string, required)
- `first_name` (string, optional)
- `last_name` (string, optional)
- `city` (string, optional)
- `state` (string, optional; ISO 3166-2 alpha-2 where applicable)
- `amount` (number, required; USD float)
- `record_source` (string, required; canonical source URL or identifier)
- `retrieval_timestamp` (string, required; ISO-8601)
- `is_us_territory` (boolean, required; default false)

### 2.2 Universal Surface Fields
These fields unify cross-surface provenance and classification.

- `surface_class` (enum, required)
  - `COURT`
  - `TREASURER`
  - `NCUA`
  - `FDIC`

- `asset_type` (string, optional)
  Examples: `Bail`, `ExcessProceeds`, `RegistryFunds`, `UnclaimedProperty`, `UncashedCheck`, `UnclaimedDeposit`, `UnclaimedDividend`

- `reporting_entity` (string, optional)
  Meaning: the entity that reported/caused the liability record (holder/reporter), not the custodian.
  Examples: `Bank of America`, `State Payroll`, `County Treasurer Office`, `Trustee`, `Failed CU`

- `custodian_name` (string, optional)
  Meaning: the public custodian publishing the artifact.
  Examples: `NCUA`, `FDIC`, `LA County Superior Court`, `Florida DFS`

- `jurisdiction` (string, optional)
  Format: free-text but stable; examples:
  - `US-FED-CA-CACB` (bankruptcy court shorthand ok)
  - `US-CA-LA` (county)
  - `US-FL` (state)

### 2.3 Surface Delta Fields (Bounded Extensions)

#### COURT-DELTA
- `case_number` (string, optional)
- `court_jurisdiction` (string, optional; may mirror `jurisdiction` but court-specific)
- `court_name` (string, optional)

#### TREASURER-DELTA
- `last_known_address` (string, optional)
- `property_type_code` (string, optional; if exposed by UCP surface)
- `property_type_desc` (string, optional)

#### FDIC-DELTA
- `failed_institution_name` (string, optional)
- `receivership_id` (string, optional)

#### NCUA-DELTA (baseline-present but explicitly modeled)
- `credit_union_name` (string, optional)

---

## 3) Deterministic Keys

### 3.1 Primary Key (UCS)
Primary keys must be stable, deterministic, and avoid identity-gated fields.

`primary_key` (string, required) is computed as:

- If `surface_class == COURT` and `case_number` is present:
  - `lower(claimant_full_name | case_number | jurisdiction)`
- Else if `surface_class in {TREASURER, NCUA, FDIC}`:
  - `lower(claimant_full_name | city | state | jurisdiction)`

### 3.2 Secondary Key (UCS)
`secondary_key` (string, required) is computed as:

- If `surface_class == NCUA` and `credit_union_name` present:
  - `lower(claimant_full_name | credit_union_name | state)`
- Else if `surface_class == FDIC` and `failed_institution_name` present:
  - `lower(claimant_full_name | failed_institution_name | state)`
- Else if `surface_class == TREASURER` and `reporting_entity` present:
  - `lower(claimant_full_name | reporting_entity | state)`
- Else if `surface_class == COURT` and `court_name` present:
  - `lower(claimant_full_name | court_name | jurisdiction)`
- Fallback:
  - `lower(claimant_full_name | jurisdiction)`

---

## 4) Normalization Rules (Mandatory)

- Preserve `claimant_full_name` as source-of-truth string (trimmed).
- `first_name` / `last_name` parsing is best-effort only; absence is acceptable.
- `city` title-case; `state` upper-case when present.
- `amount` must parse to float; failures must produce a hard error (no silent null).
- `record_source` must be non-empty.
- `retrieval_timestamp` must be ISO-8601.
- `surface_class` must be one of the enum values.

---

## 5) Validation Gates (Fail-Closed)

A UCS record is VALID only if:

- `claimant_full_name` is non-empty
- `amount` is non-null and numeric
- `record_source` is non-empty
- `retrieval_timestamp` is non-empty ISO-8601
- `surface_class` is valid enum
- `primary_key` and `secondary_key` are non-empty strings

If any condition fails: the ingestion run must HALT and emit a NERF artifact.

---

## 6) Deduplication Policy (Unified)

Default dedupe window: 30 days (sliding).

- Deduplicate by `primary_key`
- Retain the record with the highest `amount`
- If tied on `amount`, retain the record with the latest `retrieval_timestamp`

---

## 7) Canonical Column Order (CSV)

UCS canonical export MUST use this order:

1. `primary_key`
2. `secondary_key`
3. `surface_class`
4. `claimant_full_name`
5. `first_name`
6. `last_name`
7. `city`
8. `state`
9. `amount`
10. `asset_type`
11. `reporting_entity`
12. `custodian_name`
13. `jurisdiction`
14. `record_source`
15. `retrieval_timestamp`
16. `is_us_territory`
17. `credit_union_name`
18. `failed_institution_name`
19. `receivership_id`
20. `case_number`
21. `court_name`
22. `court_jurisdiction`
23. `last_known_address`
24. `property_type_code`
25. `property_type_desc`

Fields not applicable to a surface remain empty strings (not omitted).

---

## 8) Backward Compatibility

- NCUA schema is a strict subset of UCS.
- Existing NCUA normalized exports remain valid when mapped into UCS by setting:
  - `surface_class = NCUA`
  - `jurisdiction = US-FED`
  - `custodian_name = NCUA`

---

## 9) Change Control

UCS is a master schema. Any new field requires:
- A named delta block
- A deterministic key impact assessment
- Updated validation gates
- Version bump (v1.x)

End of file.
