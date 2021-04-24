# LeetCode题解(1749)：任意子数组和的绝对值的最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-absolute-sum-of-any-subarray/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 120ms (78.99%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = 0
        min_val = 0
        max_val = 0
        now = 0
        for num in nums:
            now += num
            ans = max(ans, now - min_val, max_val - now)
            if now < min_val:
                min_val = now
            if now > max_val:
                max_val = now

        return ans
```

