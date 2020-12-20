# LeetCode题解(1118)：一月有多少天(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-days-in-a-month/)（简单）

标签：常识

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 40ms (52.54%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif M in (4, 6, 9, 11):
            return 30
        elif Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0):
            return 29
        else:
            return 28
```