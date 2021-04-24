# LeetCode题解(1770)：执行乘法运算的最大分数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-score-from-performing-multiplication-operations/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(M^2)$   | $O(M^2)$   | 6684ms (64.66%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    _MAX = 10 ** 9

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        # 定义状态矩阵：dp[i][j] 前面移除i个，后面移除j个时的最大分数
        dp = [[-self._MAX] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 0

        for k in range(m):  # 遍历之前被移除的总数
            for i in range(k + 1):  # 遍历前面被移除的数量
                j = k - i

                # 状态转移
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + nums[i] * multipliers[k])
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + nums[n - j - 1] * multipliers[k])

        # 计算最终结果
        ans = -self._MAX
        for i in range(m + 1):
            j = m - i
            ans = max(ans, dp[i][j])
        return ans
```

