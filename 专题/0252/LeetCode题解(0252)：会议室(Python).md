# LeetCode题解(0252)：会议室(Python)

题目：[原题链接](https://leetcode-cn.com/problems/meeting-rooms/)（简单）

标签：排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 48ms (58.49%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        finish = 0
        for start, end in intervals:
            if start < finish:
                return False
            finish = end
        return True
```