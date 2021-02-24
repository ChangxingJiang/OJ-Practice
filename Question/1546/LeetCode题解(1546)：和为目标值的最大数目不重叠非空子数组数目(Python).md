# LeetCode题解(1546)：和为目标值的最大数目不重叠非空子数组数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)（中等）

标签：动态规划、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 148ms (71.76%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ans = 0

        count = {0: -1}
        now = -1
        last = 0
        for i, num in enumerate(nums):
            last += num
            if last - target in count and count[last - target] >= now:
                now = i
                ans += 1
            count[last] = i

        return ans
```

