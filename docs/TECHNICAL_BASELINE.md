# LIHUO LOCALITY 001 — Technical Baseline V0.1

**Standing:** ENGINEERING PROTOTYPE / NOT RELEASE-RATIFIED  
**Scope:** first local one-person-company technical foundation  
**Organization design:** reserved to the human owner

## 1. Product boundary inherited from the One-Person Company research

The source research establishes the following product direction:

- personal-use company package;
- Offline First / Network Optional;
- human owner remains the final authority;
- company base is separate from department projects;
- departments are optional, extensible project packs;
- Git, cloud APIs, shared libraries, and Agent networks are not installation prerequisites;
- manual handoff is valid when the Host does not provide automatic project-to-project communication.

This repository implements only a narrow technical slice of that direction. It does not ratify or release the full product.

## 2. Minimal architecture

~~~text
HUMAN OWNER
    |
COMPANY BASE / FILE-BASED KERNEL
    |
    +-- Company Profile
    +-- Owner Authority Record
    +-- Department Registry (initially empty)
    +-- Task Index
    +-- Handoff Index
    +-- Receipt Ledger
    +-- Local State
    |
OPTIONAL DEPARTMENT PROJECTS
    |
OPTIONAL HOST / NETWORK ADAPTERS
~~~

The first implementation is deliberately file-based and dependency-free. It can initialize a local company workspace and maintain basic registry records.

## 3. What the prototype actually does

- initializes an empty company workspace;
- records a company identity and human-owner authority boundary;
- creates an empty department registry;
- registers generic departments as PROPOSED;
- supports basic department lifecycle transitions;
- records declared work receipts with an explicit evidence basis;
- validates required files and selected invariants;
- stores state locally in JSON files and an append-only local event log.

## 4. What it does not do

- It does not run an LLM or an Agent.
- It does not create ChatGPT Projects or other Host-native resources.
- It does not automatically route tasks between independent Projects.
- It does not authenticate users or enforce permission scopes.
- It does not encrypt local files or manage secrets.
- It does not provide a sandbox or prevent direct filesystem access.
- It does not provide remote headquarters communication.
- It does not implement a SEED Runtime.
- It does not prove that SEED is necessary or improves regeneration.

## 5. Relationship to SEED

SEED is not a hard dependency of this first Company Kernel prototype. The company workspace must first be testable without assuming SEED success.

A later controlled comparison may test:

- N0: ordinary formation material without SEED;
- S1: the same formation target with a candidate SEED;
- S-M: ablation of claimed necessary SEED elements;
- A1: a conventional snapshot/context package comparison.

All groups must use matched model, Host, task, permissions, and evaluation criteria. No result is implied by this repository's existence.

## 6. Host integration boundary

GitHub is the engineering repository for this locality. It is not the local company's execution Host.

A future Host Adapter must declare, and then test, each capability separately:

- file read/write;
- workspace or Project creation;
- command execution;
- persistent storage;
- model/provider invocation;
- task scheduling;
- inter-Project messaging;
- permission enforcement;
- credential storage;
- shutdown and recovery.

A declared capability is not a verified binding. Each adapter requires an execution receipt and regression test.

## 7. Source lineage

This baseline derives from the human-provided LIHUO One-Person Company Pack V0.1 research design dated 2026-11-25. The original source package remains separate. This public repository contains a limited technical implementation and does not copy private headquarters material.

## 8. Current engineering decision

Build a small, inspectable Company Kernel before adding departments, city functions, commercial features, or Agent orchestration. Keep the department registry empty until the human owner specifies the organization shape.
