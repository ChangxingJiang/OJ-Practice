# LeetCode题解(0921)：使字符串括号有效最少需要添加多少个括号(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid/)（中等）

标签：字符串、正则表达式、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 36ms (89.89%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 40ms (74.95%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（正则表达式处理）：

```python
def minAddToMakeValid(self, S: str) -> int:
    S, num = re.subn(r"\((?=.*?)\)", "", S)
    while num > 0:
        S, num = re.subn(r"\((?=.*?)\)", "", S)
    return len(S)
```

解法二（栈）：

```python
def minAddToMakeValid(self, S: str) -> int:
    stack = []
    for ch in S:
        if ch == "(":
            stack.append(ch)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(ch)
    return len(stack)
```