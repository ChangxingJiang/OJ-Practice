# LeetCode题解(面试10.09)：排序矩阵查找(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sorted-matrix-search-lcci/)（中等）

标签：二分查找、双指针、分治算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (46.34%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 44ms (83.92%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        s1, s2 = len(matrix), len(matrix[0])

        i1, i2 = 0, bisect.bisect_left(matrix[0], target)
        last_change = 2

        while 0 <= i1 <= s1 and 0 <= i2 <= s2:
            # print(i1, i2, last_change)
            if last_change == 1 and i1 < s1 and matrix[i1][i2] == target:
                return True
            if last_change == 2 and i2 < s2 and matrix[i1][i2] == target:
                return True

            if last_change == 2:
                i2 -= 1
                i1 += bisect.bisect_left([row[i2] for row in matrix[i1:]], target) # O(N)
                last_change = 1
            else:  # last_change == 1
                if i1 < s1:
                    i2 = bisect.bisect_left(matrix[i1], target)
                    last_change = 2
                else:
                    return False

        return False
```

解法二（优化解法一）：

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        s1, s2 = len(matrix), len(matrix[0])
        i1, i2 = 0, s2

        while 0 <= i1 <= s1 and 0 <= i2 <= s2:
            # 纵向查找
            i2 -= 1
            l, r = i1, s1
            while l < r:
                m = (l + r) // 2
                if matrix[m][i2] < target:
                    l = m + 1
                elif matrix[m][i2] > target:
                    r = m
                else:
                    return True

            # 横向查找
            i1 = l
            if i1 < s1:
                l, r = i2, s2
                while l < r:
                    m = (l + r) // 2
                    if matrix[i1][m] < target:
                        l = m + 1
                    elif matrix[i1][m] > target:
                        r = m
                    else:
                        return True

                i2 = l
            else:
                return False

        return False
```