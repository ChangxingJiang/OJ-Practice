# LeetCode题解(面试05.01)：在二进制数中插入数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/insert-into-bits-lcci/)（简单）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 36ms (84.24%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        p1 = N >> (j + 1) << (j + 1)  # j位之后
        p2 = M << i  # i位到j位之间
        p3 = N & (2 ** i - 1)  # i位之前
        return p1 + p2 + p3
```