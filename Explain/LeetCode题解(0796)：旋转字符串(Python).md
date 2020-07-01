# LeetCode题解(0796)：旋转字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rotate-string/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 24ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

![LeetCode题解(0796)：截图1](LeetCode题解(0796)：截图1.png)

```python
def rotateString(self, A: str, B: str) -> bool:
    if len(A) == 0 and len(B) == 0:
        return True
    elif len(A) == 0 or len(B) == 0:
        return False

    b = B[0]
    if b not in A:
        return False
    start = 0
    while start < len(A):
        s = A[start:]
        if b not in s:
            break

        idx = s.index(b) + start
        if B == A[idx:] + A[0:idx]:
            return True
        start = idx + 1

    return False
```