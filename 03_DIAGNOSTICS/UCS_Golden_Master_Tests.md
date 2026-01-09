# UCS Golden Master Validation Tests

Purpose: Prove that all INCLUDED surfaces (NCUA, Courts, Treasurers, FDIC)
map deterministically into the Universal Claimant Schema (UCS)
without schema drift or silent data loss.

These tests are fail-closed.

---

## TEST-SET-001 — Baseline Integrity (NCUA)

Input:
- NCUA normalized record

Assertions:
- surface_class == NCUA
- claimant_full_name populated
- amount > 0
- primary_key non-empty
- secondary_key non-empty
- no COURT-DELTA fields populated
- no TREASURER-DELTA fields populated
- no FDIC-DELTA fields populated

Result:
- PASS required before any multi-surface ingestion

---

## TEST-SET-002 — COURT-DELTA Mapping (Bankruptcy)

Input:
- UCFL-style record containing:
  - claimant name
  - case number
  - court identifier
  - amount

Assertions:
- surface_class == COURT
- case_number populated
- court_name populated
- court_jurisdiction populated
- asset_type defaults to "Unclaimed Dividend" if absent
- primary_key uses (name + case_number + jurisdiction)
- amount > 0

Failure Conditions:
- Missing case_number
- Amount parsed as null
- primary_key collision across districts

---

## TEST-SET-003 — COURT-DELTA Mapping (County PDF)

Input:
- OCR-extracted county PDF row:
  - name
  - case/reference ID
  - amount

Assertions:
- surface_class == COURT
- asset_type populated (Bail | ExcessProceeds | RegistryFunds)
- court_name populated
- jurisdiction populated
- OCR confidence >= threshold OR record rejected

Hard Gate:
- Low-confidence OCR rows must be excluded, not coerced

---

## TEST-SET-004 — TREASURER-DELTA Mapping

Input:
- State or county unclaimed property record

Assertions:
- surface_class == TREASURER
- last_known_address populated if exposed
- reporting_entity populated
- property_type_code optional
- primary_key uses (name + city + state + jurisdiction)

---

## TEST-SET-005 — FDIC-DELTA Mapping

Input:
- FDIC unclaimed deposit/dividend record

Assertions:
- surface_class == FDIC
- failed_institution_name populated
- receivership_id populated if present
- secondary_key uses failed_institution_name
- no SSN/TIN fields present

---

## GLOBAL FAIL CONDITIONS

Any test fails if:
- claimant_full_name is empty
- amount is null or non-numeric
- surface_class not in enum
- primary_key empty
- secondary_key empty
- identity-gated fields appear (SSN, TIN, DOB)

---

## CANONICAL STATUS

These tests define **minimum admissibility**.
Any ingestion pipeline failing these tests MUST HALT and emit a NERF artifact.
