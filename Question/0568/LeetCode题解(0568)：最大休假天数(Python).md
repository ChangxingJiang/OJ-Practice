# LeetCode题解(0568)：最大休假天数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-vacation-days/)（困难）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时         |
| -------------- | ---------- | ---------- | ---------------- |
| Ans 1 (Python) | $O(N^2K)$  | $O(N)$     | 1472ms (100.00%) |
| Ans 2 (Python) |            |            |                  |
| Ans 3 (Python) |            |            |                  |

解法一：

```python
class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n, k = len(flights), len(days[0])

        # 构造邻接列表格式的图
        # 有向图（不一定是对称的）
        graph = collections.defaultdict(set)
        for city1 in range(n):
            for city2 in range(n):
                if flights[city1][city2]:
                    graph[city2].add(city1)  # 城市j可以由i到达

        # 按周和城市动态规划
        dp = [float("-inf")] * n
        dp[0] = 0
        for week in range(k):
            new = [float("-inf")] * n
            for city2 in range(n):
                new[city2] = dp[city2] + days[city2][week]
                for city1 in graph[city2]:
                    new[city2] = max(new[city2], dp[city1] + days[city2][week])
            dp = new

        return int(max(dp))
```