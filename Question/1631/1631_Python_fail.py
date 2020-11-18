from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        dp = [[0] * col for _ in range(row)]

        for i in range(1, row):
            dp[i][0] = max(dp[i - 1][0], abs(heights[i][0] - heights[i - 1][0]))

        for j in range(1, col):
            dp[0][j] = max(dp[0][j - 1], abs(heights[0][j] - heights[0][j - 1]))

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(
                    max(dp[i - 1][j], abs(heights[i][j] - heights[i - 1][j])),
                    max(dp[i][j - 1], abs(heights[i][j] - heights[i][j - 1]))
                )

        for i in dp:
            print(i)

        return dp[-1][-1]

    # 错误！！！


if __name__ == "__main__":
    print(Solution().minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))  # 2
    print(Solution().minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]))  # 1
    print(Solution().minimumEffortPath(
        heights=[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))  # 0
