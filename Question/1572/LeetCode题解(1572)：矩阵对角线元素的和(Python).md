# LeetCode题解(1572)：矩阵对角线元素的和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/matrix-diagonal-sum/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (99%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        ans = 0
        for i in range(n):
            ans += mat[i][i] + mat[i][n - 1 - i] if i != n - 1 - i else mat[i][i]

        return ans
```