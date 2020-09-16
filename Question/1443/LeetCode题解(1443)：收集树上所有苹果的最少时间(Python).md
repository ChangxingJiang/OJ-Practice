# LeetCode题解(1443)：收集无向树中所有苹果的最少移动距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree/)（中等）

标签：树、深度优先搜索、图、图-无向图

| 解法           | 时间复杂度             | 空间复杂度 | 执行用时       |
| -------------- | ---------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+E)$ : 其中E为边数 | $O(N+E)$   | 320ms (22.69%) |
| Ans 2 (Python) |                        |            |                |
| Ans 3 (Python) |                        |            |                |

解法一（完全视作无向图的解法）：

```python
def build_graph_set(edges):
    import collections
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = build_graph_set(edges)

        def dfs(node1, father=-1):
            val = 0
            for node2 in graph[node1]:
                if node2 != father:
                    val += dfs(node2, node1)

            if val or hasApple[node1]:
                return val + 2
            else:
                return 0

        return dfs(0) - 2 if dfs(0) else 0
```