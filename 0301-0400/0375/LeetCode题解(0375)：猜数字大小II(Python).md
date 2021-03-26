# LeetCode题解(0375)：猜数字大小II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii/)（中等）

标签：极小化极大、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 3448ms (27.07%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一（动态规划）：

```python
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            for j in range(n - i):
                print("i:", i, "j:", j)
                if i == 0:
                    dp[j][j + i] = 0
                elif i == 1:
                    dp[j][j + i] = j + 1
                elif i == 2:
                    dp[j][j + i] = j + 2
                else:
                    for k in range(i - 1):
                        dp[j][j + i] = min(dp[j][j + i], max(dp[j][j + k], dp[j + k + 2][j + i]) + (j + k + 2))
                        # print("k:", (j + k + 2), "->",
                        #       (j, j + k), "=", dp[j][j + k], ";",
                        #       (j + k + 2, j + i), "=", dp[j + k + 2][j + i],
                        #       "->", dp[j][j + k] + dp[j + k + 2][j + i] + (j + k + 2))
                    # print("i:", i, "j:", j, "->", (j, j + i), "=", dp[j][j + i])

        # for row in dp:
        #     print([str(v).zfill(3) for v in row])

        return int(dp[0][-1])
```