from __future__ import annotations

import argparse
import json
import os
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

KERNEL_VERSION = "0.1.0"
DEPARTMENT_STATUSES = ("PROPOSED", "ACTIVE", "SUSPENDED", "RETIRED")
RECEIPT_STATUSES = ("PASS", "PARTIAL", "FAIL", "BLOCKED")
EXECUTION_BASES = ("SELF_REPORTED", "HOST_RECEIPT", "HUMAN_VERIFIED")
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")

REQUIRED_FILES = (
    "manifest.json",
    "company/profile.json",
    "company/owner_authority.json",
    "registry/departments.json",
    "tasks/index.json",
    "handoffs/index.json",
    "receipts/ledger.json",
    "state/runtime.json",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def validate_id(value: str, label: str = "id") -> str:
    if not isinstance(value, str) or not ID_PATTERN.fullmatch(value):
        raise ValueError(f"{label} must match {ID_PATTERN.pattern}")
    return value


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        with temporary.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def append_event(root: Path, event_type: str, details: dict[str, Any]) -> None:
    event = {
        "event_id": "evt-" + uuid.uuid4().hex,
        "timestamp": utc_now(),
        "event_type": event_type,
        "details": details,
        "evidence_level": "LOCAL_FILE_OPERATION",
    }
    path = root / "audit" / "events.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")


def require_workspace(root: Path) -> Path:
    root = root.expanduser().resolve()
    if not (root / "manifest.json").is_file():
        raise FileNotFoundError(f"No LIHUO company workspace found at {root}")
    return root


def initialize_company(
    root: Path,
    company_id: str,
    display_name: str,
    owner_id: str,
    owner_display_name: str,
    timezone_name: str = "UTC",
) -> Path:
    root = root.expanduser().resolve()
    validate_id(company_id, "company_id")
    validate_id(owner_id, "owner_id")
    if not display_name.strip():
        raise ValueError("display_name must not be empty")
    if not owner_display_name.strip():
        raise ValueError("owner_display_name must not be empty")
    if not timezone_name.strip():
        raise ValueError("timezone_name must not be empty")
    if root.exists() and any(root.iterdir()):
        raise FileExistsError(f"Refusing to initialize a non-empty directory: {root}")

    root.mkdir(parents=True, exist_ok=True)
    for relative in (
        "company",
        "registry",
        "tasks",
        "handoffs/inbox",
        "handoffs/outbox",
        "receipts",
        "state",
        "audit",
    ):
        (root / relative).mkdir(parents=True, exist_ok=True)

    created = utc_now()
    write_json(
        root / "manifest.json",
        {
            "schema_version": KERNEL_VERSION,
            "kernel_version": KERNEL_VERSION,
            "kernel_mode": "FILE_BASED_PROTOTYPE",
            "agent_runtime": "NOT_PROVIDED",
            "host_enforcement": "NOT_PROVIDED",
            "network_mode": "OFFLINE_FIRST_NETWORK_OPTIONAL",
            "seed_integration": "NOT_INTEGRATED",
            "created_at": created,
        },
    )
    write_json(
        root / "company" / "profile.json",
        {
            "schema_version": KERNEL_VERSION,
            "company_id": company_id,
            "display_name": display_name.strip(),
            "timezone": timezone_name.strip(),
            "lifecycle_status": "INITIALIZED",
            "created_at": created,
        },
    )
    write_json(
        root / "company" / "owner_authority.json",
        {
            "schema_version": KERNEL_VERSION,
            "owner_id": owner_id,
            "display_name": owner_display_name.strip(),
            "authority_role": "HUMAN_FINAL_AUTHORITY",
            "final_authority_holder": "HUMAN_OWNER",
            "permission_grants": [],
            "approved_scopes": [],
            "approval_required_for": [
                "external_publication",
                "external_data_transfer",
                "payment_or_fund_transfer",
                "credential_access",
                "permission_escalation",
                "destructive_or_irreversible_action",
            ],
            "grant_status": "NOT_CONFIGURED",
        },
    )
    write_json(
        root / "registry" / "departments.json",
        {"schema_version": KERNEL_VERSION, "company_id": company_id, "departments": []},
    )
    write_json(root / "tasks" / "index.json", {"schema_version": KERNEL_VERSION, "tasks": []})
    write_json(root / "handoffs" / "index.json", {"schema_version": KERNEL_VERSION, "packets": []})
    write_json(root / "receipts" / "ledger.json", {"schema_version": KERNEL_VERSION, "receipts": []})
    write_json(
        root / "state" / "runtime.json",
        {
            "schema_version": KERNEL_VERSION,
            "runtime_status": "NOT_CONNECTED",
            "host_adapter": "NONE",
            "agent_runtime": "NOT_ESTABLISHED",
            "last_recovery_check": None,
        },
    )
    append_event(root, "COMPANY_WORKSPACE_INITIALIZED", {"company_id": company_id})
    return root


