# LeetCode题解(0871)：最低加油次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-refueling-stops/)（困难）

标签：堆、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 124ms (100.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一（堆）：

```python
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 最大燃料堆，当前油量可以到达的范围内的所有加油站油量
        heap = []

        # 依据距离排序加油站
        stations.sort(key=lambda x: x[0])

        i = 0  # 当前已加入堆的加油站ID
        ans = 0  # 当前停靠加油站数量
        now = startFuel  # 当前位置
        while now < target:
            # 将所有已路过的加油站加入堆
            while i < len(stations) and stations[i][0] <= now:
                heapq.heappush(heap, -stations[i][1])
                i += 1

            # 如果没有可到达的加油站
            if not heap:
                return -1

            # 在油量最多的加油站加油
            ans += 1
            fuel = -heapq.heappop(heap)
            now += fuel

        return ans
```