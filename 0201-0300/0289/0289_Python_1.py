from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _near_nums(x, y):
            res = 0
            for (xx, yy) in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1),
                             (x + 1, y), (x + 1, y + 1)]:
                if _is_valid(xx, yy) and (board[xx][yy] == 1 or board[xx][yy] == 3):
                    res += 1
            return res

        # 将复活标记为2、将刚死标记为3
        for i in range(m):
            for j in range(n):
                num = _near_nums(i, j)
                if num == 3 and board[i][j] == 0:
                    board[i][j] = 2  # 复活标记
                elif (num < 2 or num > 3) and board[i][j] == 1:
                    board[i][j] = 3  # 刚死标记

        # 将复活标记、刚死标记重新标记为1、0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0


if __name__ == "__main__":
    # [
    #   [0,0,0],
    #   [1,0,1],
    #   [0,1,1],
    #   [0,1,0]
    # ]
    matrix = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    Solution().gameOfLife(matrix)
    print(matrix)
