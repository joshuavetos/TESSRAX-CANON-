# ER_BAY_V1.3 — The Kinetic Sorting Node

## Authority Level
02_PROTOCOLS — Executable Governance Design  
Status: Stable / Stress-Tested (Mass Casualty Simulation)

## Purpose
The ER Bay is not a room.  
It is a **docking station** whose sole function is to convert **Chaos (Unknown Patient State)** into **Data (Diagnosed / Routed State)** with minimum time, minimum discretion, and controlled failure.

This protocol embeds governance into geometry so that correct action occurs **without judgment** under overload.

---

## Core Design Principles

1. **No Shuffle**
   Eliminate patient lifting, bed transfers, and redundant motion during intake.

2. **Role Separation by Geometry**
   Prevent collision between staff, patients, visitors, EMS, and security using physical boundaries rather than policy.

3. **Fail-Soft Scaling**
   System must degrade linearly under surge, not collapse into improvisation.

4. **Liability Visibility**
   All high-risk transitions (intake, restraint, contraband, escalation) must leave an auditable spatial trace.

---

## System Components

### 1. Universal Docking Bay
- Accepts both EMS stretchers and internal Dock-Cots.
- Floor-embedded latch integrates:
  - patient weight
  - vitals
  - monitoring
- **No hospital bed present.**
- Patient remains docked until disposition is determined.

### 2. Swap-Deck Protocol (V1.3 Patch)
- Each bay contains a folded internal Dock-Cot.
- EMS arrival → 10-second slide transfer → EMS stretcher released.
- Prevents ambulance fleet paralysis during surge.

### 3. CT-Adjacent Bays (1–4)
- Rear pass-through doors connect directly to CT control corridor.
- No public hallway exposure.
- Imaging comes to the bay, not the patient.

### 4. Impact / Bio Shielding
- Retractable polycarbonate walls.
- States:
  - **Open:** full visibility
  - **Lockdown:** spit / impact / sound isolation
- HVAC isolation via negative pressure (standard).

### 5. Gated Ambient Capture
- Audio capture is **OFF by default**.
- Activates only in CODE_STATE (Trauma / Resus).
- Visual strobes indicate recording state.
- Prevents ambient surveillance creep.

---

## Overflow & Surge Handling

### 6. The Overflow Rail
- Hallway walls are active clinical surfaces:
  - O2
  - power
  - data
- Ensures overflow patients retain full monitoring capability.
- Eliminates “digital cliff” between bays and hall.

### 7. The Bullpen (Walking-Wounded Containment)
- Glassed, negative-pressure holding zone.
- No loose objects.
- Fixed seating.
- Separate from clinical core and CT corridor.
- Converts high-mobility chaos into bounded observability.

### 8. Secondary / Dirty Egress
- Dedicated extraction path for:
  - security removals
  - decontamination
- Never crosses clean core or imaging paths.

---

## Failure Modes Addressed

| Failure Mode | Standard ER Outcome | V1.3 Outcome |
|-------------|-------------------|-------------|
| EMS stretcher lock | Ambulance gridlock | Rapid release via swap-deck |
| Walking wounded surge | Core contamination | Bullpen isolation |
| Imaging bottleneck | Transport delays | CT adjacency |
| Hallway overflow | Loss of monitoring | Overflow rail continuity |
| Staff overload | Judgment failure | Geometry-enforced flow |

---

## Design Summary
ER_BAY_V1.3 replaces **policy-dependent emergency care** with a **deterministic sorting engine**.

It assumes:
- overload is normal
- judgment degrades
- chaos must be *contained*, not negotiated

The result is an ER architecture that:
- scales under mass casualty
- protects staff
- preserves data integrity
- makes failure visible instead of silent

This is not an architectural preference.
It is a governance protocol instantiated in space.
