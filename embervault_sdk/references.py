"""Validation helpers for shared evidence and recovery references."""
from __future__ import annotations

from typing import Any

EVIDENCE_KINDS = {"research", "runtime", "static", "test", "build", "user-report"}
EVIDENCE_STATES = {"observed", "inferred", "hypothesis", "verified", "blocked"}


def validate_evidence_reference(value: dict[str, Any]) -> list[str]:
    if not isinstance(value, dict):
        return ["Evidence reference must be an object."]
    issues = [f"Missing evidence field: {key}" for key in ("id", "kind", "state", "summary") if key not in value]
    if not isinstance(value.get("id"), str) or not value.get("id", "").strip():
        issues.append("Evidence id must be non-empty.")
    if value.get("kind") not in EVIDENCE_KINDS:
        issues.append("Evidence kind is invalid.")
    if value.get("state") not in EVIDENCE_STATES:
        issues.append("Evidence state is invalid.")
    if not isinstance(value.get("summary"), str) or not value.get("summary", "").strip():
        issues.append("Evidence summary must be non-empty.")
    return issues


def validate_recovery_reference(value: dict[str, Any]) -> list[str]:
    if not isinstance(value, dict):
        return ["Recovery reference must be an object."]
    issues = [f"Missing recovery field: {key}" for key in ("expectation", "rollback", "verification", "backup_required") if key not in value]
    for key in ("expectation", "rollback", "verification"):
        if not isinstance(value.get(key), str) or not value.get(key, "").strip():
            issues.append(f"Recovery {key} must be non-empty.")
    if not isinstance(value.get("backup_required"), bool):
        issues.append("Recovery backup_required must be boolean.")
    return issues
