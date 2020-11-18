# LeetCode题解(面试01.09)：字符串轮转(Python)

题目：[原题链接](https://leetcode-cn.com/problems/string-rotation-lcci/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(N1)$    | 44ms (61.81%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if not s1 and not s2:
            return True
        elif not s2:
            return False
        return s2 in s1 * 3
```