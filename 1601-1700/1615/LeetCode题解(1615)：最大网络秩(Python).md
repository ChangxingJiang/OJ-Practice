# LeetCode题解(1615)：计算城市路网最大网络秩(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximal-network-rank/)（中等）

标签：图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(R+N^2)$ | $O(R)$     | 124ms (70%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
# 生成图中边的集合表示
def build_graph_set(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        graph = build_graph_set(roads)
        for i in range(n):
            for j in range(i + 1, n):
                num = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    num -= 1
                ans = max(ans, num)
        return ans
```