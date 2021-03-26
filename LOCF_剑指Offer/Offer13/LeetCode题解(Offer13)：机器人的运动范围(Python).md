# LeetCode题解(Offer13)：符合指定要求的格坐标数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)（中等）

标签：分治算法、广度优先搜索

| 解法           | 时间复杂度                              | 空间复杂度 | 执行用时      |
| -------------- | --------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×M)$                                | $O(1)$     | 52ms (89.27%) |
| Ans 2 (Python) | $O(\frac{N}{10}×\frac{M}{10}) = O(N×M)$ | $O(1)$     | 36ms (99.90%) |
| Ans 3 (Python) |                                         |            |               |

解法一（暴力的分治算法）：

```python
class Solution:
    def simple_range(self, m, n, k):
        """一个单独的区域的计算（即一个10*10的范围中的计算）"""
        ans = 0
        m, n = min(m, 10), min(n, 10)
        for i in range(m):
            for j in range(n):
                if sum([int(ch) for ch in str(i)]) + sum([int(ch) for ch in str(j)]) <= k:
                    ans += 1
        return ans

    def movingCount(self, m: int, n: int, k: int) -> int:
        ans = self.simple_range(m, n, k)
        idx = 1
        while k >= 9:
            for i in range(idx + 1):
                mm = m - i * 10
                nn = n - (idx - i) * 10
                if mm > 0 and nn > 0:
                    ans += self.simple_range(mm, nn, k)
            k -= 1
            idx += 1
        return ans
```

解法二（优化的分治算法）：

![LeetCode题解(Offer13)：截图](LeetCode题解(Offer13)：截图.png)

```python
class Solution:
    def simple_range(self, m, n, k):
        """一个单独的区域的计算（即一个10*10的范围中的计算）"""
        m = min(m, 10)
        n = min(n, 10)
        if k <= max(m, n)-1:
            k += 1
            ans = (k + 1) * k / 2
            d1 = k - m
            d2 = k - n
            ans -= (d1 + 1) * d1 / 2 if d1 > 0 else 0
            ans -= (d2 + 1) * d2 / 2 if d2 > 0 else 0
            return int(ans)
        else:
            k = (m + n - 2) - k
            return int(m * n - (k + 1) * k / 2) if k > 0 else m * n

    def movingCount(self, m: int, n: int, k: int) -> int:
        ans = self.simple_range(m, n, k)
        idx = 1
        while k >= 9:
            k -= 1
            for i in range(idx + 1):
                mm = m - i * 10
                nn = n - (idx - i) * 10
                if mm > 0 and nn > 0:
                    # print(mm, nn, k, "->", self.simple_range(mm, nn, k))
                    ans += self.simple_range(mm, nn, k)
            idx += 1
        return ans
```