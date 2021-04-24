# LeetCode题解(1814)：统计一个数组中好对子的数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-nice-pairs-in-an-array/)（中等）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 248ms (63.02%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    _MOD = 10 ** 9 + 7

    def countNicePairs(self, nums: List[int]) -> int:
        nums = [num - int(str(num)[::-1]) for num in nums]
        count = collections.Counter(nums)
        return sum(value * (value - 1) // 2 for value in count.values()) % self._MOD
```

