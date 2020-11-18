# LeetCode题解(0857)：雇佣K名工人的最低成本(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-cost-to-hire-k-workers/)（困难）

标签：堆、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 280ms (38.39%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（堆）：

```python
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        size = len(quality)

        people = [(wage[i] / quality[i], wage[i], quality[i]) for i in range(size)]
        people.sort()
        print(people)

        ans = float("inf")
        heap = []  # 当前工作质量堆
        now = 0

        for person in people:
            heapq.heappush(heap, -person[2])
            now += person[2]

            if len(heap) > K:
                now += heapq.heappop(heap)

            if len(heap) == K:
                ans = min(ans, now * person[0])

        return ans
```