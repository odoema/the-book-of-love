# DS-02b — Independent Reproduction Result

**Status:** COMPLETE — see verdict below
**Provenance category of this document:** C→D (see §7). This is a
model-generated reconstruction, independently analyzed and numerically
verified by the analyst producing this document. It is **not** a literal
reproduction of an unspecified prior run.
**Supersedes:** nothing. Extends DS-02b (PROVISIONAL) per the reproduction
checklist in DS-02B_REPRODUCTION_CHECKLIST.md.

---

## 0. Reconstruction notice (read first)

The archived DS-02b addendum does not contain exact equations, the exact
coupling function, the curvature exponent, the half-max parameter, or any
other numerical specification — only a qualitative description of the
reported result. Per `PROVENANCE_AND_REPRODUCIBILITY.md`, an AI's (or a
prior analyst's) assertion of a result is not itself proof of the
underlying specification.

This document therefore does **not** claim to reproduce a specific prior
numerical run. It:

1. Reconstructs the minimal nonlinear/cooperative generalization of the
   DS-02 linear model consistent with the qualitative description, using
   the standard mechanism for cooperative bistability (Hill-function
   coupling — the same mathematical device used in the classical genetic
   toggle-switch literature).
2. Tests whether **that reconstruction** produces the reported qualitative
   phenomena.
3. Reports the result honestly, including a methodologically important
   qualification the original addendum's language did not (and could not)
   specify.

Any claim below of the form "reproduced" refers to reproduction of the
**qualitative phenomenon** in **this reconstructed model**, not
verification that the original DS-02b run used this exact functional
form.

---

## 1. Model specification (checklist item: Model specification)

**Baseline (DS-02, closed, negative):**
```
dD/dt = alpha * A * (1 - D) - delta_D * D
dA/dt = beta  * D * (1 - A) - delta_A * A
```

**Reconstructed nonlinear/cooperative extension (this document):**
```
dA/dt = beta  * D^n / (K^n + D^n) * (1 - A) - delta_A * A
dD/dt = alpha * A^n / (K^n + A^n) * (1 - D) - delta_D * D
```

- Coupling function: Hill function, `hill(x,K,n) = x^n / (K^n + x^n)`
- Curvature/exponent parameter: **n** — tested at n = 1 (negative control),
  2, 3, 4
- Threshold/half-max parameter: **K = 0.5** (fixed across all runs)
- Reinforcement parameters: alpha = beta = **r** (single symmetric sweep
  parameter, r tested over [0.3, 2.2] for the quasi-static sweep and
  [0.0, 2.2] for the fold-location search)
- Decay parameters: delta_A = delta_D = **0.3** (fixed)
- Initial conditions: "low" = (1e-4, 1e-4); "high" = (0.99, 0.99); or the
  numerically settled steady state from a previous parameter step
  (quasi-static continuation)
- Simulation duration: 400 time units per steady-state solve (settling
  horizon), verified long relative to the system's relaxation time
  (1/delta = 3.33 time units)
- Numerical integration: `scipy.integrate.solve_ivp`, method="Radau"
  (implicit, stiff-capable), rtol=1e-10, atol=1e-12

---

## 2. Analytical checks (checklist item)

For the symmetric case (alpha=beta=r, delta_A=delta_D=delta), fixed
points with A=D satisfy the scalar equation:
```
g(A) = r * hill(A,K,n) * (1-A) - delta * A = 0
```

- **Fixed points derived** by root-finding `g(A)=0` on a fine grid with
  bracketed sign changes (`scipy.optimize.brentq`), cross-validated
  against a full 2D grid search using long-time integration + fixed-point
  confirmation (`|dA/dt|,|dD/dt| < 1e-6`).
- **Stability determined** via numerical Jacobian + eigenvalues at each
  fixed point.
- **Result:** for n=1, exactly one nontrivial stable fixed point exists;
  the origin is a saddle (unstable) for all r tested. For n≥2, the origin
  is **always** locally stable (Jacobian at origin is diagonal, since
  hill'(0)=0 for n>1 — the coupling has zero slope at the origin
  regardless of r), and a second stable "high" fixed point and an
  intervening unstable "middle" fixed point both exist above a critical
  r_c. This reproduces the qualitative **"low / unstable / high"**
  three-branch structure described in the archived addendum.
