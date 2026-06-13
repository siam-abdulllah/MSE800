"""Game loop for a single Tic Tac Toe match."""

from typing import Optional

import board
import ui


def play_game() -> Optional[board.Player]:
    game_board = board.create_board()
    current_player: board.Player = "X"

    while True:
        ui.print_board(game_board)
        row, col = ui.get_move(game_board, current_player)
        board.apply_move(game_board, row, col, current_player)

        if board.check_winner(game_board, current_player):
            ui.print_board(game_board)
            ui.announce_winner(current_player)
            return current_player

        if board.is_draw(game_board):
            ui.print_board(game_board)
            ui.announce_draw()
            return None

        current_player = board.other_player(current_player)
