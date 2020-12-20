# LeetCode题解(0464)：我能赢吗(Python)

题目：[原题链接](https://leetcode-cn.com/problems/can-i-win/)（中等）

标签：极小化极大、递归、记忆化递归、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N!)$    | $O(N!)$    | 508ms (58.70%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        if sum(range(maxChoosableInteger + 1)) < desiredTotal:
            return False

        @functools.lru_cache(None)
        def dfs(used, need):
            for i in range(maxChoosableInteger):
                cur = 1 << i
                if cur & used == 0:
                    if need <= i + 1 or not dfs(cur | used, need - i - 1):
                        return True
            return False

        return dfs(0, desiredTotal)
```