# LeetCode题解(0280)：摆动排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/wiggle-sort/)（中等）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (87.22%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        bigger = True
        for i in range(len(nums) - 1):
            if bigger:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                bigger = False
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                bigger = True
```