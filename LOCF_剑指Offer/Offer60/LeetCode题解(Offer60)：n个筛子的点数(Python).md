# LeetCode题解(Offer60)：计算n个骰子的点数的概率分布(Python)

题目：[原题链接](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)（简单）

标签：数学、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 40ms (79.79%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（数学）：

```python
class Solution:
    def twoSum(self, n: int) -> List[float]:
        max_len = 6 * n
        dp = [[0] * max_len for _ in range(n)]

        for j in range(6):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(i, 6 * (i + 1)):
                for k in range(1, 7):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k]

        total = 6 ** n

        return [i / total for i in dp[-1] if i > 0]
```