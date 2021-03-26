# LeetCode题解(1582)：计算二进制矩阵中的特殊位置(Python)

题目：[原题链接](https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix/)（简单）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N+M)$   | 60ms (61%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        maybe_line = set()
        for i in range(len(mat)):
            num = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    num += 1
            if num == 1:
                maybe_line.add(i)

        maybe_column = set()
        for j in range(len(mat[0])):
            num = 0
            for i in range(len(mat)):
                if mat[i][j] == 1:
                    num += 1
            if num == 1:
                maybe_column.add(j)

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 1 and i in maybe_line and j in maybe_column:
                    ans += 1

        return ans
```