from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))  # 8
    print(Solution().countNegatives(grid=[[3, 2], [1, 0]]))  # 0
    print(Solution().countNegatives(grid=[[1, -1], [-1, -1]]))  # 3
    print(Solution().countNegatives(grid=[[-1]]))  # 1
