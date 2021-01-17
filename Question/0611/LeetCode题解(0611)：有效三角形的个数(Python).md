# LeetCode题解(0611)：有效三角形的个数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-triangle-number/)（中等）

标签：数组、二分查找

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时       |
| -------------- | ------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2logN)$ | $O(logN)$  | 712ms (24.14%) |
| Ans 2 (Python) |              |            |                |
| Ans 3 (Python) |              |            |                |

解法一：

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                idx = bisect.bisect_left(nums, nums[i] + nums[j], lo=j + 1)
                if idx == len(nums) or nums[idx] >= nums[i] + nums[j]:
                    idx -= 1
                ans += idx - j
        return ans
```

