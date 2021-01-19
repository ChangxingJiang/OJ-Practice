# LeetCode题解(1094)：拼车(Python)

题目：[原题链接](https://leetcode-cn.com/problems/car-pooling/)（中等）

标签：贪心算法、堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 96ms (28.87%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))
        heap = []
        now = 0
        for num, start, end in trips:
            while heap and heap[0][0] <= start:
                now -= heap[0][1]
                heapq.heappop(heap)
            now += num
            if now > capacity:
                return False
            heapq.heappush(heap, (end, num))
        return True
```

