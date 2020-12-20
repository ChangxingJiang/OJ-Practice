# LeetCode题解(0800)：相似RGB颜色(Python)

题目：[原题链接](https://leetcode-cn.com/problems/similar-rgb-color/)（简单）

标签：数学、字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 44ms (50.00%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def similarRGB(self, color: str) -> str:
        lst = [i for i in range(0, 256, 17)]
        r1, g1, b1 = int(color[1:3], base=16), int(color[3:5], base=16), int(color[5:7], base=16)

        r2 = min(lst, key=lambda x: abs(r1 - x))
        g2 = min(lst, key=lambda x: abs(g1 - x))
        b2 = min(lst, key=lambda x: abs(b1 - x))

        return "#" + hex(r2)[2:].zfill(2) + hex(g2)[2:].zfill(2) + hex(b2)[2:].zfill(2)
```