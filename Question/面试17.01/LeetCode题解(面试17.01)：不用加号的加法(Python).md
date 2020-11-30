# LeetCode题解(面试17.01)：不用加号的加法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/add-without-plus-lcci/)（简单）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (29.71%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def add(self, a: int, b: int) -> int:
        while b:
            a &= 0xFFFFFFFF
            b &= 0xFFFFFFFF
            a, b = a ^ b, (a & b) << 1  # 每位相加结果、进位值
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)
```

