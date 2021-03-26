# LeetCode题解(1642)：使用梯子和砖块能够到达的最远建筑(Python)

题目：[原题链接](https://leetcode-cn.com/problems/furthest-building-you-can-reach/)（中等）

标签：贪心算法、堆、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时 |
| -------------- | ---------- | ---------- | -------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms     |
| Ans 2 (Python) |            |            |          |
| Ans 3 (Python) |            |            |          |

解法一：

```python
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # 计算翻越高度及翻越数量
        marks = [0]  # 翻越数量
        tasks = [0]  # 翻越高度
        last = heights[0]
        for i in range(1, len(heights)):
            height = heights[i]
            if height <= last:
                marks[-1] = i
            else:
                tasks.append(height - last)
                marks.append(i)
            last = height

        # print(marks, tasks)

        # 贪心攀爬

        now = []  # 当前的需要搭梯子的高度的堆
        heapq.heapify(now)

        total = 0  # 当前用砖块的高度总值

        for idx, task in enumerate(tasks):
            # 当前还有剩余梯子的情况
            if ladders > len(now):
                heapq.heappush(now, task)

            # 当前没有剩余梯子的情况
            else:
                # 如果有梯子的话，检查是否需要替换梯子的位置
                if ladders > 0:
                    smallest = heapq.heappop(now)  # 当前用梯子的最小值

                    # 替换梯子的位置
                    if smallest < task:
                        heapq.heappush(now, task)
                        total += smallest
                    # 不替换梯子的位置
                    else:
                        heapq.heappush(now, smallest)
                        total += task

                # 如果没有梯子的话，直接用砖块
                else:
                    total += task

                # 检查当前砖块是否够用
                if bricks < total:
                    # print("砖块不够用:", idx, now)
                    return marks[idx - 1]

            # print(idx, task, "->", now, total)

        return marks[-1]
```