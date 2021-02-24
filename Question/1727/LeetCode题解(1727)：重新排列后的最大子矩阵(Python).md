# LeetCode题解(1727)：重新排列后的最大子矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-submatrix-with-rearrangements/)（中等）

标签：贪心算法、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(×N)$    | $O(M×N)$   | 348ms (60.38%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # 计算列中连续相邻的长度
        con = [[0] * n for _ in range(m)]
        for j in range(n):
            con[0][j] = matrix[0][j]
            for i in range(1, m):
                con[i][j] = con[i - 1][j] + 1 if matrix[i][j] else 0

        # 计算结果
        ans = 0
        for i in range(m):
            lst = sorted(con[i], reverse=True)
            for j in range(n):
                ans = max(ans, lst[j] * (j + 1))
        return ans
```

