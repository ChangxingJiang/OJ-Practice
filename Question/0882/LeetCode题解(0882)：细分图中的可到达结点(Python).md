# LeetCode题解(0882)：细分图中的可到达结点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reachable-nodes-in-subdivided-graph/)（困难）

标签：图、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+E)$   | $O(N+E)$   | 576ms (76.19%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（广度优先搜索）：

```python
def build_graph(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    return graph


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = build_graph(edges)
        # print("有向加权图:", graph)

        visited = {0: 0}  # 已经到达节点的最小步数
        now_node_list = collections.deque([0])  # 当前层的旧节点列表

        while now_node_list:
            for _ in range(len(now_node_list)):
                now_node = now_node_list.popleft()
                now_step = visited[now_node]
                for next_node, next_step in graph[now_node].items():
                    if now_step + next_step + 1 <= M:
                        if next_node not in visited or now_step + next_step + 1 < visited[next_node]:
                            visited[next_node] = now_step + next_step + 1
                            now_node_list.append(next_node)

        # 统计能够到达的旧节点数量
        ans = len(visited)

        # 统计能够到达的新节点数量
        for n1, n2, distance in edges:
            s1 = M - visited[n1] if n1 in visited else 0
            s2 = M - visited[n2] if n2 in visited else 0
            ans += min(distance, s1 + s2)

        return ans
```