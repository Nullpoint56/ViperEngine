import csv
import functools
import os
import time
from datetime import datetime

from engine.debug.dir_setup import DEBUG_DIR

tick_counter = [0]
PROFILER_LOG_FILE = os.path.join(DEBUG_DIR, "profiler.csv")
with open(PROFILER_LOG_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Tick", "Timestamp", "Tag", "DurationSeconds"])

def profile(tag: str, log_file=PROFILER_LOG_FILE):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            tick_counter[0] += 1
            timestamp = datetime.now().isoformat()
            print(f"[PROFILE] {tag} (Tick {tick_counter[0]:04d} @ {timestamp}): {duration:.6f}s")
            with open(log_file, "a", newline="") as profiler_log:
                profiler_writer = csv.writer(profiler_log)
                profiler_writer.writerow([tick_counter[0], timestamp, tag, duration])
            return result
        return wrapper
    return decorator