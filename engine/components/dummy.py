from dataclasses import dataclass


@dataclass
class Position:
    x: float
    y: float

@dataclass
class Velocity:
    dx: float
    dy: float

@dataclass
class Command:
    type: str
    entity: int
    data: dict[str, any]