# LeetCode题解(0238)：除自身以外数组的乘积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/product-of-array-except-self/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (99.62%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]

        total = 1
        zero_num = 0
        for num in nums:
            if num == 0:
                zero_num += 1
            else:
                total *= num

        if zero_num >= 2:
            return [0] * len(nums)

        if zero_num == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = total
                else:
                    nums[i] = 0
            return nums

        else:
            for i in range(len(nums)):
                nums[i] = total // nums[i]
            return nums
```

