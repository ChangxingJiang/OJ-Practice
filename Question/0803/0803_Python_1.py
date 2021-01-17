from typing import List


class DSU2:
    def __init__(self):
        self._n = 0
        self._parent = {}
        self._size = {}

    def add(self, i):
        if i not in self._parent:
            self._parent[i] = i
            self._size[i] = 1

    def get_size(self, i):
        return self._size[self.find(i)]

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
    _CEIL = (-1, -1)
    _DIRECTION = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def is_valid(xx, yy):
            return 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1

        def merge_neighbors(x1, y1):
            """合并周围的砖"""
            for dx, dy in self._DIRECTION:
                x2, y2 = x1 + dx, y1 + dy
                if is_valid(x2, y2):
                    dsu.union((x1, y1), (x2, y2))

        m, n = len(grid), len(grid[0])

        # 构造并查集
        dsu = DSU2()

        # 将天花板添加到并查集中
        dsu.add(self._CEIL)

        # 敲掉所有会被敲掉的砖块
        for (i, j) in hits:
            grid[i][j] -= 1

        # 将剩余的砖块添加到并查集中
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dsu.add((i, j))

        # 合并不会被桥段的砖块
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    merge_neighbors(i, j)

        # 将顶部砖块与天花板合并
        for j in range(n):
            if grid[0][j] == 1:
                dsu.union((0, j), self._CEIL)

        ans = [0] * len(hits)

        # 处理敲击的情况
        for k in range(len(hits) - 1, -1, -1):
            i, j = hits[k][0], hits[k][1]

            # 敲完以后与天花板连接的数量
            after_hit = dsu.get_size(self._CEIL)

            # 还原被敲掉的砖块
            grid[i][j] += 1
            if grid[i][j] != 1:  # 处理砖块已经被敲过的情况
                continue
            dsu.add((i, j))

            merge_neighbors(i, j)
            if i == 0:
                dsu.union((i, j), self._CEIL)

            # 被敲的地方和天花板连接
            if dsu.is_connected((i, j), self._CEIL):
                # 敲之前和天花板连接的数量
                before_hit = dsu.get_size(self._CEIL)
                ans[k] = (before_hit - after_hit - 1)

        return ans


if __name__ == "__main__":
    # [2]
    print(Solution().hitBricks(grid=[[1, 0, 0, 0], [1, 1, 1, 0]],
                               hits=[[1, 0]]))

    # [0,0]
    print(Solution().hitBricks(grid=[[1, 0, 0, 0], [1, 1, 0, 0]],
                               hits=[[1, 1], [1, 0]]))
