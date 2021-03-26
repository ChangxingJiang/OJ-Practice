# LeetCode题解(1705)：吃苹果的最大数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-eaten-apples/)（中等）

标签：贪心算法、堆

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 352ms (67.97%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)

        heap = []
        ans = 0

        now = 0

        while now < n or heap:
            # 先接收当天的苹果
            if now < n:
                heapq.heappush(heap, (now + days[now], apples[now]))

            # 再腐烂旧苹果
            while heap and (heap[0][0] <= now or heap[0][1] == 0):
                heapq.heappop(heap)

            if heap:
                heap[0] = (heap[0][0], heap[0][1] - 1)
                ans += 1

            now += 1

        return ans
```

