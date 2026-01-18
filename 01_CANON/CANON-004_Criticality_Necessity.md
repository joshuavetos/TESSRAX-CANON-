# CANON-004 — Criticality Necessity

## Statement

Any locally causal (local realist) completion of quantum mechanics that reproduces observed Bell inequality violations at arbitrary spacetime separations must possess an effectively infinite correlation length in its hidden-variable substrate.

Equivalently: under standard assumptions of statistical mechanics, finite-correlation-length hidden-variable models predict a distance-dependent decay of Bell violations that is not observed experimentally.

This constitutes a hard constraint on locally causal completions of quantum mechanics.

---

## Definitions

- **Local Realist Model**: A model in which measurement outcomes are determined by local hidden variables and local detector settings, with no superluminal causal influence.
- **Hidden Variables (λ)**: Degrees of freedom underlying measurement outcomes, treated as physical field variables defined on spacetime.
- **Statistical Independence**: The assumption that measurement settings are statistically independent of hidden variables, i.e. ρ(λ | a, b) = ρ(λ).
- **Exponential Clustering**: The property that connected correlation functions of a physical field decay exponentially with distance, C(r) ∼ exp(−r / ξ), where ξ is the correlation length.
- **Bell Parameter S(D)**: The CHSH Bell parameter evaluated for measurement settings separated from the source by spacetime distance D.

---

## Assumptions Ledger

This result assumes only the following:

1. **Local Causality**  
   Measurement outcomes depend only on local hidden variables and local settings.

2. **Common Cause Structure**  
   Correlations between the source and measurement settings arise through shared causal pasts.

3. **Generic Statistical Mechanics**  
   The hidden-variable substrate obeys exponential clustering unless tuned to a critical point.

No assumptions are made about quantum mechanics itself. The result constrains only locally causal completions.

---

## Lemma (Fade-Out Lemma)

Let ℳ be a local realist model whose hidden-variable field satisfies exponential clustering with correlation length ξ.

Let λ denote hidden variables at the source event, and let a, b denote measurement settings generated at spacetime separation D from the source.

Then the CHSH Bell parameter obeys the bound:

S(D) ≤ 2 + (2√2 − 2) · exp(−2D / ξ)

Consequently, in the limit D ≫ ξ:

S(D) → 2

and the Bell inequality is restored.

---

## Proof Sketch (Non-Derivable Summary)

- In non-critical physical systems, exponential clustering bounds two-point correlations between distant degrees of freedom.
- Mutual information between hidden variables λ and distant settings (a, b) is bounded by the square of the correlation function.
- Bell inequality violation above the classical bound requires nonzero mutual information between λ and (a, b).
- As D ≫ ξ, mutual information vanishes exponentially, forcing S(D) → 2.

Maintaining a non-classical Bell parameter at arbitrary D therefore requires ξ → ∞.

---

## Consequence

Any locally causal model reproducing observed Bell violations at all tested scales must evade exponential clustering.

A known physical mechanism for this is **criticality**: a phase characterized by infinite correlation length and scale-invariant correlations.

Finite-correlation-length (“fluid-like”, gapped, or equilibrium) hidden-variable substrates are excluded by existing laboratory and cosmic Bell tests.

---

## Relation to Invariant Set Theory

Invariant Set Theory provides a concrete geometric realization of the critical state mandated by this constraint.

In this interpretation:
- The fractal geometry of the invariant set corresponds to the phase space of a system locked at criticality.
- Fractality is not postulated ad hoc, but emerges as the geometric dual of infinite correlation length.

This work does not assert the truth of Invariant Set Theory; it identifies the thermodynamic phase any viable locally causal completion must inhabit.

---

## Scope Limitation

- This result does **not** constrain standard quantum mechanics.
- It applies only to **locally causal / local realist completions** of quantum predictions.
- Retrocausal or measurement-dependent models remain subject to the same constraint unless they evade exponential clustering.

---

## Experimental Status

Existing cosmic Bell tests constrain the hidden-variable correlation length to be at least of order gigaparsecs.

Any deviation from quantum predictions at extreme spacetime separations would signal near-critical (but finite-ξ) behavior.

---

## Canonical Status

This document defines a non-derivable constraint and is canonical.

Formal derivation and phenomenological plots are provided in the associated arXiv note:
“The Criticality Necessity: Universal Bell Violations Imply Infinite Correlation Lengths in Local Realist Models”.

---

## Status

LAW — Active  
Mutation requires contradiction by either:
- Empirical observation of Bell-violation fade-out, or
- Demonstration of a finite-ξ local realist model violating exponential clustering without criticality.
