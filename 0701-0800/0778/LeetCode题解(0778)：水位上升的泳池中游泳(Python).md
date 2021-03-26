# LeetCode题解(0778)：水位上升的泳池中游泳(Python)

题目：[原题链接](https://leetcode-cn.com/problems/swim-in-rising-water/)（困难）

标签：堆、广度优先搜索、深度优先搜索、图

| 解法           | 时间复杂度       | 空间复杂度 | 执行用时       |
| -------------- | ---------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2log(N^2))$ | $O(N^2)$   | 112ms (95.70%) |
| Ans 2 (Python) |                  |            |                |
| Ans 3 (Python) |                  |            |                |

解法一：

```python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < size and 0 <= y < size

        size = len(grid)

        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        height = 0

        while heap:
            val, i1, i2 = heapq.heappop(heap)
            height = max(height, val)

            # 处理已经到达终点的情况
            if i1 == i2 == size - 1:
                return height

            # 寻找相邻节点
            near = [(i1 + 1, i2), (i1 - 1, i2), (i1, i2 - 1), (i1, i2 + 1)]
            for ii1, ii2 in near:
                if is_valid(ii1, ii2) and (ii1, ii2) not in visited:
                    visited.add((ii1, ii2))
                    heapq.heappush(heap, (grid[ii1][ii2], ii1, ii2))
```