# LeetCode题解(面试10.11)：峰与谷(Python)

题目：[原题链接](https://leetcode-cn.com/problems/peaks-and-valleys-lcci/)（中等）

标签：数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (73.43%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        size = len(nums)
        peak = True

        i = 0
        while i < size - 1:
            if peak:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                peak = False
            else:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                peak = True
            i += 1
```