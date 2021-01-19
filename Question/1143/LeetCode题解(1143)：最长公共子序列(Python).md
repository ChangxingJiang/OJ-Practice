# LeetCode题解(1143)：最长公共子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-common-subsequence/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 456ms (26.86%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1, s2 = len(text1), len(text2)

        dp = [[0] * (s2 + 1) for _ in range(s1 + 1)]

        for i in range(1, s1 + 1):
            for j in range(1, s2 + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        return dp[-1][-1]
```

