# LeetCode题解(0209)：长度最小的子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)（中等）

标签：数组、滑动窗口、双指针、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (66.10%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans = len(nums) + 1

        now = 0
        i1 = 0
        for i2 in range(len(nums)):
            now += nums[i2]
            while now - nums[i1] >= s:
                now -= nums[i1]
                i1 += 1
            if now >= s:
                ans = min(ans, i2 - i1 + 1)

        return ans if ans <= len(nums) else 0
```

