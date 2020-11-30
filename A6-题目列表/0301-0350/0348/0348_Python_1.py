class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """


if __name__ == "__main__":
    obj = TicTacToe(3)
    print(obj.move(0, 0, 1))  # 0
    print(obj.move(0, 2, 2))  # 0
    print(obj.move(2, 2, 1))  # 0
    print(obj.move(1, 1, 2))  # 0
    print(obj.move(2, 0, 1))  # 0
    print(obj.move(1, 0, 2))  # 0
    print(obj.move(2, 1, 1))  # 1
