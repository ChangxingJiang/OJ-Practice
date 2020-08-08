# LeetCode题解(1190)：反转字符串中每对括号间的子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/)（中等）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (78.74%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈）：

```
def reverseParentheses(self, s: str) -> str:
    stack = [[]]
    for ch in s:
        if ch == "(":
            stack.append([])
        elif ch == ")":
            inner = stack.pop()
            while inner:
                stack[-1].append(inner.pop())
        else:
            stack[-1].append(ch)
    return "".join(stack[0])
```