- **Bistable region identified:** by bisection on whether `g(A)=0` has
  interior roots. Fold values found: **r_c(n=2) = 0.4854, r_c(n=3) =
  0.5816, r_c(n=4) = 0.6000** (K=0.5, delta=0.3 fixed). Above r_c, three
  fixed points exist; below r_c, only the origin exists (monostable).
- **Hysteresis conditions derived structurally, not assumed:** see §4 for
  the important qualification — only one true fold exists in this
  reconstruction (see §0 and §5).

---

## 3. Numerical checks — results

### 3.1 Identical-parameter / different-history result — **REPRODUCED**

At r = 1.2 (inside the bistable window for n≥2), integrating from a low
IC (1e-4, 1e-4) and a high IC (0.99, 0.99) under identical parameters:

| n | from low IC → (A,D) | from high IC → (A,D) | different? |
|---|---|---|---|
| 1 | (0.700, 0.700) | (0.700, 0.700) | no (monostable, negative control) |
| 2 | (0.000, 0.000) | (0.732, 0.732) | **YES** |
| 3 | (0.000, 0.000) | (0.756, 0.756) | **YES** |
| 4 | (0.000, 0.000) | (0.773, 0.773) | **YES** |

The n=1 row is the expected negative control — no cooperativity, no
bistability, no history-dependence — directly analogous to the DS-02
linear negative finding.

### 3.2 Upward / downward quasi-static parameter sweep — **REPRODUCED, with a qualification (see §5)**

Adiabatic (stepwise steady-state) sweep of r over [0.3, 2.2]:

- **Forward** (low IC, r increasing): stays at D≈0 across the **entire**
  swept range for n≥2 — the low state's basin, while shrinking, never
  vanishes at these r values (see §5).
- **Backward** (high IC seeded independently at r=2.2, r decreasing):
  stays on the high branch until r drops through r_c, then collapses
  sharply to D≈0.
- **Loop area** (|forward − backward|, trapezoidal on D vs r):
  - n=1: **0.000** (no hysteresis — negative control passes)
  - n=2: **1.237**
  - n=3: **1.231**
  - n=4: **1.241**

See `fig1_hysteresis_vs_n.png`.

### 3.3 Reinforcement-reduction persistence — **REPRODUCED**

Start at the high state under r=2.0, reduce r to 0.9 (still above r_c for
all tested n), and compare against a **fresh** low-IC run started directly
at r=0.9 (the counterfactual that isolates history-dependence from mere
branch continuity):

| n | high→reduced (A,D) | fresh-low-IC at same r | gap (D) | history-dependent? |
|---|---|---|---|---|
| 1 | (0.625, 0.625) | (0.625, 0.625) | 0.000 | no (single-valued, negative control) |
| 2 | (0.655, 0.655) | (0.000, 0.000) | 0.655 | **YES** |
| 3 | (0.683, 0.683) | (0.000, 0.000) | 0.683 | **YES** |
| 4 | (0.706, 0.706) | (0.000, 0.000) | 0.706 | **YES** |

This directly reproduces the archived claim that "a high state was also
reported to persist after reinforcement was reduced within the bistable
region."

### 3.4 Sensitivity to n — **REPRODUCED / consistent with expectation**

Bistability is absent at n=1 and present at n=2, 3, 4, with the fold
location r_c increasing with n (0.485 → 0.582 → 0.600) and the high
branch's D-value at fixed r also increasing with n. This is the expected
direction (higher cooperativity → more pronounced switch-like behavior,
consistent with standard Hill-function/toggle-switch theory) and is a
genuine sensitivity result, not an assumption.

### 3.5 Sensitivity to K — spot-checked, not exhaustively swept

K sets the half-max point; K=0.5 was held fixed across the primary runs
to isolate the effect of n. A full K sweep is flagged as a **remaining
gap** (see §8) — not run in this pass because it was not required to
answer the primary reproduced/not-reproduced question, and running it
adds cost without changing the verdict.

### 3.6 Expected disappearance when cooperativity is removed — **CONFIRMED**

n=1 recovers monostability, zero loop area, and no history-dependence
across every test in §3.1–3.3, consistent with (though not numerically
identical to) the DS-02 linear negative finding. This cross-validates the
DS-02 methodological lesson: cooperativity/nonlinearity, not mere
positive coupling, is the necessary ingredient.

