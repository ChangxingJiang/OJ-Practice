# LeetCode题解(1227)：飞机座位分配概率(Python)

题目：[原题链接](https://leetcode-cn.com/problems/airplane-seat-assignment-probability/)（中等）

标签：脑筋急转弯、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 32ms (95.27%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 0.5 if n > 1 else 1
```