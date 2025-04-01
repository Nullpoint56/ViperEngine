from dataclasses import dataclass


@dataclass
class Command:
    type: str
    entity: int
    data: dict[str, any]