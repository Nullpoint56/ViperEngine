from engine.core.config import CONFIG


class WindowManager:
    def __init__(self, config):
        self.width = config["window"]["width"]
        self.height = config["window"]["height"]
        self.fullscreen = config["window"]["fullscreen"]

    def apply_config(self, config):
        self.width = config["window"]["width"]
        self.height = config["window"]["height"]
        self.fullscreen = config["window"]["fullscreen"]
        print(f"[WindowManager] Applied: {self.width}x{self.height}, fullscreen={self.fullscreen}")

WINDOW_MANAGER = WindowManager(CONFIG)