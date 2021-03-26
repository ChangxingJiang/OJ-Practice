# LeetCode题解(1245)：树的直径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/tree-diameter/)（中等）

标签：树、图、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(E)$     | $O(E)$     | 220ms (75.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
# 生成无向图中边的集合表示
def build_graph_set(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


class Solution:
    def __init__(self):
        self.ans = 0
        self.graph = collections.defaultdict(set)

    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        self.graph = build_graph_set(edges)
        self.dfs(0, -1)
        return self.ans

    def dfs(self, node, parent):
        lengths = [self.dfs(child, node) for child in self.graph[node] if child != parent]
        if len(lengths) == 0:
            return 0
        elif len(lengths) == 1:
            self.ans = max(self.ans, lengths[0] + 1)
            return lengths[0] + 1
        else:
            n1, n2 = heapq.nlargest(2, lengths)
            self.ans = max(self.ans, n1 + n2 + 2)
            return max(n1, n2) + 1
```