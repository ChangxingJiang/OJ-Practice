# LeetCode题解(0137)：只出现一次的数字II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/single-number-ii/)（中等）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (48.41%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = (~seen_twice) & (seen_once ^ num)
            seen_twice = (~seen_once) & (seen_twice ^ num)
        return seen_once
```

