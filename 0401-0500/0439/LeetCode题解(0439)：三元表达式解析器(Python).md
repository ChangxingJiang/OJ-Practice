# LeetCode题解(0439)：三元表达式解析器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ternary-expression-parser/)（中等）

标签：栈、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (94.87%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        count = 0
        now = ""
        for ch in expression:
            if ch == "?":
                if now == "T":
                    if stack:
                        count += 1
                        stack.append(now)
                else:
                    count += 1
                    stack.append(now)
            elif ch == ":":
                if count <= 0:
                    return now
                count -= 1
                stack.pop()
            else:
                now = ch
        return now
```

