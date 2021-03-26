# LeetCode题解(1608)：计算特殊数组的特征值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x/)（简单）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (64%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        lst = [0] * 101
        for n in nums:
            for i in range(min(n + 1, 101)):
                lst[i] += 1
        for i, n in enumerate(lst):
            if i == n:
                return i
        return -1
```