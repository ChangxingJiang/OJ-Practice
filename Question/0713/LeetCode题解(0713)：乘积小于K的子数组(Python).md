# LeetCode题解(0713)：乘积小于K的子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subarray-product-less-than-k/)（中等）

标签：数组、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 1236ms (47.37%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        size = len(nums)
        ans = 0
        left = right = 0
        total = 1
        while right < size:
            total *= nums[right]
            right += 1
            while left < right and total >= k:
                total //= nums[left]
                left += 1
            ans += (right - left)
        return ans
```

