"""Terminal-based Tic Tac Toe game for two players."""

import game
import ui


def main() -> None:
    print("===== Tic Tac Toe =====")
    print("Player X goes first. Enter moves as row and column (1-3).")

    while True:
        game.play_game()
        if not ui.ask_play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
