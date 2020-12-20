from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 9
    print(Solution().largest1BorderedSquare(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))

    # 1
    print(Solution().largest1BorderedSquare(grid=[[1, 1, 0, 0]]))
