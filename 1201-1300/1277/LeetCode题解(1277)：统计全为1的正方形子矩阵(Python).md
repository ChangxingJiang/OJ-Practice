# LeetCode题解(1277)：统计全为1的正方形子矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/)（中等）

标签：动态规划、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 160ms (88.15%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                        ans += 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                        ans += dp[i][j]

        return ans
```

