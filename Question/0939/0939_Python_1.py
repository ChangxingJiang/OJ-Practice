import collections
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = float("inf")
        count_x = collections.defaultdict(set)
        count_y = collections.defaultdict(set)
        for x1, y1 in points:
            for y2 in count_x[x1]:
                for x2 in count_y[y1]:
                    if x2 in count_y[y2]:
                        ans = min(ans, abs(y2 - y1) * abs(x2 - x1))
            count_x[x1].add(y1)
            count_y[y1].add(x1)
        return ans if ans != float("inf") else 0


if __name__ == "__main__":
    print(Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))  # 4
    print(Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]))  # 2
