"""Game loop for a single Tic Tac Toe match."""

from typing import Optional

from board import Board
from player import Player
from terminal import TerminalUI


class TicTacToeGame:
    """Runs one Tic Tac Toe match between two players."""

    def __init__(self, ui: TerminalUI) -> None:
        self._ui = ui

    def play(self) -> Optional[Player]:
        """Play a single game and return the winner, or None for a draw."""
        board = Board()
        current_player = Player("X")

        while True:
            self._ui.display_board(board)
            row, col = self._ui.prompt_move(board, current_player)
            board.apply_move(row, col, current_player)

            if board.has_winner(current_player):
                self._ui.display_board(board)
                self._ui.announce_winner(current_player)
                return current_player

            if board.is_draw():
                self._ui.display_board(board)
                self._ui.announce_draw()
                return None

            current_player = current_player.other()
