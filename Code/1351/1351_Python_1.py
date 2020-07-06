from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        if grid[-1][-1] >= 0:
            return 0
        ans = 0
        num = x
        for j in range(1, y + 1):
            for i in range(num, 0, -1):
                if grid[-i][-j] < 0:
                    ans += i
                    num = i
                    break
            else:
                break
        return ans


if __name__ == "__main__":
    print(Solution().countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))  # 8
    print(Solution().countNegatives(grid=[[3, 2], [1, 0]]))  # 0
    print(Solution().countNegatives(grid=[[1, -1], [-1, -1]]))  # 3
    print(Solution().countNegatives(grid=[[-1]]))  # 1
