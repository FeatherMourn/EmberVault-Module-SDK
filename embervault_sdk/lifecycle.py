from typing import Protocol

from .contracts import ModuleContext, ModuleResult


class ModuleLifecycle(Protocol):
    """Optional lifecycle boundary implemented by an EmberVault module."""

    def describe(self) -> dict: ...

    def initialize(self, context: ModuleContext) -> ModuleResult: ...

    def shutdown(self, context: ModuleContext) -> ModuleResult: ...
