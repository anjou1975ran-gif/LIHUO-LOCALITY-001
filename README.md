# LIHUO LOCALITY 001

**Purpose:** technical pilot for establishing the first local LIHUO one-person-company module.

**Current standing:** `ENGINEERING PROTOTYPE / NOT RELEASE-RATIFIED`.

This repository is a separate locality workspace. It is not the LIHUOAISYS private headquarters repository and does not replace it.

## First objective

Prove that a clean environment can initialize and maintain a minimal company workspace with:

- a company identity record;
- a human-owner authority boundary;
- an initially empty, extensible department registry;
- task, handoff, and execution-receipt ledgers;
- local state that can be read and validated after restart.

The organization shape, department selection, and later expansion are intentionally left to the human owner. This repository does not pre-create the seven starter departments or define a city plan.

## Current technical scope

The first prototype is a dependency-free, file-based Company Kernel starter. It is designed to work offline. GitHub is used here for engineering collaboration and source history; GitHub is **not** a runtime dependency of the local company workspace.

## Important limits

This prototype does **not** claim to provide:

- an independent or persistent AI Agent runtime;
- automatic communication between separate LLM Projects;
- Host-level permission enforcement, sandboxing, or credential protection;
- automatic execution of tasks by an LLM;
- a deployed SEED Runtime or proven SEED regeneration;
- a released or commercially approved One-Person Company product.

A record or policy in a file is not technical enforcement. A receipt is only as strong as its evidence and verification level.

## Quick start

Requires Python 3.11 or later. No third-party packages are required.

```bash
python -m locality_kernel init --root ./my-company --company-id my-company --name "My Company" --owner-id owner-001 --owner-name "Human Owner"
python -m locality_kernel validate --root ./my-company
python -m locality_kernel department add --root ./my-company --id research --name "Research" --purpose "Research tasks"
python -m locality_kernel department list --root ./my-company
python -m unittest discover -s tests -v
```

## Repository map

- `src/locality_kernel/` — file-based bootstrap and registry operations.
- `tests/` — local regression tests.
- `docs/` — technical contracts, boundaries, and acceptance criteria.
- `schemas/` — machine-readable JSON Schemas.

## Source lineage

This pilot is derived from the human-provided **LIHUO One-Person Company Pack V0.1 research design (2026-11-25)**. The source research remains distinct; private headquarters materials are not copied into this public repository.

## Governance

- Human owner retains final authority.
- No external action, payment, publication, credential use, or permission escalation is authorized by this repository alone.
- Changes to the product's organization shape require human direction.
- Unknown, unimplemented, or unverified capabilities remain marked as such.

