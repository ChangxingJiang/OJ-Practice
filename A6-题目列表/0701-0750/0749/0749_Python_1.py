from typing import List


class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 10
    print(Solution().containVirus(grid=
                                  [[0, 1, 0, 0, 0, 0, 0, 1],
                                   [0, 1, 0, 0, 0, 0, 0, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 1],
                                   [0, 0, 0, 0, 0, 0, 0, 0]]))

    # 4
    print(Solution().containVirus(grid=
                                  [[1, 1, 1],
                                   [1, 0, 1],
                                   [1, 1, 1]]))

    # 13
    print(Solution().containVirus(grid=
                                  [[1, 1, 1, 0, 0, 0, 0, 0, 0],
                                   [1, 0, 1, 0, 1, 1, 1, 1, 1],
                                   [1, 1, 1, 0, 0, 0, 0, 0, 0]]))
