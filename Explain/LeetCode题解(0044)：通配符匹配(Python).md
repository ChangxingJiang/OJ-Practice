# LeetCode题解(0044)：通配符匹配的*和?实现(Python)

题目：[原题链接](https://leetcode-cn.com/problems/wildcard-matching/)（困难）

标签：字符串、动态规划、动态规划-状态表格、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 1088ms (22.10%) |
| Ans 2 (Python) | $O(N×M)$   | $O(N×M)$   | 40ms (99.98%)   |
| Ans 3 (Python) |            |            |                 |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（动态规划）：

```python
def isMatch(self, s: str, p: str) -> bool:
    N1 = len(s)  # 字符串长度
    N2 = len(p)  # 模式长度

    matrix = [[False] * (N2 + 1) for _ in range(N1 + 1)]  # 状态表格
    matrix[0][0] = True

    # 状态转移
    for i in range(N1 + 1):
        for j in range(1, N2 + 1):
            if p[j - 1] == "*":
                matrix[i][j] |= matrix[i - 1][j] or matrix[i][j - 1]
            elif i > 0 and (p[j - 1] == "?" or s[i - 1] == p[j - 1]):
                matrix[i][j] |= matrix[i - 1][j - 1]
            # print(i, j, ":", p[j - 1], "->", matrix)

    return matrix[N1][N2]
```

解法二（贪心算法，每个*都匹配最短的内容）：

![LeetCode题解(0044)：截图1](LeetCode题解(0044)：截图1.png)

```python
def isMatch(self, s: str, p: str) -> bool:
    N1 = len(s)  # 字符串长度
    N2 = len(p)  # 模式长度

    # 匹配最后一个*之后的内容是否匹配
    while N1 > 0 and N2 > 0 and p[N2 - 1] != "*":
        if p[N2 - 1] == "?" or p[N2 - 1] == s[N1 - 1]:
            N1 -= 1
            N2 -= 1
        else:
            return False

    # 处理模式已空的情况
    if N2 == 0:
        return N1 == 0

    # 匹配最后一个*之前的内容是否匹配
    i1 = i2 = 0
    r1 = r2 = -1
    while i1 < N1 and i2 < N2:
        if p[i2] == "*":
            i2 += 1
            r1 = i1
            r2 = i2
        elif p[i2] == "?" or p[i2] == s[i1]:
            i1 += 1
            i2 += 1
        elif r1 != -1:
            r1 += 1
            i1 = r1
            i2 = r2
        else:
            return False
        
    return all(i == "*" for i in p[i2:N2])
```