# LeetCode题解(1021)：删除最外层的括号(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-outermost-parentheses/（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (77.50%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def removeOuterParentheses(self, S: str) -> str:
    count = 0
    ans = ""
    for s in S:
        if s == "(":
            count += 1
            if count > 1:
                ans += s
        else:
            count -= 1
            if count > 0:
                ans += s
    return ans
```

