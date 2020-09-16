# LeetCode题解(1249)：移除字符串中最少的无效括号使剩余的括号成对(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses/)（中等）

标签：栈、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 104ms (97.07%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（栈）：

```python
def minRemoveToMakeValid(self, s: str) -> str:
    stack = []
    i = 0
    N = len(s)
    while i < N:
        if s[i] == ")":
            if not stack:
                s = s[:i] + s[i + 1:]
                N -= 1
                i -= 1
            else:
                stack.pop()
        elif s[i] == "(":
            stack.append(i)
        i += 1
    while stack:
        i = stack.pop()
        s = s[:i] + s[i + 1:]

    return s
```