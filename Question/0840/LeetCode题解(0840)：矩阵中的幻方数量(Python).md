# LeetCode题解(0840)：矩阵中的幻方数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/magic-squares-in-grid/)（简单）

| 解法           | 时间复杂度                    | 空间复杂度 | 执行用时      |
| -------------- | ----------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(W×H)$ : W和H为矩阵的宽和高 | $O(1)$     | 48ms (69.47%) |
| Ans 2 (Python) |                               |            |               |
| Ans 3 (Python) |                               |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    x = len(grid)
    y = len(grid[0])
    if x < 3 or y < 3:
        return 0

    ans = 0
    for i in range(x - 2):
        for j in range(x - 2):
            # 检查是否仅包含1-9
            num_list = {grid[i][j], grid[i][j + 1], grid[i][j + 2], grid[i + 1][j], grid[i + 1][j + 1],
                        grid[i + 1][j + 2], grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]}
            if not (1 in num_list and 2 in num_list and 3 in num_list and 4 in num_list and
                    5 in num_list and 6 in num_list and 7 in num_list and 8 in num_list and 9 in num_list):
                continue

            # 检查行列对角线加和是否正确（枚举8条线）
            num = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
            if grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] != num:
                continue
            if grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] != num:
                continue
            if grid[i][j] + grid[i][j + 1] + grid[i][j + 2] != num:
                continue
            if grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] != num:
                continue
            if grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2] != num:
                continue
            if grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] != num:
                continue
            if grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2] != num:
                continue

            ans += 1

    return ans
```

