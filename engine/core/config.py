import json
import os


class ConfigManager:
    CONFIG_DIR = "config"
    CONFIG_FILE = os.path.join(CONFIG_DIR, "engine_config.json")
    DEFAULT_CONFIG = {
        "window": {
            "width": 1280,
            "height": 720,
            "fullscreen": False
        },
        "audio": {
            "volume": 0.8,
            "muted": False
        },
        "debug": {
            "log_profiling": True,
            "log_recording": True
        }
    }

    def __init__(self):
        os.makedirs(self.CONFIG_DIR, exist_ok=True)
        self.config = self._load()

    def _load(self):
        if not os.path.exists(self.CONFIG_FILE):
            with open(self.CONFIG_FILE, "w") as f:
                json.dump(self.DEFAULT_CONFIG, f, indent=4)
            return self.DEFAULT_CONFIG.copy()
        with open(self.CONFIG_FILE, "r") as f:
            return json.load(f)

    def save(self):
        with open(self.CONFIG_FILE, "w") as f:
            json.dump(self.config, f, indent=4)

    def get(self, path: str, default=None):
        keys = path.split(".")
        value = self.config
        for key in keys:
            value = value.get(key)
            if value is None:
                return default
        return value

    def update(self, path: str, new_value):
        keys = path.split(".")
        ref = self.config
        for key in keys[:-1]:
            ref = ref.setdefault(key, {})
        ref[keys[-1]] = new_value
        self.save()

CONFIG_MANAGER = ConfigManager()
CONFIG = CONFIG_MANAGER.config