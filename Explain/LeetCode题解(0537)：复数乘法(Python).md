# LeetCode题解(0537)：字符串表示的复数乘法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/complex-number-multiplication/)（中等）

标签：字符串、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 40ms (66.56%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a1, a2 = a[:-1].split("+")
        b1, b2 = b[:-1].split("+")
        a1, a2, b1, b2 = int(a1), int(a2), int(b1), int(b2)
        c1 = a1 * b1 - a2 * b2
        c2 = a1 * b2 + a2 * b1
        return str(c1) + "+" + str(c2) + "i"
```