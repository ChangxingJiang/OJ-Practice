# LeetCode题解(面试05.03)：翻转数位(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-bits-lcci/)（简单）

标签：位运算、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 40ms (67.20%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def reverseBits(self, num: int) -> int:
        last, now = 0, 0
        ans = 0
        for i in range(32):
            if num & (1 << i):
                now += 1
            else:
                ans = max(ans, last + now + 1)
                last, now = now, 0
        ans = max(ans, last + now + 1)
        return min(ans, 32)
```