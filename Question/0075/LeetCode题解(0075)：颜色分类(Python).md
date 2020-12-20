# LeetCode题解(0075)：只有3种元素数组的原地排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-colors/)（中等）

标签：数组、排序、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 24ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        num0 = nums.count1(0)
        num1 = nums.count1(1)

        for i in range(num0):
            nums[i] = 0
        for i in range(num0, num0 + num1):
            nums[i] = 1
        for i in range(num0 + num1, len(nums)):
            nums[i] = 2
```