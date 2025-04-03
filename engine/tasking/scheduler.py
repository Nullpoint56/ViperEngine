import heapq

from engine.base.tasking import BaseScheduler


class PriorityRoundRobinScheduler(BaseScheduler):
    @staticmethod
    def _get_priority_value(priority):
        mapping = {"realtime": -1000, "high": -100, "normal": 0, "low": 100}
        return mapping.get(priority, priority if isinstance(priority, int) else 0)

    def get_schedule(self, systems: list, snapshot: dict[str, any]) -> list[tuple]:
        entity_ids = list(snapshot['entities'].keys())
        batch_size = max(1, len(entity_ids) // 2)
        batches = [entity_ids[i:i + batch_size] for i in range(0, len(entity_ids), batch_size)]

        pq = []
        rr_order = 0
        for system in systems:
            if not system.should_tick():
                continue
            prio = self._get_priority_value(system.priority)
            for batch in batches:
                heapq.heappush(pq, (prio, rr_order, system, batch))
                rr_order += 1

        schedule = []
        while pq:
            _, _, sys, batch = heapq.heappop(pq)
            schedule.append((sys, batch))
        return schedule