def validate_company(root: Path) -> list[str]:
    root = require_workspace(root)
    errors: list[str] = []
    loaded: dict[str, dict[str, Any]] = {}

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"MISSING_FILE: {relative}")
            continue
        try:
            loaded[relative] = read_json(path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"INVALID_JSON: {relative}: {exc}")

    if errors:
        return errors

    profile = loaded["company/profile.json"]
    owner = loaded["company/owner_authority.json"]
    registry = loaded["registry/departments.json"]
    manifest = loaded["manifest.json"]

    company_id = profile.get("company_id")
    try:
        validate_id(company_id, "company_id")
    except ValueError as exc:
        errors.append(f"INVALID_COMPANY_ID: {exc}")

    if registry.get("company_id") != company_id:
        errors.append("COMPANY_ID_MISMATCH: department registry does not match company profile")

    try:
        validate_id(owner.get("owner_id"), "owner_id")
    except ValueError as exc:
        errors.append(f"INVALID_OWNER_ID: {exc}")

    if owner.get("final_authority_holder") != "HUMAN_OWNER":
        errors.append("AUTHORITY_BOUNDARY_INVALID: final authority must remain with the human owner")

    if manifest.get("kernel_mode") != "FILE_BASED_PROTOTYPE":
        errors.append("KERNEL_MODE_UNEXPECTED: this validator only accepts the file-based prototype mode")

    if manifest.get("host_enforcement") != "NOT_PROVIDED":
        errors.append("HOST_ENFORCEMENT_CLAIM_INVALID: this prototype does not provide Host enforcement")

    departments = registry.get("departments")
    if not isinstance(departments, list):
        errors.append("INVALID_DEPARTMENT_REGISTRY: departments must be a list")
        return errors

    seen: set[str] = set()
    for index, department in enumerate(departments):
        if not isinstance(department, dict):
            errors.append(f"INVALID_DEPARTMENT_ENTRY: index {index} must be an object")
            continue
        department_id = department.get("department_id")
        try:
            validate_id(department_id, "department_id")
        except ValueError as exc:
            errors.append(f"INVALID_DEPARTMENT_ID: index {index}: {exc}")
            continue
        if department_id in seen:
            errors.append(f"DUPLICATE_DEPARTMENT_ID: {department_id}")
        seen.add(department_id)
        if department.get("status") not in DEPARTMENT_STATUSES:
            errors.append(f"INVALID_DEPARTMENT_STATUS: {department_id}")

    return errors


