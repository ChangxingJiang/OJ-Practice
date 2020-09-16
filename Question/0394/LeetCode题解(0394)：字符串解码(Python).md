# LeetCode题解(0394)：字符串解码(Python)

题目：[原题链接](https://leetcode-cn.com/problems/decode-string/)（中等）

标签：栈、字符串、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 28ms (99.08%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈）：

```python
def decodeString(self, s: str) -> str:
    size = len(s)
    stack = [""]
    idx = 0
    while idx < size:
        ch = s[idx]
        if ch.isdigit():
            number = ch
            while idx + 1 < size and s[idx + 1].isdigit():
                idx += 1
                number += s[idx]
            stack.append(int(number))
        elif ch == "[":
            stack.append("")
        elif ch == "]":
            text = stack.pop()
            p = stack.pop()
            stack[-1] += text * p
        else:
            stack[-1] += ch
        idx += 1
    return stack[0]
```

