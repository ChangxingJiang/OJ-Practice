# LeetCode题解(1588)：所有奇数长度子数组的和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N^3)$   | $O(N)$     | 56ms (83%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for length in range(1, min(101, len(arr) + 1), 2):
            for i in range(len(arr) - length + 1):
                ans += sum(arr[i:i + length])
        return ans
```