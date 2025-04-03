import asyncio
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Queue as ProcessQueue, Process
from queue import Queue as ThreadQueue

from engine.base.system import BaseSystem, BaseProcessSystem
from engine.base.tasking import BaseScheduler


class TaskManager:
    def __init__(self, scheduler: BaseScheduler, max_workers=4):
        self.systems: list[BaseSystem] = []
        self.scheduler = scheduler
        self.thread_pool = ThreadPoolExecutor(max_workers=max_workers)
        self.loop = asyncio.get_event_loop()

    def register_system(self, system: BaseSystem):
        self.systems.append(system)

    async def run_all(self, snapshot: dict[str, any]):
        schedule = self.scheduler.get_schedule(self.systems, snapshot)
        all_commands = []
        tasks = []

        for system, batch in schedule:
            if system.execution_mode == "process":
                q = ProcessQueue()
                p = Process(target=self._run_process_system, args=(system, snapshot, batch, q))
                p.start()
                p.join()
                if not q.empty():
                    all_commands.extend(q.get())

            elif system.execution_mode == "thread":
                q = ThreadQueue()
                fut = self.thread_pool.submit(system.update, snapshot, batch, q)
                fut.result()
                if not q.empty():
                    all_commands.extend(q.get())

            elif system.execution_mode == "async":
                q = asyncio.Queue()
                await system.update(snapshot, batch, q)
                while not q.empty():
                    all_commands.extend(await q.get())

            else:  # sync
                q = ThreadQueue()
                system.update(snapshot, batch, q)
                if not q.empty():
                    all_commands.extend(q.get())

        return all_commands

    @staticmethod
    def _run_process_system(system: BaseProcessSystem, snapshot, batch, queue):
        prepared = system.prepare_data(snapshot, batch)
        system.process_update(prepared, queue)
