# LeetCode题解(0304)：二维区域和检索-矩阵不可变(Python)

题目：[原题链接](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/)（中等）

标签：数组、动态规划

| 解法           | 时间复杂度                      | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | 构造 = $O(N×M)$ ; 查询 = $O(1)$ | $O(N×M)$   | 68ms (94.43%) |
| Ans 2 (Python) |                                 |            |               |
| Ans 3 (Python) |                                 |            |               |

解法一：

```python
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.dp = None
        else:
            m, n = len(matrix), len(matrix[0])
            self.dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    self.dp[i][j] = matrix[i - 1][j - 1] + self.dp[i][j - 1] + self.dp[i - 1][j] - self.dp[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.dp is not None:
            return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]
        else:
            return 0
```

