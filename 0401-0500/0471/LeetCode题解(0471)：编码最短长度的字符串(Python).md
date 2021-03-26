# LeetCode题解(0471)：编码最短长度的字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/encode-string-with-shortest-length/)（困难）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N^2)$   | 204ms (67.86%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def encode(self, s: str) -> str:
        size = len(s)

        dp = [[""] * size for _ in range(size)]

        for l in range(1, size + 1):
            for i in range(size - l + 1):
                j = i + l - 1
                dp[i][j] = s[i:j + 1]
                if l > 4:
                    # 寻找是否为某一段的重复
                    idx = (s[i:j + 1] + s[i:j + 1]).index(s[i:j + 1], 1)
                    if idx < l:
                        dp[i][j] = str(l // idx) + "[" + dp[i][i + idx - 1] + "]"

                    # 寻找是否有更优解
                    for k in range(i, j):
                        if len(dp[i][k]) + len(dp[k + 1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k + 1][j]

        return dp[0][-1]
```