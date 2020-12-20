import collections
import itertools
from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # 不是3组长度相等的边就是矩形的经典反例：[3, 0] [1, 0] [2, 3] [2, 1]

        # 构造复数用于计算
        points = [complex(*point) for point in points]
        dic = collections.defaultdict(list)

        for p1, p2 in itertools.combinations(points, 2):
            center = (p1 + p2) / 2
            radius = abs(center - p1)
            dic[(center, radius)].append(p1)

        ans = float("inf")

        for (center, radius), candidates in dic.items():
            for p1, p2 in itertools.combinations(candidates, 2):
                ans = min(ans, abs(p1 - p2) * abs(p1 - (2 * center - p2)))

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
