from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]
        return not (x3 - x1) * (y2 - y1) == (x2 - x1) * (y3 - y1)


if __name__ == "__main__":
    print(Solution().isBoomerang([[1, 1], [2, 3], [3, 2]]))  # True
    print(Solution().isBoomerang([[1, 1], [2, 2], [3, 3]]))  # False
    print(Solution().isBoomerang([[0, 0], [0, 2], [2, 1]]))  # True
