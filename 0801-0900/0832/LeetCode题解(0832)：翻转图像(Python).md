# LeetCode题解(0832)：翻转图像(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flipping-an-image/)（简单）

| 解法           | 时间复杂度               | 空间复杂度 | 执行用时      |
| -------------- | ------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$ : N为图像的边长 | $O(1)$     | 56ms (96.07%) |
| Ans 2 (Python) |                          |            |               |
| Ans 3 (Python) |                          |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    size = len(A)
    for i in range(size):
        A[i] = [1 if A[i][j] == 0 else 0 for j in range(size - 1, -1, -1)]
    return A
```