from multiprocessing import Process, Queue


class TaskManager:
    def __init__(self):
        self.systems = []

    def register_system(self, system_func):
        self.systems.append(system_func)

    def run_all(self, snapshot: dict[str, any]):
        entity_ids = list(snapshot['entities'].keys())
        batch_size = max(1, len(entity_ids) // 2)
        batches = [entity_ids[i:i + batch_size] for i in range(0, len(entity_ids), batch_size)]

        all_commands = []
        for system in self.systems:
            processes = []
            queues = []

            for batch in batches:
                q = Queue()
                p = Process(target=system, args=(snapshot, batch, q))
                p.start()
                processes.append(p)
                queues.append(q)

            for p in processes:
                p.join()

            for q in queues:
                if not q.empty():
                    all_commands.extend(q.get())

        return all_commands