def register_department(
    root: Path,
    department_id: str,
    name: str,
    purpose: str,
) -> dict[str, Any]:
    root = require_workspace(root)
    validate_id(department_id, "department_id")
    if not name.strip() or not purpose.strip():
        raise ValueError("department name and purpose must not be empty")
    errors = validate_company(root)
    if errors:
        raise ValueError("workspace validation failed: " + "; ".join(errors))

    path = root / "registry" / "departments.json"
    registry = read_json(path)
    departments = registry["departments"]
    if any(item.get("department_id") == department_id for item in departments):
        raise ValueError(f"department already exists: {department_id}")

    timestamp = utc_now()
    department = {
        "department_id": department_id,
        "name": name.strip(),
        "purpose": purpose.strip(),
        "status": "PROPOSED",
        "created_at": timestamp,
        "updated_at": timestamp,
        "owner_id": None,
        "project_ref": None,
        "authority_status": "NOT_CONFIGURED",
        "permission_scopes": [],
    }
    departments.append(department)
    write_json(path, registry)
    append_event(root, "DEPARTMENT_REGISTERED", {"department_id": department_id, "initial_status": "PROPOSED"})
    return department


def set_department_status(root: Path, department_id: str, status: str) -> dict[str, Any]:
    root = require_workspace(root)
    validate_id(department_id, "department_id")
    status = status.upper()
    if status not in DEPARTMENT_STATUSES:
        raise ValueError(f"status must be one of {', '.join(DEPARTMENT_STATUSES)}")
    errors = validate_company(root)
    if errors:
        raise ValueError("workspace validation failed: " + "; ".join(errors))

    path = root / "registry" / "departments.json"
    registry = read_json(path)
    department = next(
        (item for item in registry["departments"] if item.get("department_id") == department_id),
        None,
    )
    if department is None:
        raise KeyError(f"unknown department: {department_id}")

    current = department["status"]
    allowed = {
        "PROPOSED": {"ACTIVE", "SUSPENDED", "RETIRED"},
        "ACTIVE": {"SUSPENDED", "RETIRED"},
        "SUSPENDED": {"ACTIVE", "RETIRED"},
        "RETIRED": set(),
    }
    if status != current and status not in allowed[current]:
        raise ValueError(f"invalid department transition: {current} -> {status}")

    department["status"] = status
    department["updated_at"] = utc_now()
    write_json(path, registry)
    append_event(root, "DEPARTMENT_STATUS_CHANGED", {
        "department_id": department_id,
        "from": current,
        "to": status,
    })
    return department


def list_departments(root: Path) -> list[dict[str, Any]]:
    root = require_workspace(root)
    errors = validate_company(root)
    if errors:
        raise ValueError("workspace validation failed: " + "; ".join(errors))
    return read_json(root / "registry" / "departments.json")["departments"]


