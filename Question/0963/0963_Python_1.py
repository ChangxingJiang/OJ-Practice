import math
from itertools import combinations
from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # 不是3组长度相等的边就是矩形的经典反例：[3, 0] [1, 0] [2, 3] [2, 1]

        def distance(x, y):
            return math.sqrt(math.pow(y[1] - x[1], 2) + math.pow(y[0] - x[0], 2))

        ans = float("inf")

        # 逐个点遍历
        for p1, p2, p3, p4 in combinations(points, 4):
            d = [distance(p1, p2), distance(p1, p3), distance(p1, p4),
                 distance(p2, p3), distance(p2, p4), distance(p3, p4)]

            d.sort()

            if d[0] == d[1] and d[2] == d[3] and d[4] == d[5]:
                print(p1, p2, p3, p4, "->", d)
                ans = min(ans, d[0] * d[2])

        return ans if ans != float("inf") else 0


if __name__ == "__main__":
    # 2
    print(Solution().minAreaFreeRect([[1, 2], [2, 1], [1, 0], [0, 1]]))

    # 1
    print(Solution().minAreaFreeRect([[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]]))

    # 0
    print(Solution().minAreaFreeRect([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]))

    # 2
    print(Solution().minAreaFreeRect([[3, 1], [1, 1], [0, 1], [2, 1], [3, 3], [3, 2], [0, 2], [2, 3]]))

    # 0
    print(Solution().minAreaFreeRect([[3, 0], [0, 1], [1, 0], [3, 3], [2, 3], [0, 2], [2, 1]]))
