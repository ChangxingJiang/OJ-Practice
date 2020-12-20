from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().hasValidPath(grid=[[2, 4, 3], [6, 5, 2]]))  # True
    print(Solution().hasValidPath(grid=[[1, 2, 1], [1, 2, 1]]))  # False
    print(Solution().hasValidPath(grid=[[1, 1, 2]]))  # False
    print(Solution().hasValidPath(grid=[[1, 1, 1, 1, 1, 1, 3]]))  # True
    print(Solution().hasValidPath(grid=[[2], [2], [2], [2], [2], [2], [6]]))  # True
