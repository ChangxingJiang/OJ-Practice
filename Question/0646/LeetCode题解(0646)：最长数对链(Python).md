# LeetCode题解(0646)：最长数对链(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-length-of-pair-chain/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 2476ms (29.87%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        size = len(pairs)
        dp = [0] * size
        for i in range(len(pairs)):
            dp[i] = 1
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```

