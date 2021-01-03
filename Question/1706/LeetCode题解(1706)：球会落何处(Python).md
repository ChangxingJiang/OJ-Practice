# LeetCode题解(1706)：球会落何处(Python)

题目：[原题链接](https://leetcode-cn.com/problems/where-will-the-ball-fall/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 68ms (53.35%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        dp = [i for i in range(n)]

        for i in range(m):

            # print(i, ":", dp)

            for j in range(n):
                # 如果这个球已经卡住则跳过
                if dp[j] == -1:
                    continue

                # 处理右侧板的情况
                if grid[i][dp[j]] == 1:
                    if dp[j] == n - 1 or grid[i][dp[j] + 1] == -1:
                        dp[j] = -1
                    else:
                        dp[j] += 1

                # 处理左侧板的情况
                else:
                    if dp[j] == 0 or grid[i][dp[j] - 1] == 1:
                        dp[j] = -1
                    else:
                        dp[j] -= 1

        return dp
```

