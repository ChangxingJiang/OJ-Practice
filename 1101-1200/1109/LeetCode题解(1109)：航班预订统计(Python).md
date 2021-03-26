# LeetCode题解(1109)：航班预订统计(Python)

题目：[原题链接](https://leetcode-cn.com/problems/corporate-flight-bookings/)（中等）

标签：数组、数学、差分数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(B+N)$   | $O(N)$     | 940ms (87.02%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        lst = [0] * (n + 1)
        for j, k, l in bookings:
            lst[j - 1] += l
            lst[k] -= l

        lst.pop()

        ans = []
        now = 0
        for i in range(len(lst)):
            now += lst[i]
            ans.append(now)

        return ans
```

