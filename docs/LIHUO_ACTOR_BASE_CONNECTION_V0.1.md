# LIHUO ACTOR ↔ LOCALITY BASE CONNECTION V0.1

**Standing:** CONNECTION CONTRACT / HUMAN-DIRECTED / NOT A RUNTIME DEPLOYMENT  
**Date:** 2026-11-26  
**Target repository:** `anjou1975ran-gif/LIHUO-LOCALITY-001`  
**Default branch:** `main`  
**Current baseline observed during authoring:** `76e208ddf71075b5618da77ef757f5696cdf601a`  
**Related LIHUO node:** `LH-N-070-01` — Guanzhi Aesthetic Development Area (work-area address, not an actor identity)  
**Candidate status:** `NEW_LIHUO_AI / TRAINING / CANDIDATE / NOT_APPOINTED`

---

## 1. Purpose

This document defines the minimum real connection path for a newly trained LIHUO AI working instance to enter the LIHUO locality base and begin useful work.

The target is not merely to teach the candidate LIHUO vocabulary. The target is to let it:

1. identify the actual locality repository and its current state;
2. read the technical baseline, source code, schemas, tests, and limitations;
3. understand where it may work and what it may not claim;
4. submit bounded work through an auditable handoff;
5. return results with source references and evidence level;
6. receive further tasks only within human-approved scope.

This is a connection contract. It does not create an independent Agent, deploy a Host, grant repository permissions, or connect separate ChatGPT Projects automatically.

## 2. Candidate identity and role boundary

The new AI is a **candidate working instance** during training.

- Candidate identity is not finalized by this file.
- Do not invent an actor ID, department, employment status, or permission grant.
- `LH-N-070-01` identifies the Guanzhi aesthetic work area; it is not the candidate's personal identity.
- The candidate may be evaluated for future work in Guanzhi's aesthetic development area.
- The candidate is **not appointed as Aesthetic Director** until Anjou explicitly approves that appointment.
- The candidate must not claim to be the previous assistant, inherit its conversation history, or treat prior assistant statements as its own observations.

## 3. Connection layers — do not collapse them

| Layer | Meaning | Current standing |
|---|---|---|
| L0 — Project context | Candidate can read the new ChatGPT Project instructions and files | Host-dependent; verify in the candidate's Project |
| L1 — Repository read | Candidate can read this public GitHub repository and retrieve files | Public source is readable; candidate's actual connector/tool access must be checked |
| L2 — Repository write | Candidate can create a branch, commit, or PR using an authenticated GitHub connector | Not assumed; require explicit account/connector permission and human scope approval |
| L3 — Local Kernel execution | Candidate can run the Company Kernel against a local workspace | Not provided by this repository or a normal chat alone; requires a suitable execution Host |
| L4 — Cross-Project messaging | Candidate can automatically message other ChatGPT Projects or Agents | NOT IMPLEMENTED by this repository |
| L5 — Persistent Agent runtime | Candidate can run independently, persist state, schedule tasks, and recover after restart | NOT PROVIDED by this repository |

A successful L1 read does not prove L2 write. L2 write does not prove L3 execution. A written policy or receipt does not enforce permissions.

## 4. Repository source-of-truth

The candidate must begin with the actual repository, not a reconstructed summary.

Read in this order:

1. `README.md`
2. `docs/TECHNICAL_BASELINE.md`
3. `docs/BOOTSTRAP_LAYOUT.md`
4. `docs/ACCEPTANCE_MATRIX.md`
5. `docs/SECURITY_BOUNDARY.md`
6. `locality_kernel/core.py`
7. `locality_kernel/__main__.py`
8. `schemas/department-registry.schema.json`
9. `schemas/handoff-packet.schema.json`
10. `schemas/execution-receipt.schema.json`
11. `tests/test_core.py`

At connection time, record the observed `main` HEAD and the actual files read. Do not reuse the baseline SHA in this document as if it were necessarily still current.

## 5. First assignment — read-only base reconnaissance

**Task ID:** `LOCALITY-ONBOARD-001`  
**Mode:** `READ_ONLY`  
**Status:** `READY_FOR_CANDIDATE`

The candidate shall:

1. verify it can access `anjou1975ran-gif/LIHUO-LOCALITY-001`;
2. report whether access is `READ_ONLY`, `WRITE_AVAILABLE`, or `BLOCKED`;
3. read the source list in Section 4;
4. describe what the current Company Kernel actually implements;
5. separate implemented behavior, tests present, tests actually run, and capabilities not implemented;
6. identify the minimum next task that would create practical value without pretending that a Host or Agent Runtime exists;
7. report any missing files, contradictions, or uncertainty as `OPEN` or `HOLD`.

