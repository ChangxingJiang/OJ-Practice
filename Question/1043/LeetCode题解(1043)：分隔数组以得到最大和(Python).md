# LeetCode题解(1043)：分隔数组以得到最大和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/partition-array-for-maximum-sum/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×K^2)$ | $O(N)$     | 504ms (70.88%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        size = len(arr)

        dp = [0] * (size + 1)
        for i in range(size):
            max_val = arr[i]
            for j in range(min(i + 1, k)):
                max_val = max(max_val, arr[i - j])
                dp[i + 1] = max(dp[i + 1], dp[i - j] + (j + 1) * max_val)

        return dp[-1]
```

