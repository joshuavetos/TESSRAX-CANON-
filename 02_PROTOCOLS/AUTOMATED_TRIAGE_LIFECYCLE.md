# Automated Triage Lifecycle

## Purpose
Prevent noise from contaminating CANON while allowing high-volume capture.

## Capture Model
- All incoming material is stored as immutable blobs:
  /RAW/captures/<timestamp>-<hash>.md

## Scanner Bias
Bias for deletion. Survival requires ALL:
- Falsifiability (MPL-expressible)
- Novelty (non-derivative vs CANON/PROTOCOLS)
- Liability acceptance (budget debit acknowledged)

## Outcomes
- FAIL → archive with termination code
- UNCERTAIN → QUARANTINE
- PASS → manual human promotion only

## Permissions
Automation may:
- READ: /RAW /01_CANON /02_PROTOCOLS
- WRITE: /RAW/archive /QUARANTINE

Automation is FORBIDDEN from writing to:
- /01_CANON
- /02_PROTOCOLS
- /03_DIAGNOSTICS
