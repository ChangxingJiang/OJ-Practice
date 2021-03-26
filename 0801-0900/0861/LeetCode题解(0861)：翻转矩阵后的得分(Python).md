# LeetCode题解(0861)：翻转矩阵后的得分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/score-after-flipping-matrix/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(1)$     | 52ms (50.31%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        s1, s2 = len(A), len(A[0])

        def reverse_row(ii):
            for jj in range(s2):
                A[ii][jj] = 1 if A[ii][jj] == 0 else 0

        def reverse_col(jj):
            for ii in range(s1):
                A[ii][jj] = 1 if A[ii][jj] == 0 else 0

        def count_col(jj):
            return sum(A[ii][jj] for ii in range(s1))

        # 将所有行第一列的数值替换为相同的
        # 替换成0和1结果是一样的，不妨替换为1
        for i in range(s1):
            if A[i][0] == 0:
                reverse_row(i)

        # 分析每一列，将出现频数更多的值替换为1
        for j in range(s2):
            if count_col(j) <= s1 // 2:
                reverse_col(j)

        # 计算最终结果
        ans = 0
        for i in range(s1):
            ans += int("".join([str(A[i][j]) for j in range(s2)]), base=2)
        return ans
```