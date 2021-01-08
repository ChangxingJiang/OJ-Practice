# LeetCode题解(1595)：连通两组点的最小成本(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-cost-to-connect-two-groups-of-points/)（困难）

标签：动态规划、深度优先搜索、记忆化递归

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时       |
| -------------- | ------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M×2^N)$ | $O(2^N)$   | 424ms (76.71%) |
| Ans 2 (Python) |              |            |                |
| Ans 3 (Python) |              |            |                |

解法一：

```python
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        s1, s2 = len(cost), len(cost[0])

        # O(M×N)
        min_val = [min(cost[i][j] for i in range(s1)) for j in range(s2)]

        @lru_cache(None)
        def dfs(idx, used):
            # 当第一组已经全部连接完成的情况
            if idx == s1:
                ans = 0
                for j in range(s2):
                    if not used & (1 << j):  # 如果第二组还有尚未连接的点，则用最小成本连接它
                        ans += min_val[j]
                return ans

            # 当第一组还没完全连接完成的情况
            res = inf
            for j in range(s2):
                # 状态转移方程：在每次新增一个第一组的链接时，只考虑增加一个第二组，不考虑第一组同时与多个第二组链接
                res = min(res, cost[idx][j] + dfs(idx + 1, used | (1 << j)))
            return res

        return dfs(0, 0)
```

