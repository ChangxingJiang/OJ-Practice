# LeetCode题解(0073)：矩阵置零(Python)

题目：[原题链接](https://leetcode-cn.com/problems/set-matrix-zeroes/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(1)$     | 48ms (71.66%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        # 统计首行和首列是否存在0
        first_row, first_col = False, False
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break

        # 统计其他位置，并将结果记录在首行和首列
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # 依据首行和首列记录的情况，更新其他位置
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # 更新首行和首列
        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
```

