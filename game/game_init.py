import asyncio

from engine.core.config import ConfigManager


async def game_init():
    config_mgr = ConfigManager("config/config.toml")
    await config_mgr.load_from_file()
    asyncio.create_task(config_mgr.watch_for_changes())

    return config_mgr