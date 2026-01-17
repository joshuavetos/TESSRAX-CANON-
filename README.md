```markdown
# TESSRAX-CANON-

[![Status](https://img.shields.io/badge/Status-FROZEN-red)]() [![License](https://img.shields.io/badge/License-MIT-blue)]() [![Engine](https://img.shields.io/badge/Engine-v0.1.0-green)]()

**TESSRAX** is a governance and safety research repository focused on *epistemic integrity*, *fail-closed systems*, and *human reconstructability under failure*.

This repository exists to prevent:
- Narrative maintenance masquerading as governance
- Automation-induced atrophy of truth
- Systems that cannot be halted, audited, or reconstructed by humans

This is not a speculative or persuasive project. **It is an enforcement-first repository.**

---

## Table of Contents
- [Core Invariants](#core-invariants)
- [Verification & Usage](#verification--usage)
- [Operational Scope](#operational-scope)
- [Claim Economy](#claim-economy)
- [Repository Structure](#repository-structure)
- [Execution Philosophy](#execution-philosophy)
- [Authority](#authority)
- [Repository Status](#repository-status)
- [License](#license)

---

## Core Invariants

TESSRAX operates under the following non-negotiable invariants:

- Truth must be reconstructable by humans using offline artifacts
- Any system that cannot survive interruption is already failed
- Silence, refusal, and HALT are valid success states
- Governance without enforceable refusal is meaningless
- **All non-trivial claims incur liability and must produce evidence**

If an invariant cannot be enforced mechanically, it is not admitted.

---

## Verification & Usage

The repository contains a reference implementation of the **Tessrax Engine** (v0.1.0) located in `engine/`. This engine is the executable enforcement mechanism for the invariants defined in `01_CANON`.

### 1. Setup
Ensure you have Python 3.x installed.
```bash
# Install dependencies (if any are listed in pyproject.toml requirements)
pip install -r requirements.txt

```

### 2. Running the Engine

The engine accepts a Claim and an Artifact, enforcing the *Fail-Closed* logic defined in `ENGINE_CONTRACT.md`.

**Command Pattern:**

```bash
python -m engine.main <claim_path> <artifact_path>

```

**Example (Passing Scenario):**

```bash
python -m engine.main examples/pass.claim.json examples/pass.artifact.json

```

*Expected Output:* JSON receipt with `verdict: PASS`.

**Example (Rejection Scenario):**

```bash
python -m engine.main examples/nerf.claim.json examples/nerf.artifact.json

```

*Expected Output:* JSON receipt with `verdict: NERF` and violation details.

### 3. System Audit

To verify the integrity of the engine and ensuring no file mutations occur during execution, run the diagnostic suite:

```bash
python -m unittest 03_DIAGNOSTICS/tests/test_validator.py

```

---

## Operational Scope

This repository contains **both research artifacts and live governance mechanisms**.

Where a domain is canonized as closed-world, the repository does not:

* speculate
* persuade
* optimize outcomes
* explore alternatives

It defines only:

* admissible execution surfaces
* governing invariants
* executable schemas that enforce them

Applied systems in this repository (including claimant-addressable liability discovery mechanisms) are governed by the same fail-closed rules as the research itself.

If a mechanism cannot be made:

* deterministic
* auditable
* haltable

it is excluded rather than approximated.

---

## Claim Economy

This repository operates under a strict **Claim Economy**:

* Speech creates obligations
* Claims must be falsifiable
* Failed claims reduce capability
* Unproven claims cannot be canonized
* Evidence is mandatory for adjudication

Language without liability is treated as a system failure.

---

## Repository Structure

This repository is intentionally structured and numbered.
Numbering reflects authority, not chronology.

* `00_README/` — identity, entrypoints, and framing artifacts
* `01_CANON/` — binding invariants and laws (non-derivable)
* `02_PROTOCOLS/` — executable governance mechanisms
* `03_DIAGNOSTICS/` — tests, audits, schemas, and receipts that expose failure
* `04_CASES/` — applied analyses and adversarial examples
* `05_LOGS/` — append-only ledgers and forensic records

Folders outside this structure are considered non-authoritative unless explicitly canonized.

---

## Execution Philosophy

This repository does not optimize for:

* readability
* persuasion
* onboarding
* completeness

It optimizes for:

* auditability
* reproducibility
* failure visibility

If this repository becomes unreadable on paper, it has failed.
If a claim cannot be proven using artifacts contained here, it is not true here.

---

## Authority

Where executable code, schemas, diagnostics, and contracts exist, they override prose.

If documentation and enforcement disagree:

* enforcement governs
* documentation must be updated or treated as invalid

All enforcement logic is provided AS-IS, without warranty or implied fitness.

---

## Repository Status

This repository is **enforcement-bound**.

As of **v0.1.0**, all executable governance mechanisms, schemas, and enforcement semantics are considered **FROZEN**.

Behavioral changes require:

* explicit version increments
* updated diagnostics proving non-regression
* contract updates where applicable

Incremental or "helpful" modification without proof is treated as corruption, not progress.

See `CONTRIBUTING.md` for strict adherence protocols.

---

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

```

```
