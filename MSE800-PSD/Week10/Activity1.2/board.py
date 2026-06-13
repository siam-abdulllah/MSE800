"""Board state and win/draw rules for Tic Tac Toe."""

from player import Player


class Board:
    """3x3 Tic Tac Toe board."""

    SIZE = 3

    def __init__(self) -> None:
        self._cells = [
            [" " for _ in range(self.SIZE)] for _ in range(self.SIZE)
        ]

    @property
    def cells(self) -> list[list[str]]:
        """Return the current board grid."""
        return self._cells

    def is_empty(self, row: int, col: int) -> bool:
        """Return True if the cell at row, col is unoccupied."""
        return self._cells[row][col] == " "

    def apply_move(self, row: int, col: int, player: Player) -> None:
        """Place a player's symbol on the board."""
        self._cells[row][col] = player.symbol

    def has_winner(self, player: Player) -> bool:
        """Return True if the given player has three in a row."""
        grid = self._cells
        symbol = player.symbol
        lines = (
            *grid,
            *[[grid[r][c] for r in range(self.SIZE)] for c in range(self.SIZE)],
            [grid[i][i] for i in range(self.SIZE)],
            [grid[i][self.SIZE - 1 - i] for i in range(self.SIZE)],
        )
        return any(all(cell == symbol for cell in line) for line in lines)

    def is_draw(self) -> bool:
        """Return True if the board is full with no winner."""
        return all(cell != " " for row in self._cells for cell in row)
