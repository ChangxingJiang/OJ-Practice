# LeetCode题解(0010)：正则表达式匹配的*和.实现(Python)

题目：[原题链接](https://leetcode-cn.com/problems/regular-expression-matching/)（困难）

标签：字符串、动态规划、动态规划-状态表格

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 56ms (87.00%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（动态规划）：

```python
def isMatch(self, s: str, p: str) -> bool:
    N1 = len(s)
    N2 = len(p)

    matrix = [[False] * (N2 + 1) for _ in range(N1 + 1)]
    matrix[0][0] = True

    for i in range(N1 + 1):
        for j in range(1, N2 + 1):
            if p[j - 1] == "*":
                matrix[i][j] |= matrix[i][j - 2]
                # print((i, j - 2), "->", (i, j))
                if i > 0 and (p[j - 2] == "." or s[i - 1] == p[j - 2]):
                    matrix[i][j] |= matrix[i - 1][j]
                    # print((i - 1, j), "->", (i, j))
            elif i > 0 and (p[j - 1] == "." or s[i - 1] == p[j - 1]):
                matrix[i][j] |= matrix[i - 1][j - 1]
                # print((i - 1, j - 1), "->", (i, j))

    return matrix[N1][N2]
```