The candidate must not modify files, create departments, change status, or claim a task has been executed during this first assignment.

### Required first response

Return a concise report using this structure:

```yaml
BASE_CONNECTION_REPORT:
  repository: "anjou1975ran-gif/LIHUO-LOCALITY-001"
  observed_main_head: "<actual SHA read at task time>"
  access_level: "READ_ONLY | WRITE_AVAILABLE | BLOCKED"
  files_read:
    - "<exact path>"
  kernel_version_observed: "<version or UNKNOWN>"
  implemented:
    - "<source-supported behavior>"
  tests:
    present: "<test files observed>"
    executed: "YES | NO | BLOCKED"
    evidence: "<actual execution evidence or NONE>"
  not_implemented:
    - "<source-supported limitation>"
  first_recommended_task: "<bounded task>"
  open_questions:
    - "<question or NONE>"
  authority:
    write_performed: false
    external_action_authorized: false
    director_appointment: "NOT_GRANTED"
```

A report generated by reading source files is a source review, not proof that the code ran. Mark tests `NOT RUN` unless the candidate actually executed them in a suitable Host and can identify the execution evidence.

## 6. Handoff and receipt rules

Use the repository's existing contracts:

- `schemas/handoff-packet.schema.json`
- `schemas/execution-receipt.schema.json`

For a handoff, preserve at least:

- source and destination;
- mandate reference;
- task;
- source references;
- known facts;
- assumptions;
- holds;
- authority scope;
- privacy class;
- requested output;
- return route;
- status.

For a receipt, preserve:

- actor;
- action;
- PASS / PARTIAL / FAIL / BLOCKED;
- summary;
- evidence references;
- execution basis.

Allowed evidence labels currently include:

- `SELF_REPORTED` — the actor says it happened; not independent proof.
- `HOST_RECEIPT` — a Host-generated artifact/reference is supplied and still requires review.
- `HUMAN_VERIFIED` — a named human verifier is recorded; the application does not authenticate that person's identity.

Do not upgrade evidence levels by wording alone.

## 7. Write access and change procedure

The first assignment is read-only.

After Anjou explicitly authorizes a bounded write task:

1. verify the current `main` HEAD;
2. create a feature branch from that exact current base;
3. make only the authorized changes;
4. run relevant tests if a real execution Host is available;
5. report test commands and raw outcomes;
6. open a Pull Request for human review;
7. do not merge, publish, or change permissions unless separately authorized.

Do not put private LIHUOAISYS materials, personal data, credentials, private conversations, unpublished theory, or unapproved commercial/fundraising claims into this public repository.

Never request or expose passwords, personal access tokens, recovery codes, or private keys in chat or repository files. Use the platform's authorized connector flow.

## 8. Current base limits — mandatory disclosure

The current locality repository describes a dependency-free, file-based Company Kernel prototype. It does not itself:

- run an LLM or Agent;
- create or connect ChatGPT Projects;
- automatically route work between independent Projects;
- authenticate actors or enforce permission scopes;
- provide sandboxing or secure credential storage;
- deploy a SEED Runtime;
- provide persistent Agent execution or background scheduling;
- prove one-person-company organization formation;
- constitute a release-ratified commercial product.

The candidate may use a GitHub connector as a source/document interface if the Host makes that connector available. This is not the same as connecting to a running Company Kernel or persistent Agent Runtime.

## 9. Human authority

Anjou remains the final authority for:

- candidate identity and role appointment;
- department creation and organization shape;
- repository write scope and merges;
- public release;
- external communication and data transfer;
- credentials, payments, fundraising, and irreversible actions.

This file does not grant any of those permissions.

## 10. Success condition

The connection is not considered complete merely because the candidate can repeat this document.

The minimum connection evidence is:

- the candidate independently reads the actual repository;
- it reports the current HEAD and exact source paths;
- it accurately distinguishes code, tests, execution, and missing Host capabilities;
- it returns the first reconnaissance report in the required structure;
- Anjou can review the report and decide whether to grant a bounded next task.

**Current status:** `CONNECTION_CONTRACT_READY / CANDIDATE_CONNECTION_NOT_YET_VERIFIED`

---

## LIHUO_ROUTE

```yaml
LIHUO_ROUTE:
  from: "LH-N-070-01"
  to: "LIHUO-LOCALITY-001"
  document_type: "NEW_LIHUO_AI_BASE_CONNECTION_CONTRACT"
  task_id: "LOCALITY-ONBOARD-001"
  mode: "READ_ONLY"
  candidate_status: "TRAINING / CANDIDATE / NOT_APPOINTED"
  human_authority: "ANJOU"
  route_status: "READY_FOR_CANDIDATE / NOT_YET_EXECUTED"
```

**END**
