from typing import List


class DSU1:
    def __init__(self, n: int):
        self._n = n
        self._array = [i for i in range(n)]
        self._size = [1] * n

    def find(self, i: int):
        if self._array[i] != i:
            self._array[i] = self.find(self._array[i])
        return self._array[i]

    def union(self, i: int, j: int):
        i, j = self.find(i), self.find(j)
        if self._size[i] >= self._size[j]:
            self._array[j] = i
            self._size[i] += self._size[j]
        else:
            self._array[i] = j
            self._size[j] += self._size[i]

    def group_num(self):
        groups = set()
        for i in range(len(self._array)):
            if self._array[i] not in groups:
                j = self.find(i)
                if j not in groups:
                    groups.add(self.find(i))
        return len(groups)

    def __repr__(self):
        return str(len(self._array)) + ":" + str(self._array)


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def connect_left(x, y):
            if y > 0 and grid[x][y - 1] in {1, 4, 6}:
                dsu.union(x * n + y, x * n + (y - 1))

        def connect_right(x, y):
            if y < n - 1 and grid[x][y + 1] in {1, 3, 5}:
                dsu.union(x * n + y, x * n + (y + 1))

        def connect_top(x, y):
            if x > 0 and grid[x - 1][y] in {2, 3, 4}:
                dsu.union(x * n + y, (x - 1) * n + y)

        def connect_bottom(x, y):
            if x < m - 1 and grid[x + 1][y] in {2, 5, 6}:
                dsu.union(x * n + y, (x + 1) * n + y)

        dsu = DSU1(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    connect_left(i, j)
                    connect_right(i, j)
                elif grid[i][j] == 2:
                    connect_top(i, j)
                    connect_bottom(i, j)
                elif grid[i][j] == 3:
                    connect_left(i, j)
                    connect_bottom(i, j)
                elif grid[i][j] == 4:
                    connect_right(i, j)
                    connect_bottom(i, j)
                elif grid[i][j] == 5:
                    connect_left(i, j)
                    connect_top(i, j)
                elif grid[i][j] == 6:
                    connect_right(i, j)
                    connect_top(i, j)

        return dsu.find(0) == dsu.find(m * n - 1)


if __name__ == "__main__":
    print(Solution().hasValidPath(grid=[[2, 4, 3], [6, 5, 2]]))  # True
    print(Solution().hasValidPath(grid=[[1, 2, 1], [1, 2, 1]]))  # False
    print(Solution().hasValidPath(grid=[[1, 1, 2]]))  # False
    print(Solution().hasValidPath(grid=[[1, 1, 1, 1, 1, 1, 3]]))  # True
    print(Solution().hasValidPath(grid=[[2], [2], [2], [2], [2], [2], [6]]))  # True
