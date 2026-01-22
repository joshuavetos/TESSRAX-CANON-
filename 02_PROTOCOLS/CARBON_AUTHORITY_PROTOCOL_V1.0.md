CARBON_AUTHORITY_PROTOCOL_V1.0

Status: ARCHITECTURAL CONVERGENCE / WRITE-LOCKED
Mode: Fail-Closed / Verification-Linked
Principle: Physics-First Enforcement (Reality > Authority > Humans)

⸻

0. PURPOSE

This protocol defines a deterministic, fail-closed system for treating carbon credits not as financial instruments, but as Physical State Claims (PSC) bound to real-world, observable, and exclusive physical reality.

The system is explicitly designed to eliminate:
   •   Phantom credits
   •   Double-counting
   •   Temporal laundering
   •   Zombie offsets
   •   Narrative-based neutrality claims

If reality cannot be verified, authority halts.
If authority conflicts with reality, authority loses.

⸻

1. CORE PRIMITIVE — THE CARBON TOKEN (C_CO2)

A Carbon Token represents a claim that a specific quantity of CO₂e is sequestered in a specific physical location for a bounded period of time.

A token is valid if and only if all three verification vectors are present, current, and above threshold.

1.1 Verification Vectors
   •   G — Geo-Physical Grounding
Real-time or near-real-time sensor or satellite data proving biomass or capture presence.
   •   P — Permanence Score
A decaying probability that the carbon remains sequestered.
P is class-specific and time-dependent.
   •   A — Authority Chain
A verifiable, ordered chain of custody from physical origin to final retire-er.

Fail-Closed Rule:
If G, P, or A is NULL, stale, or below threshold → token state becomes REJECTED or VOID.

⸻

2. TOKEN LIFECYCLE — STATE MACHINE

Carbon Tokens are live objects governed by continuous verification.

State	Condition	System Action
PROPOSED	G not yet verified	GATED — No sale permitted
ACTIVE	G verified + A valid	COMMIT — Transferable
DEGRADED	Fire detected, telemetry missing, or MAS exceeded	HALT — Trading frozen
EXPIRED	TTL exceeded or P below threshold	VOID — Removed from registry

2.1 Exclusive Addressability (Hard Rule)

Each Carbon Token is bound to a unique ADDR_KEY:
   •   WGS84 grid cell (e.g., 30m × 30m)
   •   Facility Batch ID (DAC)
   •   Soil polygon + depth range

Invariant:
A single ADDR_KEY may host only one ACTIVE token at any time.

Overlap → Conflict → HALT.

⸻

3. TEMPORAL DECAY — THE FIRE WALL

Carbon sequestration is treated as a time-bound lease on a physical state, not a permanent asset.

3.1 Oracle Intercept

If satellite or sensor telemetry detects:
   •   Biomass loss
   •   NDVI drop
   •   Capture interruption

Then:
   •   G is reduced immediately
   •   Token transitions to DEGRADED or VOID
   •   Trading is frozen or reversed

3.2 Immediate Devaluation

If G falls below the committed biomass or capture threshold:
   •   Token is AUTO-REVOKED
   •   Buyer balance flips to DEFICIT
   •   Regulator-visible forensic receipt is emitted

⸻

4. AUTHORITY HIERARCHY — JURISDICTION LOCK

To prevent self-verification and narrative laundering, authority is strictly ordered.

Tier	Authority	Notes
Tier 0	Physical Reality	Sensors / satellites — overrides all
Tier 1	Regulator	National / international bodies
Tier 2	Project	Developer / operator
Tier 3	Buyer	Offset holder

Rule:
Lower tiers may never override higher tiers.
Reality (Tier 0) overrides all human claims.

⸻

5. VERIFICATION MATRIX — CLASS-SPECIFIC GATING

Verification parameters vary by carbon class.

Feature	Forest (Tropical)	Direct Air Capture (DAC)	Soil Carbon
Primary Sensor	Sentinel-1 (SAR)	Flow metering	Physical sampling
MAS (Staleness)	7 days	1 hour	12 months
P_min	0.80	0.98	0.60
Spatial Lock	30m grid cell	Facility / batch ID	Field polygon + depth

5.1 INV-0 — Staleness Invariant

If telemetry exceeds MAS:
   •   Token transitions to DEGRADED
   •   Trading is halted
   •   Forensic receipt is emitted

No data = No credit.

⸻

6. CONFLICT ENGINE — EXCLUSIVE ADDRESSABILITY

Invariant INV-DC-1:
Physical carbon may be claimed once and only once.

6.1 Spatial Intersection Rule

If:

Polygon_A ∩ Polygon_B > 0

Then:
   •   Incoming token is REJECTED
   •   Existing address lock is preserved

Depth-segmented claims are allowed only if explicitly non-overlapping.

6.2 Collision Resolution Table

Existing Token	Incoming Token	System Response	Forensic Action
ACTIVE	PROPOSED	REJECT	DOUBLE_COUNT_CONFLICT
DEGRADED	PROPOSED	REJECT	MAINTAIN_LOCK
EXPIRED	PROPOSED	ALLOW	REISSUE
VOID	PROPOSED	ALLOW	CLEAN_SLATE

6.3 Quarantine State — INV-DC-2

After a VOID event:
   •   ADDR_KEY enters QUARANTINED
   •   Prevents arson-to-profit cycles
   •   Only Tier-1 Regulator may lift quarantine

⸻

7. DEFICIT PROTOCOL — POST-VOID LIABILITY

When a token is VOIDED after being used to offset emissions, a Carbon Debt is created.

7.1 Liability Propagation
   •   Neutrality claim → INVALID
   •   Ledger debited exact CO₂e mass
   •   Entity enters DEFICIT state

7.2 Enforcement Actions
   •   Public deficit broadcast
   •   Trading privileges suspended
   •   Mandatory replacement with high-permanence class (e.g., DAC), if contractually bound

7.3 Forensic Receipt — liability_breach.json

{
  "event": "LIABILITY_BREACH",
  "owner_id": "CORP_GENERIC_99",
  "voided_token": "CARBON-AMZ-7742",
  "mass_co2e": "1000mt",
  "current_balance": "-1000mt",
  "compliance_status": "NON_COMPLIANT",
  "remediation_required": "IMMEDIATE_REPLACEMENT"
}


⸻

8. FORENSIC RECEIPTS (NON-OPTIONAL)

All state transitions emit immutable, machine-decidable artifacts, including but not limited to:
   •   climate_audit.json
   •   double_count.json
   •   liability_breach.json
   •   staleness_event.json

Receipts are authoritative facts, not logs.

⸻

9. TERMINAL CANON STATEMENT

This protocol defines a closed, deterministic system.

There are no discretionary overrides.
There are no narrative escape hatches.
There is no “probably fine” state.

If verification fails → HALT.
If exclusivity fails → REJECT.
If reality changes → REVERSE.

Silence is enforcement.

⸻

END OF FILE — WRITE-LOCKED
