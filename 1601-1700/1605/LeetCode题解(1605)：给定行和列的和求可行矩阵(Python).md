# LeetCode题解(1605)：给定行和列的和求可行矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-valid-matrix-given-row-and-column-sums/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 460ms (63%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        x, y = len(rowSum), len(colSum)

        ans = [[0] * y for _ in range(x)]

        for i in range(x):
            for j in range(y):
                now = min(rowSum[i], colSum[j])
                ans[i][j] = now
                rowSum[i] -= now
                colSum[j] -= now

        return ans
```