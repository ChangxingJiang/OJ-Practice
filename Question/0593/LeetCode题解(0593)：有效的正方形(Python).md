# LeetCode题解(0593)：有效的正方形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-square/)（中等）

标签：数学、几何

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 28ms (98.79%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def d(point1, point2):
            return math.sqrt((point1[1] - point2[1]) ** 2 + (point1[0] - point2[0]) ** 2)

        lst = [d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4)]
        lst.sort()

        return (lst[0] > 0 and
                lst[0] == lst[1] == lst[2] == lst[3] and
                round(lst[3] * math.sqrt(2), 5) == round(lst[4], 5) == round(lst[5], 5))
```

