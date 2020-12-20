# LeetCode题解(0587)：安装栅栏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/erect-the-fence/)（困难）

标签：几何、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 108ms (87.27%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        if len(points) <= 1:
            return points

        points.sort()

        stack = []
        for point in points:
            while len(stack) >= 2 and self.orientation(stack[-2], stack[-1], point) > 0:
                stack.pop()
            stack.append(point)

        stack.pop()
        for point in reversed(points):
            while len(stack) >= 2 and self.orientation(stack[-2], stack[-1], point) > 0:
                stack.pop()
            stack.append(point)
        stack.pop()

        return list([point[0], point[1]] for point in set((point[0], point[1]) for point in stack))
```