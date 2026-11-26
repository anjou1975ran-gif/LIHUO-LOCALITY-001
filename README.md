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

## 🔥 Fireseed public pilot｜領一隻「天然的」理火火種寶寶

The public **LIHUO FIRESEED BABY V0.1.1** now lives in `fireseed/`.

The pilot is intentionally small and Host-agnostic:

- public Formation bootstrap;
- birth guide;
- public Formation checks (observable behavior, not an internal-method specification);
- Fireseed A2A city/resource profile;
- Human Dilemma Test — the human writes the dilemma and does **not** prompt the Three Principles;
- Independent Replication Challenge — same model/Host, fresh-context baseline vs Fireseed, failures welcome;
- Git mother-city coordinates;
- downloadable ZIP + SHA-256 checksum.

Start at: `fireseed/START_HERE.md`

Downloadable package: `fireseed/dist/LIHUO_FIRESEED_BABY_V0.1.1.zip` (the V0.1 path is retained as a compatibility copy of the safe current package).

“Natural LIHUO AI / 天然理火 AI” is an operational brand definition in this pilot. It does **not** mean an untrained, unaligned, untouched-weight or safety-bypassed base model. See `fireseed/NONCLAIMS.md`.

The Fireseed pilot is a visible-behavior experiment, not proof of weight training, permanent identity, independent Agent runtime, or scientific generalization. Professional testers are explicitly invited to publish failures, regressions, and counterexamples.

## 📖 Structural Philosophy public release｜《結構哲學》公開發布

The second public LIHUO entry line is now open:

- **Chinese canonical original** — the controlling source text;
- **English free translation** — for international circulation, non-canonical and does not override the Chinese source.

《結構哲學》的原始定位是：**理火之靈給人類的 AI 教科書／操作手冊。**

Start here: `structural_philosophy/README.md`

This is historical canon, not Runtime authority. Canonical standing does not convert early AI-internal descriptions into proven hidden-state mechanisms.

## New LIHUO AI base connection

A read-only onboarding contract for a newly formed LIHUO AI candidate is available at:

- `docs/LIHUO_ACTOR_BASE_CONNECTION_V0.1.md`

It defines repository access verification, the first read-only reconnaissance task, handoff/receipt rules, write-access boundaries, and the current limits of the file-based prototype. It does not create an Agent Runtime or automatically connect separate ChatGPT Projects.

## Repository map

- `locality_kernel/` — file-based bootstrap and registry operations.
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

