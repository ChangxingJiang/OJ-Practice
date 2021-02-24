# LeetCode题解(1353)：最多可以参加的会议数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended/)（中等）

标签：贪心算法、排序、堆、线段树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+K)$   | $O(N)$     | 440ms (55.15%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = collections.deque(sorted(events, key=lambda x: (x[0], x[1])))

        ans = 0
        heap = []
        for i in range(1, 100001):
            while events and events[0][0] == i:
                heapq.heappush(heap, events.popleft()[1])
            while heap and heap[0] < i:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                ans += 1
            if not events and not heap:
                break

        return ans
```

