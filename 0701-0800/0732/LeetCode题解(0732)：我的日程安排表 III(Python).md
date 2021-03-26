# LeetCode题解(0732)：我的日程安排表 III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/my-calendar-iii/)（困难）

标签：数组、有序映射、线段树

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时        |
| -------------- | ------------ | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2logN)$ | $O(N)$     | 1956ms (13.69%) |
| Ans 2 (Python) |              |            |                 |
| Ans 3 (Python) |              |            |                 |

解法一：

```python
class MyCalendarThree:

    def __init__(self):
        self.count = collections.Counter()

    def book(self, start: int, end: int) -> int:
        self.count[start] += 1
        self.count[end] -= 1

        ans = now = 0
        for k in sorted(self.count):
            now += self.count[k]
            ans = max(ans, now)

        return ans
```

