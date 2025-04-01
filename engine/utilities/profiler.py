import functools
import time
from datetime import datetime

tick_counter = [0]  # mutable counter to track tick/frame

def profile(tag: str, log_file="profiler.log"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            tick_counter[0] += 1
            timestamp = datetime.now().isoformat()
            tick_info = f"Tick {tick_counter[0]:04d} @ {timestamp}"
            print(f"[PROFILE] {tag} ({tick_info}): {duration:.6f}s")
            with open(log_file, "a") as f:
                f.write(f"{tick_info} | {tag}: {duration:.6f}s\n")
            return result
        return wrapper
    return decorator