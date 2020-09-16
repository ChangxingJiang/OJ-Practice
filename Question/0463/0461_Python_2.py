from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        ans = 0

        # 统计纵向海岸线
        for i in range(x):
            if grid[i][0] == 1:
                ans += 1
            if grid[i][-1] == 1:
                ans += 1
            for j in range(y - 1):
                if grid[i][j] != grid[i][j + 1]:
                    ans += 1

        # 统计横向海岸线
        for j in range(y):
            if grid[0][j] == 1:
                ans += 1
            if grid[-1][j] == 1:
                ans += 1
            for i in range(x - 1):
                if grid[i][j] != grid[i + 1][j]:
                    ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().islandPerimeter([[0, 1, 0, 0],
                                      [1, 1, 1, 0],
                                      [0, 1, 0, 0],
                                      [1, 1, 0, 0]]))  # 16
