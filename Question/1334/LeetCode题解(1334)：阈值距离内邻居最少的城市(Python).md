# LeetCode题解(1334)：阈值距离内邻居最少的城市(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)（中等）

标签：图、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×E)$   | $O(N+E)$   | 912ms (37.33%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(dict)
        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]

        ans_idx, ans_val = -1, n
        for city in range(n):
            visited = collections.Counter({city: 0})
            queue = collections.deque([(city, 0)])
            while queue:
                for _ in range(len(queue)):
                    city1, d1 = queue.popleft()
                    for city2 in graph[city1]:
                        d2 = d1 + graph[city1][city2]
                        if d2 <= distanceThreshold and (city2 not in visited or d2 < visited[city2]):
                            queue.append((city2, d2))
                            visited[city2] = d2
            if len(visited) <= ans_val:
                ans_idx, ans_val = city, len(visited)

        return ans_idx
```

