# LeetCode题解(0253)：会议室II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/meeting-rooms-ii/)（中等）

标签：堆、贪心算法、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 48ms (79.83%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []  # 结束时间堆
        ans = 0
        for interval in intervals:
            left, right = interval
            while heap and heap[0] <= left:
                heapq.heappop(heap)
            heapq.heappush(heap, right)
            ans = max(ans, len(heap))
        return ans
```