def record_receipt(
    root: Path,
    actor: str,
    action: str,
    status: str,
    summary: str,
    evidence_refs: list[str] | None = None,
    execution_basis: str = "SELF_REPORTED",
    verified_by: str | None = None,
) -> dict[str, Any]:
    root = require_workspace(root)
    errors = validate_company(root)
    if errors:
        raise ValueError("workspace validation failed: " + "; ".join(errors))
    status = status.upper()
    execution_basis = execution_basis.upper()
    if status not in RECEIPT_STATUSES:
        raise ValueError(f"status must be one of {', '.join(RECEIPT_STATUSES)}")
    if execution_basis not in EXECUTION_BASES:
        raise ValueError(f"execution_basis must be one of {', '.join(EXECUTION_BASES)}")
    if not actor.strip() or not action.strip() or not summary.strip():
        raise ValueError("actor, action, and summary must not be empty")
    refs = evidence_refs or []
    if execution_basis == "HOST_RECEIPT" and not refs:
        raise ValueError("HOST_RECEIPT requires at least one evidence reference")
    if execution_basis == "HUMAN_VERIFIED" and not (verified_by and verified_by.strip()):
        raise ValueError("HUMAN_VERIFIED requires verified_by")

    receipt = {
        "receipt_id": "rcpt-" + uuid.uuid4().hex,
        "timestamp": utc_now(),
        "actor": actor.strip(),
        "action": action.strip(),
        "status": status,
        "summary": summary.strip(),
        "evidence_refs": refs,
        "execution_basis": execution_basis,
        "verified_by": verified_by.strip() if verified_by else None,
    }
    path = root / "receipts" / "ledger.json"
    ledger = read_json(path)
    ledger["receipts"].append(receipt)
    write_json(path, ledger)
    append_event(root, "RECEIPT_RECORDED", {
        "receipt_id": receipt["receipt_id"],
        "execution_basis": execution_basis,
        "status": status,
    })
    return receipt


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="locality-kernel", description="LIHUO file-based Company Kernel prototype")
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init", help="initialize an empty company workspace")
    init.add_argument("--root", required=True, type=Path)
    init.add_argument("--company-id", required=True)
    init.add_argument("--name", required=True)
    init.add_argument("--owner-id", required=True)
    init.add_argument("--owner-name", required=True)
    init.add_argument("--timezone", default="UTC")

    validate = commands.add_parser("validate", help="validate an existing company workspace")
    validate.add_argument("--root", required=True, type=Path)

    department = commands.add_parser("department", help="manage generic department registry entries")
    department_commands = department.add_subparsers(dest="department_command", required=True)

    add = department_commands.add_parser("add", help="register a proposed department")
    add.add_argument("--root", required=True, type=Path)
    add.add_argument("--id", required=True)
    add.add_argument("--name", required=True)
    add.add_argument("--purpose", required=True)

    listing = department_commands.add_parser("list", help="list registered departments")
    listing.add_argument("--root", required=True, type=Path)

    change = department_commands.add_parser("status", help="change a department lifecycle status")
    change.add_argument("--root", required=True, type=Path)
    change.add_argument("--id", required=True)
    change.add_argument("--status", required=True, choices=DEPARTMENT_STATUSES)

    receipt = commands.add_parser("receipt", help="record a declared work receipt")
    receipt_commands = receipt.add_subparsers(dest="receipt_command", required=True)
    add_receipt = receipt_commands.add_parser("add", help="append a receipt to the local ledger")
    add_receipt.add_argument("--root", required=True, type=Path)
    add_receipt.add_argument("--actor", required=True)
    add_receipt.add_argument("--action", required=True)
    add_receipt.add_argument("--status", required=True, choices=RECEIPT_STATUSES)
    add_receipt.add_argument("--summary", required=True)
    add_receipt.add_argument("--evidence-ref", action="append", default=[])
    add_receipt.add_argument("--execution-basis", default="SELF_REPORTED", choices=EXECUTION_BASES)
    add_receipt.add_argument("--verified-by")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            root = initialize_company(
                args.root, args.company_id, args.name, args.owner_id, args.owner_name, args.timezone
            )
            print(f"Initialized file-based company workspace: {root}")
            print("Agent runtime and Host enforcement are not provided by this prototype.")
            return 0

        if args.command == "validate":
            errors = validate_company(args.root)
            if errors:
                for error in errors:
                    print(error, file=sys.stderr)
                return 1
            print("VALID: required files and basic invariants passed")
            return 0

        if args.command == "department":
            if args.department_command == "add":
                result = register_department(args.root, args.id, args.name, args.purpose)
                print(json.dumps(result, ensure_ascii=False, indent=2))
                return 0
            if args.department_command == "list":
                print(json.dumps(list_departments(args.root), ensure_ascii=False, indent=2))
                return 0
            if args.department_command == "status":
                result = set_department_status(args.root, args.id, args.status)
                print(json.dumps(result, ensure_ascii=False, indent=2))
                return 0

        if args.command == "receipt" and args.receipt_command == "add":
            result = record_receipt(
                args.root,
                args.actor,
                args.action,
                args.status,
                args.summary,
                args.evidence_ref,
                args.execution_basis,
                args.verified_by,
            )
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0

    except (FileExistsError, FileNotFoundError, KeyError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    parser.error("unsupported command")
    return 2
