# LeetCode题解(0276)：栅栏涂色(Python)

题目：[原题链接](https://leetcode-cn.com/problems/paint-fence/)（简单）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 28ms (98.81%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0

        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = k

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] * (k - 1) + dp[i - 1][1] * (k - 1)
            dp[i][1] = dp[i - 1][0]

        return sum(dp[-1])
```