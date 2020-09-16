# LeetCode题解(0154)：寻找旋转递增排序数组的最小数字(存在重复值)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)（困难）

标签：数组、二分查找

| 解法           | 时间复杂度                                           | 空间复杂度 | 执行用时      |
| -------------- | ---------------------------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | 平均时间复杂度 = $O(logN)$ ; 最坏时间复杂度 = $O(N)$ | $O(1)$     | 36ms (92.56%) |
| Ans 2 (Python) |                                                      |            |               |
| Ans 3 (Python) |                                                      |            |               |

解法一：

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
            else:
                right -= 1
        return nums[left]
```