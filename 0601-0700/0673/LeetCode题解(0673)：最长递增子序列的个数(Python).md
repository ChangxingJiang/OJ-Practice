# LeetCode题解(0673)：最长递增子序列的个数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 1112ms (49.05%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size

        length = [0] * size
        count = [1] * size

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if length[i] >= length[j]:
                        length[j] = length[i] + 1
                        count[j] = count[i]
                    elif length[i] + 1 == length[j]:
                        count[j] += count[i]

        longest = max(length)
        return sum(n for i, n in enumerate(count) if length[i] == longest)
```

