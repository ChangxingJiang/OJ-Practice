from typing import List


class DSU2:
    def __init__(self):
        self._n = 0
        self._parent = {}
        self._size = {}

    def __contains__(self, i):
        return i in self._parent

    def add(self, i):
        if i not in self._parent:
            self._parent[i] = i
            self._size[i] = 1

    def get_size(self, i):
        return self._size[self.find(i)]

    def size_list(self):
        return list(self._size.values())

    def find(self, i):
        if self._parent[i] != i:
            self._parent[i] = self.find(self._parent[i])
        return self._parent[i]

    def union(self, i, j):
        i, j = self.find(i), self.find(j)
        if i != j:
            self._parent[i] = j
            self._size[j] += self._size[i]
            del self._size[i]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dsu = DSU2()

        for i in range(m):
            last = (-1, -1)
            for j in range(n):
                if grid[i][j] == 1:
                    if (i, j) not in dsu:
                        dsu.add((i, j))
                    if last != (-1, -1):
                        dsu.union(last, (i, j))
                    last = (i, j)

        for j in range(n):
            last = (-1, -1)
            for i in range(m):
                if grid[i][j] == 1:
                    if (i, j) not in dsu:
                        dsu.add((i, j))
                    if last != (-1, -1):
                        dsu.union(last, (i, j))
                    last = (i, j)

        return sum(v for v in dsu.size_list() if v > 1)


if __name__ == "__main__":
    print(Solution().countServers(grid=[[1, 0], [0, 1]]))  # 0
    print(Solution().countServers(grid=[[1, 0], [1, 1]]))  # 3
    print(Solution().countServers(grid=[[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))  # 4
    # 3
    print(Solution().countServers(grid=[[1, 0, 0, 1, 0],
                                        [0, 0, 0, 0, 0],
                                        [0, 0, 0, 1, 0]]))
