# LeetCode题解(面试17.16)：按摩师(Python)

题目：[原题链接](https://leetcode-cn.com/problems/the-masseuse-lcci/)（简单）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (62.36%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def massage(self, nums: List[int]) -> int:
        a, b = [0, 0]
        for n in nums:
            a, b = b, max(a + n, b)
        return b
```