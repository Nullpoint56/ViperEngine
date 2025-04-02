from typing import Mapping

import tomli
import tomli_w
import asyncio
import aiofiles
from collections import defaultdict
from types import MappingProxyType
import os

class ConfigManager:
    def __init__(self, config_path: str):
        self._config_path = config_path
        self._full_config: dict[str, any] = {}
        self._subscribers = defaultdict(list)
        self._lock = asyncio.Lock()

    async def load_from_file(self):
        async with aiofiles.open(self._config_path, "rb") as f:
            content = await f.read()
            self._full_config = tomli.loads(content)

    def get_snapshot(self) -> Mapping[str, any]:
        return MappingProxyType(self._full_config)

    def register(self, section: str, system):
        self._subscribers[section].append(system)
        if section in self._full_config:
            system.on_config_update(section, self._full_config[section])

    async def update_section(self, section: str, new_value: dict[str, any]):
        async with self._lock:
            self._full_config[section] = new_value
            await self._write_config()
            for sys in self._subscribers.get(section, []):
                sys.on_config_update(section, new_value)

    async def _write_config(self):
        async with aiofiles.open(self._config_path, "w") as f:
            content = tomli_w.dumps(self._full_config)
            await f.write(content)

    async def watch_for_changes(self, interval: float = 1.0):
        last_modified = os.path.getmtime(self._config_path)
        while True:
            await asyncio.sleep(interval)
            current_modified = os.path.getmtime(self._config_path)
            if current_modified != last_modified:
                await self.load_from_file()
                last_modified = current_modified
                for section, subscribers in self._subscribers.items():
                    if section in self._full_config:
                        for sys in subscribers:
                            sys.on_config_update(section, self._full_config[section])
