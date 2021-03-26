import collections
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _get_near(x, y):
            return [(xx, yy) for (xx, yy) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if _is_valid(xx, yy)]

        queue1 = collections.deque([])
        visited1 = set()
        queue2 = collections.deque([])
        visited2 = set()

        # 标记地图边缘位置
        for i in range(m):
            queue1.append((i, 0))
            visited1.add((i, 0))
            queue2.append((i, n - 1))
            visited2.add((i, n - 1))
        for j in range(n):
            queue1.append((0, j))
            visited1.add((0, j))
            queue2.append((m - 1, j))
            visited2.add((m - 1, j))

        # 标记太平洋
        while queue1:
            i1, j1 = queue1.popleft()
            for i2, j2 in _get_near(i1, j1):
                if matrix[i2][j2] >= matrix[i1][j1] and (i2, j2) not in visited1:
                    visited1.add((i2, j2))
                    queue1.append((i2, j2))

        # 标记大西洋
        while queue2:
            i1, j1 = queue2.popleft()
            for i2, j2 in _get_near(i1, j1):
                if matrix[i2][j2] >= matrix[i1][j1] and (i2, j2) not in visited2:
                    visited2.add((i2, j2))
                    queue2.append((i2, j2))

        # 生成结果
        return [[i, j] for (i, j) in (visited1 & visited2)]


if __name__ == "__main__":
    # [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    print(Solution().pacificAtlantic([
        [1, 2, 2, 3, 5],
        [3, 2, 2, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]))
