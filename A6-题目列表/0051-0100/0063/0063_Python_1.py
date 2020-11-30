from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]))  # 1
