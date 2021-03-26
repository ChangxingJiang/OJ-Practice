# LeetCode题解(LCP07)：传递信息(Python)

题目：[原题链接](https://leetcode-cn.com/problems/chuan-di-xin-xi/)（简单）

标签：图、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^K)$   | $O(N^K)$   | 52ms (39.84%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
def build_graph(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
    return graph


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        graph = build_graph(relation)
        aim = n - 1

        def dfs(now, kk):
            if kk == 0:
                return 1 if now == aim else 0
            else:
                res = 0
                for child in graph[now]:
                    res += dfs(child, kk - 1)
                return res

        return dfs(0, k)
```