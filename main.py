from game.main_menu_loop import run_main_menu
from game.states import GameState

if __name__ == "__main__":
    game_state = [GameState.MAIN_MENU]  # Wrapped in list to be mutable

    print("Initial state:", game_state[0].name)
    run_main_menu(game_state)
    print("After menu interaction:", game_state[0].name)