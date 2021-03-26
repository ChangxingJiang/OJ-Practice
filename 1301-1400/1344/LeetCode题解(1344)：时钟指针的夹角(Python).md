# LeetCode题解(1344)：时钟指针的夹角(Python)

题目：[原题链接](https://leetcode-cn.com/problems/angle-between-hands-of-a-clock/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 36ms (76.64%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        n1 = ((hour + minutes / 60) % 12) * 30
        n2 = minutes * 6
        if n1 < n2:
            n1, n2 = n2, n1
        return min(n1 - n2, n2 + 360 - n1)
```

