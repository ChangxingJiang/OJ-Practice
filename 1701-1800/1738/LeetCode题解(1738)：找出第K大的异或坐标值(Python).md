# LeetCode题解(1738)：找出第K大的异或坐标值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value/)（中等）

标签：动态规划、位运算、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 1152ms (68.95%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = matrix[0][0]

        lst = [dp[0][0]]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] ^ matrix[i][0]
            lst.append(dp[i][0])
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] ^ matrix[0][j]
            lst.append(dp[0][j])

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] ^ dp[i][j - 1] ^ dp[i - 1][j - 1] ^ matrix[i][j]
                lst.append(dp[i][j])

        lst.sort(reverse=True)

        return lst[k - 1]
```

