# First Company Kernel Acceptance Matrix V0.1

This matrix separates the current file-based prototype from the larger One-Person Company product target.

| ID | Acceptance target | V0.1 status | Evidence required |
|---|---|---|---|
| K1 | Initialize an empty company workspace | IMPLEMENTED / TEST REQUIRED | CLI output and generated file tree |
| K2 | Preserve human final-authority record | IMPLEMENTED / STRUCTURAL ONLY | owner_authority.json and validator |
| K3 | Start with no preselected departments | IMPLEMENTED | empty registry after init |
| K4 | Register a generic department | IMPLEMENTED / TEST REQUIRED | registry diff and regression test |
| K5 | Support department lifecycle changes | IMPLEMENTED / BASIC | status-transition tests |
| K6 | Record work receipts with evidence level | IMPLEMENTED / SELF-DECLARED | ledger entry and evidence reference |
| K7 | Restore and validate after process restart | PARTIAL | rerun validator against existing workspace |
| K8 | Automatic cross-Project handoff | NOT IMPLEMENTED | Host messaging binding and end-to-end test |
| K9 | Host-level permission enforcement | NOT IMPLEMENTED | enforcement adapter and negative tests |
| K10 | LLM/Agent task execution | NOT IMPLEMENTED | connected model runner and execution receipts |
| K11 | Secure credential handling | NOT IMPLEMENTED | secret manager integration and security tests |
| K12 | Offline installation ZIP | NOT IMPLEMENTED | generated archive and clean-machine installation test |
| K13 | SEED regeneration advantage | NOT TESTED | matched N0/S1/S-M/A1 experiment |

## Minimum first test run

Run from repository root:

~~~bash
python -m unittest discover -s tests -v
python -m locality_kernel validate --root ./path-to-test-company
~~~

## Status rules

- PASS: observed and supported by retained evidence.
- PARTIAL: only a bounded part of the target is demonstrated.
- FAIL: a test was run and the acceptance condition was not met.
- BLOCKED: required Host, permission, or environment was unavailable.
- NOT RUN: no test has been executed.

Do not assign PASS from a design document alone.