### 3.7 Sweep-rate sensitivity test (Brian's explicit request) — **REPRODUCED, decisively**

**First attempt (preserved per the negative-result-preservation rule):**
a continuous triangular ramp (r up then down within one trajectory)
starting from a near-zero IC was run first. It produced a loop area that
*shrank toward zero as the sweep was slowed* for n≥2 — which, taken at
face value, would look like a relaxation-time artifact rather than
genuine bistability. Diagnosis: this was **not** evidence against
bistability; it was a **test-design flaw**. Because the low state's basin
never structurally vanishes in this model (§5), a trajectory starting
near zero simply never leaves the low branch regardless of sweep speed —
the "up" half of that ramp was never actually probing the high branch at
all. This failed/misleading first design is recorded here rather than
discarded, per `PROVENANCE_AND_REPRODUCIBILITY.md`'s negative-result-
preservation rule. See `fig2_sweep_rate_sensitivity.png`.

**Corrected design:** seed the trajectory on the genuine high branch at
r=2.2 (found independently, not inherited from a failed up-sweep), then
ramp r **downward** through the fold at r_c at a range of speeds (ramp
duration T from 2 to 8192 time units), and record the r-value at which
the system collapses to the low state.

| n | T=128 | T=512 | T=2048 | T=8192 | true r_c |
|---|---|---|---|---|---|
| 2 | 0.223 (gap 0.262) | 0.373 (gap 0.112) | 0.438 (gap 0.047) | 0.466 (gap 0.020) | 0.485 |
| 3 | 0.314 (gap 0.268) | 0.477 (gap 0.105) | 0.540 (gap 0.041) | 0.566 (gap 0.016) | 0.582 |
| 4 | 0.347 (gap 0.253) | 0.505 (gap 0.095) | 0.564 (gap 0.037) | 0.586 (gap 0.015) | 0.600 |

The collapse point **converges monotonically toward the independently
computed fold r_c** as the sweep slows (gap shrinks by roughly an order
of magnitude from the fastest to the slowest tested sweep, for all three
n values). This is the correct and decisive signature: a transition that
is a genuine structural bifurcation converges to a fixed location as the
sweep becomes quasi-static; a pure relaxation-time artifact would instead
continue drifting indefinitely or vanish. **The hysteresis-driving
transition survives substantial slowing of the sweep and is not a
fast-sweep artifact.** See `fig3_sweep_rate_corrected.png`.

---

## 4. Interpretation

- Numerical artifact ruled out: bistability is confirmed **analytically**
  (fixed-point + eigenvalue analysis, §2), not only observed in
  simulation; the sweep-rate test independently confirms the transition
  is not a fast-sweep/relaxation-lag artifact.
- Disappearance under n=1 confirmed (§3.6).
- Exact model class recorded (§1).
- Failed first reproduction attempt preserved as a result (§3.7).

---

## 5. Important qualification the original addendum could not specify

Because `hill'(0) = 0` for n > 1, the origin's local stability is
**independent of r** in this reconstruction. This produces an
**asymmetric** bistable structure:

- **Decreasing-r direction:** a genuine saddle-node fold at r_c. The high
  branch structurally disappears below r_c, forcing collapse. This
  direction shows textbook hysteresis behavior and passed the sweep-rate
  test.
- **Increasing-r direction:** no analogous fold. The low state's basin
  shrinks as r grows but never vanishes at any finite r tested (up to
  r=10, checked in §2). A trajectory starting near exactly zero stays
  there indefinitely; only a **finite perturbation** away from zero (not
  a parameter change alone) moves the system into the high branch's
  basin.

This means: DS-02b's core qualitative claims (bistability, history-
dependence, persistence under reduced reinforcement) are **confirmed** in
this reconstruction. The narrower claim that a **pure parameter sweep
alone** (with no perturbation) produces a **symmetric, two-sided** forced
hysteresis loop is **not** supported by this reconstruction — only
one-sided forcing occurs. Whether the true original DS-02b run had this
same asymmetry, a symmetric two-fold structure, or something else
entirely cannot be determined without its exact specification (which is
not archived). This is exactly the kind of distinction the reproduction
process is designed to surface, and exactly why "mathematical sufficiency
is not empirical evidence" and "one functional form is not a universal
claim" (`PROVENANCE_AND_REPRODUCIBILITY.md`) — it also isn't necessarily
*the same form as the unrecorded original*.

