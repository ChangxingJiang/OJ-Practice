# LeetCode题解(1260)：二维网格迁移(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shift-2d-grid/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $N(k*N^2)$ | $O(N^2)$   | 212ms (51.16%) |
| Ans 2 (Python) | $N(k*N^2)$ | $O(N^2)$   | 188ms (85.27%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    def helper():
        a = grid[-1][-1]
        for i in range(len(grid)):
            a, grid[i] = grid[i][-1], [a] + grid[i][:-1]

    for _ in range(k):
        helper()

    return grid
```

解法二（每次移动相当于将所有内容右移，如果到头就换行；故据此直接计算结果）：

```python
def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    x = len(grid)
    y = len(grid[0])
    size = x * y

    ans = []
    for i in range(x):
        line = []
        for j in range(y):
            p = (i * y + j - k) % size
            m = p // y
            n = p % y
            line.append(grid[m][n])
        ans.append(line)

    return ans
```

