# LeetCode题解(面试08.05)：递归乘法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/recursive-mulitply-lcci/)（中等）

标签：递归、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(A+B)$   | $O(A+B)$   | 28ms (99.25%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A == 0 or B == 0:
            return 0
        elif A >= B:
            return self.multiply(A, B - 1) + A
        else:
            return self.multiply(A - 1, B) + B
```