# LeetCode题解(0487)：最大连续1的个数II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-consecutive-ones-ii/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 468ms (63.10%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 1
        last = -1
        now = 0
        for n in nums:
            if n == 1:
                now += 1
                ans = max(ans, last + now + 1)
            else:
                last = now
                now = 0
                ans = max(ans, last + 1)

        return ans
```