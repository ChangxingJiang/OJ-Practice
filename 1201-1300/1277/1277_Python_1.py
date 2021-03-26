from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                        ans += 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                        ans += dp[i][j]

        return ans


if __name__ == "__main__":
    # 15
    print(Solution().countSquares(matrix=
    [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]))

    # 7
    print(Solution().countSquares(matrix=
    [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]))
