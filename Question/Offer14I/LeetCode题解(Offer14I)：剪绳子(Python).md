# LeetCode题解(Offer14I)：将整数n拆分为m个和为n的整数，求m个整数的最大乘积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/jian-sheng-zi-lcof/)（中等）

标签：数学

| 解法           | 时间复杂度                | 空间复杂度 | 执行用时      |
| -------------- | ------------------------- | ---------- | ------------- |
| Ans 1 (Python) | 最坏平均复杂度 : $O(N^2)$ | $O(N)$     | 36ms (92.78%) |
| Ans 2 (Python) |                           |            |               |
| Ans 3 (Python) |                           |            |               |

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
                
        return ans
```