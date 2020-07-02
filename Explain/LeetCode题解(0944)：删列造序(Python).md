# LeetCode题解(0944)：删列造序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-columns-to-make-sorted/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 156ms (69.72%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def minDeletionSize(self, A: List[str]) -> int:
    size = len(A)
    ans = 0
    for j in range(len(A[0])):
        for i in range(1, size):
            if A[i - 1][j] > A[i][j]:
                ans += 1
                break
    return ans
```