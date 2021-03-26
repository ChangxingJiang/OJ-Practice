from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.dp = None
        else:
            m, n = len(matrix), len(matrix[0])
            self.dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    self.dp[i][j] = matrix[i - 1][j - 1] + self.dp[i][j - 1] + self.dp[i - 1][j] - self.dp[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.dp is not None:
            return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]
        else:
            return 0


if __name__ == "__main__":
    obj = NumMatrix(matrix=[
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ])
    print(obj.sumRegion(2, 1, 4, 3))  # 8
    print(obj.sumRegion(1, 1, 2, 2))  # 11
    print(obj.sumRegion(1, 2, 2, 4))  # 12

    obj = NumMatrix(matrix=[
        [-1]
    ])
    print(obj.sumRegion(0, 0, 0, 0))  # -1
