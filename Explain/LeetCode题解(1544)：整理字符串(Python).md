# LeetCode题解(1544)：移除字符串中连续的、相同字母的大写和小写字符(Python)

题目：[原题链接](https://leetcode-cn.com/problems/make-the-string-great/)（简单）

标签：栈、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (99.70%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（栈）：

![LeetCode题解(1544)：截图](LeetCode题解(1544)：截图.png)

```python
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack or abs(ord(stack[-1]) - ord(ch)) != 32:
                stack.append(ch)
            else:
                stack.pop()
        return "".join(stack)
```