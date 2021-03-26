# LeetCode题解(面试16.10)：生存人数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/living-people-lcci/)（中等）

标签：数组、堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 164ms (47.20%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（堆）：

```python
class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        size = len(birth)
        people = [(birth[i], death[i]) for i in range(size)]
        people.sort()

        max_idx, max_val = 0, 0

        heap = []
        for b, d in people:
            while heap and heap[0] < b:
                heapq.heappop(heap)

            heapq.heappush(heap, d)
            if len(heap) > max_val:
                max_idx, max_val = b, len(heap)

        return max_idx
```