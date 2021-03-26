# LeetCode题解(0132)：分割回文串II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)（困难）

标签：动态规划、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 404ms (86.90%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minCut(self, s):
        size = len(s)

        # 计算是否为回文串
        is_palindrome = [[False] * size for _ in range(size)]
        for r in range(size):
            for l in range(r, -1, -1):
                if s[l] == s[r] and (r - l <= 2 or is_palindrome[l + 1][r - 1]):
                    is_palindrome[l][r] = True

        # 动态规划计算结果
        dp = [i for i in range(size)]
        for i in range(1, size):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j] + 1 for j in range(i) if is_palindrome[j + 1][i])

        return dp[-1]
```