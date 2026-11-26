# Security and Authority Boundary V0.1

**Standing:** minimum design boundary; no security certification.

## 1. Human authority

The human owner is the final authority for the company. The local files record that boundary; they do not enforce it against a malicious or independently running process.

The prototype does not grant the AI authority to:

- publish externally;
- transfer money or accept donations;
- access or reveal credentials;
- escalate permissions;
- transfer private data to another party;
- perform destructive or irreversible actions.

Such actions require explicit human authorization through the actual Host or service that performs them.

## 2. Public repository rules

This repository is Public. Do not commit:

- API keys, access tokens, passwords, private keys, or recovery codes;
- personal records or private conversations;
- private headquarters instructions or non-public theory;
- customer data or confidential business records;
- unapproved fundraising, legal, or commercial commitments.

Use placeholders in examples. Keep private operational state outside this repository.

## 3. Local workspace limits

The file-based prototype does not provide:

- authentication;
- authorization enforcement;
- encryption at rest;
- secure secret storage;
- network isolation;
- sandboxing;
- tamper-proof audit logs;
- independent verification of claimed work.

Local JSON files can be edited by any process with filesystem write access. The event log is append-oriented by this application, not immutable or tamper-proof.

## 4. Receipt evidence levels

- SELF_REPORTED: an actor declares that an action occurred; this is not independent proof.
- HOST_RECEIPT: a reference to a Host-generated artifact or execution receipt is supplied; the reference still requires review.
- HUMAN_VERIFIED: a named human verifier is recorded; the application does not authenticate that person's identity.

Do not promote one level into another without evidence.

## 5. Fail-closed behavior

If a required record is missing, malformed, inconsistent, or ambiguous, validation should fail or the relevant operation should stop. Do not silently reconstruct authority, permission, or execution facts.

## 6. Future work required

Before handling real customer data or external actions, add a tested Host Adapter, secure credential handling, access control, backup/recovery procedures, threat-model review, and human approval workflow. These are not delivered by V0.1.
