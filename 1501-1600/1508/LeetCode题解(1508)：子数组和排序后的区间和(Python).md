# LeetCode题解(1508)：子数组和排序后的区间和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/range-sum-of-sorted-subarray-sums/)（中等）

标签：数组、排序

| 解法           | 时间复杂度     | 空间复杂度 | 执行用时    |
| -------------- | -------------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N^2logN^2)$ | $O(N^2)$   | 440ms (41%) |
| Ans 2 (Python) |                |            |             |
| Ans 3 (Python) |                |            |             |

解法一：

```python
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # 计算所有结果
        # O(N^2)
        lst = []
        for length in range(1, len(nums) + 1):
            first = sum(nums[:length])
            lst.append(first)
            for i in range(len(nums) - length):
                first = first - nums[i] + nums[i + length]
                lst.append(first)

        # 排序结果
        # O(N^2logN^2)
        lst.sort()

        return sum(lst[left - 1:right]) % (10 ** 9 + 7)
```