# LeetCode题解(1792)：最大平均通过率(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-average-pass-ratio/)（中等）

标签：堆

| 解法           | 时间复杂度       | 空间复杂度 | 执行用时        |
| -------------- | ---------------- | ---------- | --------------- |
| Ans 1 (Python) | $O(ClogC+ElogC)$ | $O(C)$     | 2308ms (38.13%) |
| Ans 2 (Python) |                  |            |                 |
| Ans 3 (Python) |                  |            |                 |

解法一：

```python
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # 计算每一个班级所能带来的增益
        classes = sorted((-((p + 1) / (t + 1) - p / t), t, p) for p, t in classes)

        while extraStudents:
            add, t, p = heapq.heappop(classes)
            heapq.heappush(classes, (-((p + 2) / (t + 2) - (p + 1) / (t + 1)), t + 1, p + 1))
            extraStudents -= 1

        ans = []
        for add, t, p in classes:
            ans.append(p / t)

        return sum(ans) / len(ans)
```

