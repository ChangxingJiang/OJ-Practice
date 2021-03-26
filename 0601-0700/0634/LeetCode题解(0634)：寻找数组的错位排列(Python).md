# LeetCode题解(0634)：寻找数组的错位排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-derangement-of-an-array/)（中等）

标签：动态规划、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 460ms (18.18%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def findDerangement(self, n: int) -> int:
        dp = [0] * max(2, n + 1)
        dp[0], dp[1] = 1, 0
        for i in range(2, n + 1):
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % self._MOD
        return dp[n]
```

