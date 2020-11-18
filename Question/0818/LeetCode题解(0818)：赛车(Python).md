# LeetCode题解(0818)：赛车(Python)

题目：[原题链接](https://leetcode-cn.com/problems/race-car/)（困难）

标签：动态规划、数学、递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 300ms (65.79%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def racecar(self, target: int) -> int:
        dp = [float("inf")] * (target + 1)
        dp[0] = 0
        for t in range(1, target + 1):
            k1 = t.bit_length()

            # 处理不用重置直接到达的情况
            if t == 2 ** k1 - 1:
                dp[t] = k1
                continue

            # 考虑重置前最后一步走出后的最优解
            # 换句话说就是在之前的移动中考虑是否需要穿插一个反向的步子
            # 加的2为两次转身的步数
            for k2 in range(k1 - 1):
                dp[t] = min(dp[t], dp[t - 2 ** (k1 - 1) + 2 ** k2] + (k1 - 1) + k2 + 2)

            # 考虑从后面走回来的情况
            # (2**k1-1)为下一次移动到的位置
            # 加的1位一次转身的步数
            dp[t] = min(dp[t], dp[(2 ** k1 - 1) - t] + k1 + 1)

        # print(dp)

        return int(dp[-1])
```