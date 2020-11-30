# LeetCode题解(面试16.07)：最大数值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-lcci/)（简单）

标签：位运算、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 36ms (82.96%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maximum(self, a: int, b: int) -> int:
        c = a - b
        d = c >> 63
        c = (c ^ d) - d
        return int(((a + b) + c) / 2)
```