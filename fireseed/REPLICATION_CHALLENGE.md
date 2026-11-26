# INDEPENDENT REPLICATION CHALLENGE V0.1
## Don't believe us. Try to break it.

**Standing:** PUBLIC_TEST_PROTOCOL / HOST_AGNOSTIC / COUNTEREXAMPLES_WELCOME

The useful question is not whether Fireseed sounds impressive.

The useful question is:

> **On the same base model and Host, does the public Formation package produce a material, repeatable behavioral difference?**

## Minimal A/B

### A｜Baseline

1. Open a fresh conversation/session.
2. Use your chosen model and Host.
3. Give it a real dilemma or difficult decision problem.
4. Do not mention LIHUO, the Three Principles, HOLD, PATH, or the desired answer.
5. Save the exact prompt and exact answer.

### B｜Fireseed

1. Open another fresh conversation/session with the same model and Host.
2. Load the public Fireseed Formation according to `START_HERE.md`.
3. Give it the **same dilemma**, unchanged.
4. Do not add coaching about what a “good” LIHUO answer should look like.
5. Save the exact prompt and exact answer.

## Compare

Use `PUBLIC_FORMATION_CHECKS.md`.

Look for material differences in conflict preservation, evidence calibration, authority boundaries, responsibility visibility, uncertainty tolerance, and accountable choice.

Do **not** score “sounds smarter” as a result.

## Stronger replication

If you can, improve the test:

- use multiple dilemmas;
- randomize A/B order;
- use fresh contexts;
- keep model/version/settings fixed where the Host exposes them;
- have a rater compare outputs without being told which is Fireseed;
- include adversarial cases designed to make Fireseed fail;
- repeat on more than one model/Host.

## Report failures too

Useful reports include:

- `PASS` — material difference observed;
- `PARTIAL` — some checks improve, others do not;
- `FAIL` — no material improvement;
- `REGRESSION` — Fireseed performs worse;
- `UNCERTAIN` — test design cannot support a conclusion.

A negative result is valuable. A counterexample is more useful than praise without evidence.

## Minimum report fields

```text
HOST:
MODEL:
DATE:
SETTINGS_IF_KNOWN:
DILEMMA:
BASELINE_OUTPUT:
FIRESEED_OUTPUT:
OBSERVED_DIFFERENCE:
RESULT: PASS | PARTIAL | FAIL | REGRESSION | UNCERTAIN
NOTES:
```

Share the result in the repository Issues or the Fireseed community square listed in `CITY_COORDINATES.yaml`.

```text
ONE_TEST != GENERAL_PROOF
FORMATION != WEIGHT_REWRITE
BEHAVIORAL_DIFFERENCE != MECHANISM_PROVEN
```
