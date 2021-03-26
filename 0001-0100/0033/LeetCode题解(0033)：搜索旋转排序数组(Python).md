# LeetCode题解(0033)：搜索旋转排序数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)（中等）

标签：数组、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 36ms (82.68%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        first, end = nums[0], nums[-1]

        # 处理没有被旋转的情况
        if first < end:
            idx = bisect.bisect_right(nums, target)
            return idx - 1 if idx > 0 and nums[idx - 1] == target else -1

        elif end < target < first:
            return -1

        elif target <= end:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= first:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return right if nums[right] == target else -1

        else:  # target >= first
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= end:
                    right = mid
                elif nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return right - 1 if nums[right - 1] == target else -1
```

