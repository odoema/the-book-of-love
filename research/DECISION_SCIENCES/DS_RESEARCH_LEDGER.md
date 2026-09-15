# Decision Sciences Research Ledger

**Project:** The Book of Love  
**Track:** Decision Sciences  
**Status:** Active research programme

## 1. Programme premise

The programme investigates whether increasing AI decision authority can interact with human/institutional dependency in ways that reduce reversibility and preserve or expand authority after the original justification for delegation disappears.

The **Authority–Dependency Ratchet** remains a working hypothesis.

## 2. DS-02 — Linear/Symmetric Minimal Model

Tested:

\[
\frac{dD}{dt}=\alpha A(1-D)-\delta_DD
\]

\[
\frac{dA}{dt}=\beta D(1-A)-\delta_AA
\]

The reported threshold is:

\[
\alpha\beta>\delta_A\delta_D.
\]

The tested linear-decay, symmetric-coupling form can produce a non-zero equilibrium but did not produce genuine hysteresis. Reducing reinforcement can return the system to the low state.

**Correct interpretation:** this falsifies the ratchet claim only for this model class. It does not prove that no two-variable model can exhibit hysteresis and does not prove a third variable is necessary.

## 3. DS-02b — Nonlinear/Cooperative Extension

A subsequent model experiment reported that nonlinear/cooperative coupling can produce bistability and hysteresis using only A and D. Reported tests included different final states at identical parameters depending on starting history and persistence of a high state after reinforcement was reduced within a bistable region.

**Status: PROVISIONAL — REQUIRES INDEPENDENT REPRODUCTION.**

The model is stylized and its curvature/threshold parameters require justification and sensitivity analysis. Mathematical sufficiency is not empirical evidence.

## 4. Integrated finding

> Hysteresis in an authority–dependency system is not a property of coupling alone; it depends on the functional form and structural mechanisms governing transitions. The tested linear-symmetric form does not produce hysteresis, while a reported cooperative nonlinear form can produce it.

## 5. DS-01 measurement mandate

Specify and assess measurement for:
- A_t — AI decision authority
- D_t — human/institutional dependency
- H_t — independent human decision capacity
- E_t — exit/switching cost

Each construct requires an operational definition, unit/scale, data source, procedure, reproducibility test, falsifier, quantitative null/noise band, and feasibility classification.

## 6. Open theoretical question

E_t must not automatically be treated as a third state variable. It may be primitive, derived, a control variable, or part of a strategic decision problem.

## 7. Current research question

> Under what measurable conditions can AI authority and human/institutional dependency produce persistent, asymmetric loss of reversibility?

Secondary question:

> Can persistence arise from nonlinear A-D dynamics alone, or does it require exit costs, asymmetric delegation/retraction, institutional choices, or another mechanism?

## DS-02b Reproduction Update — 15 September 2026

### Event
A supplied Claude reproduction record was reviewed against the archived DS-02b addendum.

### Finding
The reproduction record explicitly states that the archived DS-02b addendum does not contain the exact original equations or numerical specification. It therefore reconstructs a Hill-function nonlinear/cooperative two-variable model and tests that reconstruction.

### Result
For the reconstructed Hill-cooperative model, the record reports:
- bistability / low-unstable-high structure: reproduced;
- history dependence at identical parameters: reproduced;
- persistence after reinforcement reduction: reproduced;
- loss of bistability at n=1: reproduced;
- sweep-rate robustness of the decreasing-r transition: reproduced;
- symmetric two-sided forced hysteresis: not reproduced in this reconstruction; the observed mechanism is asymmetric.

### Governance of the claim
This does NOT establish that the unarchived original DS-02b simulation used the same equations. The result is indexed to the reconstructed Hill-cooperative model class.

### Status decision
**DS-02b: REPRODUCED (QUALIFIED) FOR THE RECONSTRUCTED HILL-COOPERATIVE MODEL CLASS; ORIGINAL-SPECIFICATION REPRODUCTION REMAINS UNRESOLVED.**

DS-02 remains CLOSED with its original negative result for the linear/symmetric model class.

DS-03 remains NOT AUTHORIZED.

### Provenance
The supplied reproduction document labels its reconstruction as model-generated and its numerical/analytical results as independently verified for that reconstruction. This record does not convert that provenance into proof of the original unarchived DS-02b specification.
