# LeetCode题解(1514)：概率最大的路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/path-with-maximum-probability/)（中等）

标签：图

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 280ms (33.75%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(dict)
        for i, edge in enumerate(edges):
            graph[edge[0]][edge[1]] = succProb[i]
            graph[edge[1]][edge[0]] = succProb[i]

        visited = {start: 1}
        queue = collections.deque([start])
        while queue:
            n1 = queue.popleft()
            for n2 in graph[n1]:
                p2 = visited[n1] * graph[n1][n2]
                if n2 not in visited or p2 > visited[n2]:
                    visited[n2] = p2
                    queue.append(n2)

        return visited[end] if end in visited else 0
```

