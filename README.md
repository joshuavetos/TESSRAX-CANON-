<img width="1536" height="1024" alt="B383BCEA-33E9-49F4-83CC-07CFA179C1C1" src="https://github.com/user-attachments/assets/a89418e7-ab97-426e-8c3f-2e268af3cbae" />

# TESSRAX-CANON-

**Enforcement-first governance.**  
Fail-closed systems.  
Human reconstructability under failure.

---

## What this repository is

TESSRAX is a governance and safety repository focused on **epistemic integrity under real failure conditions**.

This is not a collection of ideas.  
It is a collection of **mechanisms** that continue to function when systems are stressed, interrupted, or misused.

If a system cannot be halted, audited, and reconstructed by a human, it is already failed.

---

## What runs here

This repository contains **live enforcement artifacts**, not speculative frameworks:

- Deterministic claim validation
- Fail-closed execution logic
- Append-only forensic receipts
- Diagnostics that surface failure modes
- Infrastructure designed to stop safely (including Kubernetes enforcement paths)

Where executable code, contracts, or diagnostics exist, **they override prose**.

Explanation is secondary.  
Enforcement is authoritative.

---

## Core invariants

TESSRAX operates under non-negotiable constraints:

- Truth must be reconstructable using offline artifacts
- Silence, refusal, and HALT are valid success states
- Governance without enforceable refusal is meaningless
- All non-trivial claims incur liability and must produce evidence

If an invariant cannot be enforced mechanically, it is not admitted.

---

## Verification & usage

The reference enforcement engine lives in `engine/`.

It evaluates claims against artifacts using fail-closed logic defined in canon.

Example execution:

    python -m engine.main <claim_path> <artifact_path>

Expected output is a machine-readable receipt with an explicit verdict and failure surface.

Diagnostics live in `03_DIAGNOSTICS/` and are designed to prove:
- No hidden state mutation
- No silent degradation
- No narrative override of enforcement

---

## Repository structure

Numbering reflects **authority**, not chronology:

- `00_README/` — identity and entrypoints
- `01_CANON/` — binding invariants and laws
- `02_PROTOCOLS/` — executable governance mechanisms
- `03_DIAGNOSTICS/` — tests, audits, receipts
- `04_CASES/` — adversarial and applied analyses
- `05_LOGS/` — append-only forensic records

Folders outside this structure are non-authoritative unless explicitly canonized.

---

## Execution philosophy

This repository does not optimize for:

- Persuasion
- Onboarding
- Narrative clarity
- Outcome smoothing

It optimizes for:

- Auditability
- Determinism
- Failure visibility
- Human reconstruction

If this repository cannot be understood after failure, it has failed.

---

## Authority

Where code, schemas, diagnostics, and contracts exist, **they govern**.

If documentation and enforcement disagree:
- enforcement stands
- documentation is invalid until corrected

---

## Repository status

As of v0.1.0:

- Canonical invariants are frozen
- Enforcement semantics are locked
- Behavioral changes require versioned proof of non-regression

Incremental or “helpful” modification without receipts is treated as corruption.

See `CONTRIBUTING.md` for strict change-control rules.

---

## License

MIT License. See `LICENSE`.
