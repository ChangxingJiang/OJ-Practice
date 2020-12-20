import collections
from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def get_near(x, y):
            res = []
            for xx, yy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if is_valid(xx, yy):
                    res.append((xx, yy))
            return res

        if not grid or not grid[0]:
            return 0

        s1, s2 = len(grid), len(grid[0])

        people = []
        for i1 in range(s1):
            for i2 in range(s2):
                if grid[i1][i2] == 1:
                    people.append((i1, i2))

        dp = [[0] * s2 for _ in range(s1)]
        for person in people:
            visited = {person}
            queue = collections.deque([person])
            distance = 0
            while queue:
                distance += 1
                for _ in range(len(queue)):
                    (i1, i2) = queue.popleft()
                    for (j1, j2) in get_near(i1, i2):
                        if (j1, j2) not in visited:
                            visited.add((j1, j2))
                            queue.append((j1, j2))
                            dp[j1][j2] += distance

        return min(min(dp[i1]) for i1 in range(s1))


if __name__ == "__main__":
    # 6
    print(Solution().minTotalDistance([
        [1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0]
    ]))
