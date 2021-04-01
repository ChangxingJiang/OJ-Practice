# LeetCode题解(1808)：好因子的最大数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximize-number-of-nice-divisors/)（困难）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 32ms (95.80%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    # 相当于找n个数，它们的和为primeFactors，求乘积的最大值
    def maxNiceDivisors(self, f: int) -> int:
        if f == 1:
            return 1

        a, b = divmod(f, 3)
        if b == 0:
            return pow(3, a, mod=self._MOD)
        elif b == 1:
            return pow(3, a - 1, mod=self._MOD) * 4 % self._MOD
        else:  # b==2
            return pow(3, a, mod=self._MOD) * 2 % self._MOD
```

