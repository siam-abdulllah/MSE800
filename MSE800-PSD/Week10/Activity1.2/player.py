"""Player representation for Tic Tac Toe."""


class Player:
    """A player identified by board symbol X or O."""

    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def other(self) -> "Player":
        """Return the opposing player."""
        return Player("O" if self.symbol == "X" else "X")

    def __str__(self) -> str:
        return self.symbol
