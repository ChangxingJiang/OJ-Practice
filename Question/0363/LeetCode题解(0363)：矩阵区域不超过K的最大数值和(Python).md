# LeetCode题解(0363)：矩阵区域不大于K的最大矩形和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/)（困难）

标签：数组、查找、查找-二分查找、动态规划、双指针

| 解法           | 时间复杂度                                      | 空间复杂度               | 执行用时        |
| -------------- | ----------------------------------------------- | ------------------------ | --------------- |
| Ans 1 (Python) | $O(column^2×row)$ : 其中row为行数，column为列数 | $O(row)$ : 其中row为行数 | 1048ms (71.60%) |
| Ans 2 (Python) |                                                 |                          |                 |
| Ans 3 (Python) |                                                 |                          |                 |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
    ans = float('-inf')
    column = len(matrix[0])
    rows = len(matrix)

    for left in range(column):
        nums = [0] * rows
        for right in range(left, column):
            for i in range(rows):
                nums[i] += matrix[i][right]
            array = [0]
            now = 0
            for n in nums:
                now += n
                idx = bisect.bisect_left(array, now - k)
                if idx < len(array):
                    ans = max(ans, now - array[idx])
                bisect.insort(array, now)

    return ans
```

