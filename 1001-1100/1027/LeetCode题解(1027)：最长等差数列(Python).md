# LeetCode题解(1027)：最长等差数列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-arithmetic-subsequence/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N×K)$   | $O(N×K)$   | 5752ms (10.82%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        size = len(A)

        ans = 0

        dp = [[1] * 20001 for _ in range(size)]

        for i in range(size):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff + 10000] = dp[j][diff + 10000] + 1
                ans = max(ans, dp[i][diff + 10000])

        return ans
```

