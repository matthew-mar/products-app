from dataclasses import dataclass, asdict
from typing import TypedDict


class ProductKeys(TypedDict):
    name: str
    price: float
    id: int|None = None
    description: str|None = None


@dataclass
class ProductDTO:
    name: str
    price: float
    id: int|None = None
    description: str|None = None

    @property
    def dict(self) -> ProductKeys:
        return asdict(self)
