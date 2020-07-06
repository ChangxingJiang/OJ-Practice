# LeetCode题解(1232)：判断一些点是否在一条线上(python)

题目：[原题链接](https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (82.44%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（斜率计算）：

```python
def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    x1, y1 = coordinates[0][0], coordinates[0][1]
    x2, y2 = coordinates[1][0], coordinates[1][1]
    for (x3, y3) in coordinates[2:]:
        if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
            return False
    else:
        return True
```