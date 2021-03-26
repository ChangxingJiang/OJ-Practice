# LeetCode题解(1563)：石子游戏V(Python)

题目：[原题链接](https://leetcode-cn.com/problems/stone-game-v/)（困难）

标签：动态规划、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时              |
| -------------- | ---------- | ---------- | --------------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N^2)$   | 超出时间限制(118/131) |
| Ans 2 (Python) | $O(N^3)$   | $O(N^2)$   | 9944ms (5.75%)        |
| Ans 3 (Python) |            |            |                       |

解法一：

```python
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        size = len(stoneValue)

        # 计算前缀和
        prefix = [0]
        last = 0
        for stone in stoneValue:
            last += stone
            prefix.append(last)

        # 初始化状态矩阵
        dp = [[0] * size for _ in range(size)]

        # 从短到长的状态转移
        for l in range(1, size):  # 遍历行的长度
            for i in range(0, size - l):  # 遍历行的第一个下标位置
                j = i + l  # 计算行的最后一个下标位置
                for k in range(i, i + l):  # 遍历行中每一个分割位置
                    left_val, right_val = prefix[k + 1] - prefix[i], prefix[j + 1] - prefix[k + 1]
                    if left_val < right_val:
                        dp[i][j] = max(dp[i][j], left_val + dp[i][k])
                    elif left_val > right_val:
                        dp[i][j] = max(dp[i][j], right_val + dp[k + 1][j])
                    else:
                        dp[i][j] = max(dp[i][j], left_val + max(dp[i][k], dp[k + 1][j]))

        # 返回最终结果
        return dp[0][-1]
```

解法二（记忆化递归）：

```python
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @lru_cache(None)
        def dfs(left: int, right: int) -> int:
            if left == right:
                return 0

            total = sum(stoneValue[left:right + 1])
            sum1 = ans = 0
            for i in range(left, right):
                sum1 += stoneValue[i]
                sum2 = total - sum1
                if sum1 < sum2:
                    ans = max(ans, dfs(left, i) + sum1)
                elif sum1 > sum2:
                    ans = max(ans, dfs(i + 1, right) + sum2)
                else:
                    ans = max(ans, max(dfs(left, i), dfs(i + 1, right)) + sum1)
            return ans

        n = len(stoneValue)
        return dfs(0, n - 1)
```

