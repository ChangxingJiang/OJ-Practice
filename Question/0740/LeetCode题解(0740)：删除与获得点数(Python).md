# LeetCode题解(0740)：删除与获得点数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-and-earn/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (97.08%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lst = [0] * (max(nums) + 1)
        for num in nums:
            lst[num] += num

        if len(lst) <= 3:
            return max(lst)

        dp = [0] * len(lst)
        dp[1], dp[2] = lst[1], lst[2]
        for i in range(2, len(lst)):
            dp[i] = max(dp[i - 1], dp[i - 2] + lst[i])
        return dp[-1]
```

