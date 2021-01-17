# LeetCode题解(0474)：一和零(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ones-and-zeroes/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N×M×S)$ | $O(M×N)$   | 2928ms (81.41%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def findMaxForm(self, ss: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in ss:
            n1, n2 = s.count("0"), s.count("1")
            for i in range(m, n1 - 1, -1):
                for j in range(n, n2 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - n1][j - n2] + 1)
        return dp[-1][-1]
```

