import collections
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)] if
                    is_valid(x2, y2)]

        m, n = len(matrix), len(matrix[0])

        ans = [[-1] * n for _ in range(m)]
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    ans[i][j] = 0

        while queue:
            for _ in range(len(queue)):
                i1, j1 = queue.popleft()
                for i2, j2 in get_neighbors(i1, j1):
                    if ans[i2][j2] == -1:
                        ans[i2][j2] = ans[i1][j1] + 1
                        queue.append((i2, j2))

        return ans


if __name__ == "__main__":
    # [[0,0,0],
    #  [0,1,0],
    #  [0,0,0]]
    print(Solution().updateMatrix([[0, 0, 0],
                                   [0, 1, 0],
                                   [0, 0, 0]]))

    # [[0,0,0],
    #  [0,1,0],
    #  [1,2,1]]
    print(Solution().updateMatrix([[0, 0, 0],
                                   [0, 1, 0],
                                   [1, 1, 1]]))
