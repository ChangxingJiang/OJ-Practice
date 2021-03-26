# LeetCode题解(0034)：在排序数组中查找元素的第一个和最后一个位置(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)（中等）

标签：数组、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 44ms (57.43%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return [left, right - 1] if left != right else [-1, -1]
```

