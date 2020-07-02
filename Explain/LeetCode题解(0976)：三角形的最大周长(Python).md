# LeetCode题解(0976)：三角形的最大周长(Python)

题目：[原题链接](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 228ms (97.47%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（排序法）：

```python
def largestPerimeter(self, A: List[int]) -> int:
    A.sort(reverse=True)
    for i in range(len(A) - 2):
        if A[i] < A[i + 1] + A[i + 2]:
            return A[i] + A[i + 1] + A[i + 2]
    else:
        return 0
```

