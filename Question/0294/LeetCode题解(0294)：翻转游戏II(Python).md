# LeetCode题解(0294)：翻转游戏II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flip-game-ii/)（中等）

标签：极小化极大、回溯算法、递归、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×2^N)$ | $O(N×2^N)$ | 68ms (82.02%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def canWin(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i] == "+" and s[i + 1] == "+":
                if not self.canWin(s[:i] + "--" + s[i + 2:]):
                    return True
        return False
```