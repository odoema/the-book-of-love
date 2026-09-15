# DS-01a — Operational Definitions

**Status:** OPEN

## Reproducibility test

> Could two independent researchers, given the same raw data and measurement protocol, arrive at the same value?

If not, the construct is not yet adequately measured.

## A_t — AI Decision Authority

**Definition:** Proportion of critical decisions executed autonomously without mandatory human pre-approval.

\[
A_t=\frac{\text{autonomous AI decisions}}{\text{total critical decisions}}
\]

Range: 0–1.

**Sources:** decision-rights audits, execution logs, process documentation.

Distinguish AI recommendation + meaningful human decision, rubber-stamped approval, and autonomous execution. Track override rates.

## D_t — Dependency

**Definition:** Functional degradation when the AI system is unavailable or downgraded.

Candidate measures: interruption performance, completion time, error rate, viable non-AI fallback share, and fallback currency.

**Sources:** outage logs, air-gap drills, manual override tests.

A falsifier must use a calibrated test-retest/noise band rather than “any difference.”

## H_t — Independent Human Decision Capacity

**Definition:** Ability to complete relevant decisions without AI while meeting specified standards of speed, accuracy, and quality.

**Sources:** controlled experiments, drills, outages, held-out comparisons.

Do not define H_t as simply the inverse of D_t.

## E_t — Exit/Switching Cost

**Definition:** Resources required to transition from AI-mediated decision production to a functionally comparable independent workflow.

Dimensions may include time, money, retraining, portability, disruption, and substitute availability.

**Sources:** substitution tests, outage recovery, migration/resource estimates.

**Open:** E_t may be a primitive state, derived quantity, control variable, or strategic choice.

## Measurement rule

Each construct must have a quantitative null/noise band capable of distinguishing measurement error from substantive change.
