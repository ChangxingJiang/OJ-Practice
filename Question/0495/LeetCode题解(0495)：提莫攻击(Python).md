# LeetCode题解(0495)：提莫攻击(Python)

题目：[原题链接](https://leetcode-cn.com/problems/teemo-attacking/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 284ms (74.87%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        ans = 0
        last = timeSeries[0]
        for i in range(1, len(timeSeries)):
            time = timeSeries[i]
            ans += min((time - last), duration)
            last = time
        return ans + duration
```

