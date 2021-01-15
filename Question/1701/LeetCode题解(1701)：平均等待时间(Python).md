# LeetCode题解(1701)：平均等待时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/average-waiting-time/)（中等）

标签：数学、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 140ms (63.43%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        size = len(customers)
        ans = 0

        now = 0
        for arrival, time in customers:
            if now < arrival:
                ans += time
                now = arrival + time
            else:
                ans += (now - arrival) + time
                now += time

        return ans / size
```

