# LeetCode题解(面试08.11)：硬币(Python)

题目：[原题链接](https://leetcode-cn.com/problems/coin-lcci/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 920ms (62.46%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（动态规划）：

```python
class Solution:
    def waysToChange(self, n: int) -> int:
        # 处理1分硬币
        dp = [[1] * (n + 1)] + [[0] * (n + 1) for _ in range(3)]

        # 处理5分硬币
        for i in range(n + 1):
            dp[1][i] = dp[0][i] + (dp[1][i - 5] if i >= 5 else 0)

        # 处理10分硬币
        for i in range(n + 1):
            dp[2][i] = dp[1][i] + (dp[2][i - 10] if i >= 10 else 0)

        # 处理25分硬币
        for i in range(n + 1):
            dp[3][i] = dp[2][i] + (dp[3][i - 25] if i >= 25 else 0)

        return dp[-1][-1] % 1000000007
```