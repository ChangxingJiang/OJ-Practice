# LeetCode题解(0837)：新21点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/new-21-game/)（中等）

标签：动态规划

| 解法           | 时间复杂度      | 空间复杂度 | 执行用时      |
| -------------- | --------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(min(K+W,N))$ | $O(K+W)$   | 92ms (58.26%) |
| Ans 2 (Python) |                 |            |               |
| Ans 3 (Python) |                 |            |               |

解法一：

```python
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0

        dp = [0.0] * (K + W)
        for i in range(K, min(N + 1, K + W)):
            dp[i] = 1

        dp[K - 1] = min(N - K + 1, W) / W

        for i in range(K - 2, -1, -1):
            dp[i] += dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]
```

