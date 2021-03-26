import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
                    if _is_valid(x2, y2)]

        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        waiting = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    waiting.add((i, j))

        if not queue:
            if not waiting:
                return 0
            else:
                return -1

        time = 0
        while queue:
            for _ in range(len(queue)):
                i1, j1 = queue.popleft()
                for (i2, j2) in _get_neighbors(i1, j1):
                    if (i2, j2) in waiting:
                        waiting.remove((i2, j2))
                        queue.append((i2, j2))
            time += 1

        if waiting:
            return -1

        return time - 1


if __name__ == "__main__":
    print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
    print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
    print(Solution().orangesRotting([[0, 2]]))  # 0
    print(Solution().orangesRotting([[0]]))  # 0
