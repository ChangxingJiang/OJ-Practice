# LeetCode题解(面试17.23)：最大黑方阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-black-square-lcci/)（中等）

标签：动态规划、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 172ms (96.43%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（动态规划）：

```python
class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)

        dp = [[(0, 0)] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 0:
                    x0 = dp[i][j + 1][0] + 1 if j < n - 1 else 1
                    x1 = dp[i + 1][j][1] + 1 if i < n - 1 else 1
                    dp[i][j] = (x0, x1)

        # for row in dp:
        #     print(row)

        ans_idx, ans_val = (0, 0), 0

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    size = min(dp[i][j])
                    if size > ans_val:
                        for k in range(1, size):
                            if min(dp[i + k][j + k]) < size - k:
                                break
                        else:
                            ans_idx, ans_val = (i, j), size

        return [ans_idx[0], ans_idx[1], ans_val] if ans_val > 0 else []
```