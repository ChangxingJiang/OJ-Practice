from typing import List


class Solution:
    _BIG = 10001

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        size = len(A)
        dp = [[self._BIG] * size for i in range(size)]

        for j in range(size):
            dp[0][j] = A[0][j]

        for i in range(1, size):
            for j in range(size):
                dp[i][j] = min(dp[i - 1][j - 1] if j > 0 else self._BIG,
                               dp[i - 1][j],
                               dp[i - 1][j + 1] if j < size - 1 else self._BIG) + A[i][j]
        return min(dp[-1])


if __name__ == "__main__":
    # 12
    print(Solution().minFallingPathSum([[1, 2, 3],
                                        [4, 5, 6],
                                        [7, 8, 9]]))

    # -27
    print(Solution().minFallingPathSum([[17, 82],
                                        [1, -44]]))
