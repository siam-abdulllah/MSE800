"""Terminal display and input for Tic Tac Toe."""

from board import Board, Player


def print_board(board: Board) -> None:
    print("\n    1   2   3")
    for row_index, row in enumerate(board, start=1):
        print("  +---+---+---+")
        cells = " | ".join(cell if cell != " " else " " for cell in row)
        print(f"{row_index} | {cells} |")
    print("  +---+---+---+\n")


def get_move(board: Board, player: Player) -> tuple[int, int]:
    while True:
        raw = input(f"Player {player}, enter row and column (e.g. 1 2): ").strip()

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

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid position. Row and column must be between 1 and 3.")
            continue

        if board[row][col] != " ":
            print("That cell is already taken. Choose another one.")
            continue

        return row, col


def announce_winner(player: Player) -> None:
    print(f"Player {player} wins!")


def announce_draw() -> None:
    print("It's a draw!")


def ask_play_again() -> bool:
    while True:
        choice = input("Play again? (y/n): ").strip().lower()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no"}:
            return False
        print("Please enter y or n.")
