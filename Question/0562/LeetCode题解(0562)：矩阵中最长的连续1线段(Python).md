# LeetCode题解(0562)：矩阵中最长的连续1线段(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-line-of-consecutive-one-in-matrix/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M)$   | $O(1)$     | 616ms (41.82%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0

        s1, s2 = len(M), len(M[0])

        ans = 0

        # 检查所有水平的
        for i1 in range(s1):
            now = 0
            for i2 in range(s2):
                if M[i1][i2] == 1:
                    now += 1
                    ans = max(ans, now)
                else:
                    now = 0

        # 检查所有垂直的
        for i2 in range(s2):
            now = 0
            for i1 in range(s1):
                if M[i1][i2] == 1:
                    now += 1
                    ans = max(ans, now)
                else:
                    now = 0

        # 检查所有对角线的
        for i1 in range(s1):
            i2 = 0
            now = 0
            for i3 in range(min(s1 - i1, s2 - i2)):
                if M[i1 + i3][i2 + i3] == 1:
                    now += 1
                    ans = max(ans, now)
                else:
                    now = 0
        for i2 in range(s2):
            i1 = 0
            now = 0
            for i3 in range(min(s1 - i1, s2 - i2)):
                if M[i1 + i3][i2 + i3] == 1:
                    now += 1
                    ans = max(ans, now)
                else:
                    now = 0

        # 检查所有反对角线的
        for i2 in range(s2):
            i1 = 0
            now = 0
            for i3 in range(min(s1 - i1, i2 + 1)):
                if M[i1 + i3][i2 - i3] == 1:
                    now += 1
                    ans = max(ans, now)
                else:
                    now = 0
        for i1 in range(s1):
            i2 = s2 - 1
            now = 0
            for i3 in range(min(s1 - i1, i2 + 1)):
                if M[i1 + i3][i2 - i3] == 1:
                    now += 1
                    ans = max(ans, now)
                else:
                    now = 0

        return ans
```