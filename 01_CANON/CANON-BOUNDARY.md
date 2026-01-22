# CANON-BOUNDARY — SURVIVOR vs DESIGN

This document defines the enforced boundary between implemented, falsified systems
(SURVIVOR) and speculative or unproven architectures (DESIGN).

This boundary is canonical and binding.

No claim may cross this boundary without a demonstrated, adversarially tested implementation.

---

## 1. DEFINITIONS

### SURVIVOR
A system or component is classified as SURVIVOR if and only if:

1. It exists as running code
2. It enforces fail-closed behavior under real economic or operational cost
3. It produces forensic artifacts on both success and refusal
4. It has survived at least one hostile falsification attempt
5. Its maximum operating domain and scale are explicitly bounded

### DESIGN
A system or component is classified as DESIGN if any of the following are true:

- It exists only as documentation, diagrams, or specifications
- It depends on external legal, economic, or hardware conditions not yet present
- It has not incurred real-world cost when failing
- Its failure modes have not been adversarially exercised

DESIGN components may be explored but must not be represented as operational.

---

## 2. CURRENT SURVIVORS (AS OF COMMIT)

The following systems are classified as SURVIVOR:

- VK-01 statutory audit system (MAS enforcement, payment boundary, checksum integrity)
- Tessrax validator engine with explicit invariants
- Procedural topology constraint solver
- Fail-closed validation pipelines with forensic receipts

These systems are:
- Domain-bounded
- Human-grounded
- Economically exposed
- Safe to ship within their stated scope

---

## 3. CURRENT DESIGN COMPONENTS

The following are explicitly DESIGN and NOT operational:

- Global Public Truth Ledger (PTL)
- Continuous R-vector telemetry
- MVH-01 hardware identity layer
- Cross-domain invariant enforcement
- Emergency override governance frameworks
- AI alignment or ASI governance claims

Any representation of these as solved or deployed is incorrect.

---

## 4. PROHIBITED CLAIMS

The following claims are explicitly disallowed:

- “This system solves AI alignment”
- “Fail-closed governance scales globally without tradeoffs”
- “Safety is binary at institutional scale”
- “Emergency overrides are solved”

Violation of this section constitutes diagnostic theater.

---

## 5. PROMOTION RULE

A DESIGN component may be promoted to SURVIVOR only if:

1. A concrete implementation exists
2. A falsification protocol has been run
3. At least one kill condition has been triggered or narrowly avoided
4. The maximum safe operating boundary is documented

Absent all four, promotion is forbidden.

---

## 6. CANONICAL STATUS

This document is CANON.
It overrides diagrams, README language, blog posts, and presentations.

If this document conflicts with any other description, this document wins.
