from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        pass


if __name__ == "__main__":
    # 6
    print(Solution().shortestPath(grid=
                                  [[0, 0, 0],
                                   [1, 1, 0],
                                   [0, 0, 0],
                                   [0, 1, 1],
                                   [0, 0, 0]],
                                  k=1))

    # -1
    print(Solution().shortestPath(grid=
                                  [[0, 1, 1],
                                   [1, 1, 1],
                                   [1, 0, 0]],
                                  k=1))
