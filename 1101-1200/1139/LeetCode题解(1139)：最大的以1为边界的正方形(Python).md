# LeetCode题解(1139)：最大的以1为边界的正方形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-1-bordered-square/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 180ms (56.30%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]  # 左上右下

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i > 0:
                        dp[i][j][0] = dp[i - 1][j][0] + 1
                    else:
                        dp[i][j][0] = 1

                    if j > 0:
                        dp[i][j][1] = dp[i][j - 1][1] + 1
                    else:
                        dp[i][j][1] = 1

        ans = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    if i < m - 1:
                        dp[i][j][2] = dp[i + 1][j][2] + 1
                    else:
                        dp[i][j][2] = 1

                    if j < n - 1:
                        dp[i][j][3] = dp[i][j + 1][3] + 1
                    else:
                        dp[i][j][3] = 1

                    v1 = min(dp[i][j][2], dp[i][j][3])

                    if v1 > ans:
                        for v2 in range(ans + 1, v1 + 1):
                            if v2 > ans:
                                if min(dp[i + v2 - 1][j + v2 - 1][0], dp[i + v2 - 1][j + v2 - 1][1]) >= v2:
                                    ans = v2

        return ans * ans
```

