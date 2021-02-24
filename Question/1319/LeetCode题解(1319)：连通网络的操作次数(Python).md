# LeetCode题解(1319)：连通网络的操作次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/)（中等）

标签：并查集、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 312ms (16.07%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu = DSU1(n)
        surplus = 0
        for a, b in connections:
            if dsu.find(a) == dsu.find(b):
                surplus += 1
            else:
                dsu.union(a, b)

        return dsu.group_num() - 1 if dsu.group_num() - 1 <= surplus else -1
```

