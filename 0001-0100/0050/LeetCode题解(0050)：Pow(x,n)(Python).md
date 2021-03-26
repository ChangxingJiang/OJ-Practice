# LeetCode题解(0050)：Pow(x,n)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/powx-n/)（中等）

标签：数学、递归、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 36ms (90.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x

        def count(xx, nn):
            if nn == 0:
                return 1
            if nn == 1:
                return x
            a = nn // 2
            b = nn - a
            if a == b:
                val = count(xx, a)
                return val * val
            else:
                return count(xx, a) * count(xx, b)

        return count(x, n)
```