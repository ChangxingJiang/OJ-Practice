# LeetCode题解(1621)：大小为K的不重叠线段的数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N×K)$   | $O(N×K)$   | 544ms (59%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一（动态规划）：

```python
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # 处理不够分的情况
        if n - 1 < k:
            # print("计算:", n, k, "->", 0)
            return 0

        # 处理刚好够分的情况
        if n - 1 == k:
            # print("计算:", n, k, "->", 1)
            return 1

        # 处理只分成一个的情况
        if k == 1:
            # print("计算:", n, k, "->", n * (n - 1) // 2)
            return n * (n - 1) // 2

        # 处理一般的情况

        # 定义状态表格
        # O(N×K)
        dp = [[0] * n for _ in range(k)]

        # 计算第一行
        for j in range(1, n):
            dp[0][j] = j * (j + 1) // 2

        # 计算其他行
        for i in range(1, k):
            total = dp[i - 1][i]
            for j in range(i + 1, n):
                dp[i][j] = dp[i][j - 1] + total
                total += dp[i - 1][j]

        return dp[-1][-1] % (10 ** 9 + 7)
```