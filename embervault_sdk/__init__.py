"""Dependency-free helpers shared by EmberVault modules."""
from .contracts import ModuleContext, ModuleResult
from .lifecycle import ModuleLifecycle
__all__ = ["ModuleContext", "ModuleResult", "ModuleLifecycle"]
