# LeetCode题解(0261)：以图判树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/graph-valid-tree/)（中等）

标签：深度优先搜索、广度优先搜索、并查集、图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (91.01%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class DSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if self.size[i] >= self.size[j]:
            self.array[j] = i
            self.size[i] += self.size[j]
        else:
            self.array[i] = j
            self.size[j] += self.size[i]


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        dsu = DSU(n)
        for n1, n2 in edges:
            # 出现环，同时必定出现不能连接的点
            if dsu.find(n1) == dsu.find(n2):
                return False
            else:
                dsu.union(n1, n2)

        return True
```