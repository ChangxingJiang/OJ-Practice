# LeetCode题解(0498)：对角线遍历(Python)

题目：[原题链接](https://leetcode-cn.com/problems/diagonal-traverse/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(1)$     | 208ms (76.56%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        i, j, d1, d2 = 0, 0, -1, 1

        ans = []

        while len(ans) < m * n:
            ans.append(matrix[i][j])
            if 0 <= i + d1 < m and 0 <= j + d2 < n:
                i, j = i + d1, j + d2
            else:
                if j + d2 >= n:
                    i += 1
                elif i + d1 < 0:
                    j += 1
                elif i + d1 >= m:
                    j += 1
                elif j + d2 < 0:
                    i += 1
                d1, d2 = d2, d1

        return ans
```

