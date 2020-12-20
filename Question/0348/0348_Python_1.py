class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        for i in range(self.n):
            if self.board[row][i] != player:
                break
        else:
            return player

        for i in range(self.n):
            if self.board[i][col] != player:
                break
        else:
            return player

        # 检查左上-右下对角线
        if row == col:
            for i in range(self.n):
                if self.board[i][i] != player:
                    break
            else:
                return player

        # 检查右上-左下对角线
        if row + col == self.n - 1:
            for i in range(self.n):
                if self.board[i][self.n - i - 1] != player:
                    break
            else:
                return player

        return 0


if __name__ == "__main__":
    obj = TicTacToe(3)
    print(obj.move(0, 0, 1))  # 0
    print(obj.move(0, 2, 2))  # 0
    print(obj.move(2, 2, 1))  # 0
    print(obj.move(1, 1, 2))  # 0
    print(obj.move(2, 0, 1))  # 0
    print(obj.move(1, 0, 2))  # 0
    print(obj.move(2, 1, 1))  # 1
