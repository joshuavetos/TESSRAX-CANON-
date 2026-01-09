# NCUA Unclaimed Deposits Normalization

## Fields
- claimant_full_name
- first_name
- last_name
- city
- state
- credit_union_name
- amount
- record_source (URL / timestamp)

## Keys
- primary: claimant_full_name + city + state
- secondary: claimant_full_name + credit_union_name

## Notes
- Must dedupe by (name, city/state) within 30 days.
- Flag non-US states/territories for separate handling.
