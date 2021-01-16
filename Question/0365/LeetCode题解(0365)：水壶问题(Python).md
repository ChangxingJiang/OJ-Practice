# LeetCode题解(0365)：水壶问题(Python)

题目：[原题链接](https://leetcode-cn.com/problems/water-and-jug-problem/)（中等）

标签：数学、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(XY)$    | $O(XY)$    | 6028ms (5.02%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        ans = set()
        visited = {(0, 0)}
        queue = collections.deque([(0, 0)])
        while queue:
            x1, y1 = queue.popleft()

            ans.add(x1)
            ans.add(y1)
            ans.add(x1 + y1)

            # 将左侧倒满
            x2, y2 = x, y1
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将右侧倒满
            x2, y2 = x1, y
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将左侧倒空
            x2, y2 = 0, y1
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将右侧倒空
            x2, y2 = x1, 0
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将左侧倒到右侧
            t = min(y - y1, x1)
            x2, y2 = x1 - t, y1 + t
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

            # 将右侧倒到左侧
            t = min(x - x1, y1)
            x2, y2 = x1 + t, y1 - t
            if (x2, y2) not in visited:
                visited.add((x2, y2))
                queue.append((x2, y2))

        return z in ans
```

