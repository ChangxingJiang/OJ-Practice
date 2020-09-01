# LeetCode题解(1106)：解析字符串表示的布尔表达式(Python)

题目：[原题链接](https://leetcode-cn.com/problems/parsing-a-boolean-expression/)（困难）

标签：字符串、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 76ms (69.74%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 64ms (90.79%) |
| Ans 3 (Python) |            |            |               |

解法一（栈）：

```python
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = [[]]
        i = 0
        while i < len(expression):
            ch = expression[i]
            if ch == "!" or ch == "|" or ch == "&":
                stack.append([ch])
                i += 1
            elif ch == ")":
                now = stack.pop()
                if now[0] == "!":
                    tmp = not now[1]
                elif now[0] == "&":
                    tmp = all(now[1:])
                else:
                    tmp = any(now[1:])
                stack[-1].append(tmp)
            elif ch == "t":
                stack[-1].append(True)
            elif ch == "f":
                stack[-1].append(False)
            i += 1
            # print(stack)
        return stack[0][0]
```

解法二（将符号栈单独拆分）：

```python
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        mark_sign = []
        stack = [[]]
        for ch in expression:
            if ch == "!" or ch == "|" or ch == "&":
                mark_sign.append(ch)
                stack.append([])
            elif ch == ")":
                mark = mark_sign.pop()
                now = stack.pop()
                if mark == "!":
                    tmp = not now[0]
                elif mark == "&":
                    tmp = all(now)
                else:
                    tmp = any(now)
                stack[-1].append(tmp)
            elif ch == "t":
                stack[-1].append(True)
            elif ch == "f":
                stack[-1].append(False)
        return stack[0][0]
```