from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = pow((points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2, 0.5)
        b = pow((points[0][0] - points[2][0]) ** 2 + (points[0][1] - points[2][1]) ** 2, 0.5)
        c = pow((points[1][0] - points[2][0]) ** 2 + (points[1][1] - points[2][1]) ** 2, 0.5)
        return not max([a, b, c]) * 2 == sum([a, b, c])


if __name__ == "__main__":
    print(Solution().isBoomerang([[1, 1], [2, 3], [3, 2]]))  # True
    print(Solution().isBoomerang([[1, 1], [2, 2], [3, 3]]))  # False
    print(Solution().isBoomerang([[0, 0], [0, 2], [2, 1]]))  # True
