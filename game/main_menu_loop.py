from multiprocessing import Queue

import pygame

from engine.commands.command_executor import CommandExecutor
from engine.ecs.registry import Registry
from engine.systems.input import UIInputSystem
from engine.systems.menu_ui import MenuUISystem
from engine.systems.ui_render import UIRenderSystem
from engine.utilities.profiler import profile
from game.scenes.ui_scene_manager import load_main_menu_ui
from game.states import GameState

@profile("MainMenuLoop")
def run_main_menu(game_state):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("ECS Main Menu")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    registry = Registry()
    executor = CommandExecutor(registry)
    load_main_menu_ui(registry)

    running = True
    while running and game_state[0] == GameState.MAIN_MENU:
        screen.fill((30, 30, 30))
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and render ECS systems
        UIInputSystem(registry, mouse_pos, mouse_pressed)
        UIRenderSystem(screen, registry, font, active_scene="main_menu")

        # Handle logic (1 frame ECS simulation)
        snapshot = registry.create_snapshot()
        command_queue = Queue()
        MenuUISystem(snapshot, list(snapshot['entities'].keys()), command_queue)

        if not command_queue.empty():
            for cmd in command_queue.get():
                executor.apply(cmd, game_state)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()