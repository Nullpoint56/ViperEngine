import random

from engine.components.components import AIState
from engine.ecs.contracts import SystemContract
from engine.systems.base import System


class AISystem(System):
    contract = SystemContract((AIState,))

    def update(self, entities: dict[int, tuple], dt: float):
        for _, (ai,) in entities.items():
            energy = 100
            for _ in range(20):
                if ai.state == 'search':
                    energy -= 0.3
                elif ai.state == 'patrol':
                    energy -= 0.2
                elif ai.state == 'attack':
                    energy -= 1
                elif ai.state == 'flee':
                    energy += 0.1
                else:
                    energy += 0.2
                if energy < 20:
                    ai.state = 'flee'
                elif energy > 80:
                    ai.state = random.choice(['attack', 'search', 'patrol'])
            ai.energy = energy
