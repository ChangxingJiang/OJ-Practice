# LeetCode题解(1824)：最少侧跳次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-sideway-jumps/)（中等）

标签：动态规划、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 1160ms (74.09%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    _MAX = 10 ** 6

    def minSideJumps(self, obstacles: List[int]) -> int:
        # 定义状态矩阵
        dp = [self._MAX, 0, self._MAX]

        for num in obstacles:
            if num == 1:
                dp[0] = self._MAX
                dp[1] = min(dp[1], dp[2] + 1)
                dp[2] = min(dp[2], dp[1] + 1)
            elif num == 2:
                dp[1] = self._MAX
                dp[0] = min(dp[0], dp[2] + 1)
                dp[2] = min(dp[2], dp[0] + 1)
            elif num == 3:
                dp[2] = self._MAX
                dp[0] = min(dp[0], dp[1] + 1)
                dp[1] = min(dp[1], dp[0] + 1)
            else:  # num == 0
                dp[0] = min(dp[0], dp[1] + 1, dp[2] + 1)
                dp[1] = min(dp[1], dp[0] + 1, dp[2] + 1)
                dp[2] = min(dp[2], dp[0] + 1, dp[1] + 1)

        return min(dp)
```

