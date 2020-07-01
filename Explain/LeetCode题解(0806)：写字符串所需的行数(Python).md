# LeetCode题解(0806)：写字符串所需的行数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-lines-to-write-string/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (78.76%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def numberOfLines(self, widths: List[int], S: str) -> List[int]:
    line = 1
    now = 0
    for s in S:
        width = widths[ord(s) - 97]
        if now + width > 100:
            line += 1
            now = 0
        now += width
    return [line, now]
```

