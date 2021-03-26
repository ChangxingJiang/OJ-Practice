# LeetCode题解(1129)：颜色交替的最短路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shortest-path-with-alternating-colors/)（中等）

标签：图、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 132ms (24.37%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
def build_graph(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
    return graph


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_graph = build_graph(red_edges)
        blue_graph = build_graph(blue_edges)

        ans = [-1] * n

        # 先红色边的情况
        visited_red = {0}
        visited_blue = set()
        queue = collections.deque([0])
        step = 0
        while queue:
            for _ in range(len(queue)):
                n1 = queue.popleft()
                if ans[n1] == -1 or ans[n1] > step:
                    ans[n1] = step
                if step % 2 == 0:
                    for n2 in red_graph[n1]:
                        if n2 not in visited_blue:
                            visited_blue.add(n2)
                            queue.append(n2)
                else:
                    for n2 in blue_graph[n1]:
                        if n2 not in visited_red:
                            visited_red.add(n2)
                            queue.append(n2)
            step += 1

        # 先蓝色边的情况
        visited_red = set()
        visited_blue = {0}
        queue = collections.deque([0])
        step = 0
        while queue:
            for _ in range(len(queue)):
                n1 = queue.popleft()
                if ans[n1] == -1 or ans[n1] > step:
                    ans[n1] = step
                if step % 2 == 0:
                    for n2 in blue_graph[n1]:
                        if n2 not in visited_red:
                            visited_red.add(n2)
                            queue.append(n2)
                else:
                    for n2 in red_graph[n1]:
                        if n2 not in visited_blue:
                            visited_blue.add(n2)
                            queue.append(n2)
            step += 1

        return ans
```

