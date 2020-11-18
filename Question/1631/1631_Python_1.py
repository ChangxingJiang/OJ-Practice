import collections
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        table = [[0] * col for _ in range(row)]

        for i in range(1, row):
            table[i][0] = max(table[i - 1][0], abs(heights[i][0] - heights[i - 1][0]))

        for j in range(1, col):
            table[0][j] = max(table[0][j - 1], abs(heights[0][j] - heights[0][j - 1]))

        need = collections.deque()

        for i in range(1, row):
            for j in range(1, col):
                table[i][j] = min(
                    max(table[i - 1][j], abs(heights[i][j] - heights[i - 1][j])),
                    max(table[i][j - 1], abs(heights[i][j] - heights[i][j - 1]))
                )
                if max(table[i][j], abs(heights[i][j] - heights[i - 1][j])) < table[i - 1][j]:
                    table[i - 1][j] = max(table[i][j], abs(heights[i][j] - heights[i - 1][j]))
                    need.append((i - 1, j))
                if max(table[i][j], abs(heights[i][j] - heights[i][j - 1])) < table[i][j - 1]:
                    table[i][j - 1] = max(table[i][j], abs(heights[i][j] - heights[i][j - 1]))
                    need.append((i, j - 1))

        while need:
            i, j = need.popleft()
            if i > 0 and max(table[i][j], abs(heights[i][j] - heights[i - 1][j])) < table[i - 1][j]:
                table[i - 1][j] = max(table[i][j], abs(heights[i][j] - heights[i - 1][j]))
                need.append((i - 1, j))
            if i < row - 1 and max(table[i][j], abs(heights[i][j] - heights[i + 1][j])) < table[i + 1][j]:
                table[i + 1][j] = max(table[i][j], abs(heights[i][j] - heights[i + 1][j]))
                need.append((i + 1, j))
            if j > 0 and max(table[i][j], abs(heights[i][j] - heights[i][j - 1])) < table[i][j - 1]:
                table[i][j - 1] = max(table[i][j], abs(heights[i][j] - heights[i][j - 1]))
                need.append((i, j - 1))
            if j < col - 1 and max(table[i][j], abs(heights[i][j] - heights[i][j + 1])) < table[i][j + 1]:
                table[i][j + 1] = max(table[i][j], abs(heights[i][j] - heights[i][j + 1]))
                need.append((i, j + 1))

        return table[-1][-1]


if __name__ == "__main__":
    print(Solution().minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))  # 2
    print(Solution().minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]))  # 1
    print(Solution().minimumEffortPath(
        heights=[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]))  # 0
