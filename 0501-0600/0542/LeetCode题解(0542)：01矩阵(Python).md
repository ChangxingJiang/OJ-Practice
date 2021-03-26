# LeetCode题解(0542)：01矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/01-matrix/)（中等）

标签：广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N)$   | $O(M×N)$   | 756ms (49.79%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（广度优先搜索）：

```python
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)] if
                    is_valid(x2, y2)]

        m, n = len(matrix), len(matrix[0])

        ans = [[-1] * n for _ in range(m)]
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    ans[i][j] = 0

        while queue:
            for _ in range(len(queue)):
                i1, j1 = queue.popleft()
                for i2, j2 in get_neighbors(i1, j1):
                    if ans[i2][j2] == -1:
                        ans[i2][j2] = ans[i1][j1] + 1
                        queue.append((i2, j2))

        return ans
```

