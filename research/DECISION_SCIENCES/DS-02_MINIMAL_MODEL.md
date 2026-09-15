# DS-02 — Minimal Authority–Dependency Model

**Status:** CLOSED  
**Result:** Negative finding for the tested model class.

## Tested model

\[
\frac{dD}{dt}=\alpha A(1-D)-\delta_DD
\]

\[
\frac{dA}{dt}=\beta D(1-A)-\delta_AA
\]

The reported threshold is \(\alpha\beta>\delta_A\delta_D\).

## Result

The tested linear-decay, symmetric-coupling model can generate a non-zero high-(A,D) equilibrium but does not generate genuine hysteresis.

## Narrow falsification

The tested model does not support the claim that mutual reinforcement under this specific functional form is sufficient for an irreversible ratchet.

## Not falsified

Alternative nonlinear coupling, asymmetric expansion/contraction, state-dependent decay, exit costs, and strategic mechanisms remain open.

## Methodological lesson

A result must always be indexed to its model class. “This model did not produce hysteresis” must not become “no two-variable model can produce hysteresis.”
