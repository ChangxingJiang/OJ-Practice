# LeetCode题解(0311)：稀疏矩阵的乘法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sparse-matrix-multiplication/)（中等）

标签：数学、数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N^2)$   | 160ms (23.87%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（标准矩阵乘法）：

```python
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        size1, size2 = len(A), len(B[0])  # A的行数 和 B的列数
        size3 = len(A[0])  # A的列数和B的行数相等
        ans = [[0] * size2 for _ in range(size1)]
        for i1 in range(size1):
            for i2 in range(size2):
                for i3 in range(size3):
                    ans[i1][i2] += A[i1][i3] * B[i3][i2]
        return ans
```