from abc import ABC, abstractmethod
from typing import Literal, Union

from engine.base.command import BaseCommand
from engine.base.types import ExecutionMode


class BaseSystem(ABC):
    """
    Base ECS System. Defines lifecycle hooks and is meant to be inherited.
    Every system should declare an execution_mode and optionally override lifecycle methods.
    """
    execution_mode: ExecutionMode = "sync"
    priority: Union[int, Literal["realtime", "high", "normal", "low"]] = "low"

    def __init__(self):
        self._config: dict[str, any] = {}

    def on_config_update(self, section: str, config_value: dict[str, any]):
        """
        Optional. Called by ConfigManager when the config section for this system is updated.
        """
        self._config = config_value

    @staticmethod
    def should_tick() -> bool:
        """
        Optional. Override to control when the system should run.
        Useful for skipping systems when paused.
        """
        return True

    @abstractmethod
    def update(self, snapshot: dict[str, any], entities: list[int], queue: any) -> list[BaseCommand]:
        """
        Required for all systems. Must emit commands to the output queue.
        Should be multiprocessing/thread-safe.
        """
        pass


class BaseAsyncSystem(BaseSystem):
    execution_mode: ExecutionMode = "async"

    @abstractmethod
    async def update(self, snapshot: dict[str, any], entities: list[int], queue: any) -> list[BaseCommand]:
        pass


class BaseThreadedSystem(BaseSystem):
    execution_mode: ExecutionMode = "thread"

    @abstractmethod
    def update(self, snapshot: dict[str, any], entities: list[int], queue: any) -> list[BaseCommand]:
        pass


class BaseProcessSystem(BaseSystem):
    execution_mode: ExecutionMode = "process"

    @staticmethod
    def prepare_data(snapshot: dict[str, any], entities: list[int]) -> dict[str, any]:
        """
        Optional: Override this to prepare minimal, pickle-safe data for the subprocess.
        Called before the system is dispatched to a separate process.
        """
        return {"snapshot": snapshot, "entities": entities}

    def update(self, snapshot: dict[str, any], entities: list[int], queue: any) -> list[BaseCommand]:
        """
        Override the base signature but delegate to the process-specific logic.
        """
        return self.process_update(self.prepare_data(snapshot, entities), queue)

    @abstractmethod
    def process_update(self, prepared_data: dict[str, any], queue: any) -> list[BaseCommand]:
        """
        Main process-safe update method.
        """
        pass
