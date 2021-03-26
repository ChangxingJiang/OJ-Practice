import collections
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _is_border(x, y):
            return x == 0 or x == m - 1 or y == 0 or y == n - 1

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
                    if _is_valid(x2, y2)]

        ans = 0

        mainland = set()
        island = set()
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and (i, j) not in island and (i, j) not in mainland:
                    is_island = True
                    now = {(i, j)}
                    queue = collections.deque([(i, j)])
                    while queue:
                        i1, j1 = queue.popleft()
                        for i2, j2 in _get_neighbors(i1, j1):
                            if grid[i2][j2] == 0:
                                if _is_border(i2, j2) or (i2, j2) in mainland:
                                    is_island = False
                                    break
                                if (i2, j2) not in now:
                                    now.add((i2, j2))
                                    queue.append((i2, j2))
                        if not is_island:
                            break
                    if is_island:
                        ans += 1
                        island |= now
                    else:
                        mainland |= now

        return ans


if __name__ == "__main__":
    # 2
    print(Solution().closedIsland(
        grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 0]]))

    # 1
    print(Solution().closedIsland(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))

    # 2
    print(Solution().closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1],
                                        [1, 0, 0, 0, 0, 0, 1],
                                        [1, 0, 1, 1, 1, 0, 1],
                                        [1, 0, 1, 0, 1, 0, 1],
                                        [1, 0, 1, 1, 1, 0, 1],
                                        [1, 0, 0, 0, 0, 0, 1],
                                        [1, 1, 1, 1, 1, 1, 1]]))

    # 5
    print(Solution().closedIsland(
        [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
         [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
         [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]))
