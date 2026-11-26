# Generated Company Workspace Layout V0.1

Running the bootstrap command creates a local directory similar to:

~~~text
my-company/
├── manifest.json
├── company/
│   ├── profile.json
│   └── owner_authority.json
├── registry/
│   └── departments.json
├── tasks/
│   └── index.json
├── handoffs/
│   ├── index.json
│   ├── inbox/
│   └── outbox/
├── receipts/
│   └── ledger.json
├── state/
│   └── runtime.json
└── audit/
    └── events.jsonl
~~~

The bootstrap does not create department projects. The registry begins empty.

The workspace is local file state. It is not synchronized across multiple LLM Projects unless a future, separately tested Host Adapter provides that behavior.

## Command examples

~~~bash
python -m locality_kernel init --root ./my-company --company-id my-company --name "My Company" --owner-id owner-001 --owner-name "Human Owner"
python -m locality_kernel validate --root ./my-company
python -m locality_kernel department add --root ./my-company --id research --name "Research" --purpose "Research tasks"
python -m locality_kernel department status --root ./my-company --id research --status ACTIVE
python -m locality_kernel receipt add --root ./my-company --actor local-agent --action draft-plan --status PARTIAL --summary "Draft created; not independently verified"
~~~

For a HOST_RECEIPT, provide one or more evidence references. For HUMAN_VERIFIED, provide --verified-by. These flags label the declared evidence basis; they do not authenticate it.
