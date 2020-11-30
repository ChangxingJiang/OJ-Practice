# LeetCode题解(面试17.24)：最大子矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-submatrix-lcci/)（困难）

标签：数组、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N×M^2)$ | $O(N×M)$   | 3288ms (29.62%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一（动态规划）：

```python
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        s1, s2 = len(matrix), len(matrix[0])

        # 计算前缀和矩阵
        # O(N×M)
        T1 = [[0] * (s2 + 1) for _ in range(s1)]  # 左上缀和

        T1[0][1] = matrix[0][0]

        for i1 in range(1, s1):
            T1[i1][1] = T1[i1 - 1][1] + matrix[i1][0]

        for i2 in range(1, s2):
            T1[0][i2 + 1] = T1[0][i2] + matrix[0][i2]

        for i1 in range(1, s1):
            for i2 in range(1, s2):
                T1[i1][i2 + 1] = matrix[i1][i2] + T1[i1 - 1][i2 + 1] + T1[i1][i2] - T1[i1 - 1][i2]

        ans_idx, ans_val = [-1, -1, -1, -1], float("-inf")

        # 计算前缀差矩阵
        # O(N×M^2)
        T2 = [[(0, -1)] * (s2 + 1) for _ in range(s2 + 1)]  # 左上缀差
        for i1 in range(s1):
            for i2 in range(s2):
                for i3 in range(i2, s2):
                    v1 = T1[i1][i3 + 1] - T1[i1][i2]
                    v2 = v1 - T2[i2][i3][0]

                    # print(i1, i2, i3, "->", v2, ":", (T2[i2][i3][1] + 1, i2), ",", (i1, i3), "(", T2[i2][i3], ")")

                    if v2 > ans_val:
                        ans_idx, ans_val = [T2[i2][i3][1] + 1, i2, i1, i3], v2
                        # print("[Maybe]", ans_idx, ans_val)

                    if v1 < T2[i2][i3][0]:
                        T2[i2][i3] = (v1, i1)

                    # T2[i2][i3] = min(T2[i2][i3], v)

        return ans_idx
```