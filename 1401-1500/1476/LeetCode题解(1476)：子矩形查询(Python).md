# LeetCode题解(1476)：子矩形查询(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subrectangle-queries/)（中等）

标签：设计、数组

| 解法           | 时间复杂度                      | 空间复杂度 | 执行用时    |
| -------------- | ------------------------------- | ---------- | ----------- |
| Ans 1 (Python) | 更新 : $O(N^2)$ ; 查询 : $O(1)$ | $O(N^2)$   | 120ms (68%) |
| Ans 2 (Python) |                                 |            |             |
| Ans 3 (Python) |                                 |            |             |

解法一：

```python
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
```