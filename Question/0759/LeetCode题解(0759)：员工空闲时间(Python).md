# LeetCode题解(0759)：员工空闲时间(Python)

题目：[原题链接](https://leetcode-cn.com/problems/employee-free-time/)（困难）

标签：堆、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 104ms (85.39%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # 初始化员工下一次工作开始的时间堆
        # O(NlogN)
        heap = []
        for p in range(len(schedule)):
            people = schedule[p]
            heapq.heappush(heap, (people[0].start, p, 0))
        print(heap)

        # 不断推移时间线
        # O(N^2)
        ans = []
        finish_time = -1
        while heap:
            now_time, p, i = heapq.heappop(heap)

            # 如果工作时间开始于上一段工作时间结束之后，则添加空闲时间段
            if finish_time != -1 and now_time > finish_time:
                ans.append(Interval(finish_time, now_time))

            # 如果当前工作的结束时间比上一段工作的结束时间更晚，则更新工作结束时间
            if schedule[p][i].end > finish_time:
                finish_time = schedule[p][i].end

            # 将该员工下一次工作添加到堆
            if i + 1 < len(schedule[p]):
                heapq.heappush(heap, (schedule[p][i + 1].start, p, i + 1))

        return ans
```