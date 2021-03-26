# LeetCode题解(0801)：使序列递增的最小交换次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时 |
| -------------- | ---------- | ---------- | -------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 112ms () |
| Ans 2 (Python) |            |            |          |
| Ans 3 (Python) |            |            |          |

解法一：

```python
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        size = len(A)
        dp = [0, 1]  # dp[0]=到i递增且i没有被交换,dp[1]=到i递增且i被交换
        for i in range(1, size):
            nxt = [float("inf"), float("inf")]
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                nxt[0] = min(nxt[0], dp[0])
                nxt[1] = min(nxt[1], dp[1] + 1)
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                nxt[0] = min(nxt[0], dp[1])
                nxt[1] = min(nxt[1], dp[0] + 1)
            dp = nxt
        return int(min(dp))
```

