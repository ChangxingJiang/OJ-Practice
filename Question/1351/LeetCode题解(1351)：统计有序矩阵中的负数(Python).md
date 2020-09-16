# LeetCode题解(1351)：统计有序矩阵中的负数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (97.97%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def countNegatives(self, grid: List[List[int]]) -> int:
    x = len(grid)
    y = len(grid[0])
    if grid[-1][-1] >= 0:
        return 0
    ans = 0
    num = x
    for j in range(1, y + 1):
        for i in range(num, 0, -1):
            if grid[-i][-j] < 0:
                ans += i
                num = i
                break
        else:
            break
    return ans
```