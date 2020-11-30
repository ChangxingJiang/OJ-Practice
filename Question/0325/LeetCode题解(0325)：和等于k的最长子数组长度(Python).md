# LeetCode题解(0325)：和等于k的最长子数组长度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k/)（中等）

标签：哈希表、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 72ms (47.37%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        last = 0
        ans = 0
        count = {}
        for i in range(len(nums)):
            if last not in count:
                count[last] = i
            last += nums[i]
            aim = last - k
            if aim in count:
                ans = max(ans, i - count[aim] + 1)
        return ans
```