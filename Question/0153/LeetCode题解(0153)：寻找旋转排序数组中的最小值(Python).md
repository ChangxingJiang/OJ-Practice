# LeetCode题解(0153)：寻找旋转递增排序数组的最小数字(不存在重复值)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)（中等）

标签：数组、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 40ms (72.40%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（二分查找）：

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]
```