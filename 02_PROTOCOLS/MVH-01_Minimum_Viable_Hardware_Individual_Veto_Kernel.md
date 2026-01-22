MODE: ARTIFACT
SPEC: MVH-01 — MINIMUM VIABLE HARDWARE (INDIVIDUAL VETO KERNEL)
STATUS: CANON-ADJACENT / DEPLOYMENT-GRADE
AUTHORITY: FAIL-CLOSED GOVERNANCE
VERSION: 1.0
DATE: 2026-01-22

0. PURPOSE

MVH-01 defines the Minimum Viable Hardware required to instantiate the Individual Financial Shield as a physically enforced veto kernel. It is the non-bypassable consent and refusal layer that prevents institutions, algorithms, or courts from routing around an individual’s fail-closed protections.

MVH-01 is not a convenience device.
It is a physical choke point.

If MVH-01 does not sign, the world does not proceed.

1. CORE ROLE — THE PHYSICAL VETO

MVH-01 is the only entity authorized to mint or countersign Capability Tokens (CT) on behalf of the individual.

No CT → No execution.
No execution → No liability.

The MVH enforces the following absolute rule:

Authority, capability, and execution are permitted ONLY when independent reality vectors converge.
On ambiguity, staleness, or missing proof → HALT.

2. POSITION IN THE ARCHITECTURE

MVH-01 sits between the individual and all external claimants.

All inbound requests (financial, legal, administrative) must pass through the MVH before reaching the individual’s assets, identity, or telemetry.

The MVH performs three functions:
• Verifies institutional authority via the Public Truth Ledger (PTL)
• Verifies local reality vectors (income, residence, status)
• Enforces explicit, physical consent from the individual

The MVH never trusts narratives.
It only evaluates proofs.

3. CAPABILITY TOKEN SIGNING RULES

A Capability Token (CT) may be signed IFF all of the following are true:

• Local invariants are satisfied
• Individual state is VALID
• Requesting agency has sufficient Authority Score (AAS) from the PTL
• Physical presence is confirmed

If any check fails, the MVH emits a HALT_SIGNAL and no token is minted.

4. MVH ⇄ PUBLIC TRUTH LEDGER HANDSHAKE

Before evaluating any external request, the MVH performs a one-way pull from the PTL.

The MVH never accepts authority claims directly from agencies.

Required PTL attestation fields:
• agency_id
• domain
• aas_current
• status
• nullification_reason
• last_valid_receipt
• ptl_signature
• timestamp

Enforcement logic:
effective_authority = min(local_invariants, individual_state, aas_current)

Decision thresholds:
• AAS ≥ 0.9 → Normal evaluation
• 0.7 ≤ AAS < 0.9 → DEGRADED (no new liabilities)
• AAS < 0.7 → NULL (all requests refused)

Any attempt to bypass the PTL triggers a BYPASS_ATTEMPT_SCAR and an automatic AAS penalty.

5. FAIL-CLOSED DEFAULTS

The MVH is fail-closed by design.

• Missing data = failure
• Stale data = failure
• Opaque data = failure
• Probabilistic claims = failure

Silence is success.
Refusal is safety.

6. LOSS, THEFT, AND DESTRUCTION RECOVERY CEREMONY

Sovereignty implies irreversibility.
Recovery must be slower than abuse.

Event classifications:
• Lost MVH — Recoverable (high friction)
• Stolen MVH — Recoverable with coercion checks
• Destroyed MVH — Identity extinction
• Compromised MVH — Forced extinction

Recovery process (loss or theft only):

Phase 0 — Global Freeze
• All new CTs refused
• All agencies receive HALT
• Existing A3 survival buffers continue only

Phase 1 — Time Lock
• Mandatory delay: 21–45 days

Phase 2 — Multi-Vector Reconstitution
• Physical re-presence
• Cross-domain receipt consistency
• PTL confirmation of no parallel MVH

Phase 3 — Scarred Re-Issuance
• New root key issued
• Old root key permanently revoked
• Reconstitution scar published to PTL

If MVH is destroyed or compromised:
• Identity does not recover
• All prior claims enter TERMINAL_CLEAR
• New identity begins with public scars

7. SCARS AND FORENSIC EXHAUST

Every exceptional event emits an append-only scar.

Examples:
• BYPASS_ATTEMPT_SCAR
• IDENTITY_RECONSTITUTED
• AUTHORITY_REFUSAL
• GLOBAL_FREEZE

Scars are permanent facts, not logs.
They are non-erasable and publicly auditable.

8. HARDWARE BILL OF MATERIALS (BOM)

Design principle:
Assume the vendor is hostile.

Mandatory components:
• Secure Element (TPM 2.0 or equivalent)
• Non-exportable private keys
• Hardware monotonic counter
• Independent, battery-backed clock
• Physical presence interface (touch, mechanical, or local biometric)

Forbidden components:
• Always-on wireless radios
• Remote management controllers
• Cloud-bound identity chips
• Writable external storage
• Proprietary opaque firmware

Acceptable form factors:
• USB-C hardware key
• Smartcard with display
• Air-gapped handheld signer

Phones do not qualify unless paired with external secure hardware.

All designs must publish:
• Full schematics
• Deterministic firmware builds
• Third-party reproducibility audits

Opacity is grounds for rejection.

9. NON-BYPASSABILITY GUARANTEE

No court order, emergency memo, or operational necessity can compel MVH execution.

If an override is attempted:
• MVH refuses
• Scar is emitted
• PTL penalizes the requesting authority

Power is not negotiated.
It is proven or denied.

10. TERMINAL RULE

If the MVH does not sign, the system does not proceed.
If proof cannot be reconstructed, authority does not exist.
If reality cannot be verified, execution halts.

Silence is stability.

END OF MVH-01
