# LeetCode题解(0935)：骑士拨号器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/knight-dialer/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 1164ms (34.67%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    _JUMP = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }
    _MOD = 10 ** 9 + 7

    def knightDialer(self, n: int) -> int:
        dp1 = [1] * 10
        for _ in range(n - 1):
            dp2 = [0] * 10
            for i in range(10):
                for j in self._JUMP[i]:
                    dp2[j] += dp1[i]
                    dp2[j] %= self._MOD
            dp1 = dp2
        return sum(dp1) % self._MOD
```

