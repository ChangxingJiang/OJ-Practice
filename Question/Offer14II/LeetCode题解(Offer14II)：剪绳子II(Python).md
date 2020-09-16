# LeetCode题解(Offer14II)：将整数n拆分为m个和为n的整数，求m个整数的最大乘积(结果取模)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/)（中等）

标签：数学

| 解法           | 时间复杂度                    | 空间复杂度 | 执行用时      |
| -------------- | ----------------------------- | ---------- | ------------- |
| Ans 1 (Python) | 最坏情况时间复杂度 : $O(N^2)$ | $O(N)$     | 92ms (38.63%) |
| Ans 2 (Python) | $O(N)$                        | $O(1)$     | 36ms (93.45%) |
| Ans 3 (Python) |                               |            |               |

解法一（数学）：

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        ans = 0
        for m in range(2, n + 1):
            a, b = divmod(n, m)
            lst = [a + 1 if i < b else a for i in range(m)]
            val = 1
            for v in lst:
                val *= v
            if val >= ans:
                ans = val
            else:
                break

        return ans % 1000000007
```

解法二（归纳）：

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        ans = 1
        while n > 4:
            ans *= 3
            n -= 3
        return (ans * n) % 1000000007
```