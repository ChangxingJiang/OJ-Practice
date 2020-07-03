# LeetCode题解(1033)：连续移动石子直到连续(Python)

题目：[原题链接](https://leetcode-cn.com/problems/moving-stones-until-consecutive/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 40ms (72.92%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
    t = sorted([a, b, c])
    d1 = t[2] - t[1] - 1
    d2 = t[1] - t[0] - 1
    maximum = d1 + d2
    if d1 == 0 and d2 == 0:
        minimum = 0
    elif d1 == 0 or d2 == 0 or d1 == 1 or d2 == 1:
        minimum = 1
    else:
        minimum = 2
    return [minimum, maximum]
```

