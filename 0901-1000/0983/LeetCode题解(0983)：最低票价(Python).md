# LeetCode题解(0983)：最低票价(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-cost-for-tickets/)（中等）

标签：动态规划、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (76.92%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _BIG = 10 ** 9 + +1

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        size = len(days)
        costs = [[1, costs[0]], [7, costs[1]], [30, costs[2]]]

        @functools.lru_cache(None)
        def dp(i):
            if i >= size:
                return 0
            ans = self._BIG
            j = i
            for day, cost in costs:
                while j < size and days[j] < days[i] + day:
                    j += 1
                ans = min(ans, dp(j) + cost)
            return ans

        return dp(0)
```

