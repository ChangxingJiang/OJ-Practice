# LeetCode题解(0059)：螺旋矩阵II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/spiral-matrix-ii/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 44ms (33.11%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]

        # 方向列表
        flags = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右->下->左->上

        x1, y1, flag = 0, 0, 0  # 当前坐标、方向
        for i in range(1, n * n + 1):
            ans[x1][y1] = i

            x2, y2 = x1 + flags[flag][0], y1 + flags[flag][1]
            # 如果前方可以移动
            if 0 <= x2 < n and 0 <= y2 < n and ans[x2][y2] == 0:
                x1, y1 = x2, y2

            # 如果前方不可以移动
            else:
                flag = (flag + 1) % 4
                x1, y1 = x1 + flags[flag][0], y1 + flags[flag][1]

        return ans
```

