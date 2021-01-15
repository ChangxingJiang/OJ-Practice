# LeetCode题解(0162)：寻找峰值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-peak-element/)（中等）

标签：二分查找、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 36ms (82.52%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 处理数组长度为1的情况
        if len(nums) == 1:
            return 0

        # 处理两侧边缘就是峰值的情况
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1

        # 二分查找
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
```

