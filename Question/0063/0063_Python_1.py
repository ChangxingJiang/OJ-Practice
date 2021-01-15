from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 如果出发点或目标点有障碍物，则无法到达
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = (dp[i - 1][j] if i > 0 else 0) + (dp[i][j - 1] if j > 0 else 0)
                print((i, j), ":", dp[i][j])

        return dp[-1][-1]


if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]))  # 1
