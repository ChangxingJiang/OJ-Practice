from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().closedIsland(
        grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 0]]))

    # 1
    print(Solution().closedIsland(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))

    # 2
    print(Solution().closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1],
                                        [1, 0, 0, 0, 0, 0, 1],
                                        [1, 0, 1, 1, 1, 0, 1],
                                        [1, 0, 1, 0, 1, 0, 1],
                                        [1, 0, 1, 1, 1, 0, 1],
                                        [1, 0, 0, 0, 0, 0, 1],
                                        [1, 1, 1, 1, 1, 1, 1]]))
