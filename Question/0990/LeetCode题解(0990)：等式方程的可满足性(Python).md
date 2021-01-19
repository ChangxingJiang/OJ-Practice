# LeetCode题解(0990)：等式方程的可满足性(Python)

题目：[原题链接](https://leetcode-cn.com/problems/satisfiability-of-equality-equations/)（中等）

标签：并查集、图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 80ms (6.89%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

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
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU2()

        for equation in equations:
            if "==" in equation:
                n1, n2 = equation.split("==")
                if n1 not in dsu:
                    dsu.add(n1)
                if n2 not in dsu:
                    dsu.add(n2)
                dsu.union(n1, n2)

        for equation in equations:
            if "!=" in equation:
                n1, n2 = equation.split("!=")
                if n1 not in dsu:
                    dsu.add(n1)
                if n2 not in dsu:
                    dsu.add(n2)
                if dsu.find(n1) == dsu.find(n2):
                    return False

        return True
```

