# LeetCode题解(面试05.07)：配对交换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/exchange-lcci/)（简单）

标签：位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (31.92%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def exchangeBits(self, num: int) -> int:
        p1, p2 = int("10101010101010101010101010101010", base=2), int("01010101010101010101010101010101", base=2)
        n1 = num & p1  # 所有偶数位
        n2 = num & p2  # 所有奇数位
        return (n1 >> 1) | (n2 << 1)
```