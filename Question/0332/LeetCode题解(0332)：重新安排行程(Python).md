# LeetCode题解(0332)：重新安排行程(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reconstruct-itinerary/)（中等）

标签：图、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 44ms (87.47%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for city1, city2 in tickets:
            graph[city1].append(city2)
        for city in graph:
            heapq.heapify(graph[city])

        def dfs(c1):
            while graph[c1]:
                c2 = heapq.heappop(graph[c1])
                dfs(c2)
            stack.append(c1)

        stack = []
        dfs("JFK")
        return stack[::-1]
```

