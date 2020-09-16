# LeetCode题解(1184)：公交站间的距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/distance-between-bus-stops/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (84.48%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
    if start > destination:
        start, destination = destination, start
    s = sum(distance[start:destination])
    return min(s, sum(distance) - s)
```