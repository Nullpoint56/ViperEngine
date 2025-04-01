import threading
from datetime import datetime


class ECSRecorder:
    def __init__(self, log_file="ecs_record.log"):
        self._log = []
        self._lock = threading.Lock()
        self._log_file = log_file
        with open(self._log_file, "w") as f:
            f.write("# ECS Record Log\n")

    def record(self, entity_id: int, component_name: str, data: dict[str, any], tick: int = -1):
        timestamp = datetime.now().isoformat()
        log_entry = (tick, timestamp, entity_id, component_name, data)
        threading.Thread(target=self._async_store, args=(log_entry,), daemon=True).start()

    def _async_store(self, entry):
        with self._lock:
            self._log.append(entry)
            with open(self._log_file, "a") as f:
                f.write(str(entry) + "\n")

    def get_log(self):
        return self._log.copy()

recorder = ECSRecorder()