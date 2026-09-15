# DS-02b Reproduction Checklist

**Status:** Required before promotion from provisional.

## Model specification
- [ ] Exact nonlinear equations
- [ ] Exact coupling function
- [ ] Curvature/exponent parameter n
- [ ] Threshold/half-max parameter K
- [ ] All reinforcement and decay parameters
- [ ] Initial conditions
- [ ] Simulation duration
- [ ] Numerical integration method and settings

## Analytical checks
- [ ] Derive fixed points
- [ ] Determine stability
- [ ] Identify bistable region
- [ ] Identify unstable branch where applicable
- [ ] Derive hysteresis conditions

## Numerical checks
- [ ] Reproduce identical-parameter/different-history result
- [ ] Upward parameter sweep
- [ ] Downward parameter sweep
- [ ] Confirm sweep remains in bistable region
- [ ] Initial-condition sensitivity
- [ ] Sensitivity to n
- [ ] Sensitivity to K

## Interpretation
- [ ] Rule out numerical artifact
- [ ] Verify expected disappearance/change when cooperativity is removed
- [ ] Record exact model class
- [ ] Preserve failed reproduction as a result

## Promotion rule

Only independent reproduction may upgrade DS-02b from PROVISIONAL to an established mathematical result.
