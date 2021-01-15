# LeetCode题解(0384)：打乱数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shuffle-an-array/)（中等）

标签：设计、随机

| 解法           | 时间复杂度        | 空间复杂度 | 执行用时       |
| -------------- | ----------------- | ---------- | -------------- |
| Ans 1 (Python) | 所有操作 = $O(N)$ | $O(N)$     | 224ms (72.27%) |
| Ans 2 (Python) |                   |            |                |
| Ans 3 (Python) |                   |            |                |

解法一：

```python
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = self.original
        self.original = list(self.original)
        return self.nums

    def shuffle(self) -> List[int]:
        for i1 in range(len(self.nums)):
            i2 = random.randrange(i1, len(self.nums))
            self.nums[i1], self.nums[i2] = self.nums[i2], self.nums[i1]
        return self.nums
```

