# LeetCode题解(0074)：搜索二维矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/search-a-2d-matrix/)（中等）

标签：数组、二分查找

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时      |
| -------------- | ------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(log(N×M))$ | $O(1)$     | 40ms (60.68%) |
| Ans 2 (Python) |               |            |               |
| Ans 3 (Python) |               |            |               |

解法一：

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n
        while left < right:
            mid = (left + right) // 2
            i, j = divmod(mid, n)

            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid
            else:
                return True

        return False
```

