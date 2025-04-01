from enum import Enum


class GameState(Enum):
    MAIN_MENU = 1
    PLAYING = 2
    SETTINGS = 3
    EXIT = 4