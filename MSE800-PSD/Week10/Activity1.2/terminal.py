"""Terminal display and input for Tic Tac Toe."""

from board import Board
from player import Player


class TerminalUI:
    """Handles terminal output and user input."""

    def show_welcome(self) -> None:
        """Display the game title and instructions."""
        print("===== Tic Tac Toe =====")
        print("Player X goes first. Enter moves as row and column (1-3).")

    def show_goodbye(self) -> None:
        """Display the exit message."""
        print("Thanks for playing!")

    def display_board(self, board: Board) -> None:
        """Print the current board with row and column labels."""
        print("\n    1   2   3")
        for row_index, row in enumerate(board.cells, start=1):
            print("  +---+---+---+")
            cells = " | ".join(cell if cell != " " else " " for cell in row)
            print(f"{row_index} | {cells} |")
        print("  +---+---+---+\n")

    def prompt_move(self, board: Board, player: Player) -> tuple[int, int]:
        """Prompt until the player enters a valid move."""
        while True:
            raw = input(
                f"Player {player}, enter row and column (e.g. 1 2): "
            ).strip()

            parts = raw.replace(",", " ").split()
            if len(parts) != 2:
                print("Invalid input. Use two numbers between 1 and 3.")
                continue

            try:
                row = int(parts[0]) - 1
                col = int(parts[1]) - 1
            except ValueError:
                print("Invalid input. Row and column must be numbers.")
                continue

            if not (0 <= row < Board.SIZE and 0 <= col < Board.SIZE):
                print("Invalid position. Row and column must be between 1 and 3.")
                continue

            if not board.is_empty(row, col):
                print("That cell is already taken. Choose another one.")
                continue

            return row, col

    def announce_winner(self, player: Player) -> None:
        """Print the winner message."""
        print(f"Player {player} wins!")

    def announce_draw(self) -> None:
        """Print the draw message."""
        print("It's a draw!")

    def ask_play_again(self) -> bool:
        """Ask whether to start another game."""
        while True:
            choice = input("Play again? (y/n): ").strip().lower()
            if choice in {"y", "yes"}:
                return True
            if choice in {"n", "no"}:
                return False
            print("Please enter y or n.")
