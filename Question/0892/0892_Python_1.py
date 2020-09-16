from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        size = len(grid)
        ans = 0
        for i in range(size):
            for j in range(size):
                if grid[i][j]:
                    ans += 2

                if i == 0:
                    ans += grid[i][j]
                elif grid[i][j] > grid[i - 1][j]:
                    ans += grid[i][j] - grid[i - 1][j]

                if i == size - 1:
                    ans += grid[i][j]
                elif grid[i][j] > grid[i + 1][j]:
                    ans += grid[i][j] - grid[i + 1][j]

                if j == 0:
                    ans += grid[i][j]
                elif grid[i][j] > grid[i][j - 1]:
                    ans += grid[i][j] - grid[i][j - 1]

                if j == size - 1:
                    ans += grid[i][j]
                elif grid[i][j] > grid[i][j + 1]:
                    ans += grid[i][j] - grid[i][j + 1]

        return ans


if __name__ == "__main__":
    print(Solution().surfaceArea([[2]]))  # 10
    print(Solution().surfaceArea([[1, 2], [3, 4]]))  # 34
    print(Solution().surfaceArea([[1, 0], [0, 2]]))  # 16
    print(Solution().surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 32
    print(Solution().surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))  # 46
