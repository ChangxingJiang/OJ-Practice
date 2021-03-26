# LeetCode题解(0210)：课程表II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/course-schedule-ii/)（中等）

标签：图、拓扑排序、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 84ms (12.88%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
def build_graph(edges):
    graph_in = collections.defaultdict(set)
    graph_out = collections.defaultdict(set)
    for edge in edges:
        graph_in[edge[1]].add(edge[0])
        graph_out[edge[0]].add(edge[1])
    return graph_out, graph_in


def topo(graph_in, graph_out):
    count = {}  # 节点入射边统计
    queue = []  # 当前入射边为0的节点列表

    # 统计所有节点的入射边
    for node in graph_in:
        count[node] = len(graph_in[node])
    for node in graph_out:
        if node not in count:
            count[node] = 0
            queue.append(node)

    # 拓扑排序
    order = []
    while queue:
        node = queue.pop()
        order.append(node)
        for next in graph_out[node]:
            count[next] -= 1
            if count[next] == 0:
                queue.append(next)

    return order


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 生成有向图中边的邻接列表结构
        graph_in, graph_out = build_graph(prerequisites)

        # 拓扑排序
        order = topo(graph_in, graph_out)
        order_set = set(order)

        for node in graph_in:
            if node not in order:
                return []

        for i in range(numCourses):
            if i not in order_set:
                order.append(i)

        return order
```