# LeetCode题解(1834)：单线程CPU(Python)

题目：[原题链接](https://leetcode-cn.com/problems/single-threaded-cpu/)（中等）

标签：堆、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 680ms (89.37%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
import heapq


class Solution:
    def getOrder(self, original_tasks: List[List[int]]) -> List[int]:
        size = len(original_tasks)

        # 将下标值添加到任务中
        tasks = []
        for i in range(size):
            e, p = original_tasks[i]
            tasks.append((e, p, i))

        # 排序任务列表
        tasks.sort()

        waiting = []  # 等待执行的任务堆
        now = 0  # 当前时间：第1个任务出现的时间
        j = 0  # 下一个需要加入任务堆的任务下标

        ans = []

        while j < size:
            # 将之前已出现的任务添加到任务堆中
            while j < size and tasks[j][0] <= now:
                heapq.heappush(waiting, (tasks[j][1], tasks[j][2]))
                j += 1

            # 处理当前时间结点已没有任务的情况
            if not waiting:
                now = tasks[j][0]
                heapq.heappush(waiting, (tasks[j][1], tasks[j][2]))
                j += 1

            # 将相同时间点的任务添加到任务堆中
            while j < size and tasks[j][0] <= now:
                heapq.heappush(waiting, (tasks[j][1], tasks[j][2]))
                j += 1

            # 处理需要优先处理的任务
            p, i = heapq.heappop(waiting)
            now += p
            ans.append(i)

        # 处理积压的任务
        while waiting:
            p, i = heapq.heappop(waiting)
            ans.append(i)

        return ans
```

