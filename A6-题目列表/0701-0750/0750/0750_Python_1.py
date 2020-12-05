from typing import List


class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 1
    print(Solution().countCornerRectangles(grid=
                                           [[1, 0, 0, 1, 0],
                                            [0, 0, 1, 0, 1],
                                            [0, 0, 0, 1, 0],
                                            [1, 0, 1, 0, 1]]))

    # 9
    print(Solution().countCornerRectangles(grid=
                                           [[1, 1, 1],
                                            [1, 1, 1],
                                            [1, 1, 1]]))

    # 0
    print(Solution().countCornerRectangles(grid=
                                           [[1, 1, 1, 1]]))
