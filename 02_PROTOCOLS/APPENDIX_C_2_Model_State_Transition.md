# Appendix C.2 — Model State Transition Diagram

## States
- TELEMETRY
- EVIDENTIARY
- CHRONIC
- HALT

## Transitions

TELEMETRY
→ (intervention_rate >10% once)
→ EVIDENTIARY

EVIDENTIARY
→ (intervention_rate >10% second time)
→ CHRONIC

CHRONIC
→ (forensic_logging_fails)
→ HALT

## State Properties

TELEMETRY:
- Standard deletion
- No preservation duty

EVIDENTIARY:
- 180-day forensic hold
- CFPB 2022-03 alignment

CHRONIC:
- Indefinite retention
- Presumptive unreliability
- No discretion

HALT:
- Decision engine disabled
- Sev-1 incident triggered
- No outputs permitted

## Invariant
A model may never transition backward.
State regression is forbidden.
