# LeetCode题解(1786)：从第一个节点出发到最后一个节点的受限路径数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-restricted-paths-from-first-to-last-node/)（中等）

标签：图、动态规划、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 4564ms (5.05%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
import collections
import functools
import heapq


# 生成无向图加权中边的邻接列表结构
def build_graph(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    return graph


class Solution:
    _MOD = 10**9+7
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # 将边存储到字典结构中
        graph = build_graph(edges)

        # 计算所有点距离结点n的距离
        distances = {}
        cloud = [[0, n]]
        while cloud:
            while cloud and cloud[0][1] in distances:
                heapq.heappop(cloud)
            if not cloud:
                break
            d, i = heapq.heappop(cloud)
            distances[i] = d
            for j in graph[i]:
                if j not in distances:
                    heapq.heappush(cloud, [d + graph[i][j], j])

        # 记忆化递归计算受限路径数量
        @functools.lru_cache(None)
        def dfs(n1):
            if n1 == 1:
                return 1
            res = sum(dfs(n2) for n2 in graph[n1] if distances[n2] > distances[n1])
            return res

        return dfs(n) % self._MOD
```

