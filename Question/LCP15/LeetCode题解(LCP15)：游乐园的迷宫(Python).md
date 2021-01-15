# LeetCode题解(LCP15)：游乐园的迷宫(Python)

题目：[原题链接](https://leetcode-cn.com/problems/you-le-yuan-de-mi-gong/)（困难）

标签：贪心算法、几何、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 1996ms (13.33%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
def sub(a, b):
    """求点a到点b的向量"""
    return [b[0] - a[0], b[1] - a[1]]


def cross(a, b):
    """求向量a到向量b的向量叉积"""
    return a[0] * b[1] - a[1] * b[0]


class Solution:
    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        size = len(points)
        visited = [False] * size

        ans = []

        # 将最左侧的点作为出发点
        start = 0
        for i in range(size):
            if points[i][0] < points[start][0]:
                start = i
        ans.append(start)
        visited[start] = True

        for direct in direction:
            next = -1
            # 下一个转向方向为L，则当前这一步选择最右侧的点
            if direct == "L":
                for j in range(size):
                    if not visited[j]:
                        if next == -1 or cross(sub(points[start], points[j]), sub(points[start], points[next])) > 0:
                            next = j

            # 下一个转向方向为R，则当前这一步选择最左侧的点
            if direct == "R":
                for j in range(size):
                    if not visited[j]:
                        if next == -1 or cross(sub(points[start], points[j]), sub(points[start], points[next])) < 0:
                            next = j

            ans.append(next)
            visited[next] = True
            start = next

        # 将最后一个点添加到结果中
        for i in range(size):
            if not visited[i]:
                ans.append(i)

        return ans
```

