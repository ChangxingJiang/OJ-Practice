import collections
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color2: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
                    if _is_valid(x2, y2)]

        color1 = grid[r0][c0]

        need = set()
        visited = {(r0, c0)}
        queue = collections.deque([(r0, c0)])
        while queue:
            i1, j1 = queue.popleft()

            neighbors = _get_neighbors(i1, j1)

            # 如果(i1,j1)位于边缘
            if len(neighbors) < 4:
                need.add((i1, j1))

            for i2, j2 in neighbors:
                # 如果(i1,j1)与其他颜色相邻
                if grid[i2][j2] != color1:
                    need.add((i1, j1))
                    continue

                if (i2, j2) in visited:
                    continue

                if grid[i2][j2] == color1:
                    visited.add((i2, j2))
                    queue.append((i2, j2))

        for i, j in need:
            grid[i][j] = color2
        return grid


if __name__ == "__main__":
    # [[3, 3],
    #  [3, 2]]
    print(Solution().colorBorder(grid=[[1, 1],
                                       [1, 2]],
                                 r0=0, c0=0, color2=3))

    # [[1, 3, 3],
    #  [2, 3, 3]]
    print(Solution().colorBorder(grid=[[1, 2, 2],
                                       [2, 3, 2]],
                                 r0=0, c0=1, color2=3))

    # [[2, 2, 2],
    #  [2, 1, 2],
    #  [2, 2, 2]]
    print(Solution().colorBorder(grid=[[1, 1, 1],
                                       [1, 1, 1],
                                       [1, 1, 1]],
                                 r0=1, c0=1, color2=2))
