# LeetCode题解(1466)：调整有向图中边的方向使所有节点都能到达指定点的最少调整方向数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)（中等）

标签：树、深度优先搜索、图、图-无向图

| 解法           | 时间复杂度                 | 空间复杂度 | 执行用时       |
| -------------- | -------------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+E)$ : 其中E为连接数   | $O(N+E)$   | 468ms (22.94%) |
| Ans 2 (Python) | $O(N×H)$ : 其中H为最大深度 | $O(1)$     | 104ms (99.08%) |
| Ans 3 (Python) |                            |            |                |

解法一：

```python
def build_graph_set(edges):
    import collections
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add((edge[1], 1))
        graph[edge[1]].add((edge[0], 0))
    return graph


class Solution:
    def __init__(self):
        self.ans = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = build_graph_set(connections)

        def dfs(node1, father=None):
            for node2, point in graph[node1]:
                if node2 != father:
                    self.ans += point
                    dfs(node2, node1)

        dfs(0)

        return self.ans
```

解法二：

![LeetCode题解(1466)：截图](LeetCode题解(1466)：截图.png)

```python
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        visited = {0}

        while len(visited) < n:
            for city1, city2 in connections:
                if city2 in visited:
                    visited.add(city1)
                elif city1 in visited:
                    ans += 1
                    visited.add(city2)

        return ans
```