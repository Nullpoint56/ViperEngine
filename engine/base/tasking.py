from abc import ABC, abstractmethod


class BaseScheduler(ABC):
    @abstractmethod
    def get_schedule(self, systems: list, snapshot: dict[str, any]) -> list[tuple]:
        """
        Returns a list of (system, batch) tuples ordered by the scheduling strategy.
        """
        pass


class BaseTaskManager(ABC):

    @abstractmethod
    def register_system(self, system_func):
        pass

    @abstractmethod
    def run_all(self, snapshot: dict[str, any]):
        pass
