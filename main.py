from engine.debug.ecs_recorder import recorder
from game.main_menu_loop import run_main_menu
from game.states import GameState

if __name__ == "__main__":
    game_state = [GameState.MAIN_MENU]  # Wrapped in list to be mutable

    print("Initial state:", game_state[0].name)
    run_main_menu(game_state)
    print("After menu interaction:", game_state[0].name)

    print("\nRecorded ECS State Changes:")
    for entry in recorder.get_log():
        print(entry)