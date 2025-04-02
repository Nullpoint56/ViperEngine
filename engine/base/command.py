# === Command Base ===
from abc import ABC, abstractmethod


class BaseCommand(ABC):
    """
    Base class for all ECS-emitted commands.
    Commands encapsulate side effects or actions triggered by systems,
    and are processed after all systems finish their update cycle.
    """

    @abstractmethod
    def execute(self, engine_context: any):
        """
        Called by the CommandExecutor. Applies the command to the engine or game state.
        """
        pass
