# LeetCode题解(0463)：计算岛屿周长(Python)

题目：[原题链接](https://leetcode-cn.com/problems/island-perimeter/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 552ms (92.95%) |
| Ans 2 (Python) | O(n)       | O(1)       | 548ms (94.71%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（通过岛屿点计算）：

```python
def islandPerimeter(self, grid: List[List[int]]) -> int:
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                ans += 4
                if i != 0 and grid[i - 1][j] == 1:  # 如果上方也是岛屿的话
                    ans -= 2
                if j != 0 and grid[i][j - 1] == 1:  # 如果左方也是岛屿的话
                    ans -= 2
    return ans
```

解法二（横纵分别统计海岸线）：

```python
def islandPerimeter(self, grid: List[List[int]]) -> int:
    x = len(grid)
    y = len(grid[0])
    ans = 0

    # 统计纵向海岸线
    for i in range(x):
        if grid[i][0] == 1:
            ans += 1
        if grid[i][-1] == 1:
            ans += 1
        for j in range(y - 1):
            if grid[i][j] != grid[i][j + 1]:
                ans += 1

    # 统计横向海岸线
    for j in range(y):
        if grid[0][j] == 1:
            ans += 1
        if grid[-1][j] == 1:
            ans += 1
        for i in range(x - 1):
            if grid[i][j] != grid[i + 1][j]:
                ans += 1
    return ans
```