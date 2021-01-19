import collections
from typing import List


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        def _is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
                    if _is_valid(x2, y2)]

        # 遍历半岛
        mainland = set()
        queue = collections.deque()
        for i in range(m):
            if A[i][0] == 1:
                queue.append((i, 0))
                mainland.add((i, 0))
            if A[i][n - 1] == 1:
                queue.append((i, n - 1))
                mainland.add((i, n - 1))
        for j in range(1, n - 1):
            if A[0][j] == 1:
                queue.append((0, j))
                mainland.add((0, j))
            if A[m - 1][j] == 1:
                queue.append((m - 1, j))
                mainland.add((m - 1, j))
        while queue:
            i1, j1 = queue.popleft()
            for i2, j2 in _get_neighbors(i1, j1):
                if A[i2][j2] == 1 and (i2, j2) not in mainland:
                    queue.append((i2, j2))
                    mainland.add((i2, j2))

        # 遍历岛屿
        island = set()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and (i, j) not in mainland and (i, j) not in island:
                    island.add((i, j))
                    queue = collections.deque([(i, j)])
                    while queue:
                        i1, j1 = queue.popleft()
                        for i2, j2 in _get_neighbors(i1, j1):
                            if A[i2][j2] == 1 and (i2, j2) not in mainland and (i2, j2) not in island:
                                queue.append((i2, j2))
                                island.add((i2, j2))

        return len(island)


if __name__ == "__main__":
    # 3
    print(Solution().numEnclaves([[0, 0, 0, 0],
                                  [1, 0, 1, 0],
                                  [0, 1, 1, 0],
                                  [0, 0, 0, 0]]))

    # 0
    print(Solution().numEnclaves([[0, 1, 1, 0],
                                  [0, 0, 1, 0],
                                  [0, 0, 1, 0],
                                  [0, 0, 0, 0]]))
