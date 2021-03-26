from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minCost(grid=[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))  # 3
    print(Solution().minCost(grid=[[1, 1, 3], [3, 2, 2], [1, 1, 4]]))  # 0
    print(Solution().minCost(grid=[[1, 2], [4, 3]]))  # 1
    print(Solution().minCost(grid=[[2, 2, 2], [2, 2, 2]]))  # 3
    print(Solution().minCost(grid=[[4]]))  # 0
