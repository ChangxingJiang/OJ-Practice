# LeetCode题解(1438)：绝对差不超过限制的最长连续子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)（中等）

标签：数组、滑动窗口、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 300ms (88.63%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        size = len(nums)

        ans = 0

        left = 0
        stack1, stack2 = collections.deque(), collections.deque()  # 单调递增栈、单调递减栈
        for right, n in enumerate(nums):
            while stack1 and n < stack1[-1]:
                stack1.pop()
            stack1.append(n)

            while stack2 and n > stack2[-1]:
                stack2.pop()
            stack2.append(n)

            while stack2[0] - stack1[0] > limit:
                if stack2[0] == nums[left]:
                    stack2.popleft()
                if stack1[0] == nums[left]:
                    stack1.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

