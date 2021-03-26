# LeetCode题解(0477)：汉明距离总和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/total-hamming-distance/)（中等）

标签：位运算、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 516ms (63.27%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count = [0] * 31  # 10**9 < 2*30
        size = len(nums)
        max_length = 0

        for num in nums:
            length = num.bit_length()
            max_length = max(max_length, length)
            for i in range(length):
                if num & (1 << i):
                    count[i] += 1

        return sum(n * (size - n) for n in count)
```

