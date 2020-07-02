# LeetCode题解(0836)：判断矩阵是否重叠(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rectangle-overlap/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 36ms (88.24%) |
| Ans 2 (Python) | $O(1)$     | $O(1)$     | 32ms (96.26%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（不使用左下角、右上角的顺序）：

```python
def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    x_max_1 = max(rec1[0], rec1[2])
    x_max_2 = max(rec2[0], rec2[2])
    x_min_1 = min(rec1[0], rec1[2])
    x_min_2 = min(rec2[0], rec2[2])
    y_max_1 = max(rec1[1], rec1[3])
    y_max_2 = max(rec2[1], rec2[3])
    y_min_1 = min(rec1[1], rec1[3])
    y_min_2 = min(rec2[1], rec2[3])
    return (x_max_1 > x_min_2 and x_max_2 > x_min_1) and (y_max_1 > y_min_2 and y_max_2 > y_min_1)
```

解法二：

```python
def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    return not (rec1[2] <= rec2[0] or  # 1右<2左
                rec2[2] <= rec1[0] or  # 2右<1左
                rec1[3] <= rec2[1] or  # 1上<3下
                rec2[3] <= rec1[3])  # 3上<1下
```