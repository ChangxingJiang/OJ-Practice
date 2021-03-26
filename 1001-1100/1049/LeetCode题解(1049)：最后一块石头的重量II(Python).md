# LeetCode题解(1049)：最后一块石头的重量II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/last-stone-weight-ii/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 56ms (64.52%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [True] + [False] * target
        stones.sort()
        for stone in stones:
            for i in range(target, -1, -1):
                if dp[i] is True and i + stone <= target:
                    # print(i, "+", stone, "=", i + stone)
                    dp[i + stone] = True

        # print(total, len(dp), dp)

        while dp and dp[-1] is False:
            dp.pop()

        return int(2 * (total / 2 - (len(dp) - 1)))
```

