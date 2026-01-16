SECURITY POLICY

TESSRAX is an enforcement and governance repository.
This document defines what constitutes a security issue and how it is handled.

--------------------------------------------------

WHAT COUNTS AS A SECURITY ISSUE

A valid security issue is any defect that:

- Allows bypass of a fail-closed condition
- Permits execution to proceed when a halt is required
- Corrupts or suppresses diagnostic evidence
- Allows silent mutation of canonized behavior
- Produces inconsistent or non-reconstructable outputs

--------------------------------------------------

WHAT DOES NOT COUNT

The following are NOT security issues:

- Philosophical disagreement
- Requests for additional features
- Performance complaints
- Claims that enforcement is “too strict”
- Absence of convenience, UX, or flexibility
- Disagreement with refusal semantics

--------------------------------------------------

REPORTING

Security issues must include:

- Exact reproduction steps
- Input artifacts
- Observed output
- Expected fail-closed behavior
- A clear explanation of the violation

Issues without reproduction artifacts will be ignored.

--------------------------------------------------

GUARANTEES

This repository provides NO guarantees beyond those explicitly defined
in executable contracts and diagnostics.

All enforcement logic is provided AS-IS, without warranty.

--------------------------------------------------

END SECURITY POLICY
