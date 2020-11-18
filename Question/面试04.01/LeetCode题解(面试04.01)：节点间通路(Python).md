# LeetCode题解(面试04.01)：有向图节点之间是否存在通路(Python)

题目：[原题链接](https://leetcode-cn.com/problems/route-between-nodes-lcci/)（中等）

标签：图、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(E+N)$   | $O(E+N)$   | 236ms (53.90%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（广度优先搜索）：

```python
# 生成有向图中边的集合表示
def build_graph_set_d(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
    return graph


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        if start == target:
            return True

        graph = build_graph_set_d(graph)

        visited = {start}
        node_list = collections.deque([start])

        while node_list:
            now = node_list.popleft()
            for new in graph[now]:
                if new not in visited:
                    node_list.append(new)
                    visited.add(new)
                    if new == target:
                        return True

        return False
```