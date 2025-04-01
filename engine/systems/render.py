from engine.components.components import Renderable
from engine.ecs.contracts import SystemContract
from engine.systems.base import System
import math
import random

class RenderSystem(System):
    contract = SystemContract((Renderable,))

    def update(self, entities: dict[int, tuple], dt: float):
        for _, (r,) in entities.items():
            angle = random.random() * 360
            x, y, z = 1, 0, 0.5
            for _ in range(30):
                cos = math.cos(angle)
                sin = math.sin(angle)
                y, z = y * cos - z * sin, y * sin + z * cos
                x, z = x * cos + z * sin, -x * sin + z * cos
                x, y = x * cos - y * sin, x * sin + y * cos
                angle += 0.01
