# LeetCode题解(1063)：有效子数组的数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-valid-subarrays/)（困难）

标签：栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 532ms (100.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            stack.append(n)
            ans += len(stack)
        return ans
```