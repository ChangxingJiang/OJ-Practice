# LeetCode题解(0502)：IPO(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ipo/)（中等）

标签：堆、贪心算法、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(KlogN)$ | $O(N)$     | 128ms (25.96%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（堆）：

```python
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        size = len(Profits)

        # 依据成本排序项目
        lst = [(- Profits[i], Capital[i]) for i in range(size)]
        lst.sort(key=lambda x: x[1])

        i = 0  # 当前准备添加的项目
        heap = []  # 可完成的项目堆（项目收益最大值优先）

        # 贪心选择最优项目
        for _ in range(k):
            # 将资金满足的项目添加到列表
            while i < size and lst[i][1] <= W:
                heapq.heappush(heap, lst[i])
                i += 1

            if heap:
                # 选择当前收益最高的项目
                w, c = heapq.heappop(heap)
                W += -w
            else:
                return W  # 如果没有可以选择的项目则返回当前的资本

        return W
```