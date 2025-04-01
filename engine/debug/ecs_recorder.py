import csv
import os
import threading
from datetime import datetime

from engine.debug.dir_setup import DEBUG_DIR


class ECSRecorder:
    def __init__(self, log_file=os.path.join(DEBUG_DIR, "ecs_record.csv")):
        self._log = []
        self._lock = threading.Lock()
        self._log_file = log_file
        with open(self._log_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Tick", "Timestamp", "Entity", "Component", "Data"])

    def record(self, entity_id: int, component_name: str, data: dict[str, any], tick: int = -1):
        timestamp = datetime.now().isoformat()
        log_entry = (tick, timestamp, entity_id, component_name, data)
        threading.Thread(target=self._async_store, args=(log_entry,), daemon=True).start()

    def _async_store(self, entry):
        with self._lock:
            self._log.append(entry)
            with open(self._log_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(entry)

    def get_log(self):
        return self._log.copy()

recorder = ECSRecorder()
