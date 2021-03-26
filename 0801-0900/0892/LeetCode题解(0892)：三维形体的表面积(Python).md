# LeetCode题解(0892)：三维形体的表面积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/surface-area-of-3d-shapes/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(1)$     | 116ms (68.17%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def surfaceArea(self, grid: List[List[int]]) -> int:
    size = len(grid)
    ans = 0
    for i in range(size):
        for j in range(size):
            if grid[i][j]:
                ans += 2

            if i == 0:
                ans += grid[i][j]
            elif grid[i][j] > grid[i - 1][j]:
                ans += grid[i][j] - grid[i - 1][j]

            if i == size - 1:
                ans += grid[i][j]
            elif grid[i][j] > grid[i + 1][j]:
                ans += grid[i][j] - grid[i + 1][j]

            if j == 0:
                ans += grid[i][j]
            elif grid[i][j] > grid[i][j - 1]:
                ans += grid[i][j] - grid[i][j - 1]

            if j == size - 1:
                ans += grid[i][j]
            elif grid[i][j] > grid[i][j + 1]:
                ans += grid[i][j] - grid[i][j + 1]

    return ans
```