import json
import tempfile
import unittest
from pathlib import Path

from locality_kernel.core import (
    initialize_company,
    list_departments,
    record_receipt,
    register_department,
    set_department_status,
    validate_company,
)


class CompanyKernelTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "company"
        initialize_company(
            self.root,
            company_id="test-company",
            display_name="Test Company",
            owner_id="owner-001",
            owner_display_name="Human Owner",
            timezone_name="Asia/Taipei",
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_initial_workspace_validates(self):
        self.assertEqual(validate_company(self.root), [])
        self.assertEqual(list_departments(self.root), [])

    def test_init_refuses_non_empty_directory(self):
        with self.assertRaises(FileExistsError):
            initialize_company(
                self.root,
                "another-company",
                "Another Company",
                "owner-002",
                "Another Owner",
            )

    def test_department_lifecycle(self):
        department = register_department(
            self.root, "research", "Research", "Research tasks"
        )
        self.assertEqual(department["status"], "PROPOSED")
        active = set_department_status(self.root, "research", "ACTIVE")
        self.assertEqual(active["status"], "ACTIVE")
        suspended = set_department_status(self.root, "research", "SUSPENDED")
        self.assertEqual(suspended["status"], "SUSPENDED")
        resumed = set_department_status(self.root, "research", "ACTIVE")
        self.assertEqual(resumed["status"], "ACTIVE")
        self.assertEqual(validate_company(self.root), [])

    def test_retired_department_cannot_be_reactivated(self):
        register_department(self.root, "archive", "Archive", "Archive work")
        set_department_status(self.root, "archive", "RETIRED")
        with self.assertRaises(ValueError):
            set_department_status(self.root, "archive", "ACTIVE")

    def test_receipt_requires_evidence_for_host_receipt(self):
        with self.assertRaises(ValueError):
            record_receipt(
                self.root,
                actor="local-agent",
                action="create-resource",
                status="PASS",
                summary="A resource was created",
                execution_basis="HOST_RECEIPT",
            )

    def test_human_verified_receipt_requires_verifier(self):
        with self.assertRaises(ValueError):
            record_receipt(
                self.root,
                actor="local-agent",
                action="review",
                status="PASS",
                summary="Review completed",
                execution_basis="HUMAN_VERIFIED",
            )

    def test_self_reported_receipt_is_explicitly_labelled(self):
        receipt = record_receipt(
            self.root,
            actor="local-agent",
            action="draft-plan",
            status="PARTIAL",
            summary="Draft created; not independently verified",
        )
        self.assertEqual(receipt["execution_basis"], "SELF_REPORTED")
        ledger = json.loads((self.root / "receipts" / "ledger.json").read_text(encoding="utf-8"))
        self.assertEqual(len(ledger["receipts"]), 1)

    def test_company_id_mismatch_is_detected(self):
        registry_path = self.root / "registry" / "departments.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["company_id"] = "wrong-company"
        registry_path.write_text(json.dumps(registry), encoding="utf-8")
        self.assertTrue(any("COMPANY_ID_MISMATCH" in error for error in validate_company(self.root)))


if __name__ == "__main__":
    unittest.main()
