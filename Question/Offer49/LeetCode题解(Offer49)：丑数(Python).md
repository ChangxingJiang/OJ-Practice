# LeetCode题解(Offer49)：计算第N个丑数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/chou-shu-lcof/)（中等）

标签：数学、动态规划

| 解法           | 时间复杂度                 | 空间复杂度 | 执行用时       |
| -------------- | -------------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(MlogM)$ : M为丑数的个数 | $O(1)$     | 超出时间限制   |
| Ans 2 (Python) | $O(N)$                     | $O(N)$     | 148ms (94.04%) |
| Ans 3 (Python) |                            |            |                |

解法一（最暴力的暴力解法）：

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num = 1
        cnt = 0
        while cnt < n:
            tmp = num
            while tmp % 2 == 0:
                tmp /= 2
            while tmp % 3 == 0:
                tmp /= 3
            while tmp % 5 == 0:
                tmp /= 5
            if tmp == 1:
                cnt += 1
                if cnt == n:
                    return num
            num += 1
```

解法二（动态规划）：

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        i1, i2, i3 = 0, 0, 0
        for i in range(1, n):
            n1, n2, n3 = dp[i1] * 2, dp[i2] * 3, dp[i3] * 5
            dp[i] = min(n1, n2, n3)
            if n1 == dp[i]:
                i1 += 1
            if n2 == dp[i]:
                i2 += 1
            if n3 == dp[i]:
                i3 += 1
        return dp[-1]
```