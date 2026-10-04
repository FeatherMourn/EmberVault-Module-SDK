"""Dependency-free helpers shared by EmberVault modules."""
from .contracts import ModuleContext, ModuleResult
from .lifecycle import ModuleLifecycle
from .manifest import is_compatible, validate_manifest
__all__ = ["ModuleContext", "ModuleResult", "ModuleLifecycle", "is_compatible", "validate_manifest"]
