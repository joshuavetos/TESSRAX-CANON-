# NCUA Unclaimed Deposits — Normalization Schema

## Canonical Fields
- claimant_full_name
- first_name
- last_name
- city
- state
- credit_union_name
- amount
- record_source
- retrieval_timestamp
- is_us_territory

---

## Keys

### Primary Key
- claimant_full_name + city + state

### Secondary Key
- claimant_full_name + credit_union_name

---

## Normalization Rules

- Names preserved as source-of-truth strings
- City normalized to title case
- State normalized to ISO 3166-2 alpha-2
- Amount parsed to float USD
- Territories (PR, VI, GU, AS, MP) flagged

---

## Deduplication

- Sliding 30-day window
- Deduplicate by primary key
- Retain highest amount within window

This schema is authoritative for all NCUA ingestion.
