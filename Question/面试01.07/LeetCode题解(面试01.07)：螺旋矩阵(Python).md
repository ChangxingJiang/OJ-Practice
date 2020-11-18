# LeetCode题解(面试01.07)：顺时针旋转矩阵90度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rotate-matrix-lcci/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 36ms (90.78%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（翻转代替旋转）：

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        # 沿左上-右下对角线翻转
        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 水平翻转
        for i in range(N):
            for j in range(N // 2):
                matrix[i][j], matrix[i][N - j - 1] = matrix[i][N - j - 1], matrix[i][j]
```