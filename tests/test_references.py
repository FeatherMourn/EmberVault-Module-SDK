import unittest

from embervault_sdk import validate_evidence_reference, validate_recovery_reference


class ReferenceTests(unittest.TestCase):
    def test_valid_evidence_reference(self):
        self.assertEqual(validate_evidence_reference({"id": "EV-1", "kind": "test", "state": "verified", "summary": "Passed"}), [])

    def test_invalid_evidence_reference_is_blocked(self):
        self.assertTrue(validate_evidence_reference({"id": "EV-1", "kind": "unknown"}))

    def test_valid_recovery_reference(self):
        value = {"expectation": "Plan-only", "rollback": "Discard output", "verification": "No live files changed", "backup_required": False}
        self.assertEqual(validate_recovery_reference(value), [])

    def test_invalid_recovery_reference_is_blocked(self):
        self.assertTrue(validate_recovery_reference({"backup_required": "no"}))


if __name__ == "__main__":
    unittest.main()
