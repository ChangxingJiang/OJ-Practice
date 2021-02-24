# LeetCode题解(1329)：将矩阵按对角线排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-the-matrix-diagonally/)（中等）

标签：数组、排序

| 解法           | 时间复杂度             | 空间复杂度    | 执行用时      |
| -------------- | ---------------------- | ------------- | ------------- |
| Ans 1 (Python) | $O(M×N×log(min(M,N)))$ | $O(min(M,N))$ | 44ms (97.99%) |
| Ans 2 (Python) |                        |               |               |
| Ans 3 (Python) |                        |               |               |

解法一：

```python
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for d in range(-m + 1, n):
            if d < 0:
                i0, j0, num = -d, 0, min(m + d, n)
            else:
                i0, j0, num = 0, d, min(n - d, m)

            lst = []
            for k in range(num):
                i1, j1 = i0 + k, j0 + k
                lst.append(mat[i1][j1])
            lst.sort()
            for k in range(num):
                i1, j1 = i0 + k, j0 + k
                mat[i1][j1] = lst[k]

        return mat
```

