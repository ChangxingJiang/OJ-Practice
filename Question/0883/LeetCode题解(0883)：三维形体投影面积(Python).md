# LeetCode题解(0883)：三维形体投影面积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/projection-area-of-3d-shapes/)（简单）

| 解法           | 时间复杂度             | 空间复杂度           | 执行用时       |
| -------------- | ---------------------- | -------------------- | -------------- |
| Ans 1 (Python) | $O(N^2)$ : N为矩阵宽度 | $O(N)$ : N为矩阵宽度 | 104ms (33.86%) |
| Ans 2 (Python) | $O(N^2)$ : N为矩阵宽度 | $O(1)$               | 80ms (99.06%)  |
| Ans 3 (Python) |                        |                      |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（记录所有投影结果）：

```python
def projectionArea(self, grid: List[List[int]]) -> int:
    size = len(grid)

    max_x = [0 for _ in range(size)]
    max_y = [0 for _ in range(size)]
    ans = 0
    for i in range(size):
        for j in range(size):
            if grid[i][j] > 0:
                ans += 1
                max_x[i] = max(max_x[i], grid[i][j])
                max_y[j] = max(max_y[j], grid[i][j])
    return ans + sum(max_x) + sum(max_y)
```

解法二（不记录投影结果）：

```python
def projectionArea(self, grid):
    size = len(grid)
    ans = 0
    for i in range(size):
        max_x = 0
        max_y = 0
        for j in range(size):
            if grid[i][j]:
                ans += 1
            max_x = max(max_x, grid[i][j])
            max_y = max(max_y, grid[j][i])
        ans += max_x + max_y
    return ans
```