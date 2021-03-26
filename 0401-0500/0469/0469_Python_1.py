from typing import List


class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        size = len(points)
        pre = 0
        for i in range(size):
            x1 = points[(i + 1) % size][0] - points[i][0]
            x2 = points[(i + 2) % size][0] - points[i][0]
            y1 = points[(i + 1) % size][1] - points[i][1]
            y2 = points[(i + 2) % size][1] - points[i][1]
            cur = x1 * y2 - x2 * y1
            if cur != 0:
                if cur * pre < 0:
                    return False
                else:
                    pre = cur
        return True


if __name__ == "__main__":
    print(Solution().isConvex([[0, 0], [0, 1], [1, 1], [1, 0]]))  # True
    print(Solution().isConvex([[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]))  # False
