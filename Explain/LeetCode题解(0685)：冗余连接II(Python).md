# LeetCode题解(0685)：找出有向图中唯一的一条冗余的边(Python)

题目：[原题链接](https://leetcode-cn.com/problems/redundant-connection-ii/)（困难）

标签：树、图、图-有向图、并查集

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 76ms (82.82%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（并查集）：

```python
class DDSU:
    def __init__(self, n):
        self.array = [i for i in range(n)]

    def find(self, i):
        if self.array[i] != i:
            self.array[i] = self.find(self.array[i])
        return self.array[i]

    def union(self, i, j):
        self.array[self.find(j)] = self.find(i)


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DDSU(len(edges) + 1)  # 构造并查集实例
        candidates = []  # 候选结果
        parent = {}
        last = None
        for edge in edges:
            if edge[1] in parent:  # 当前目标节点已经有父节点
                candidates.append([parent[edge[1]], edge[1]])
                candidates.append([edge[0], edge[1]])
            else:
                parent[edge[1]] = edge[0]
                if dsu.find(edge[0]) == dsu.find(edge[1]):
                    last = edge
                else:
                    dsu.union(edge[0], edge[1])

        if not candidates:
            return last

        if dsu.find(candidates[1][0]) == dsu.find(candidates[1][1]):
            return candidates[1]
        else:
            return candidates[0]
```

