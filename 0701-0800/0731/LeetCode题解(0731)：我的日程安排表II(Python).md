# LeetCode题解(0731)：我的日程安排表II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/my-calendar-ii/)（中等）

标签：数组、有序映射、线段树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 1412ms (27.85%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class MyCalendarTwo:

    def __init__(self):
        self.lst1 = []
        self.lst2 = []

    def book(self, start: int, end: int) -> bool:
        for l, r in self.lst2:
            if max(start, l) < min(end, r):
                return False
        for l, r in self.lst1:
            t1, t2 = max(start, l), min(end, r)
            if t1 < t2:
                self.lst2.append([t1, t2])
        self.lst1.append([start, end])
        return True
```

