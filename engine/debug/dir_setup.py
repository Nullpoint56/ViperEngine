import os
from datetime import datetime

DEBUG_DIR = os.path.join("debug_logs", datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
os.makedirs(DEBUG_DIR, exist_ok=True)
