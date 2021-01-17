# LeetCode题解(0650)：只有两个键的键盘(Python)

题目：[原题链接](https://leetcode-cn.com/problems/2-keys-keyboard/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 96ms (35.73%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[1] = 0
        for i in range(1, n + 1):
            for j in range(1, n // i):
                dp[i * (j + 1)] = min(dp[i * (j + 1)], dp[i] + 1 + j)
        return dp[-1]
```

