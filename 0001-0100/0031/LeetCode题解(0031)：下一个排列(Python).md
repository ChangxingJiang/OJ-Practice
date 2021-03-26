# LeetCode题解(0031)：下一个排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/next-permutation/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (89.30%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i1, i2 = -1, -1
        for i in range(len(nums) - 1):
            # 处理递增的情况
            if nums[i] < nums[i + 1]:
                i1, i2 = i, i + 1

            # 处理递减的情况
            elif i1 == -1 or nums[i + 1] > nums[i1]:
                i2 = i + 1

        # 处理完全单调递减的情况
        if i1 == -1:
            i1, i2 = 0, len(nums) - 1
            while i1 <= i2:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i1, i2 = i1 + 1, i2 - 1

        # 处理不完全单调递减的情况
        else:
            # 交换最后一个递增和递减中最小的值
            nums[i1], nums[i2] = nums[i2], nums[i1]

            # 交换递减中的值
            i1, i2 = i1 + 1, len(nums) - 1
            while i1 <= i2:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i1, i2 = i1 + 1, i2 - 1
```