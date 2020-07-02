# LeetCode题解(0868)：二进制间距(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-gap/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (90.24%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (77.44%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（字符串遍历）：

```python
def binaryGap(self, N: int) -> int:
    N = bin(N)

    ans = 0
    start = -1
    for i in range(len(N)):
        if N[i] == "1":
            if start != -1:
                ans = max(ans, i - start)
            start = i
    return ans
```

解法二（移位）：

```python
def binaryGap(self, N: int) -> int:
    ans = 0
    now = -1
    while N > 0:
        if N & 1 == 1:
            if now != -1:
                ans = max(ans, now)
            now = 0
        if now != -1:
            now += 1
        N = N >> 1
    return ans
```