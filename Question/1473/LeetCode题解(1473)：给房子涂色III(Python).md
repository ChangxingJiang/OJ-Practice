# LeetCode题解(1473)：给房子涂色III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/paint-house-iii/)（困难）

标签：动态规划

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时        |
| -------------- | ------------ | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2×T×M)$ | $O(N×M×T)$ | 2124ms (58.73%) |
| Ans 2 (Python) |              |            |                 |
| Ans 3 (Python) |              |            |                 |

解法一：

```python
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # 定义状态矩阵：i=当前房子的序数，j=上一个房子的颜色，k=当前街区数；dp[i][j][k]=最小成本
        dp = [[[-1] * (target + 1) for _ in range(n)] for _ in range(m)]

        # 处理第一间房子的情况
        if houses[0] == 0:  # 如果第一间房子还没有被染色
            for j in range(n):
                dp[0][j][1] = cost[0][j]
        else:  # 如果第一间房子已经被染色
            j = houses[0] - 1
            dp[0][j][1] = 0

        # 状态转移
        for i in range(1, m):
            if houses[i] == 0:  # 如果当前房子还没有被染色
                for j2 in range(n):  # 遍历当前房子可能的颜色
                    for k in range(1, target + 1):  # 遍历街区总数
                        for j1 in range(n):  # 遍历上一个房子的颜色
                            if j1 == j2:
                                if dp[i - 1][j1][k] != -1:
                                    if dp[i][j2][k] == -1 or dp[i - 1][j1][k] + cost[i][j2] < dp[i][j2][k]:
                                        dp[i][j2][k] = dp[i - 1][j1][k] + cost[i][j2]
                            else:
                                if dp[i - 1][j1][k - 1] != -1:
                                    if dp[i][j2][k] == -1 or dp[i - 1][j1][k - 1] + cost[i][j2] < dp[i][j2][k]:
                                        dp[i][j2][k] = dp[i - 1][j1][k - 1] + cost[i][j2]

            else:  # 如果当前房子已经被染色
                j2 = houses[i] - 1  # 当前房子的颜色
                for k in range(1, target + 1):  # 遍历各个街区数
                    for j1 in range(n):  # 遍历上一个房子的颜色
                        if j1 == j2:
                            if dp[i - 1][j1][k] != -1:
                                if dp[i][j2][k] == -1 or dp[i - 1][j1][k] < dp[i][j2][k]:
                                    dp[i][j2][k] = dp[i - 1][j1][k]
                        else:
                            if dp[i - 1][j1][k - 1] != -1:
                                if dp[i][j2][k] == -1 or dp[i - 1][j1][k - 1] < dp[i][j2][k]:
                                    dp[i][j2][k] = dp[i - 1][j1][k - 1]

        # 返回最终结果
        ans = [dp[-1][j][-1] for j in range(n) if dp[-1][j][-1] != -1]
        return min(ans) if ans else -1
```

