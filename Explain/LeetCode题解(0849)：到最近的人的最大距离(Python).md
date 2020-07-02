# LeetCode题解(0849)：到最近的人的最大距离(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximize-distance-to-closest-person/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 80ms (81.98%)  |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 36ms (100.00%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双向遍历）：

```python
def maxDistToClosest(self, seats: List[int]) -> int:
    distance = [float("inf") for _ in range(len(seats))]
    for i in range(len(seats)):
        if seats[i] == 1:
            distance[i] = 0
        elif i > 0:
            distance[i] = distance[i - 1] + 1
    for i in range(len(seats) - 1, -1, -1):
        if seats[i] == 1:
            distance[i] = 0
        elif i < len(seats) - 1:
            distance[i] = min(distance[i],distance[i + 1] + 1)
    return max(distance)
```

解法二（双指针）：

![LeetCode题解(0849)：截图1](LeetCode题解(0849)：截图1.png)

```python
def maxDistToClosest(self, seats: List[int]) -> int:
    distance = 0
    start = -1
    for i in range(len(seats)):
        if seats[i] == 1:
            if start == -1:
                distance = max(distance, i)
            else:
                distance = max(distance, (i - start) // 2)
            start = i
    else:
        distance = max(distance, (len(seats) - start) - 1)
    return distance
```