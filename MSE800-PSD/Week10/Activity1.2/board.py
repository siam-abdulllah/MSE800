"""Board state and win/draw rules for Tic Tac Toe."""

Board = list[list[str]]
Player = str


def create_board() -> Board:
    return [[" " for _ in range(3)] for _ in range(3)]


def check_winner(board: Board, player: Player) -> bool:
    lines = (
        *board,
        [[board[r][c] for r in range(3)] for c in range(3)],
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)],
    )
    return any(all(cell == player for cell in line) for line in lines)


def is_draw(board: Board) -> bool:
    return all(cell != " " for row in board for cell in row)


def other_player(player: Player) -> Player:
    return "O" if player == "X" else "X"


def apply_move(board: Board, row: int, col: int, player: Player) -> None:
    board[row][col] = player
