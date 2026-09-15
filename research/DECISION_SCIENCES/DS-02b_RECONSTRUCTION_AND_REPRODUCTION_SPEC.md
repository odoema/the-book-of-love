# DS-02b — Reconstruction and Independent Reproduction Specification

**Status:** QUALIFIED REPRODUCTION ACHIEVED FOR THE RECONSTRUCTED HILL-COOPERATIVE MODEL CLASS  
**Track:** Decision Sciences  
**Hypothesis:** Authority–Dependency Ratchet (working hypothesis)  
**Related artifact:** `DS-02b_NONLINEAR_HYSTERESIS_ADDENDUM.md`

## 1. Decision

A supplied independent reproduction record reports successful reproduction of bistability, history dependence, and persistence after reinforcement reduction for a reconstructed two-variable Hill/cooperative model.

The reproduced high-history state is nonzero. In the reported sweep of cooperativity:

| n | Low-history final (A,D) | High-history final (A,D) |
|---|---|---|
| 1 | (0.700, 0.700) | (0.700, 0.700) |
| 2 | (0.000, 0.000) | (0.732, 0.732) |
| 3 | (0.000, 0.000) | (0.756, 0.756) |
| 4 | (0.000, 0.000) | (0.773, 0.773) |

These results support a qualified reproduction of the reconstructed nonlinear/cooperative model class.

**Important provenance qualification:** the historical DS-02b addendum does not preserve the complete original equations, exact numerical parameters, initial conditions, solver settings, or original outputs. Therefore this is **not certified as a literal reproduction of the historical DS-02b run**.

The earlier all-zero output that appeared in a prior version of this document is withdrawn from the research record. It was inconsistent with the supplied reproduction record and is not used as evidence for any status downgrade.

## 2. What the source addendum establishes

The existing DS-02b addendum reports that a nonlinear/cooperative response was reported to produce:

- a bistable low/unstable/high structure;
- history-dependent outcomes at identical parameter values;
- persistence of a high state after reinforcement was reduced within the bistable region.

It further states that the result would establish mathematical sufficiency of nonlinear cooperativity without a third state variable **if independently reproduced with fully specified equations and methods**.

The addendum identifies the following as required for complete reproduction:

- complete equations;
- exact parameters;
- initial conditions;
- numerical method;
- integration settings;
- parameter sweeps;
- stability analysis;
- hysteresis tests.

## 3. Provenance requirement

The generating source of the historical simulation should still be recovered where possible.

Priority source:

> The original AI response/session that actually generated the nonlinear/hysteresis result.

For provenance, record:

```text
Source AI:
Session/date:
Exact response location:
Equation:
Parameter values:
Initial conditions:
Nonlinear function:
Half-max parameter(s), if any:
Parameter sweep:
Reverse sweep:
Integration method:
Time step:
Convergence/stability criterion:
Original output:
Original plots/data, if any:
```

## 4. Reconstruction rule

No equation or parameter may be inferred merely because it produces the reported qualitative result.

If a missing component must be reconstructed, it must be labelled:

**RECONSTRUCTED / NOT SOURCE-SPECIFIED**

and tested separately from the source-exact reproduction.

## 5. Independent reproduction sequence

After a reconstruction or source specification is fully recorded:

1. Transcribe the equations exactly.
2. Independently implement the equations.
3. Reproduce fixed-parameter trajectories from the recorded initial conditions.
4. Test stability of reported equilibria.
5. Perform the recorded parameter sweep.
6. Perform the reverse sweep where specified.
7. Test history dependence at identical parameter values.
8. Repeat with substantially slower sweep rates.
9. Compare numerical outputs against the available record.
10. Record the verdict.

### Permitted verdicts

- **REPRODUCED**
- **NOT REPRODUCED**
- **AMBIGUOUS**
- **NOT REPRODUCIBLE FROM AVAILABLE RECORD**

## 6. Interpretation boundary

A successful mathematical reproduction establishes only that the specified reconstructed mathematical system can exhibit the reported behavior.

It does **not** establish that:

- real AI deployments exhibit the mechanism;
- the Authority–Dependency Ratchet exists empirically;
- CASE_009 validates the model;
- a third variable is unnecessary in real institutions;
- DS-03 is thereby authorized.

## 7. Current research state

| Artifact | Status |
|---|---|
| DS-02 linear/symmetric model | CLOSED — negative result for that model class |
| DS-02b nonlinear/cooperative extension | **QUALIFIED REPRODUCTION** |
| DS-02b historical source specification | UNDER-SPECIFIED / not fully recovered |
| Reconstructed Hill-cooperative model | **REPRODUCED** |
| DS-02b empirical validation | OPEN |
| DS-01a | OPEN |
| DS-01b | OPEN |
| DS-03 | **NOT AUTHORIZED** |

## 8. Research integrity rule

> A model is not independently reproducible merely because another implementation can be made to generate a similar qualitative result.

Conversely, a reproducible reconstructed model should not be downgraded merely because the historical generating specification is unavailable. The correct status is to distinguish **reproduction of the reconstructed model class** from **literal reproduction of the historical run**.
