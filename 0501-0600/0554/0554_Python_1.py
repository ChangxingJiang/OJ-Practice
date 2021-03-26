import collections
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        total = len(wall)
        interval = collections.Counter()
        for w in wall:
            now = 0
            for n in w[:-1]:
                now += n
                interval[now] += 1

        ans = interval.most_common(1)
        return total - (ans[0][1] if ans else 0)


if __name__ == "__main__":
    # 2
    print(Solution().leastBricks([[1, 2, 2, 1],
                                  [3, 1, 2],
                                  [1, 3, 2],
                                  [2, 4],
                                  [3, 1, 2],
                                  [1, 3, 1, 1]]))

    # 3
    print(Solution().leastBricks([[1],
                                  [1],
                                  [1]]))
