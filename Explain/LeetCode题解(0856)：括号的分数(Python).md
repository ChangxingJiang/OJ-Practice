# LeetCode题解(0856)：依据指定规则计算平衡括号字符串的分数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/score-of-parentheses/)（中等）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 32ms (96.56%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈）：

```python
def scoreOfParentheses(self, S: str) -> int:
    stack = []
    for ch in S:
        if ch == "(":
            stack.append(ch)
        else:
            now = 0
            while stack and stack[-1] != "(":
                now += stack.pop()
            stack.pop()
            stack.append(now * 2 if now else 1)
    return sum(stack)
```