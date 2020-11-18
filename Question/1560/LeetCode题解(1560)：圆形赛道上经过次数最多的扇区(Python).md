# LeetCode题解(1560)：圆形赛道上经过次数最多的扇区(Python)

题目：[原题链接](https://leetcode-cn.com/problems/most-visited-sector-in-a-circular-track/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(1)$     | $O(N)$     | 44ms (76%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一：

```python
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        circle = [i for i in range(1, n + 1)]
        start, end = rounds[0], rounds[-1]

        if start <= end:
            return circle[start - 1:end]
        else:
            return circle[:end] + circle[start - 1:]
```