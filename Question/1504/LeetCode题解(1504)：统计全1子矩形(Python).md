# LeetCode题解(1504)：统计二维数组中所有点全为1的子矩形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-submatrices-with-all-ones/)（中等）

标签：数组、数学、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N^4)$   | $O(1)$     | 660ms (22%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, columns = len(mat), len(mat[0])

        ans = 0

        # 每一个点计算以它做左上角顶点的情况
        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 1:
                    m = i
                    max_height, max_width = rows, columns
                    while m < max_height and mat[m][j] == 1:
                        n = j
                        while n < max_width and mat[m][n] == 1:
                            ans += 1
                            n += 1
                        else:
                            max_width = n
                        m += 1

        return ans
```