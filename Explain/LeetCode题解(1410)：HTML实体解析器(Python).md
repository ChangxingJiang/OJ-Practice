# LeetCode题解(1410)：HTML特殊字符实体解析器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/html-entity-parser/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 140ms (49.70%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 56ms (98.82%)  |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（字符串检索替换）：

```python
def entityParser(self, text: str) -> str:
    marks = {
        "&quot;": "\"",
        "&apos;": "'",
        "&amp;": "&",
        "&gt;": ">",
        "&lt;": "<",
        "&frasl;": "/"
    }
    i = 0
    N = len(text)
    ans = []
    while i < N:
        try:
            start = text.index("&", i)
            end = text.index(";", start)
            mark = text[start:end + 1]
            if mark in marks:
                ans.append(text[i:start])
                ans.append(marks[mark])
            else:
                ans.append(text[i:end + 1])
            i = end + 1
        except ValueError:
            ans.append(text[i:])
            break
    return "".join(ans)
```

解法二（字符串直接替换）：

```python
def entityParser(self, text: str) -> str:
    return text.replace("&quot;", "\"").replace("&apos;", "'").replace("&gt;", ">").replace("&lt;", "<").replace("&frasl;", "/").replace("&amp;", "&")
```