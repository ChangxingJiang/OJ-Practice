# LeetCode题解(1155)：掷骰子的N种方法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(D×F×T)$ | $O(T)$     | 396ms (52.10%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp1 = [1] + [0] * target

        for _ in range(d):
            dp2 = [0] * (target + 1)
            for i in range(target + 1):
                if dp1[i] > 0:
                    for j in range(i + 1, min(i + f + 1, target + 1)):
                        dp2[j] += dp1[i]
                        dp2[j] %= self._MOD
            dp1 = dp2

        return dp1[target]
```

