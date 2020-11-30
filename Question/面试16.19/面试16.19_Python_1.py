import collections
from typing import List


class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        if not land or not land[0]:
            return []

        s1, s2 = len(land), len(land[0])

        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def neighbours(x1, y1):
            res = []
            for x2, y2 in [(x1 + 1, y1 - 1), (x1 + 1, y1), (x1 + 1, y1 + 1),
                           (x1, y1 - 1), (x1, y1 + 1),
                           (x1 - 1, y1 - 1), (x1 - 1, y1), (x1 - 1, y1 + 1)]:
                if is_valid(x2, y2):
                    res.append((x2, y2))
            return res

        ans = []

        visited = set()
        for i1 in range(s1):
            for i2 in range(s2):
                if land[i1][i2] == 0 and (i1, i2) not in visited:
                    pools = {(i1, i2)}
                    now = 1
                    waiting = collections.deque([(i1, i2)])
                    while waiting:
                        j1, j2 = waiting.popleft()
                        for k1, k2 in neighbours(j1, j2):
                            if land[k1][k2] == 0 and (k1, k2) not in visited and (k1, k2) not in pools:
                                waiting.append((k1, k2))
                                now += 1
                                pools.add((k1, k2))
                    ans.append(now)
                    visited |= pools

        ans.sort()
        return ans


if __name__ == "__main__":
    # [1,2,4]
    print(Solution().pondSizes([
        [0, 2, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 1, 0, 1]
    ]))
