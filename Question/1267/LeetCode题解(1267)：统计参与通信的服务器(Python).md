# LeetCode题解(1267)：统计参与通信的服务器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-servers-that-communicate/)（中等）

标签：并查集、图、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 144ms (22.40%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
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
```

