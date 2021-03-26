# LeetCode题解(0390)：消除游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/elimination-game/)（中等）

标签：递归、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 56ms (38.57%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def lastRemaining(self, n: int, reverse=False) -> int:
        if n == 1:
            return 1
        if not reverse:
            return self.lastRemaining(n // 2, not reverse) * 2
        else:
            if n % 2 == 0:
                return self.lastRemaining(n // 2, not reverse) * 2 - 1
            else:
                return self.lastRemaining(n // 2, not reverse) * 2
```

