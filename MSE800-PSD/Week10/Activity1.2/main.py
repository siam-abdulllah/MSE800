"""Terminal-based Tic Tac Toe game for two players."""

from game import TicTacToeGame
from terminal import TerminalUI


class TicTacToeApp:
    """Application entry point and replay loop."""

    def __init__(self) -> None:
        self._ui = TerminalUI()
        self._game = TicTacToeGame(self._ui)

    def run(self) -> None:
        """Start the application and handle replay."""
        self._ui.show_welcome()

        while True:
            self._game.play()
            if not self._ui.ask_play_again():
                self._ui.show_goodbye()
                break


def main() -> None:
    """Run the Tic Tac Toe application."""
    TicTacToeApp().run()


if __name__ == "__main__":
    main()
