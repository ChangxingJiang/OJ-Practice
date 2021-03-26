from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ans += 4
                    if i != 0 and grid[i - 1][j] == 1:  # 如果上方也是岛屿的话
                        ans -= 2
                    if j != 0 and grid[i][j - 1] == 1:  # 如果左方也是岛屿的话
                        ans -= 2
        return ans


if __name__ == "__main__":
    print(Solution().islandPerimeter([[0, 1, 0, 0],
                                      [1, 1, 1, 0],
                                      [0, 1, 0, 0],
                                      [1, 1, 0, 0]]))  # 16
