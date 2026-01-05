from dataclasses import asdict, dataclass
from typing import Self


@dataclass(slots=True, frozen=True)
class DataTransferObject:
    
    def to_dict(self) -> dict[str, object]:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict[str, object]) -> Self:
        return cls(**data)
    