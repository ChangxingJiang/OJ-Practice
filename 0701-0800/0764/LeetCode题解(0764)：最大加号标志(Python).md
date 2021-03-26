# LeetCode题解(0764)：最大加号标志(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-plus-sign/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2+M)$ | $O(N^2)$   | 4016ms (22.22%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        dp = [[[0] * 4 for _ in range(N)] for _ in range(N)]  # dp[i][j] = [1,1,1,1] 上左下右的长度
        for (i, j) in mines:
            dp[i][j] = [-1] * 4

        for i in range(N):
            for j in range(N):
                if dp[i][j][0] == -1:
                    continue
                # 统计上方连续1的数量
                if i == 0 or dp[i - 1][j][0] == -1:
                    dp[i][j][0] = 0
                else:
                    dp[i][j][0] = dp[i - 1][j][0] + 1
                # 统计左方连续1的数量
                if j == 0 or dp[i][j - 1][1] == -1:
                    dp[i][j][1] = 0
                else:
                    dp[i][j][1] = dp[i][j - 1][1] + 1

        ans = 0
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if dp[i][j][0] == -1:
                    continue
                # 统计下方连续1的数量
                if i == N - 1 or dp[i + 1][j][2] == -1:
                    dp[i][j][2] = 0
                else:
                    dp[i][j][2] = dp[i + 1][j][2] + 1
                # 统计右方连续1的数量
                if j == N - 1 or dp[i][j + 1][3] == -1:
                    dp[i][j][3] = 0
                else:
                    dp[i][j][3] = dp[i][j + 1][3] + 1
                # 统计最大加号
                ans = max(ans, min(dp[i][j]) + 1)

        return ans
```

