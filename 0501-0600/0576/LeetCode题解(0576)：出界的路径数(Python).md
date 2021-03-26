# LeetCode题解(0576)：出界的路径数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/out-of-boundary-paths/)（中等）

标签：动态规划、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(M×N×T)$ | $O(M×N×T)$ | 816ms (5.07%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findPaths(self, m: int, n: int, t: int, ii: int, jj: int) -> int:
        def _is_valid(x, y):
            return 1 <= x <= m and 1 <= y <= n

        def _get_neighbors(x1, y1):
            return [(x2, y2) for (x2, y2) in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]
                    if _is_valid(x2, y2)]

        # 初始化状态矩阵
        dp = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(t + 1)]
        dp[0][ii + 1][jj + 1] = 1

        # 状态转移
        ans = 0
        for k in range(1, t + 1):
            for i1 in range(m + 2):
                for j1 in range(n + 2):
                    for (i2, j2) in _get_neighbors(i1, j1):
                        dp[k][i1][j1] += dp[k - 1][i2][j2]
                    if i1 == 0 or i1 == m + 1 or j1 == 0 or j1 == n + 1:
                        ans += dp[k][i1][j1]
            # print("第{}步".format(k))
            # for row in dp[k]:
            #     print(row)

        return ans % (10 ** 9 + 7)
```

