# LeetCode题解(0223)：矩形面积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rectangle-area/)（中等）

标签：几何、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 72ms (14.66%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    @staticmethod
    def count(a, b, c, d):
        if a <= c <= b <= d:
            return b - c
        elif c <= a <= d <= b:
            return d - a
        elif a <= c <= d <= b:
            return d - c
        elif c <= a <= b <= d:
            return b - a
        else:
            return 0

    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        res1 = self.count(A, C, E, G)
        res2 = self.count(B, D, F, H)

        s1 = abs(A - C) * abs(B - D)
        s2 = abs(E - G) * abs(F - H)

        return s1 + s2 - res1 * res2
```

