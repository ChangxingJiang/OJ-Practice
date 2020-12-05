from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    print(Solution().colorBorder(grid=[[1, 1], [1, 2]], r0=0, c0=0, color=3))  # [[3, 3], [3, 2]]
    print(Solution().colorBorder(grid=[[1, 2, 2], [2, 3, 2]], r0=0, c0=1, color=3))  # [[1, 3, 3], [2, 3, 3]]
    print(Solution().colorBorder(grid=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], r0=1, c0=1,
                                 color=2))  # [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
