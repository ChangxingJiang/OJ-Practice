# LeetCode题解(Offer53II)：找出排序数组中缺失的整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof/)（简单）

标签：数组、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 44ms (78.76%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（二分查找）：

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid
        return nums[left] - 1 if left < len(nums) else len(nums)
```