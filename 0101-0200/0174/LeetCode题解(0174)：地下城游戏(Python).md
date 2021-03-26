# LeetCode题解(0174)：地下城游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/dungeon-game/)（困难）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 64ms (20.53%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _BIG = 2 ** 31

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # 初始化状态矩阵
        dp = [[self._BIG] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1  # 右下角位置的右侧和下方

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                res = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(res, 1)

        return dp[0][0]
```

