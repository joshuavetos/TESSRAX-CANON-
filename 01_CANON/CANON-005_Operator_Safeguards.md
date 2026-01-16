# CANON-005 — Operator Safeguards for Chronic Systems

## Rationale
Forensic retention regimes introduce secondary human risk. Operator safeguards are required to prevent the weaponization of safety infrastructure against human operators.

## Burnout Circuit-Breaker
No operator (SRE, SOC, or equivalent) may be assigned primary responsibility for a CHRONIC model for more than **90 consecutive days**. Mandatory rotation is required.

## Anti-Repurposing Clause
Forensic artifacts generated under CANON-004 may not be used for:
- Performance improvement plans (PIPs)
- Promotion or compensation decisions
- Termination rationale

Exception: documented criminal intent.

## Query Provenance
All access to Category 1 (indefinite retention) forensic artifacts must record:
- Requester identity
- Stated purpose
- Timestamp
- Dual sign-off (SRE + Compliance)

## Right of Refusal
Operators retain the right to refuse operation of a CHRONIC model if:
- The Decision Engine Halt Rule is bypassed, or
- Forensic logging integrity is degraded

Such refusal constitutes protected safety activity.

## Enforcement
Violation of operator safeguards triggers an immediate governance audit.
