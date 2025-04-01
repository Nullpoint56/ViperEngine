from dataclasses import dataclass


@dataclass
class UITransform:
    x: float
    y: float
    width: float
    height: float

@dataclass
class TextComponent:
    text: str

@dataclass
class ButtonComponent:
    id: str
    clicked: bool = False
    hovered: bool = False

@dataclass
class SceneTag:
    name: str
