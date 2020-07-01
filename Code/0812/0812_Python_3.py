import itertools
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                   for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(points, 3)) / 2


if __name__ == "__main__":
    print(Solution().largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))  # 2
    print(Solution().largestTriangleArea([[1, 0], [0, 0], [0, 1]]))  # 0.5
    print(Solution().largestTriangleArea(
        [[35, -23], [-12, -48], [-34, -40], [21, -25], [-35, -44], [24, 1], [16, -9], [41, 4], [-36, -49], [42, -49],
         [-37, -20], [-35, 11], [-2, -36], [18, 21], [18, 8], [-24, 14], [-23, -11], [-8, 44], [-19, -3], [0, -10],
         [-21, -4], [23, 18], [20, 11], [-42, 24], [6, -19]]))  # 3627
