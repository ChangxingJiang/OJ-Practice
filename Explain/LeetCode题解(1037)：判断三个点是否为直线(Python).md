# LeetCode题解(1037)：判断三个点是否为直线(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-boomerang/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 44ms (59.85%) |
| Ans 2 (Python) | --         | --         | 48ms (37.45%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（距离法）：

```python
def isBoomerang(self, points: List[List[int]]) -> bool:
    a = pow((points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2, 0.5)
    b = pow((points[0][0] - points[2][0]) ** 2 + (points[0][1] - points[2][1]) ** 2, 0.5)
    c = pow((points[1][0] - points[2][0]) ** 2 + (points[1][1] - points[2][1]) ** 2, 0.5)
    return not max([a, b, c]) * 2 == sum([a, b, c])
```

解法二（斜率法）：

```python
def isBoomerang(self, points: List[List[int]]) -> bool:
    x1, y1 = points[0][0], points[0][1]
    x2, y2 = points[1][0], points[1][1]
    x3, y3 = points[2][0], points[2][1]
    return not (x3 - x1) * (y2 - y1) == (x2 - x1) * (y3 - y1)
```