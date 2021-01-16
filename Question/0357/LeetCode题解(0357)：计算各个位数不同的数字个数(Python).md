# LeetCode题解(0357)：计算各个位数不同的数字个数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-numbers-with-unique-digits/)（中等）

标签：数学、回溯算法、动态规划

| 解法           | 时间复杂度  | 空间复杂度 | 执行用时      |
| -------------- | ----------- | ---------- | ------------- |
| Ans 1 (Python) | $O(log^2N)$ | $O(logN)$  | 40ms (54.68%) |
| Ans 2 (Python) |             |            |               |
| Ans 3 (Python) |             |            |               |

解法一：

```python
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 9 + self.countNumbersWithUniqueDigits(0)
        else:
            res = 9 * 9
            for i in range(2, n):
                res *= (10 - i)
            return res + self.countNumbersWithUniqueDigits(n - 1)
```

