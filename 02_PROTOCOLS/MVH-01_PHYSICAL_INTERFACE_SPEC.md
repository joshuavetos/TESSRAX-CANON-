MODE: ARTIFACT
SPEC: MVH-01 — PHYSICAL INTERFACE SPEC (INDIVIDUAL VETO KERNEL)
STATUS: CANON-ADJACENT / DEPLOYMENT-GRADE
AUTHORITY: FAIL-CLOSED GOVERNANCE
VERSION: 1.0
DATE: 2026-01-23
SESSION: 2026-01-23-TX-CONV

0. PURPOSE

This document specifies the minimum physical/electrical/user interface required for MVH-01 to function as a non-bypassable veto chokepoint for Capability Token (CT) minting. MVH-01 is the only entity authorized to mint or countersign CTs on behalf of the individual; if MVH-01 does not sign, the world does not proceed.  [oai_citation:0‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

This is an interface spec. It defines ports, signals, user presence primitives, tamper response, and the request/response envelope at the hardware boundary. It does not define PTL economics, AAS scoring policy, or domain adapter semantics.

1. NON-NEGOTIABLE BEHAVIOR (HARD REQUIREMENTS)

1.1 Fail-Closed Defaults
- Missing data = failure
- Stale data = failure
- Opaque data = failure
- Probabilistic claims = failure
- On any check failure: emit HALT_SIGNAL; mint no token.  [oai_citation:1‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo) [oai_citation:2‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

1.2 CT Signing Rule (Gate)
CT may be signed IFF:
- Local invariants are satisfied
- Individual state is VALID
- Requesting agency has sufficient Authority Score (AAS) pulled from PTL
- Physical presence is confirmed
Else: HALT_SIGNAL and CT = NULL.  [oai_citation:3‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

1.3 No Manual Bypass
There is no “manual override” path inside MVH-01. Silence/HALT is a valid terminal success state.  [oai_citation:4‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

2. PHYSICAL FORM FACTOR (ALLOWED)

2.1 Acceptable Form Factors
At least one of:
- USB-C hardware key (hosted signer)
- Smartcard with display (reader-based)
- Air-gapped handheld signer (offline signer)  [oai_citation:5‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

2.2 Disallowed Platform
- Phones do not qualify unless paired with external secure hardware.  [oai_citation:6‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

3. PORTS, POWER, AND CONNECTIVITY

3.1 Mandatory Port Set (Minimum)
- 1× USB-C (USB 2.0 or better) for:
  - Power (bus power)
  - Data (CT signing requests / receipts)
  - Firmware load in FACTORY mode only (see §8)

3.2 Optional Port Set (If Form Factor Requires)
- 1× Contact pads (ISO 7816) for smartcard variant
- 1× Camera/QR window (displayed QR only; no camera required on MVH-01)
- 1× Passive NFC (tap-to-present) ONLY if it is non-routable and cannot receive remote commands without physical proximity

3.3 Forbidden Connectivity (Hard)
- Always-on wireless radios
- Remote management controllers
- Cloud-bound identity chips  [oai_citation:7‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

Interpretation:
- No Wi-Fi, no cellular, no Bluetooth.
- If NFC is present: it must be passive, proximity-only, and usable only as a transport for already-approved artifacts, never as a control plane.

3.4 Power
- Primary: USB-C bus power.
- Mandatory: independent, battery-backed clock subsystem (see §5.3) that maintains time and monotonicity without host power.  [oai_citation:8‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

4. USER PRESENCE INTERFACE (NON-OPTIONAL)

MVH-01 MUST require explicit physical presence to sign any CT.  [oai_citation:9‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

4.1 Presence Primitives (Choose ≥1; 2 recommended)
A) Touch-and-hold capacitive sensor (≥ 1.0s hold)
B) Mechanical button (momentary, debounced)
C) Local biometric (on-device match only; template sealed inside secure element; no export)
D) “Consent chord” (two inputs simultaneously; e.g., button + touch)

4.2 Presence Window
- Presence is sampled only inside an explicit consent window (e.g., 10 seconds) opened by rendering the request summary on-device.
- If window expires without presence: HALT_SIGNAL(reason=PRESENCE_TIMEOUT).

4.3 Anti-Coercion (Minimal)
- Long-press “panic chord” (e.g., 5s) triggers GLOBAL_FREEZE event emission and forces CT refusal for a fixed cooldown window.
- This does not prove coercion; it ensures refusal is mechanically available under duress.

5. HARDWARE ROOT OF TRUST AND CRYPTO

5.1 Secure Element (Mandatory)
- TPM 2.0 or equivalent secure element with:
  - Non-exportable private keys
  - Hardware monotonic counter
  - Secure key storage
  - Measured boot / attestation optional but permitted  [oai_citation:10‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

5.2 Keys
- Root signing key: K_root (non-exportable)
- Device identity key: K_dev (non-exportable; used for attestation)
- Optional witness quorum keys are NOT stored on MVH-01; MVH-01 consumes witness proofs as inputs.

5.3 Time and Monotonicity (Mandatory)
- Independent, battery-backed clock + monotonic counter.
- MVH-01 maintains:
  - t_now (secure time)
  - ctr (monotonic counter)
  - last_nonce (monotonic anti-replay)
- Any time rollback, counter rollback, or nonce regression: HALT_SIGNAL(reason=TIME_ROLLBACK) and SCAR emission.

6. DISPLAY AND REQUEST SUMMARIZATION (HUMAN-READABLE, MINIMUM)

6.1 Display Requirements (Minimum)
One of:
- E-ink / OLED microdisplay on device
- LED + paired host display with on-device confirm code
- For smartcard: reader display is acceptable only if MVH-01 renders an on-device confirm code that the user verifies (prevents “host lies”)

6.2 What Must Be Shown Before Consent
- Requesting agency_id + domain
- PTL AAS band (≥0.9 / 0.7–0.9 / <0.7)
- Requested capability scope (short label)
- Liability direction (NEW_LIABILITY allowed? yes/no)
- Freshness age (seconds since PTL attestation timestamp)
- A one-line outcome: “SIGN CT” or “HALT”

7. MVH ⇄ PTL HANDSHAKE INPUT CONTRACT (AUTHORITY INGEST)

Before evaluating any external request, MVH-01 performs a one-way pull from PTL; it never accepts authority claims directly from agencies.  [oai_citation:11‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

7.1 Required PTL Attestation Fields (Input)
- agency_id
- domain
- aas_current
- status
- nullification_reason
- last_valid_receipt
- ptl_signature
- timestamp  [oai_citation:12‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

7.2 Authority Threshold Behavior
- AAS ≥ 0.9 → Normal evaluation allowed
- 0.7 ≤ AAS < 0.9 → DEGRADED (no new liabilities)
- AAS < 0.7 → NULL (refuse all requests)  [oai_citation:13‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

Any attempt to bypass PTL triggers BYPASS_ATTEMPT_SCAR and automatic AAS penalty (policy executed by PTL, not MVH-01).  [oai_citation:14‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

8. DATA PLANE: SIGNING REQUEST / RESPONSE (HARDWARE BOUNDARY)

8.1 Transport
- USB HID or USB CDC-ACM (serial) recommended.
- All requests are length-bounded, single-shot, and require explicit user presence per request.

8.2 Message Encoding
- Canonical JSON (deterministic field ordering) OR CBOR with canonical encoding.
- All messages include:
  - schema_version
  - msg_type
  - device_id
  - ctr
  - timestamp_utc
  - payload
  - signature (where applicable)

8.3 SIGN_REQUEST (Host → MVH-01)
Fields (minimum):
- schema_version: "MVH-PI-1.0"
- msg_type: "SIGN_REQUEST"
- request_id: UUID
- ptl_attestation: object (per §7.1)
- requested_scope: string
- local_vectors_snapshot: object (income/residence/status proofs as hashes or pointers)
- invariants_digest: hash (local invariant set hash)
- individual_state: "VALID" | "DEGRADED" | "VOID" | "HALT"
- nonce: uint64 (monotonic; host-proposed)
- prev_state: string (for state binding)
- mas_window_s: int (maximum allowable staleness window for this request)
- host_context_hash: hash (prevents UI swap attacks)

8.4 SIGN_RESPONSE (MVH-01 → Host)
Case A: Approved
- msg_type: "SIGN_RESPONSE"
- decision: "SIGNED"
- ct: object
  - ct_id
  - agency_id
  - domain
  - scope
  - nonce
  - issued_at
  - expires_at
  - effective_authority = min(local_invariants, individual_state, aas_current)  [oai_citation:15‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)
  - vectors_snapshot_hash
  - ptl_attestation_hash
  - mvh_device_attestation (optional)
- signature: Sig(K_root, ct_hash)

Case B: Refused
- msg_type: "SIGN_RESPONSE"
- decision: "HALT"
- halt_reason_code: enum
- halt_reason_detail: string (bounded)
- receipt_min_fields:
  - event
  - address_key (if applicable)
  - vectors_snapshot
  - thresholds
  - decision
  - reason
  - timestamp  [oai_citation:16‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

8.5 HALT_REASON_CODE (Minimum Enum)
- PTL_MISSING
- PTL_SIG_INVALID
- PTL_STALE
- AAS_NULL
- AAS_DEGRADED_NO_NEW_LIABILITY
- PRESENCE_MISSING
- PRESENCE_TIMEOUT
- INVARIANT_FAIL
- NONCE_REPLAY
- TIME_ROLLBACK
- TAMPER_DETECTED
- STORAGE_CORRUPT
- UNSUPPORTED_SCOPE

9. TAMPER RESPONSE AND FORENSIC EXHAUST

9.1 Tamper Detection (Minimum)
Any of:
- Case-open switch
- Light sensor (enclosure breach)
- Voltage/fault injection detector in secure element
- Temperature anomaly thresholds

9.2 Tamper Response (Hard)
On tamper detection:
- Zeroize volatile secrets immediately.
- Permanently revoke K_root via secure element policy if supported; otherwise render device TERMINAL_IDLE (no signing forever).
- Emit SCAR: "TAMPER_EVENT" with immutable receipt fields.

9.3 Forensic Exhaust (Non-Optional)
Every decision emits an immutable receipt; refusal is evidence; HALT is logged as intentional.  [oai_citation:17‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

10. LOSS / THEFT / DESTRUCTION RECOVERY CEREMONY (INTERFACE IMPLICATIONS)

Event classifications:
- Lost MVH — recoverable (high friction)
- Stolen MVH — recoverable with coercion checks
- Destroyed MVH — identity extinction
- Compromised MVH — forced extinction  [oai_citation:18‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

Recovery process (loss/theft only):
- Phase 0: Global Freeze (no new CTs; agencies receive HALT; A3 survival buffers only)
- Phase 1: Time Lock (mandatory delay 21–45 days)
- Phase 2: Multi-Vector Reconstitution (physical re-presence; cross-domain receipt consistency; PTL confirmation of no parallel MVH)
- Phase 3: Scarred Re-Issuance (new root key; old key revoked; reconstitution scar published)  [oai_citation:19‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

Interface requirements to support recovery:
- MVH-01 must expose a RECOVERY_MODE entry that:
  - refuses CT signing unconditionally
  - allows only identity reconstitution ceremony messages
  - requires multi-step physical presence (two-factor on-device actions)
  - rate-limits attempts
  - emits scars on repeated failure

11. FORBIDDEN STORAGE AND FIRMWARE PRACTICES

11.1 Forbidden Components (Hard)
- Writable external storage
- Proprietary opaque firmware  [oai_citation:20‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

11.2 Required Publication (For Any Shipping Design)
- Full schematics
- Deterministic firmware builds
- Third-party reproducibility audits  [oai_citation:21‡Tessrax.md](file-service://file-NYi6yYBTYFBXbUAmq4eiFo)

12. SCOPE BOUNDARY (THIS SPEC DOES NOT COVER)

- PTL network protocol details (endpoints, witness quorum transport, consensus)
- AAS scoring algorithm or penalties (policy belongs to PTL)
- Domain-specific adapter logic (medical, housing, student aid, etc.)
- Legal packaging, jurisdictional hooks, or compliance claims
- Manufacturing test plans beyond “FACTORY mode” gating

13. KNOWN COMPROMISES (EXPLICIT)

- This spec defines “minimum” interface requirements but does not select a single presence primitive or enclosure design; multiple allowed implementations exist.
- Anti-coercion is limited to a mechanical refusal pathway (panic chord + freeze); it cannot prove duress.
- “Passive NFC optional” is allowed only under strict constraints; if implementation risk is non-zero, omit NFC entirely.
- Display-trust is not fully solved in hosted signer variants; confirm-code verification is the minimum mitigation.

END OF SPEC — WRITE-LOCKED (SESSION COMMIT)
