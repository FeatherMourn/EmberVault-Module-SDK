"""Small, dependency-free helpers for validating module manifests."""
from __future__ import annotations

from typing import Any

SUPPORTED_CONTRACT_VERSION = 1
ALLOWED_FEATURE_STATES = {"stable", "verified", "experimental", "research-only", "blocked"}
ALLOWED_PROCESS_MODES = {"embedded", "separate"}


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    """Return human-readable issues without executing or importing a module."""
    issues: list[str] = []
    if not isinstance(manifest, dict):
        return ["Module manifest must be an object."]
    required = ("id", "name", "version", "publisher", "capabilities",
                "feature_state", "process_mode", "contract_version",
                "safety", "recovery", "operation_types")
    for key in required:
        if key not in manifest:
            issues.append(f"Missing manifest field: {key}")
    module_id = manifest.get("id")
    if not isinstance(module_id, str) or not module_id.startswith("embervault."):
        issues.append("Module id must start with 'embervault.'")
    if manifest.get("contract_version") != SUPPORTED_CONTRACT_VERSION:
        issues.append("Unsupported module contract version.")
    if manifest.get("feature_state") not in ALLOWED_FEATURE_STATES:
        issues.append("Unsupported module feature state.")
    if manifest.get("process_mode") not in ALLOWED_PROCESS_MODES:
        issues.append("Unsupported module process mode.")
    for key in ("capabilities", "operation_types"):
        value = manifest.get(key)
        if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
            issues.append(f"{key} must be a list of non-empty strings.")
    safety = manifest.get("safety")
    if not isinstance(safety, dict) or not isinstance(safety.get("read_only"), bool) or not isinstance(safety.get("requires_backup"), bool):
        issues.append("Safety must declare boolean read_only and requires_backup fields.")
    recovery = manifest.get("recovery")
    if not isinstance(recovery, dict) or any(not isinstance(recovery.get(key), str) or not recovery[key].strip() for key in ("rollback", "verification")):
        issues.append("Recovery must declare rollback and verification text.")
    return issues


def is_compatible(manifest: dict[str, Any], contract_version: int = SUPPORTED_CONTRACT_VERSION) -> bool:
    return not validate_manifest({**manifest, "contract_version": manifest.get("contract_version")}) and manifest.get("contract_version") == contract_version