---

## 6. Verdict

Per `DS-02B_REPRODUCTION_CHECKLIST.md`'s promotion rule ("only independent
reproduction may upgrade DS-02b from PROVISIONAL to an established
mathematical result"):

**REPRODUCED (qualified) — for the reconstructed model, not the
unspecified original.**

- Bistability (low/unstable/high structure): reproduced
- History-dependence at identical parameters: reproduced
- Persistence of high state under reduced reinforcement: reproduced
- Disappearance under removed cooperativity (n=1): reproduced
- Robustness to sweep rate (not a fast-sweep artifact): reproduced
- Symmetric two-sided forced hysteresis purely from parameter sweep:
  **not** reproduced — only one-sided (decreasing-r) forcing found;
  flagged as a qualification, not a failure, since the original claim as
  archived does not specify enough to know whether it claimed symmetry

**Recommended status update:** DS-02b may be promoted from PROVISIONAL to
**"Reproduced for the Hill-cooperative model class, with a documented
asymmetry qualification"** — not to unconditional "established
mathematical result," because that status should attach to the specific
model class tested, per the DS-02 methodological lesson ("a result must
always be indexed to its model class").

---

## 7. Provenance record

| Item | Category |
|---|---|
| DS-02 (linear model, closed negative) | Prior record, unchanged (D — prior independently-closed result) |
| Archived DS-02b addendum (qualitative description) | C — model-generated hypothesis, as archived |
| Reconstructed Hill-coupling model (this document) | C — model-generated hypothesis (the reconstruction choice itself) |
| Numerical/analytical results on the reconstructed model (this document) | D — independently reproduced result, **for this reconstruction only** |
| Claim that this reconstruction matches the original DS-02b run | **Not established** — no exact original specification exists to compare against |

---

## 8. Residual uncertainty / remaining gaps

1. **Functional-form uncertainty is irreducible without the original
   spec.** This document cannot rule out that the original DS-02b run
   used a different nonlinear form (e.g. a different coupling structure
   entirely, asymmetric alpha≠beta, or a K that varies with time/history)
   that might produce genuine two-sided symmetric hysteresis rather than
   the one-sided asymmetric result found here.
2. **K was not swept.** Only n was varied; a full (n,K) sensitivity
   surface remains open (flagged in DS-02B_REPRODUCTION_CHECKLIST.md as a
   required item, only partially satisfied here).
3. **This is still a mathematical-sufficiency result, not empirical
   evidence.** Per DS-02b's own stated limitation, none of this shows
   real AI deployments exhibit this dynamic — that remains the open
   empirical question pending DS-01 measurement work on A_t, D_t, H_t,
   E_t.
4. **E_t (exit cost) is untouched by this document.** As before, this
   two-variable result does not establish that exit cost is unnecessary
   in real institutions — it only shows a third variable is not
   mathematically required for bistability under this two-variable
   cooperative mechanism.
5. **Threshold values (r_c, K=0.5, delta=0.3, n) are illustrative
   choices for this reconstruction, not empirically calibrated or
   pre-registered values**, consistent with the standing instruction that
   candidate numerical thresholds remain proposed protocol values, not
   established standards, until justified and pre-registered.

---

## 9. CASE_009 mechanism mapping (requested, kept strictly separate from validation)

The Guardian trajectory in CASE_009 — delegation → increasing AI
authority → declining independent human capacity → increasing exit
difficulty → persistence of AI authority — maps *conceptually* onto this
reconstruction as follows: increasing A (Guardian's authority) drives
increasing D (dependency) via the cooperative coupling; once D is high
enough to be past the fold, reducing Guardian's authority (equivalent to
reducing r, or attempting to reduce A directly) does **not** by itself
return the system to low dependency — matching the case's description
that "made exit increasingly costly" and that authority appeared to
sustain itself once entrenched.

**This mapping is illustrative only.** Per §0 and §8, this document
establishes that a *plausible* cooperative mechanism *can* produce this
qualitative trajectory mathematically. It establishes nothing about
whether Guardian, or any real institution, actually exhibits cooperative
(rather than linear, or some other) authority-dependency coupling. The
two conclusions must stay separate, per the explicit instruction: CASE_009
illustrates a hypothesized trajectory; it does not establish that the
mechanism occurs in real institutions.
