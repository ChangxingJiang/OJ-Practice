# LeetCode题解(0361)：轰炸敌人(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bomb-enemy/)（中等）

标签：数组、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(1)$     | 396ms (73.33%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        s1, s2 = len(grid), len(grid[0])

        ans = 0

        for i1 in range(s1):
            for i2 in range(s2):
                if grid[i1][i2] == "0":
                    count = 0
                    for i3 in range(i1 - 1, -1, -1):
                        if grid[i3][i2] == "W":
                            break
                        if grid[i3][i2] == "E":
                            count += 1
                    for i3 in range(i1 + 1, s1, 1):
                        if grid[i3][i2] == "W":
                            break
                        if grid[i3][i2] == "E":
                            count += 1
                    for i4 in range(i2 - 1, -1, -1):
                        if grid[i1][i4] == "W":
                            break
                        if grid[i1][i4] == "E":
                            count += 1
                    for i4 in range(i2 + 1, s2, 1):
                        if grid[i1][i4] == "W":
                            break
                        if grid[i1][i4] == "E":
                            count += 1
                    ans = max(ans, count)

        return ans
```