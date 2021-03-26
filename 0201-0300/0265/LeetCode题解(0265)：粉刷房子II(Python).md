# LeetCode题解(0265)：粉刷房子II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/paint-house-ii/)（困难）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NK)$    | $O(NK)$    | 120ms (27.21%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0

        s1, s2 = len(costs), len(costs[0])  # s1=房子数量，s2=颜色数量

        dp = [[0] * s2 for _ in range(s1)]
        for i2 in range(s2):
            dp[0][i2] = costs[0][i2]

        for i1 in range(1, s1):
            for i2 in range(s2):
                dp[i1][i2] = costs[i1][i2] + min(dp[i1 - 1][ii2] for ii2 in range(s2) if ii2 != i2)

        return min(dp[-1])
```