from typing import Callable

from engine.commands.command import Command
from engine.debug.ecs_recorder import recorder
from engine.utilities.profiler import tick_counter


class CommandBus:
    def __init__(self):
        self.subscribers: dict[str, list[Callable[[Command], None]]] = {}

    def subscribe(self, command_type: str, handler: Callable[[Command], None]):
        if command_type not in self.subscribers:
            self.subscribers[command_type] = []
        self.subscribers[command_type].append(handler)

    def dispatch(self, command: Command):
        handlers = self.subscribers.get(command.type, [])
        for handler in handlers:
            handler(command)

command_bus = CommandBus()
command_bus.subscribe("ChangeState", lambda cmd: recorder.record(cmd.entity, "GameState", cmd.data, tick_counter[0]))

