from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().largestIsland([[1, 0], [0, 1]]))  # 3
    print(Solution().largestIsland([[1, 1], [1, 0]]))  # 4
    print(Solution().largestIsland([[1, 1], [1, 1]]))  # 4
