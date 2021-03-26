# LeetCode题解(面试01.08)：将矩阵中有零的行和列清空(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zero-matrix-lcci/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 56ms (42.48%) |
| Ans 2 (Python) | $O(N^2)$   | $O(1)$     | 52ms (63.23%) |
| Ans 3 (Python) |            |            |               |

解法一（两次遍历）：

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        N1, N2 = len(matrix), len(matrix[0])

        remove_x = set()
        remove_y = set()

        for i in range(N1):
            for j in range(N2):
                if matrix[i][j] == 0:
                    remove_x.add(i)
                    remove_y.add(j)

        for i in remove_x:
            for j in range(N2):
                matrix[i][j] = 0

        for j in remove_y:
            for i in range(N1):
                matrix[i][j] = 0
```

解法二（不占用额外空间）：

```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        N1, N2 = len(matrix), len(matrix[0])

        # 检查首行的首列是否需要清空
        first_row, first_column = False, False
        if 0 in matrix[0]:
            first_row = True
        for i in range(N1):
            if matrix[i][0] == 0:
                first_column = True
                break

        # 检查中间部分是否需要清空并标记
        for i in range(N1):
            for j in range(N2):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 清空中间部分需要清空的内容
        for i in range(1, N1):
            if matrix[i][0] == 0:
                for j in range(1, N2):
                    matrix[i][j] = 0

        for j in range(1, N2):
            if matrix[0][j] == 0:
                for i in range(N1):
                    matrix[i][j] = 0

        # 清处理首行和首列
        if first_row:
            for j in range(1, N2):
                matrix[0][j] = 0

        if first_column:
            for i in range(N1):
                matrix[i][0] = 0
```