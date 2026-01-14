# TESSRAX-CANON

This repository is a **low-entropy body of truth**.

It exists to solve one problem:

> How do humans retain agency, reconstruct truth, and assign responsibility
> in systems where machines act faster than people can understand?

## What This Is
- A **canon**, not a brainstorm
- A **reconstruction-first** knowledge base
- A place where ideas must survive loss of power, tools, and context

## What This Is Not
- A note dump
- An AI alignment scrapbook
- A startup pitch
- A real-time journal

## Operating Principles
1. **Reconstructability over continuity**
2. **Fail-closed over plausible deniability**
3. **Humans must be able to re-derive truth by hand**
4. **If it can’t be explained on paper, it doesn’t exist**

## File Discipline
- Files in `01_CANON` are rare and hard to add.
- Protocols must be runnable by tired humans.
- Diagnostics must expose failure, not explain it away.
- Anything obsolete moves to `99_ARCHIVE`, never deleted.

## Authority
This repo is authoritative **only** where explicitly stated.
Silence means “unknown,” not “assumed false.”

If the screens go dark, this is what remains.
diff --git a/00_README/README.md b/00_README/README.md
index 4a1b9c2..9f7c8d1 100644
--- a/00_README/README.md
+++ b/00_README/README.md
@@ -1,3 +1,24 @@
 # TESSRAX
 
 This repository is the canonical record of governance primitives, diagnostics, and invariants.
+
+---
+
+## CNS EMPIRICAL AUDIT (ACTIVE)
+
+### Established Invariants
+- **CNS_MAX_MASS**: 2.30 M_sun  
+  Upper bound beyond which the hypothesis that physical laws are optimized for maximal black hole production is falsified.
+
+- **NEUTRON_STAR_ANCHOR**: PSR J0740+6620  
+  Observed mass: 2.08 ± 0.07 M_sun (Shapiro delay).  
+  This value constitutes the current hard observational floor for neutron star maximum mass.
+
+### Active Monitors
+- **PSR J0952−0607**  
+  Reported mass ~2.35 M_sun.  
+  Status: PENDING. Verification requires independent confirmation beyond irradiation-dependent optical modeling.
+
+### Change Control
+Any enforcement artifact, diagnostic, or governance action referencing an unlisted or unanchored concept MUST be treated as INVALID.
+
+Audit Status: PENDING
+Last Review: 2026-01-14
---

## CNS EMPIRICAL AUDIT (FAIL-CLOSED)

### Scope
This repository treats Cosmological Natural Selection (CNS) as a falsifiable hypothesis, not a metaphysical explanation. CNS is evaluated **only** via machine-decidable astrophysical constraints. Narrative, metaphorical, or anthropic arguments are explicitly excluded.

### Falsification Criterion (HARD)
**CNS_MAX_MASS = 2.30 M☉**

If a neutron star with gravitational mass **M > 2.30 M☉** is independently confirmed via two or more observational channels (e.g., radio timing + optical RV, or GW constraints), the hypothesis that physical laws are optimized for maximal black hole production is **REJECTED**.

This threshold is chosen to lie above current hard observational anchors while remaining incompatible with the soft Equation of State required by CNS.

### Observational Anchors
- **PSR J0740+6620**  
  Mass: **2.08 ± 0.07 M☉**  
  Method: Shapiro delay  
  Status: CONFIRMED  
  Role: Hard observational floor for neutron star maximum mass.

### Active Monitor (Contested)
- **PSR J0952−0607**  
  Reported mass: ~**2.35 M☉**  
  Method: Optical light-curve modeling of irradiated companion  
  Status: PENDING  
  Note: Measurement subject to significant systematic uncertainty. Independent confirmation required.

### Epistemic Status
- CNS is **falsifiable but not confirmable** by neutron star mass measurements alone.
- Survival below CNS_MAX_MASS does not validate CNS; it only preserves non-rejection.
- Enforcement actions, registry updates, or governance claims derived from CNS are **INVALID** unless this audit state is explicitly referenced.

### Explicit Exclusions
The following are **not admissible** as CNS evidence or support:
- Metaphorical mappings (e.g., “CMB as event horizon”)
- Chemical cooling narratives not applicable to Pop III star formation
- Parameter tuning arguments without a defined optimization function
- Epoch claims without anchored observational citations

### Audit Status
**Status:** PENDING  
**Last Review:** 2026-01-14
