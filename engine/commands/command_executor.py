from engine.commands.command import Command
from engine.ecs.registry import Registry
from game.states import GameState


class CommandExecutor:
    def __init__(self, registry: Registry):
        self.registry = registry

    def apply(self, command: Command, game_state_ref):
        if command.type == 'ChangeState':
            game_state_ref[0] = GameState[command.data['state']]