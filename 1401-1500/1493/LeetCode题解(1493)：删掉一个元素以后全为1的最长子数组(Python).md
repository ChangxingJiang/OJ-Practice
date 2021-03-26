# LeetCode题解(1493)：删掉一个元素以后全为1的最长子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (98%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if set(nums) == {1}:
            return len(nums) - 1

        ans = 0

        last, now = 0, 0
        for n in nums:
            if n == 1:
                now += 1
            else:
                ans = max(ans, last + now)
                last = now
                now = 0

        ans = max(ans, last + now)

        return ans
```