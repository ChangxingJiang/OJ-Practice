# LeetCode题解(面试17.04)：消失的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/missing-number-lcci/)（简单）

标签：位运算、数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (57.49%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expect = 0
        actual = 0
        for i in range(len(nums)):
            expect ^= i
            actual ^= nums[i]
        expect ^= len(nums)

        return expect ^ actual
```