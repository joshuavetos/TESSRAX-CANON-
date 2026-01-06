# EVIDENCE ENGINE SPEC
Version: v1.0
Status: ACTIVE
Authority: CANON-003_Claim_Economy

## PURPOSE
The Evidence Engine binds every CLAIM to immutable, inspectable proof.
A claim without evidence is treated as UNADJUDICATED and may not be promoted,
relied upon, or used as a dependency.

This eliminates “claims about claims” and prevents vibe-based canonization.

---

## CORE PRINCIPLE

> A Claim PASSES only if its Evidence Pointer resolves to immutable data
> that independently verifies the predicate.

---

## EVIDENCE OBJECT MODEL

Every Claim MAY reference zero or more Evidence Objects.

Each Evidence Object MUST:

- Be immutable after creation
- Be content-addressed (hash-based)
- Live under `/03_DIAGNOSTICS/`
- Be human-inspectable without tooling magic

---

## DIRECTORY STRUCTURE

/03_DIAGNOSTICS/
├── evidence/
│   ├── <CLAIM_ID>/
│   │   ├── <timestamp>-<sha256>.md
│   │   ├── <timestamp>-<sha256>.png
│   │   └── <timestamp>-<sha256>.log
│   └── index.md

Automation MAY write here.
Automation MAY NOT modify or delete existing evidence.

---

## EVIDENCE POINTER FORMAT (REQUIRED)

Any Claim referencing evidence MUST include:

EVIDENCE:
- path: /03_DIAGNOSTICS/evidence/<CLAIM_ID>/<file>
- sha256: <hash>
- type: {log | document | image | receipt | transcript}
- provenance: {human | tool | system}

Claims without valid Evidence blocks:
→ STATUS = UNADJUDICATED
→ NOT ELIGIBLE FOR PASS
→ NOT ELIGIBLE AS DEPENDENCY

---

## ADJUDICATION RULES

A Claim may transition:
PENDING → PASSED
ONLY IF:

1. Predicate is machine-checkable
2. Evidence pointer resolves
3. Hash matches
4. Evidence provenance is declared

If evidence is missing, altered, or ambiguous:
→ STATUS = FAILED
→ Penalties apply per Budget Arithmetic

---

## FAILURE MODES PREVENTED

- Vibe-based validation
- Retroactive justification
- “Trust me” claims
- Model self-certification
- Evidence laundering

---

## CANONICAL BINDING

BIND: sys.claim.evidence_binding.v1  
PREDICATE: FORALL claim WHERE status == PASSED :
           EXISTS evidence_pointer(claim) == TRUE  
TIER: Structural  
DEPENDENCIES:
- CANON-003_Claim_Economy.md
- 02_PROTOCOLS/BUDGET_ARITHMETIC_SPEC.md

---

## NOTES

Evidence is not truth.
Evidence is *cost*.

If you don’t want to pay the cost of proof,
you don’t get to keep the claim.
