# LeetCode题解(面试17.19)：消失的两个数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/missing-two-lcci/)（困难）

标签：数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 60ms (85.67%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        size = len(nums) + 2
        expect = (1 + size) * size // 2
        total = sum(nums)

        disappear = expect - total

        mark = disappear // 2

        expect1 = (1 + mark) * mark // 2
        expect2 = expect - expect1
        total1, total2 = 0, 0

        for n in nums:
            if n <= mark:
                total1 += n
            else:
                total2 += n

        n1 = expect1 - total1
        n2 = expect2 - total2

        return [n1, n2]
```