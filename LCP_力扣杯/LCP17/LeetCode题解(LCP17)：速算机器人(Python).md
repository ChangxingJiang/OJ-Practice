# LeetCode题解(LCP17)：速算机器人(Python)

题目：[原题链接](https://leetcode-cn.com/problems/nGK0Fy/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(S)$     | $O(1)$     | 32ms (94.86%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for ch in s:
            if ch == "A":
                x = 2 * x + y
            else:
                y = 2 * y + x
        return x + y
```