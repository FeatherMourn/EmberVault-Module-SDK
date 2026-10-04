import unittest

from embervault_sdk import is_compatible, validate_manifest


def manifest():
    return {
        "id": "embervault.example",
        "name": "Example",
        "version": "1.0.0",
        "publisher": "EmberVault",
        "capabilities": ["example"],
        "feature_state": "experimental",
        "process_mode": "embedded",
        "contract_version": 1,
        "safety": {"read_only": True, "requires_backup": False},
        "recovery": {"rollback": "Discard plan", "verification": "No live files touched"},
        "operation_types": ["example-check"],
    }


class ManifestTests(unittest.TestCase):
    def test_valid_manifest_is_compatible(self):
        self.assertEqual(validate_manifest(manifest()), [])
        self.assertTrue(is_compatible(manifest()))

    def test_missing_safety_is_blocked(self):
        value = manifest()
        del value["safety"]
        self.assertTrue(validate_manifest(value))
        self.assertFalse(is_compatible(value))

    def test_unknown_contract_version_is_blocked(self):
        value = manifest()
        value["contract_version"] = 99
        self.assertTrue(validate_manifest(value))
        self.assertFalse(is_compatible(value))


if __name__ == "__main__":
    unittest.main()
