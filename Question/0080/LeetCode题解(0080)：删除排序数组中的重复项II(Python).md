# LeetCode题解(0080)：删除排序数组中的重复项II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (90.85%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    _SMALL = -10001

    def removeDuplicates(self, nums: List[int]) -> int:
        i1 = 0
        now_val, now_num = self._SMALL, 0
        for i2 in range(len(nums)):
            if nums[i2] != now_val:
                nums[i1] = nums[i2]
                now_val, now_num = nums[i2], 1
                i1 += 1
            elif now_num < 2:
                nums[i1] = nums[i2]
                now_num += 1
                i1 += 1
            else:
                now_num += 1
        nums[i1:] = []
        return len(nums)
```

