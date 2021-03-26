# LeetCode题解(Offer04)：在顺序二维数组中查找(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)（简单）

标签：数组、二分查找、双指针

| 解法           | 时间复杂度  | 空间复杂度 | 执行用时      |
| -------------- | ----------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×logM)$ | $O(1)$     | 52ms (48.16%) |
| Ans 2 (Python) | $O(N+M)$    | $O(1)$     | 52ms (48.16%) |
| Ans 3 (Python) | $O(N+M)$    | $O(1)$     | 40ms (94.46%) |

解法一（逐行二分查找）：

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 处理特殊情况
        n = len(matrix)
        if n == 0:
            return False

        m = len(matrix[0])
        if m == 0:
            return False

        idx1 = 0  # 当前行号
        idx2 = m  # 当前行比目标值大的位置
        while idx1 < n and idx2:
            idx2 = bisect.bisect_right(matrix[idx1], target, hi=idx2)
            if matrix[idx1][idx2 - 1] == target:
                return True
            idx1 += 1

        return False
```

解法二（逐行移动指针）：

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 处理特殊情况
        n = len(matrix)
        if n == 0:
            return False

        m = len(matrix[0])
        if m == 0:
            return False

        # 计算第一行中的坐标
        idx1 = 0
        idx2 = bisect.bisect_right(matrix[idx1], target)
        while idx1 < n and idx2:
            idx2 -= 1
            while idx1 < n and matrix[idx1][idx2] < target:
                idx1 += 1
            if idx1 < n and matrix[idx1][idx2] == target:
                return True
        return False
```

解法三：

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 处理特殊情况
        n = len(matrix)
        if n == 0:
            return False

        m = len(matrix[0])
        if m == 0:
            return False

        # 计算第一行中的坐标
        idx1 = 0
        idx2 = m - 1
        while idx1 < n and idx2 >= 0:
            if matrix[idx1][idx2] > target:
                idx2 -= 1
            elif matrix[idx1][idx2] < target:
                idx1 += 1
            else:
                return True
        return False
```