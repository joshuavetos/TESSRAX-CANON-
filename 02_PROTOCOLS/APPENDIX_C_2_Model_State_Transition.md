# Appendix C.2 — Model State Transition Diagram (v3.0)

TELEMETRY (30d)
    |
    | breach_count = 1
    v
EVIDENTIARY (180d)
    |
    | breach_count >= 2
    v
CHRONIC (Indefinite)
    |
    | forensic_logging_fails
    v
HALT (Sev-1)

Rehabilitation Path:
CHRONIC
    |
    | 12m zero breaches + external audit + board certification
    v
EVIDENTIARY
