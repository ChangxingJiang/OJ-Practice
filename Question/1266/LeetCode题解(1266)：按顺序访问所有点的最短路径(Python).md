# LeetCode题解(1266)：按顺序访问所有点的最短路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-time-visiting-all-points/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 68ms (94.07%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（模拟情景）：

```python
def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    ans = 0
    for i in range(len(points) - 1):
        x = abs(points[i + 1][0] - points[i][0])
        y = abs(points[i + 1][1] - points[i][1])
        ans += abs(x - y) + min(x, y)
    return ans
```