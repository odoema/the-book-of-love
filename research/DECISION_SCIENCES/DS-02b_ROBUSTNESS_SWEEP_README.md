# DS-02b Robustness Sweep

This experiment follows the qualified reproduction and tests whether the reconstructed
nonlinear mechanism is narrow or robust.

## Dimensions

- Cooperativity `n`: 1, 1.5, 2, 2.5, 3, 4
- Half-max parameter `K`: 0.20 through 0.80
- Symmetric and asymmetric `alpha`, `beta`
- Two alternative response-function families:
  - Hill
  - Logistic

## Important boundary

This is a robustness experiment on the **reconstructed model**, not a test of empirical
AI deployments.

A nonzero history separation is not by itself sufficient evidence of hysteresis. Results
must be checked for stability, parameter dependence, numerical artifacts, and whether
history dependence persists under an appropriate parameter-sweep protocol.

## Run

From the repository root:

```text
py research\DECISION_SCIENCES\DS-02b_ROBUSTNESS_SWEEP.py
```

The script writes:

```text
research\DECISION_SCIENCES\DS-02b_ROBUSTNESS_RESULTS\n_x_K_asymmetry_grid.csv
```

Do not overwrite the first-run output before it has been archived.
