# LeetCode题解(0006)：Z字形变换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zigzag-conversion/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 60ms (92.45%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 60ms (92.45%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def convert(self, s: str, numRows: int) -> str:
    # 处理特殊情况
    if numRows == 1:
        return s

    N = len(s)
    L = numRows * 2 - 2
    ans = [[] for _ in range(numRows)]
    for i in range(N):
        now = i % L
        if now > L / 2:
            now = L - now
        ans[now].append(s[i])
    return "".join(["".join(p) for p in ans])
```

解法二（优化计算量）：

```python
def convert(self, s: str, numRows: int) -> str:
    # 处理特殊情况
    if numRows == 1:
        return s

    L = numRows - 1
    now = 0
    orient = 1
    ans = ["" for _ in range(numRows)]
    for ch in s:
        ans[now] += ch
        now += orient
        if now == 0:
            orient = 1
        elif now == L:
            orient = -1
    return "".join(ans)
```

