# LeetCode题解(1292)：元素和小于等于阈值的正方形的最大边长(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)（中等）

标签：数组、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 1092ms (57.48%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def maxSideLength(self, matrix: List[List[int]], threshold: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # 计算前缀和
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + matrix[i - 1][j - 1]

        # 计算范围内的和
        def count(x1, y1, x2, y2):
            return prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]

        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for c in range(ans + 1, min(m, n) + 1):
                    if i + c - 1 <= m and j + c - 1 <= n and count(i, j, i + c - 1, j + c - 1) <= threshold:
                        ans += 1
                    else:
                        break

        return ans
```

