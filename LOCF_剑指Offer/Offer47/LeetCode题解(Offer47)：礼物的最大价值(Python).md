# LeetCode题解(Offer47)：计算从礼物二维数组的左上角向右下走到右下角所能得到的礼物最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)（中等）

标签：数组、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 52ms (92.89%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（动态规划）：

```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        N1 = len(grid)
        N2 = len(grid[0])

        dp = [[0] * N2 for _ in range(N1)]
        dp[0][0] = grid[0][0]

        for i in range(1, N1):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, N2):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, N1):
            for j in range(1, N2):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[-1][-1]
```