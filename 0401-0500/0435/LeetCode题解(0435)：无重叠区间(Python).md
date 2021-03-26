# LeetCode题解(0435)：无重叠区间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/non-overlapping-intervals/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 84ms (77%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        size = len(intervals)

        now = intervals[0][1]

        ans = size - 1

        for i in range(1, size):
            if intervals[i][0] >= now:
                ans -= 1
                now = intervals[i][1]

        return ans
```

