from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 24
    print(Solution().cherryPickup(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))

    # 28
    print(Solution().cherryPickup(
        grid=[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
              [1, 0, 2, 3, 0, 0, 6]]))

    # 22
    print(Solution().cherryPickup(grid=[[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]]))

    # 4
    print(Solution().cherryPickup(grid=[[1, 1], [1, 1]]))
