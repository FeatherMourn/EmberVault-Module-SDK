from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class ModuleContext:
    module_id: str
    profile_id: str | None
    operation_id: str | None
    capability_state: str = "plan-only"
    backup_id: str | None = None

@dataclass(frozen=True)
class ModuleResult:
    status: str
    message: str
    data: dict[str, Any] = field(default_factory=dict)
    contract_version: int = 1

    def to_dict(self) -> dict[str, Any]:
        return {"contract_version": self.contract_version, "status": self.status,
                "message": self.message, "data": dict(self.data)}
