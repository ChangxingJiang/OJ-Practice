# LeetCode题解(0787)：K站中转内最便宜的航班(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/)（中等）

标签：图、广度优先搜索、堆、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NK)$    | $O(N)$     | 48ms (95.60%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（图的广度优先搜索）：

```python
def build_graph(edges):
    graph = collections.defaultdict(dict)
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    return graph


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = build_graph(flights)

        visited = collections.Counter({src: 0})

        ans = float("inf")
        now_city = collections.deque([(src, 0)])
        while K >= 0:
            for _ in range(len(now_city)):
                city, cost1 = now_city.popleft()
                for near, cost2 in graph[city].items():
                    cost = cost1 + cost2
                    if near == dst and cost < ans:
                        ans = cost
                    elif (near not in visited or visited[near] > cost) and cost < ans:
                        now_city.append((near, cost))
                        visited[near] = cost

            K -= 1

        return ans if ans != float("inf") else -1
```