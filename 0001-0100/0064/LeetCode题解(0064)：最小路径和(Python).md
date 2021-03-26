# LeetCode题解(0064)：最小路径和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-path-sum/)（中等）

标签：数组、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 88ms (6.12%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    _BIG = 200 * 100

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min((dp[i - 1][j] if i > 0 else self._BIG),
                                                (dp[i][j - 1] if j > 0 else self._BIG))

        return dp[-1][-1]
```

