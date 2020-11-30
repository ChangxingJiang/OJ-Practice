# LeetCode题解(面试16.17)：连续数列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/contiguous-sequence-lcci/)（简单）

标签：数组、分治算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (48.16%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        min_val = 0
        last = 0
        for n in nums:
            min_val = min(last, min_val)
            last += n
            ans = max(ans, last - min_val)
        return ans
```