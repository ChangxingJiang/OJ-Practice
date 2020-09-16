# LeetCode题解(0684)：找出树中唯一的一条冗余的边(Python)

题目：[原题链接](https://leetcode-cn.com/problems/redundant-connection/)（中等）

标签：树、图、图-无向图、并查集

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 124ms (8.02%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 72ms (64.08%) |
| Ans 3 (Python) |            |            |               |

解法一（集合列表）：

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited_group = []
        for edge in edges:
            group0, group1 = None, None
            for group in visited_group:
                if edge[0] in group:
                    group0 = group
                if edge[1] in group:
                    group1 = group
            if group0 and group1:
                if group0 == group1:
                    return edge
                else:
                    visited_group.remove(group0)
                    visited_group.remove(group1)
                    visited_group.append(group0 | group1)
            elif group0:
                group0.add(edge[1])
            elif group1:
                group1.add(edge[0])
            else:
                visited_group.append({edge[0], edge[1]})
```

解法二（并查集）：

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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))  # 构造并查集实例
        for edge in edges:
            if dsu.find(edge[0] - 1) == dsu.find(edge[1] - 1):
                return edge
            else:
                dsu.union(edge[0] - 1, edge[1] - 1)
```

