# LeetCode题解(1072)：按列翻转得到最大值等行数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flip-columns-for-maximum-number-of-equal-rows/)（中等）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 136ms (81.67%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        size1, size2 = len(matrix), len(matrix[0])

        count = collections.Counter()

        for i1 in range(size1):
            if matrix[i1][0] == 1:
                count[tuple(matrix[i1])] += 1
            else:
                count[tuple(1 if x == 0 else 0 for x in matrix[i1])] += 1

        return count.most_common(1)[0][1]
```