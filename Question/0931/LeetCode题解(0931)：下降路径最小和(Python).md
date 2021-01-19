# LeetCode题解(0931)：下降路径最小和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-falling-path-sum/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 68ms (56.74%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _BIG = 10001

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        size = len(A)
        dp = [[self._BIG] * size for i in range(size)]

        for j in range(size):
            dp[0][j] = A[0][j]

        for i in range(1, size):
            for j in range(size):
                dp[i][j] = min(dp[i - 1][j - 1] if j > 0 else self._BIG,
                               dp[i - 1][j],
                               dp[i - 1][j + 1] if j < size - 1 else self._BIG) + A[i][j]
        return min(dp[-1])
```

