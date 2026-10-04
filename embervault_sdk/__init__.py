"""Dependency-free helpers shared by EmberVault modules."""
from .contracts import ModuleContext, ModuleResult
from .lifecycle import ModuleLifecycle
from .manifest import is_compatible, validate_manifest
from .references import validate_evidence_reference, validate_recovery_reference
__all__ = ["ModuleContext", "ModuleResult", "ModuleLifecycle", "is_compatible", "validate_manifest", "validate_evidence_reference", "validate_recovery_reference"]
