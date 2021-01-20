# LeetCode题解(1283)：使结果不超过阈值的最小除数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-smallest-divisor-given-a-threshold/)（中等）

标签：二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogK)$ | $O(1)$     | 364ms (20.09%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2

            res = 0
            for num in nums:
                res += math.ceil(num / mid)

            if res > threshold:
                left = mid + 1
            else:
                right = mid

        return left
```

